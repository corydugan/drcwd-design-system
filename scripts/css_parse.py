#!/usr/bin/env python3
"""
css_parse.py  ·  a CSS reader that knows what is code and what is not.

Why this exists
---------------
An audit on 2026-08-12 found every generator in this folder shared one defect:
they scanned colors_and_type.css as raw text. Comments and strings were
indistinguishable from code, which produced four ways for a build to be wrong
while `--check` reported green, because build and compare re-derived the same
wrong answer.

The worst of them, verified end to end:

    --ink-500:    #6E6F75;   /* muted / meta / captions */
    /* was --ink-500: #797A80; before the WCAG fix of 2026-07-27 */

The declaration regex matched inside the comment, later-wins overwrote the live
value, and tokens.json, PASTE-INTO-TOOLS.md and _diagram.css all silently
shipped #797A80: the pre-WCAG value at 4.28:1 that these scripts exist to keep
out. Writing down WHY a value changed is the most natural edit anyone makes to
this file, and it was the edit that broke it.

Two more from the same root: a comment mentioning `[data-surface="ink"]` made
block() return the :root block instead, so the ink surface silently carried
paper values; and a `}` inside a comment let css_guard call a genuinely
unclosed rule balanced.

So: mask first, parse second. Everything here operates on a masked copy where
comments and string contents are replaced by spaces of equal length, which keeps
every offset valid against the original text.
"""

from __future__ import annotations

import re

__all__ = ["mask", "strip_comments", "find_block", "declarations", "scan_problems", "split_top_level"]


def mask(css: str) -> str:
    """
    Return a same-length copy of `css` with comment bodies and string contents
    replaced by spaces. Offsets stay valid against the original.

    Delimiters are preserved so the result is still syntactically shaped:
    /* ... */ keeps its slashes and stars, "..." keeps its quotes.
    """
    out = list(css)
    i, n = 0, len(css)
    while i < n:
        # comment
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            end = n if j == -1 else j + 2
            for k in range(i + 2, min(end - 2, n) if j != -1 else n):
                if out[k] != "\n":
                    out[k] = " "
            i = end
            continue
        # string, single or double quoted, with backslash escapes
        if css[i] in "\"'":
            q = css[i]
            j = i + 1
            while j < n:
                if css[j] == "\\":
                    j += 2
                    continue
                if css[j] == q:
                    break
                j += 1
            for k in range(i + 1, min(j, n)):
                if out[k] != "\n":
                    out[k] = " "
            i = min(j + 1, n)
            continue
        i += 1
    return "".join(out)


def inside_comment(css: str) -> list[bool]:
    """Per-character: is this index inside a /* ... */ comment?"""
    flags = [False] * len(css)
    i, n = 0, len(css)
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            end = n if j == -1 else j + 2
            for k in range(i, end):
                flags[k] = True
            i = end
            continue
        i += 1
    return flags


def find_block(css: str, selector: str) -> str:
    """
    Return the body of the first `selector { ... }` block.

    The selector is searched in the ORIGINAL text, because a legitimate
    selector can contain a string: `[data-surface="ink"]` is the obvious one,
    and masking blanks its contents. A match is rejected if it STARTS inside a
    comment, which is what stopped a comment mentioning the selector from
    hijacking this and handing back the wrong block.

    Braces are matched on masked text, so a `{` inside a comment or a string
    cannot shift the boundary.

    Raises LookupError if the selector never appears as code.
    """
    m = mask(css)
    in_comment = inside_comment(css)
    start = 0
    while True:
        i = css.find(selector, start)
        if i == -1:
            raise LookupError(f"selector {selector!r} does not appear as code")
        if in_comment[i]:
            start = i + 1
            continue
        brace = m.find("{", i + len(selector))
        if brace == -1:
            raise LookupError(f"selector {selector!r} is not followed by a block")
        # reject a match that is only a prefix of a longer selector token
        between = m[i + len(selector):brace]
        if between.strip(" \t\r\n,>+~") == "":
            depth, j = 1, brace + 1
            while depth and j < len(m):
                if m[j] == "{":
                    depth += 1
                elif m[j] == "}":
                    depth -= 1
                j += 1
            if depth:
                raise LookupError(f"block for {selector!r} is never closed")
            return css[brace + 1:j - 1]
        start = i + 1


