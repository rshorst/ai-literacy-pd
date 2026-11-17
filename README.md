# AI literacy for teachers

Free professional learning resources on AI for teachers, by Rachel Horst (University of British Columbia).

**Site:** https://rshorst.github.io/ai-literacy-pd/

## What's here

| Page | File |
|---|---|
| Home | `index.html` |
| AI map: who makes what in AI | `map.html` |
| Scenario cards | `cards.html` |
| Activities | `activities.html` |
| Handouts | `handouts.html`, `what-these-systems-are.html`, `practical-moves.html`, `class-ai-agreement.html`, `copilot-and-prompting.html` |
| Readings | `readings.html` |
| Policy examples | `policies.html` |
| Frameworks | `frameworks.html` |

## Offline use

Every page is a single self-contained HTML file and runs offline in any browser. To keep the links between pages working, download this repository as a zip (green **Code** button, then **Download ZIP**), unzip it, and open `index.html`.

## Editing

The pages are generated from `_build/content.py` (all page text) and `_build/map-source.html` (the AI map). To change something, edit those files and run:

```
python3 _build/build.py
```

That rewrites the HTML pages in the top folder. Editing the HTML pages directly also works, but the next build will overwrite those edits.

## Licence

Text and pages © 2026 Rachel Horst, shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Linked readings and policies belong to their authors.
