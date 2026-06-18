"""Outline DM Serif Display text to SVG paths (print-safe, no font dependency).
Generates the delta logo lockups for the drCWDugan v3 system."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = ".build/fonts/DMSerifDisplay-Regular.ttf"
GRAPE = "#352051"

def text_path(font, string, size, x, baseline):
    """Return an SVG path 'd' for `string` set in `font` at `size`px,
    starting pen at (x, baseline). Y is flipped (SVG y-down)."""
    upem = font["head"].unitsPerEm
    s = size / upem
    glyphSet = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    cursor = x
    out = SVGPathPen(glyphSet)
    for ch in string:
        gname = cmap.get(ord(ch))
        if gname is None:
            gname = ".notdef"
        # transform: scale s, flip y, translate to (cursor, baseline)
        tpen = TransformPen(out, (s, 0, 0, -s, cursor, baseline))
        glyphSet[gname].draw(tpen)
        adv = hmtx[gname][0]
        cursor += adv * s
    return out.getCommands(), cursor

def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img">\n{body}\n</svg>\n')

def main():
    f = TTFont(FONT)

    # PRIMARY: delta + "Dr. Cory Dugan"
    d, _ = text_path(f, "Dr. Cory Dugan", 64, 76, 80)
    body = (f'  <title>Dr. Cory Dugan</title>\n'
            f'  <polygon points="32,38 9,80 55,80" fill="{GRAPE}"/>\n'
            f'  <path d="{d}" fill="{GRAPE}"/>')
    open("logo/lockup-primary-delta-outlined.svg", "w").write(svg(600, 120, body))

    # STACKED: small delta top-left + "Dr. Cory" / "Dugan"
    d1, _ = text_path(f, "Dr. Cory", 60, 0, 132)
    d2, _ = text_path(f, "Dugan", 60, 0, 196)
    body = (f'  <title>Dr. Cory Dugan</title>\n'
            f'  <polygon points="24,8 6,44 42,44" fill="{GRAPE}"/>\n'
            f'  <g transform="translate(0,4)">\n'
            f'    <path d="{d1}" fill="{GRAPE}"/>\n'
            f'    <path d="{d2}" fill="{GRAPE}"/>\n'
            f'  </g>')
    open("logo/wordmark-stacked-delta-outlined.svg", "w").write(svg(320, 220, body))

    # CREDENTIAL serif line: delta + "Dr. Cory Dugan, PhD" (eyebrow added separately as web text in the .svg web version)
    d, _ = text_path(f, "Dr. Cory Dugan, PhD", 60, 72, 100)
    body = (f'  <title>Dr. Cory Dugan, PhD</title>\n'
            f'  <polygon points="30,62 9,100 51,100" fill="{GRAPE}"/>\n'
            f'  <path d="{d}" fill="{GRAPE}"/>')
    open("logo/lockup-credential-delta-outlined.svg", "w").write(svg(640, 130, body))

    print("wrote 3 outlined lockups")

if __name__ == "__main__":
    main()
