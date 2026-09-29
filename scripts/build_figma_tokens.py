#!/usr/bin/env python3
"""Flatten tokens.json into files a Figma variable importer can read.

tokens.json is the source. This writes two derived files into build/:

    build/figma-tokens.json   DTCG-style ($type, $value), every value literal
    build/figma-tokens.csv    name,type,value, the same tokens

Figma variables hold only colours, numbers and strings, so the flattening:
  - resolves aliases such as {color.ink.1000} to their hex
  - turns rem into px (1rem = 16px) and clamp(min, fluid, max) into its max,
    the desktop size
  - splits each dataviz array into numbered variables
  - types font weights as numbers and drops the gradient token

Rerun after any change to tokens.json:
    python3 scripts/build_figma_tokens.py
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tokens.json"
OUT = ROOT / "build"


def to_px(v):
    v = str(v).strip()
    m = re.match(r"clamp\((.*)\)$", v)
    if m:
        v = m.group(1).split(",")[-1].strip()
    if v.endswith("rem"):
        return round(float(v[:-3]) * 16, 2)
    if v.endswith("px"):
        return float(v[:-2])
    return float(v)


def main():
    src = json.loads(SRC.read_text())
    flat = {}

    def walk(node, path):
        if isinstance(node, dict) and ("$value" in node or "value" in node):
            flat[".".join(path)] = (node.get("$type", node.get("type")), node.get("$value", node.get("value")))
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, path + [k])

    walk(src, [])

    def resolve(v, seen=()):
        m = re.fullmatch(r"\{(.+)\}", str(v))
        if not m:
            return v
        key = m.group(1)
        if key in seen or key not in flat:
            raise SystemExit(f"unresolvable alias {v}")
        return resolve(flat[key][1], seen + (key,))

    rows = []
    for name, (typ, val) in flat.items():
        top = name.split(".")[0]
        if top == "gradient":
            continue
        val = resolve(val)
        if isinstance(val, list):
            for i, item in enumerate(val, 1):
                rows.append((f"{name}.{i}", "color", str(item)))
        elif top in ("fontSize", "spacing", "radius"):
            rows.append((name, "number", to_px(val)))
        elif top == "fontWeight":
            rows.append((name, "number", float(val)))
        elif typ == "fontFamily":
            rows.append((name, "string", str(val)))
        elif typ == "color":
            rows.append((name, "color", str(val)))
        else:
            raise SystemExit(f"unhandled token {name} ({typ}) = {val}")

    OUT.mkdir(exist_ok=True)
    tree = {}
    for name, typ, val in rows:
        node = tree
        parts = name.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"$type": typ, "$value": val}
    (OUT / "figma-tokens.json").write_text(json.dumps(tree, indent=2) + "\n")

    with open(OUT / "figma-tokens.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "type", "value"])
        for name, typ, val in rows:
            w.writerow([name.replace(".", "/"), typ, val])

    print(f"{len(rows)} tokens written to build/figma-tokens.json and build/figma-tokens.csv")


if __name__ == "__main__":
    main()
