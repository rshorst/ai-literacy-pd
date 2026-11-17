#!/usr/bin/env python3
"""Builds the site as flat HTML pages.

Every page carries its own CSS and script, so a single page still runs when opened
on its own, offline. Decorative collage images live in assets/ and simply drop out
if a page is copied without that folder. Links between pages are relative file
links (map.html, cards.html), which work on GitHub Pages and from a downloaded folder.

Run:  python3 _build/build.py
"""
import re, sys, html
from pathlib import Path
import markdown

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent
MAP_SRC = HERE / "map-source.html"
sys.path.insert(0, str(HERE))
from content import PAGES, NAV, SITE, PAGE_STYLE  # noqa: E402
from scenarios import SCENARIO_PAGES  # noqa: E402

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800;900&family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

TOKENS = """--bg:#f4efe4;--surface:#fffcf5;--ink:#141414;--muted:#55514b;--line:#d6cdbb;--accent:#1d5bd8;--hover:#efe7d6;
--pink:#f59bbd;--yellow:#fbd441;--teal:#8bdad3;--blue:#4a80ea;--orange:#f2703f;
--c-company:#2a2a2a;--c-model:#0f7c74;--c-app:#2c5ad1;--c-cat:#c2541c;--c-concept:#c53273;
--font-display:"Archivo","Arial Black","Helvetica Neue",Arial,sans-serif;--font-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--font-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;color-scheme:light"""

