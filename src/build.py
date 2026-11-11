"""Builds index.html for the PRG page.

Banners are real medieval marginalia (drolleries), cut out of public-domain scans
from Wikimedia Commons and standing on a painted border bar.
Run from the repo root or from src/:  python3 src/build.py
"""
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE_PATH = HERE / "template.html"
OUT_PATH = HERE.parent / "index.html" if HERE.name == "src" else HERE / "index.html"

INK = "#2b2118"
VERM = "#b83a26"
LAPIS = "#2a4a8c"
GOLD = "#c0922f"
LEAF = "#6d8a45"

# ---------------------------------------------------------------- the figures
# name: (display height in px, alt text, source credit)
FIGS = {
    "fox-preaching": (120, "A fox dressed as a friar preaching to a flock of geese",
                      "Smithfield Decretals, c. 1340. British Library, Royal MS 10 E IV, f. 49v"),
    "rabbit-greyhound": (168, "A rabbit riding a greyhound",
                         "Medieval manuscript marginalia, 14th century"),
    "fox-reading": (200, "A fox in a cleric's hood reading a book",
                    "Book of Hours, Utrecht, c. 1460. Museum Meermanno, MS 10 F 50, f. 6r"),
    "fox-queck": (140, "A fox running off with a goose, which says 'queck'",
                  "Gorleston Psalter, 1310s. British Library, Add MS 49622"),
    "axe-rabbit": (116, "A rabbit swinging a battle-axe",
                   "Gorleston Psalter, 1310s. British Library, Add MS 49622"),
    "grimace": (176, "A man pulling a face",
                "Gorleston Psalter, 1310s. British Library, Add MS 49622, f. 123r"),
    "knight-fish": (132, "A knight riding a fish into battle with a two-headed hybrid",
                    "Breviary of Renaud de Bar, 1302–03. Verdun, Bibliothèque municipale, MS 107, f. 111"),
    "headless-saints": (140, "Two headless saints carrying their own heads",
                        "Breviary of Renaud de Bar, 1302–05. Verdun, Bibliothèque municipale, MS 107, f. 99v"),
    "monkey-boar": (160, "A monkey jousting on the back of a boar",
                    "Maastricht Hours, early 14th century. British Library, Stowe MS 17, f. 124r"),
}

TOP = (["fox-preaching", "rabbit-greyhound"], "fox-reading", ["fox-queck", "axe-rabbit", "grimace"])
BOTTOM = (["knight-fish"], "headless-saints", ["monkey-boar"])


def fig(name, cls=""):
    h, alt, credit = FIGS[name]
    return (f'<img class="fig {cls}" src="marginalia/{name}.webp" alt="{alt}" title="{credit}" '
            f'style="--h:{h}px">')