def split_top_level(body: str) -> list[str]:
    """
    Split a declaration body on `;` at depth 0, ignoring semicolons inside
    comments, strings, parens and nested blocks. `url("a;b.png")` and
    `url(data:image/svg+xml;utf8,...)` survive intact.
    """
    m = mask(body)
    parts, start, depth = [], 0, 0
    for i, ch in enumerate(m):
        if ch in "({[":
            depth += 1
        elif ch in ")}]":
            depth -= 1
        elif ch == ";" and depth == 0:
            parts.append(body[start:i])
            start = i + 1
    tail = body[start:]
    if tail.strip():
        parts.append(tail)
    return parts


NAME = re.compile(r"^\s*--([A-Za-z0-9_-]+)\s*:\s*(.*)$", re.S)


def declarations(body: str, *, strict: bool = True) -> dict[str, str]:
    """
    Parse `--name: value` pairs from a block body, comment-blind and
    string-safe. Values keep their original text.

    strict=True (the default) raises ValueError on a fragment that looks like a
    declaration but was never terminated, because a dropped semicolon otherwise
    makes one token swallow the next. That exact failure silently produced a
    _diagram.css where --grape-800 was never declared and every var() using it
    resolved to nothing, with the script exiting 0.
    """
    out: dict[str, str] = {}
    parts = split_top_level(body)
    masked_body = mask(body)
    unterminated = masked_body.rstrip().endswith(tuple("};")) is False
    for idx, part in enumerate(parts):
        # Comments are removed from the fragment first. Splitting on ';' leaves
        # the comment that FOLLOWED the previous declaration glued to the front
        # of this one, so matching before stripping loses every declaration that
        # has a documented neighbour, which in this stylesheet is most of them.
        code = strip_comments(part)
        m = NAME.match(code)
        if not m:
            continue
        name, value = m.group(1).lower(), m.group(2).strip()
        # A value containing another custom-property declaration means the
        # semicolon before it was dropped, so this token swallowed the next one.
        # Caught here rather than in each consumer, because the consumers use
        # `if name in root` guards and would otherwise skip the swallowed token
        # in silence: that produced a _diagram.css where --grape-800 was never
        # declared, every var(--grape-800) resolved to nothing, and the script
        # still exited 0.
        swallowed = re.search(r"--([A-Za-z0-9_-]+)\s*:", value)
        if strict and swallowed:
            raise ValueError(
                f"--{name} has no terminating ';', so its value ran on and "
                f"swallowed --{swallowed.group(1)}. Add the semicolon after "
                f"--{name}."
            )
        if strict and idx == len(parts) - 1 and unterminated:
            raise ValueError(
                f"--{name} has no terminating ';'. Its value would swallow "
                f"everything after it, including comment text. Add the semicolon."
            )
        if strict and name in out and out[name] != value:
            raise ValueError(
                f"--{name} is declared twice in the same block with different "
                f"values ({out[name]!r} then {value!r}). Remove one."
            )
        out[name] = value
    return out


def strip_comments(text: str) -> str:
    """Remove `/* ... */` blocks entirely, keeping everything else verbatim."""
    out, i, n = [], 0, len(text)
    while i < n:
        if text.startswith("/*", i):
            j = text.find("*/", i + 2)
            i = n if j == -1 else j + 2
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def scan_problems(css: str) -> list[str]:
    """
    Structural problems that make a stylesheet unparseable. Operates on masked
    text, so a brace or a comment terminator inside a comment or a string is
    correctly ignored.
    """
    problems: list[str] = []

    # unterminated comment, and comments that close early
    depth, i, line, open_line = 0, 0, 1, 0
    while i < len(css):
        if css.startswith("/*", i) and depth == 0:
            depth, open_line = 1, line
            i += 2
            continue
        if css.startswith("*/", i):
            if depth == 0:
                problems.append(
                    f"line {line}: stray '*/' with no open comment. Something "
                    f"earlier closed a comment sooner than intended, most often "
                    f"a path or glob containing the two characters that "
                    f"terminate a comment."
                )
            else:
                depth = 0
            i += 2
            continue
        if css[i] == "\n":
            line += 1
        i += 1
    if depth:
        problems.append(
            f"line {open_line}: comment opened here and never closed. "
            f"Everything after it is swallowed."
        )

    # brace balance AND nesting, on code only
    m = mask(css)
    level, line, negative_at = 0, 1, 0
    for ch in m:
        if ch == "\n":
            line += 1
        elif ch == "{":
            level += 1
        elif ch == "}":
            level -= 1
            if level < 0 and not negative_at:
                negative_at = line
                level = 0
    if negative_at:
        problems.append(f"line {negative_at}: '}}' with no open rule.")
    if level > 0:
        problems.append(f"{level} rule(s) opened and never closed.")

    return problems