# Collage look: cream paper, torn tape behind headings, stickers and cut-outs.
# One committed light theme (a paper world), so no dark variant.
BASE_CSS = r"""
:root:not(#_){""" + TOKENS + r"""}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{margin:0}
body{background:var(--bg) url(assets/paper.jpg) repeat;background-size:1100px auto;color:var(--ink);font-family:var(--font-body);font-size:16.5px;line-height:1.6}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-999px;top:8px;background:var(--surface);padding:8px 12px;border-radius:6px;z-index:50}
.skip:focus{left:12px}
img{max-width:100%}

/* Torn tape */
.tape{display:inline-block;padding:.06em .22em .02em;clip-path:polygon(0 6%,3% 0,30% 4%,62% 0,97% 3%,100% 0,99% 48%,100% 100%,70% 96%,36% 100%,3% 96%,0 100%,1% 52%)}
.tape.pink{background:var(--pink)}.tape.teal{background:var(--teal)}.tape.yellow{background:var(--yellow)}.tape.blue{background:var(--blue)}.tape.orange{background:var(--orange)}

/* Header */
.site-header{background:rgba(255,252,245,.92);border-bottom:2px solid var(--ink);position:relative;z-index:5}
.site-header .inner{max-width:1240px;margin:0 auto;padding:10px 20px;display:flex;align-items:center;gap:8px 18px;flex-wrap:wrap}
.brand{font-family:var(--font-display);font-weight:900;text-transform:uppercase;font-size:15.5px;line-height:1.1;color:var(--ink);text-decoration:none;letter-spacing:-.01em;margin-right:auto}
.brand small{display:block;font-family:var(--font-mono);font-weight:500;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:2px}
.menu-btn{display:none;border:2px solid var(--ink);background:var(--surface);color:var(--ink);border-radius:6px;padding:5px 12px;font:inherit;font-size:14px;font-weight:600;cursor:pointer}
.site-nav ul{display:flex;flex-wrap:wrap;gap:2px;list-style:none;margin:0;padding:0}
.site-nav a{display:block;padding:6px 10px;border-radius:4px;text-decoration:none;color:var(--ink);font-size:14.5px;font-weight:500}
.site-nav a:hover{background:var(--hover)}
.site-nav a[aria-current="page"]{background:var(--yellow);font-weight:700;clip-path:polygon(0 8%,4% 0,96% 4%,100% 0,100% 92%,95% 100%,4% 96%,0 100%)}
@media (max-width:900px){
  .menu-btn{display:inline-block}
  .site-nav{flex-basis:100%;display:none}
  .site-nav.open{display:block}
  .site-nav ul{flex-direction:column;padding:4px 0 6px}
}

/* Pages */
main{position:relative}
.doc{position:relative;max-width:800px;margin:0 auto;padding:36px 20px 64px}
.doc.wide{max-width:1120px}
.eyebrow{font-family:var(--font-mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);margin:0 0 10px}
h1,h2,h3{font-family:var(--font-display);text-wrap:balance}
.doc h1{font-weight:900;text-transform:uppercase;font-size:clamp(32px,5vw,54px);line-height:.98;letter-spacing:-.02em;margin:0 0 18px;display:inline-block;padding:.08em .24em .02em;background:var(--page-tape,var(--yellow));transform:rotate(-1.2deg);clip-path:polygon(0 5%,3% 0,40% 4%,70% 0,97% 4%,100% 0,99% 50%,100% 100%,60% 96%,30% 100%,2% 95%,0 100%,1% 50%)}
.doc h2{font-weight:900;text-transform:uppercase;font-size:24px;line-height:1.1;letter-spacing:-.01em;margin:44px 0 12px}
.doc h2::after{content:"";display:block;width:56px;height:4px;background:var(--ink);margin-top:10px}
.doc h3{font-weight:800;font-size:19px;line-height:1.25;margin:24px 0 6px}
.lede{font-size:19px;line-height:1.55;max-width:62ch}
.doc p,.doc li{max-width:68ch}
.doc ul,.doc ol{padding-left:22px}
.doc li{margin-bottom:6px}
.doc table{border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:15.5px;background:var(--surface)}
.doc th,.doc td{border-bottom:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}
.doc th{font-family:var(--font-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:500}
.note{border-left:5px solid var(--ink);background:var(--surface);padding:12px 16px;margin:20px 0;box-shadow:3px 3px 0 var(--teal)}
.meta{font-size:14px;color:var(--muted)}
.tag{display:inline-block;font-family:var(--font-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);background:var(--surface);border:1.5px solid var(--ink);border-radius:999px;padding:1px 9px;margin:0 4px 4px 0}
.page-deco{position:absolute;right:max(20px,calc(50% - 560px));top:18px;width:150px;height:auto;pointer-events:none;transform:rotate(4deg)}
@media (max-width:860px){.page-deco{display:none}}

.tools{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}
.btn{display:inline-flex;align-items:center;gap:6px;border:2px solid var(--ink);background:var(--surface);color:var(--ink);border-radius:6px;padding:6px 13px;font:inherit;font-size:14.5px;font-weight:600;cursor:pointer;text-decoration:none;box-shadow:3px 3px 0 var(--ink)}
.btn:hover{transform:translate(1px,1px);box-shadow:2px 2px 0 var(--ink)}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;margin:20px 0}
.tile{position:relative;display:block;background:var(--surface);border:2px solid var(--ink);border-radius:4px;padding:18px 16px 14px;text-decoration:none;color:var(--ink);box-shadow:4px 4px 0 var(--ink);transition:transform .12s}
.tile:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
.tile h3{margin:0 0 6px;font-weight:900;text-transform:uppercase;font-size:18px}
.tile p{margin:0;font-size:15px;color:var(--muted)}

.card{position:relative;background:var(--surface);border:1.5px solid var(--ink);border-radius:3px;padding:22px 20px 16px;margin:16px 0;break-inside:avoid;page-break-inside:avoid;box-shadow:3px 3px 0 rgba(20,20,20,.12)}
.card::before{content:"";position:absolute;top:-9px;left:22px;width:84px;height:18px;background:var(--pink);opacity:.92;transform:rotate(-3deg);clip-path:polygon(0 10%,4% 0,96% 8%,100% 0,98% 100%,3% 92%)}
.card:nth-of-type(4n+2)::before{background:var(--teal);transform:rotate(2deg)}
.card:nth-of-type(4n+3)::before{background:var(--yellow);transform:rotate(-1deg)}
.card:nth-of-type(4n+4)::before{background:var(--blue);transform:rotate(3deg)}
.card h3{margin:0 0 6px}
.card .num{font-family:var(--font-mono);font-size:12px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase;margin:0}
.card dl{margin:10px 0 0;display:grid;grid-template-columns:max-content 1fr;gap:5px 12px;font-size:15.5px}
.card dt{font-weight:700}
.card dd{margin:0}
.cards{columns:2 340px;column-gap:22px}
.cards .card{display:inline-block;width:100%;margin:12px 0 18px}

/* Home: hero */
.hero{position:relative;overflow:hidden;border-bottom:2px solid var(--ink)}
.hero-inner{position:relative;z-index:2;max-width:1180px;margin:0 auto;padding:40px 20px 170px;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:24px;align-items:center}
.title{font-family:var(--font-display);font-weight:900;text-transform:uppercase;font-size:clamp(44px,6.8vw,90px);line-height:.9;letter-spacing:-.03em;margin:0}
.title .l{display:block;width:max-content;max-width:100%}
.title .tape{padding:.02em .12em 0;margin:.04em 0}
.title .l:nth-child(2){transform:rotate(-1.5deg)}
.title .l:nth-child(3){transform:rotate(.8deg)}
.title .l:nth-child(5){transform:rotate(-1deg)}
.title .and{font-size:.6em;margin:.1em 0 0 .06em}
.title .ai{font-size:1.5em;line-height:.85}
.byline{margin:14px 0 0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(16px,1.8vw,21px);line-height:1.2}
.byline .tape{transform:rotate(-1deg)}
.kicker{font-family:var(--font-mono);font-size:14px;letter-spacing:.12em;text-transform:uppercase;margin:22px 0 0;max-width:34ch;line-height:1.5}
.kicker::after{content:"";display:block;width:64px;height:4px;background:var(--ink);margin-top:14px}
.when{font-weight:600;margin:12px 0 0}
.hero-art{position:relative;aspect-ratio:1/1.08;width:100%;max-width:560px;justify-self:center}
.hero-art img{position:absolute;height:auto}
.a-bulb{left:20%;top:0;width:40%;z-index:3}
.a-plant{left:6%;top:28%;width:42%;z-index:2}
.a-laptop{left:18%;top:55%;width:68%;z-index:4;transform:rotate(-2deg)}
.a-ai{left:0;top:67%;width:30%;z-index:1;opacity:.95}
.a-critical{right:0;top:3%;width:36%;z-index:5;transform:rotate(-4deg)}
.a-creative{right:3%;top:18%;width:34%;z-index:5;transform:rotate(2deg)}
.a-practical{right:0;top:32%;width:34%;z-index:5;transform:rotate(-3deg)}
.a-collective{right:5%;top:46%;width:32%;z-index:5;transform:rotate(2deg)}
.deco-corner{position:absolute;left:0;top:0;width:240px;pointer-events:none;z-index:0}
.deco-mountains{position:absolute;left:0;bottom:-6px;width:260px;pointer-events:none;z-index:1}
.deco-forest{position:absolute;right:0;bottom:-6px;width:360px;pointer-events:none;z-index:1}
@media (max-width:860px){
  .hero-inner{grid-template-columns:1fr;padding:28px 20px 90px}
  .hero-art{max-width:420px;order:2}
  .deco-corner{width:150px}
  .deco-mountains{width:180px}.deco-forest{width:220px}
}

/* Home: agenda */
.agenda{list-style:none;margin:20px 0 0;padding:0;border-left:3px solid var(--ink)}
.agenda li{position:relative;display:grid;grid-template-columns:76px 1fr;gap:6px 16px;padding:16px 0 16px 18px;max-width:none}
.agenda li::before{content:"";position:absolute;left:-9px;top:24px;width:15px;height:15px;background:var(--surface);border:3px solid var(--ink);border-radius:50%}
.agenda time{font-family:var(--font-mono);font-size:15px;font-weight:500;padding-top:3px}
.agenda h3{margin:0 0 4px;font-size:20px}
.agenda p{margin:0 0 8px}
.agenda li.pause{padding:6px 0 6px 18px;color:var(--muted)}
.agenda li.pause::before{width:11px;height:11px;left:-7px;top:13px;border-width:2px;background:var(--line)}
.agenda li.pause time{padding-top:0}
.agenda li.pause span{font-family:var(--font-mono);font-size:13px;letter-spacing:.1em;text-transform:uppercase}
.res{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.res a,.res span{display:inline-flex;align-items:center;font-size:13.5px;font-weight:600;text-decoration:none;color:var(--ink);border:1.5px solid var(--ink);border-radius:999px;padding:2px 11px;background:var(--surface)}
.res a:hover{background:var(--yellow)}
.res span{border-style:dashed;color:var(--muted);font-weight:500}
.leave li{margin-bottom:10px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:28px}
@media (max-width:760px){.two{grid-template-columns:1fr}}
.contact{font-family:var(--font-mono);font-size:14px;line-height:1.7}

/* Footer */
.site-footer{border-top:2px solid var(--ink);background:rgba(255,252,245,.92);font-size:14px;color:var(--muted)}
.site-footer .inner{max-width:1240px;margin:0 auto;padding:16px 20px;display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
.site-footer a{color:var(--muted)}

@media print{
  .site-header,.site-footer,.tools,.skip,.no-print,.page-deco,.hero-art,.deco-corner,.deco-mountains,.deco-forest{display:none!important}
  body{background:#fff;color:#000;font-size:12pt}
  .doc{max-width:none;padding:0}
  .doc h1{background:none;transform:none;clip-path:none;padding:0}
  .card{border:1px solid #888;background:#fff;box-shadow:none}
  .card::before{display:none}
  a{color:#000;text-decoration:none}
  h2{break-after:avoid}
}
@media (prefers-reduced-motion: reduce){*{transition:none!important;animation:none!important}}
"""

