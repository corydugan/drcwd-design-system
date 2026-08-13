#!/usr/bin/env python3
"""
css_guard.py  ·  refuse to generate anything from a stylesheet that will not parse.

Why this exists
---------------
On 2026-08-12, colors_and_type.css was found to contain this in a comment:

    ~/.claude/plugins/cache/anthropic-agent-skills/example-skills/*/skills/...

The two characters after "example-skills/" are a comment terminator. The block
opened on line 13 therefore closed on line 16, the remainder of that line became
stray CSS, and the trailing "*/" became a second stray. Every consumer loading
this file got an unparseable stylesheet: the design system's own preview cards
rendered with no styling at all, and had done since the comment was written.

It was invisible because the file looked correct in an editor, the brace count
balanced, and the website was not affected, having forked before the comment
existed. The design system was documented as "the source everything inherits
from" while being, in practice, unloadable.

Per ~/.claude/CLAUDE.md rule 2, a rule that must always hold is a script.
Both build_tokens.py and sync_website.py call check() and refuse to write when
it fails, so this cannot reach an artifact again.

Run standalone to check a file:
    python3 scripts/css_guard.py colors_and_type.css
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from css_parse import scan_problems


class CssGuardError(Exception):
    """The stylesheet will not parse. Nothing should be generated from it."""


def scan(text: str) -> list[str]:
    """Delegates to css_parse.scan_problems, which masks comments and
    strings first. The previous hand-rolled version counted braces over
    raw text: a `}` inside a comment masked a genuinely unclosed rule,
    and `content:"}"` was reported as unbalanced. Both directions were
    wrong, and the false-negative direction is the dangerous one."""
    return scan_problems(text)


def check(path: Path) -> None:
    """Raise CssGuardError if the stylesheet will not parse."""
    problems = scan(path.read_text(encoding="utf-8"))
    if problems:
        raise CssGuardError(
            f"{path} will not parse, so nothing was generated from it:\n  "
            + "\n  ".join(problems)
        )


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 scripts/css_guard.py <file.css> [...]", file=sys.stderr)
        return 2
    failed = False
    for arg in sys.argv[1:]:
        p = Path(arg)
        try:
            check(p)
            print(f"ok  {p}")
        except CssGuardError as e:
            print(str(e), file=sys.stderr)
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