def border_bar(seed, W=1400, H=26):
    """Painted manuscript bar: alternating vermilion/lapis with gold knots and a vine."""
    rng = random.Random(seed)
    y = H / 2
    out = [f'<svg class="bar" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" '
           f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    x, i = 0.0, 0
    while x < W:
        w = rng.uniform(80, 140)
        col = VERM if i % 2 == 0 else LAPIS
        out.append(f'<rect x="{x:.1f}" y="{y-2.5:.1f}" width="{w:.1f}" height="5" fill="{col}"/>')
        out.append(f'<path d="M{x+6:.1f} {y:.1f} L{x+w-6:.1f} {y:.1f}" stroke="#f4ecdb" stroke-width="0.8" stroke-dasharray="1 5" opacity="0.8"/>')
        x += w
        i += 1
    pts = " L".join(f"{xx} {y + 6*math.sin(xx/40):.1f}" for xx in range(0, W + 10, 10))
    out.append(f'<path d="M{pts}" fill="none" stroke="{LEAF}" stroke-width="1" opacity="0.85"/>')
    for xx in range(24, W, 70):
        yy = y + 6 * math.sin(xx / 40)
        rot = 40 if (xx // 70) % 2 else -40
        out.append(f'<path transform="translate({xx} {yy:.1f}) rotate({rot})" '
                   'd="M0 0 C-6 -4 -7 -11 -2 -13 C0 -12 0 -11 0 -10 C0 -11 0 -12 2 -13 C7 -11 6 -4 0 0 Z" '
                   f'fill="{LEAF}" stroke="{INK}" stroke-width="0.6"/>')
    x, i = 0.0, 0
    rng = random.Random(seed)
    while x < W:
        out.append(f'<circle cx="{x:.1f}" cy="{y}" r="4" fill="{GOLD}" stroke="{INK}" stroke-width="0.7"/>')
        x += rng.uniform(80, 140)
        i += 1
    out.append('</svg>')
    return "".join(out)


def banner(layout, seed):
    left, mid, right = layout
    return (
        '<div class="figs">'
        f'<div class="side left">{"".join(fig(n) for n in left)}</div>'
        f'<div class="mid">{fig(mid, "centre")}</div>'
        f'<div class="side right">{"".join(fig(n) for n in right)}</div>'
        '</div>' + border_bar(seed)
    )


# ---------------------------------------------------------------- readings

PAST = [
    ("Václav Havel", "“The Power of the Powerless”", "1978", "prg-s2e1-havel.pdf"),
    ("Susan Sontag", "“Fascinating Fascism”", "1975", "prg-s2e2-sontag.pdf"),
    ("Martin Luther", "<em>To the Christian Nobility of the German Nation</em>", "1520", "prg-s2e3-luther.pdf"),
]

UPCOMING = [
    ("Nick Land", "“The Dark Enlightenment,” Part 1", "2012"),
    ("Amia Srinivasan", "“Talking to My Students About Porn”", "2021"),
    ("Val Plumwood &amp; Nick Bostrom", "“Being Prey” + “The Fable of the Dragon-Tyrant”", "1996 / 2005"),
    ("Marquis de Sade", "“Yet Another Effort, Frenchmen, If You Would Become Republicans”", "1795"),
    ("Ayn Rand", "“The Objectivist Ethics”", "1961"),
    ("Timothy Leary", "“Start Your Own Religion”", "1967"),
    ("Camille Paglia", "“Rape and Modern Sex War”", "1991"),
    ("Leon Trotsky", "“Their Morals and Ours”", "1938"),
    ("Friedrich Nietzsche", "<em>On the Genealogy of Morals</em>, First Essay", "1887"),
    ("Anonymous", "<em>The Gospel of Thomas</em>", "c. 100"),
]


def items(rows, linked):
    out = []
    for row in rows:
        if linked:
            a, t, y, f = row
            what = f'<a class="what" href="{f}">{t}</a>'
        else:
            a, t, y = row
            what = f'<span class="what">{t}</span>'
        out.append(f'        <li><span class="who">{a}</span> {what} <span class="yr">{y}</span></li>')
    return "\n".join(out)


def grain_uri():
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
           "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/>"
           "<feColorMatrix values='0 0 0 0 0.35  0 0 0 0 0.25  0 0 0 0 0.12  0 0 0 0.5 0'/></filter>"
           "<rect width='100%' height='100%' filter='url(#n)'/></svg>")
    return "data:image/svg+xml;utf8," + svg.replace("#", "%23").replace("<", "%3C").replace(">", "%3E")


def main():
    html = (TEMPLATE_PATH.read_text(encoding="utf-8")
            .replace("{{BANNER_TOP}}", banner(TOP, 3))
            .replace("{{BANNER_BOTTOM}}", banner(BOTTOM, 41))
            .replace("{{UPCOMING}}", items(UPCOMING, False))
            .replace("{{PAST}}", items(PAST, True))
            .replace("{{GRAIN}}", grain_uri()))
    OUT_PATH.write_text(html, encoding="utf-8")
    print("wrote", OUT_PATH, len(html))


if __name__ == "__main__":
    main()