NAV_JS = """<script>(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('site-nav');if(!b||!n)return;b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');});})();</script>"""


def header(current):
    items = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == current else ""}>{label}</a></li>'
        for key, label, href in NAV
    )
    return (
        '<a class="skip" href="#main">Skip to content</a>'
        '<header class="site-header"><div class="inner">'
        f'<a class="brand" href="index.html">{SITE["name"]}<small>{SITE["byline"]}</small></a>'
        '<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>'
        f'<nav class="site-nav" id="site-nav" aria-label="Site"><ul>{items}</ul></nav>'
        '</div></header>'
    )


def footer():
    return (
        '<footer class="site-footer"><div class="inner">'
        f'<span>{SITE["credit"]}</span>'
        f'<span>{SITE["updated"]} · <a href="{SITE["repo"]}">Source and offline copy</a></span>'
        '</div></footer>'
    )


def page(title, current, body_html, desc="", og=False):
    style = PAGE_STYLE.get(current, {})
    tape = f'<style>:root{{--page-tape:var(--{style["tape"]})}}</style>' if style.get("tape") else ""
    deco = f'<img class="page-deco" src="assets/{style["deco"]}" alt="">' if style.get("deco") else ""
    ogtags = ""
    if og:
        ogtags = (f'<meta property="og:title" content="{html.escape(title)}">'
                  f'<meta property="og:description" content="{html.escape(desc)}">'
                  f'<meta property="og:image" content="{SITE["url"]}assets/cover.jpg">'
                  f'<meta property="og:url" content="{SITE["url"]}">')
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{html.escape(title)}</title>\n'
        f'<meta name="description" content="{html.escape(desc)}">{ogtags}\n'
        f'{FONTS}\n<style>{BASE_CSS}</style>{tape}\n</head>\n<body>\n'
        f'{header(current)}\n<main id="main">{deco}\n{body_html}\n</main>\n{footer()}\n{NAV_JS}\n</body>\n</html>\n'
    )


