#!/usr/bin/env python3
"""Builds the ai-literacy-pd site as flat, self-contained HTML pages.

Every page carries its own CSS so it works when opened on its own, offline.
Links between pages are relative file links (map.html, cards.html), which work
both on GitHub Pages and from a downloaded folder.
"""
import re, sys, html
from pathlib import Path
import markdown

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent
MAP_SRC = HERE / "map-source.html"
sys.path.insert(0, str(HERE))
from content import PAGES, NAV, SITE  # noqa: E402

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">'

BASE_CSS = r"""
/* Site frame: same tokens as the AI map so every page reads as one family. */
:root{--bg:#edf0ef;--surface:#fbfcfc;--ink:#17202a;--muted:#5a6570;--line:#c3cbcf;--accent:#0b5cad;--hover:#e6ecf1;
--c-company:#2f3b48;--c-model:#0b7a6a;--c-app:#2b52c4;--c-cat:#9c5a05;--c-concept:#99286f;
--font-display:"Archivo","Helvetica Neue",Arial,sans-serif;--font-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--font-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;color-scheme:light}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#10151a;--surface:#171f27;--ink:#e5eaee;--muted:#9aa6b1;--line:#36424d;--accent:#72b2ff;--hover:#22303c;--c-company:#c5cfd9;--c-model:#3cc4ae;--c-app:#8ea8ff;--c-cat:#e2a64c;--c-concept:#e57cc3;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#10151a;--surface:#171f27;--ink:#e5eaee;--muted:#9aa6b1;--line:#36424d;--accent:#72b2ff;--hover:#22303c;--c-company:#c5cfd9;--c-model:#3cc4ae;--c-app:#8ea8ff;--c-cat:#e2a64c;--c-concept:#e57cc3;color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--font-body);font-size:16px;line-height:1.6}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-999px;top:8px;background:var(--surface);padding:8px 12px;border-radius:6px;z-index:50}
.skip:focus{left:12px}

.site-header{background:var(--surface);border-bottom:1px solid var(--line)}
.site-header .inner{max-width:1240px;margin:0 auto;padding:10px 20px;display:flex;align-items:center;gap:8px 18px;flex-wrap:wrap}
.brand{font-family:var(--font-display);font-weight:800;font-size:17px;color:var(--ink);text-decoration:none;letter-spacing:-.01em;margin-right:auto}
.brand small{display:block;font-family:var(--font-mono);font-weight:500;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.menu-btn{display:none;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:6px 12px;font:inherit;font-size:14px;cursor:pointer}
.site-nav ul{display:flex;flex-wrap:wrap;gap:2px;list-style:none;margin:0;padding:0}
.site-nav a{display:block;padding:6px 10px;border-radius:6px;text-decoration:none;color:var(--muted);font-size:14.5px;font-weight:500}
.site-nav a:hover{background:var(--hover);color:var(--ink)}
.site-nav a[aria-current="page"]{color:var(--ink);background:var(--hover);font-weight:600}
@media (max-width:860px){
  .menu-btn{display:inline-block}
  .site-nav{flex-basis:100%;display:none}
  .site-nav.open{display:block}
  .site-nav ul{flex-direction:column;padding:4px 0 6px}
}

.doc{max-width:780px;margin:0 auto;padding:32px 20px 56px}
.doc.wide{max-width:1100px}
.eyebrow{font-family:var(--font-mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
h1{font-family:var(--font-display);font-weight:800;font-size:clamp(28px,4vw,40px);line-height:1.1;margin:0 0 12px;letter-spacing:-.01em;text-wrap:balance}
h2{font-family:var(--font-display);font-weight:700;font-size:23px;line-height:1.2;margin:36px 0 10px;text-wrap:balance}
h3{font-family:var(--font-display);font-weight:700;font-size:18px;line-height:1.3;margin:24px 0 6px}
.lede{font-size:18px;max-width:65ch}
.doc p,.doc li{max-width:68ch}
.doc ul,.doc ol{padding-left:22px}
.doc li{margin-bottom:6px}
.doc table{border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:15px}
.doc th,.doc td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
.doc th{font-family:var(--font-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500}
.note{border-left:3px solid var(--accent);background:var(--hover);padding:10px 14px;border-radius:0 8px 8px 0;margin:18px 0}
.meta{font-size:14px;color:var(--muted)}
.tag{display:inline-block;font-family:var(--font-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin:0 4px 4px 0}

.tools{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}
.btn{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:7px 12px;font:inherit;font-size:14px;cursor:pointer;text-decoration:none}
.btn:hover{background:var(--hover)}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;margin:18px 0}
.tile{display:block;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 16px 14px;text-decoration:none;color:var(--ink)}
.tile:hover{border-color:var(--accent)}
.tile h3{margin:0 0 4px}
.tile p{margin:0;font-size:14.5px;color:var(--muted)}

.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:14px 0;break-inside:avoid;page-break-inside:avoid}
.card h3{margin:0 0 6px}
.card .num{font-family:var(--font-mono);font-size:12px;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}
.card dl{margin:10px 0 0;display:grid;grid-template-columns:max-content 1fr;gap:4px 12px;font-size:15px}
.card dt{font-weight:600}
.card dd{margin:0}
.cards{columns:2 340px;column-gap:16px}
.cards .card{display:inline-block;width:100%;margin:0 0 16px}

.site-footer{border-top:1px solid var(--line);background:var(--surface);font-size:14px;color:var(--muted)}
.site-footer .inner{max-width:1240px;margin:0 auto;padding:16px 20px;display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
.site-footer a{color:var(--muted)}

@media print{
  .site-header,.site-footer,.tools,.skip,.no-print{display:none!important}
  body{background:#fff;color:#000;font-size:12pt}
  .doc{max-width:none;padding:0}
  .card{border:1px solid #888;background:#fff}
  a{color:#000;text-decoration:none}
  h2{break-after:avoid}
}
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


def page(title, current, body_html, desc=""):
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{html.escape(title)}</title>\n'
        f'<meta name="description" content="{html.escape(desc)}">\n'
        f'{FONTS}\n<style>{BASE_CSS}</style>\n</head>\n<body>\n'
        f'{header(current)}\n<main id="main">\n{body_html}\n</main>\n{footer()}\n{NAV_JS}\n</body>\n</html>\n'
    )


def md(text):
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def build_map():
    src = MAP_SRC.read_text()
    # Scope the map's own footer rules so they don't touch the site footer.
    src = src.replace("\nfooter{", "\n.page > footer{").replace("\nfooter p{", "\n.page > footer p{")
    src = src.replace("\nfooter details summary{", "\n.page > footer details summary{")
    src = src.replace("\nfooter ul{", "\n.page > footer ul{").replace("\nfooter a{", "\n.page > footer a{")
    # Site frame CSS goes before the map's own CSS.
    src = src.replace("<style>", "<style>" + BASE_CSS + "\n", 1)
    src = src.replace("<body>\n", "<body>\n" + header("map") + '\n<main id="main">\n', 1)
    src = src.replace("\n<script>", "\n</main>\n" + footer() + "\n" + NAV_JS + "\n<script>", 1)
    src = src.replace(
        '<p>Idea adapted from the AI map in ThinkBeyondAI\'s AI Basics course.</p>',
        '<p>Idea adapted from the AI map in ThinkBeyondAI\'s AI Basics course.</p>\n    <p>Link to any entry: add its name after a #, for example <code>map.html#o-k-detect</code> opens the AI detectors.</p>',
    )
    return src


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PAGES:
        body = p["html"] if "html" in p else md(p["md"])
        (OUT / p["file"]).write_text(page(p["title"], p["nav"], body, p.get("desc", "")))
    (OUT / "map.html").write_text(build_map())
    # sanity: no em dashes anywhere in output
    for f in OUT.glob("*.html"):
        t = f.read_text()
        if "—" in t:
            print("EM DASH in", f.name, [m.start() for m in re.finditer("—", t)][:5])
    print("built", sorted(x.name for x in OUT.glob("*.html")))


if __name__ == "__main__":
    main()