def md(text):
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def build_map():
    src = MAP_SRC.read_text()
    # Scope the map's own footer rules so they don't touch the site footer.
    src = src.replace("\nfooter{", "\n.page > footer{").replace("\nfooter p{", "\n.page > footer p{")
    src = src.replace("\nfooter details summary{", "\n.page > footer details summary{")
    src = src.replace("\nfooter ul{", "\n.page > footer ul{").replace("\nfooter a{", "\n.page > footer a{")
    src = src.replace(FONTS_MAP_OLD, FONTS) if FONTS_MAP_OLD in src else src
    # Site frame CSS goes before the map's own CSS; the palette override goes after it.
    src = src.replace("<style>", "<style>" + BASE_CSS + "\n", 1)
    override = ("<style>:root:not(#_){" + TOKENS + "}"
                "body{background:var(--bg) url(assets/paper.jpg) repeat;background-size:1100px auto}"
                ".map-card,.panel{border:2px solid var(--ink);border-radius:4px;box-shadow:4px 4px 0 var(--ink)}"
                ".page h1{font-weight:900;text-transform:uppercase;letter-spacing:-.02em}"
                ".tab[aria-selected=\"true\"]{border-bottom-color:var(--ink);background:var(--yellow)}"
                "</style>\n</head>")
    src = src.replace("</head>", override, 1)
    src = src.replace("<body>\n", "<body>\n" + header("map") + '\n<main id="main">\n', 1)
    src = src.replace("\n<script>", "\n</main>\n" + footer() + "\n" + NAV_JS + "\n<script>", 1)
    src = src.replace(
        '<p>Idea adapted from the AI map in ThinkBeyondAI\'s AI Basics course.</p>',
        '<p>Idea adapted from the AI map in ThinkBeyondAI\'s AI Basics course.</p>\n    <p>Link to any entry: add its name after a #, for example <code>map.html#o-k-detect</code> opens the AI detectors.</p>',
    )
    return src


FONTS_MAP_OLD = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PAGES + SCENARIO_PAGES:
        body = p["html"] if "html" in p else md(p["md"])
        (OUT / p["file"]).write_text(page(p["title"], p["nav"], body, p.get("desc", ""), og=p["file"] == "index.html"))
    (OUT / "map.html").write_text(build_map())
    for f in OUT.glob("*.html"):
        t = f.read_text()
        if "—" in t:
            print("EM DASH in", f.name, [m.start() for m in re.finditer("—", t)][:5])
    print("built", sorted(x.name for x in OUT.glob("*.html")))


if __name__ == "__main__":
    main()
