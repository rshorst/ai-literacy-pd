"""The day, block by block: the home page agenda and one page per block.

Edit a block here and rebuild. Each block has the plan's description (word for word),
"What we'll do" steps (draft), and the materials for that block.
"""
import html
from scenarios import COPILOT_URL

ED = "https://claude.ai/artifact/WSF2rJt3rngbyucXuhWF9N"  # interactive Entangled Dimensions
FUT = "https://rshorst.github.io/AI-Futures/"
PADLET = "https://padlet.com/embed/s025k2ljostv9t2zbjfr"
QD = "https://quickdraw.withgoogle.com/"


def esc(s):
    return html.escape(s, quote=False)


# A block: file, start, end, title, desc (the plan's words), chips (home page links),
# steps (what we'll do), tiles (materials: href, title, blurb), optional note and embed.
# A pause: {"pause": "Break", "start": "10:25"}.
DAY = [
    {
        "file": "welcome.html", "start": "9:00", "end": "9:15", "title": "Welcome",
        "desc": "A chance to reconnect, introduce the day, and begin with what matters to us in teaching and learning.",
        "chips": [("metaphor.html", "My AI Metaphor"), ("quickdraw.html", "Quick, Draw!")],
        "steps": [
            "Welcome, introductions, and where I’m coming from.",
            "A look at the day ahead.",
            "My AI Metaphor: what is your AI metaphor, and what emotion or feeling do you associate with it? Add it to the board, or to the poster on a sticky note.",
            "Quick, Draw!: play a round, then look at what the neural network learned from other people’s drawings.",
        ],
        "embed": f'<div class="board"><iframe src="{PADLET}" title="My AI Metaphor board" allow="clipboard-write" loading="lazy"></iframe></div>',
        "tiles": [
            ("metaphor.html", "My AI Metaphor", "The board, and a paper version with a poster and table cards."),
            (QD, "Play Quick, Draw!", "Opens the game in a new tab."),
            ("quickdraw.html", "About Quick, Draw!", "How it learns, what gets left out, and what Google did with the drawings."),
        ],
    },
    {
        "file": "systems.html", "start": "9:15", "end": "9:40", "title": "What are these strange systems, anyway?",
        "desc": "A plain-language introduction to how generative AI systems compose outputs, and the minimum technical background we need to make informed decisions about them. Then we experiment and see what happens.",
        "chips": [("talk.html", "Talk slides"), ("map.html", "AI map")],
        "steps": [
            "What we call AI: many kinds of systems, not one thing.",
            "How a language model composes text, one likely next piece at a time.",
            "A live demo, then we experiment and see what happens.",
            "Plausible is not the same as true.",
            "The iceberg: what sits underneath a chatbot.",
            "Three questions to carry into the rest of the day.",
        ],
        "tiles": [
            ("talk.html", "Talk slides", "The slides for this block."),
            ("map.html", "AI map", "Who makes what, what each model takes in and gives back, and what each app can do."),
            ("map.html#o-k-detect", "Other kinds of AI", "Detectors, recommenders, risk scores and the rest."),
        ],
    },
    {
        "file": "scenarios.html", "start": "9:40", "end": "10:25", "title": "Classroom situations",
        "desc": "Small groups work through real and plausible situations involving generative AI in teaching and learning. We look closely at what is happening, what choices are available, and what different responses might mean for students, teachers, and the classroom.",
        "chips": [("scenarios.html", "Classroom situations"), ("responses.html", "Shared board")],
        "existing": True,  # the cases page is this block's page
    },
    {"pause": "Break", "start": "10:25"},
    {
        "file": "copilot.html", "start": "10:40", "end": "11:25", "title": "Some things worth trying in Copilot",
        "desc": "A hands-on look at a small number of useful things generative AI can do for teaching: generating alternatives, explaining something in different ways, creating examples and counterexamples, testing instructions, looking for gaps, and helping you see a lesson from another angle. Try a few with something you actually teach and decide what is useful, what is not, and what you would want to change.",
        "chips": [("copilot-and-prompting.html", "Copilot and prompting"), ("practical-moves.html", "Practical moves")],
        "steps": [
            "A short demo of a few things worth trying: generating alternatives, explaining something in different ways, examples and counterexamples, testing instructions, looking for gaps, and seeing a lesson from another angle.",
            "Try a few yourself with something you actually teach, using the links below.",
            "Decide what was useful, what was not, and what you would want to change.",
        ],
        "tiles": [
            (COPILOT_URL, "Open Copilot", "Opens in a new tab."),
            ("copilot-and-prompting.html", "Copilot and prompting", "Prompting strategies, and the limits of Copilot in a school account."),
            ("practical-moves.html", "Practical moves", "What is worth doing, what to skip, and how to tell."),
        ],
    },
    {
        "file": "fit.html", "start": "11:25", "end": "11:55", "title": "How should AI fit into classroom work?",
        "desc": "A look at several ways educators and schools are approaching AI use in learning and assessment, from blanket rules to more nuanced frameworks such as the AI Assessment Scale. We consider what each approach makes possible, what assumptions it carries, and where it might break down in different K-12 contexts. Then we use a collaborative protocol to make decisions about AI use in a real classroom activity or assignment.",
        "chips": [("aias.html", "AI Assessment Scale"), ("class-ai-agreement.html", "Collaborative protocol")],
        "steps": [
            "Several approaches, from blanket rules to frameworks such as the AI Assessment Scale.",
            "For each: what it makes possible, what it assumes, and where it might break down in a K-12 classroom.",
            "Use the collaborative protocol to decide about AI use in a real activity or assignment.",
        ],
        "tiles": [
            ("aias.html", "AI Assessment Scale", "Five kinds of task, from no AI to AI exploration."),
            ("class-ai-agreement.html", "Collaborative protocol", "Deciding together, with students, how AI is used in the room."),
        ],
    },
    {"pause": "Lunch", "start": "11:55"},
    {
        "file": "rethinking.html", "start": "12:45", "end": "1:45", "title": "Rethinking something you already teach",
        "desc": "Bring a lesson, activity, assignment, or unit you already teach. We use what we have explored so far to reconsider where AI might support the learning, where it might change or bypass something important, and where it may not belong at all.",
        "chips": [("activities.html#activity-11", "Activities for educators"), ("readings.html", "Readings on assessment")],
        "steps": [
            "Bring a lesson, activity, assignment or unit you already teach.",
            "Where might AI support the learning? Where might it change or bypass something important? Where may it not belong at all?",
            "Redesign one part, and name what the redesign protects.",
        ],
        "tiles": [
            ("aias.html", "AI Assessment Scale", "Which kind of task is this, and why?"),
            ("activities.html#activity-11", "Activities for educators", "Short moves for a staff meeting or workshop."),
            ("readings.html", "Readings on assessment", "Research and practice to draw on."),
        ],
    },
    {
        "file": "bigger-picture.html", "start": "1:45", "end": "2:15", "title": "Looking at the bigger picture",
        "desc": "We use the Entangled Dimensions of AI Literacy framework to step back from individual classroom uses and explore some of the wider questions connected to AI: knowledge, relationships, institutions, resources, values, and planetary systems. Participants explore the framework themselves and use it to look at a classroom example, question, or concern from another angle.",
        "chips": [("frameworks.html", "Frameworks"), ("map.html#o-k-rec", "Other kinds of AI")],
        "steps": [
            "A short introduction to the Entangled Dimensions of AI Literacy.",
            "Explore the framework yourselves.",
            "Use it to look at a classroom example, question or concern from another angle.",
        ],
        "embed": f'<a class="launch" href="{ED}" target="_blank" rel="noopener"><span class="big">Open the Entangled Dimensions ↗</span><span class="small">The interactive framework, with a classroom activity for each dimension.</span></a>',
        "tiles": [
            ("frameworks.html", "Frameworks", "The frameworks behind the day."),
            ("map.html#o-k-rec", "Other kinds of AI", "The systems around us that are not chatbots."),
        ],
    },
    {"pause": "Break", "start": "2:15"},
    {
        "file": "collective.html", "start": "2:25", "end": "2:50", "title": "From classroom choices to collective decisions",
        "desc": "We bring together the questions that have surfaced throughout the day and consider what can be decided by an individual educator, what may need shared school guidance, and what calls for broader community conversation. We look at emerging approaches elsewhere as possibilities to examine, not templates to adopt.",
        "note": "What needs to be decided here, who needs to be part of that decision, and what should remain open?",
        "chips": [("policies.html", "Policy examples"), ("activities.html#activity-13", "The document audit")],
        "steps": [
            "Gather the questions that came up through the day.",
            "Sort them: what an individual educator can decide, what may need shared school guidance, and what calls for broader community conversation.",
            "Look at approaches from elsewhere as possibilities to examine, not templates to adopt.",
        ],
        "tiles": [
            ("responses.html", "Shared board", "The groups’ responses from the morning."),
            ("policies.html", "Policy examples", "What other schools and districts have written."),
            ("activities.html#activity-13", "The document audit", "What do we already say that covers this?"),
        ],
    },
    {
        "file": "close.html", "start": "2:50", "end": "3:00", "title": "Close",
        "desc": "We close by imagining the kinds of futures with AI we would want to move toward, and the ones we would want to resist.",
        "chips": [(FUT, "AI Futures map")],
        "steps": [
            "Imagine the futures with AI we would want to move toward, and the ones we would want to resist.",
        ],
        "tiles": [
            (FUT, "AI Futures map", "Where voices on AI place our futures."),
            ("metaphor.html", "My AI Metaphor", "The board from this morning."),
        ],
    },
]

BLOCKS = [b for b in DAY if "pause" not in b]


def _href(h):
    ext = h.startswith("http")
    return f'href="{h}"' + (' target="_blank" rel="noopener"' if ext else "")


def agenda_html():
    out = ['<ol class="agenda">']
    for b in DAY:
        if "pause" in b:
            out.append(f'<li class="pause"><time>{b["start"]}</time><span>{esc(b["pause"])}</span></li>')
            continue
        note = f'<p><em>{esc(b["note"])}</em></p>' if b.get("note") else ""
        chips = "".join(f'<a {_href(h)}>{esc(t)}</a>' for h, t in b["chips"])
        out.append(f'<li><time>{b["start"]}</time><div><h3><a href="{b["file"]}">{esc(b["title"])}</a></h3>'
                   f'<p>{esc(b["desc"])}</p>{note}<p class="res">{chips}</p></div></li>')
    out.append("</ol>")
    return "\n".join(out)


AGENDA = agenda_html()


def pager(i):
    prev_b = BLOCKS[i - 1] if i > 0 else None
    next_b = BLOCKS[i + 1] if i < len(BLOCKS) - 1 else None
    p = '<nav class="pager" aria-label="The day">'
    p += (f'<a href="{prev_b["file"]}"><small>← {prev_b["start"]}</small>{esc(prev_b["title"])}</a>'
          if prev_b else '<a href="index.html"><small>← The day</small>Home</a>')
    p += (f'<a href="{next_b["file"]}"><small>{next_b["start"]} →</small>{esc(next_b["title"])}</a>'
          if next_b else '<a href="index.html"><small>The day →</small>Home</a>')
    return p + "</nav>"


CSS = """<style>
.steps{counter-reset:st;list-style:none;padding:0!important;margin:16px 0 8px;max-width:68ch}
.steps li{counter-increment:st;position:relative;padding:4px 0 10px 50px;min-height:40px}
.steps li::before{content:counter(st);position:absolute;left:0;top:0;width:34px;height:34px;display:grid;place-items:center;background:var(--ink);color:var(--surface);font-family:var(--font-mono);font-weight:500;font-size:15px;border-radius:50%}
.note-q{font-family:var(--font-display);font-weight:800;font-size:clamp(20px,2.4vw,26px);line-height:1.25;background:var(--surface);border:2px solid var(--ink);box-shadow:5px 5px 0 var(--yellow);padding:16px 20px;margin:22px 0;max-width:62ch}
.launch{display:block;text-decoration:none;color:var(--ink);background:var(--yellow);border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);padding:30px 24px;margin:18px 0 22px;text-align:center}
.launch:hover{box-shadow:7px 7px 0 var(--ink)}
.launch .big{display:block;font-family:var(--font-display);font-weight:900;text-transform:uppercase;font-size:clamp(24px,3.6vw,36px);line-height:1.05}
.launch .small{display:block;margin-top:10px;font-size:15px}
.board{border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);background:#f4f4f4;overflow:hidden;margin:16px 0 22px}
.board iframe{display:block;width:100%;height:560px;border:0}
@media (max-width:700px){.board iframe{height:440px}}
.pager{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:44px;border-top:2px solid var(--ink);padding-top:14px;max-width:none}
.pager a{text-decoration:none;font-weight:700;color:var(--ink);max-width:46%}
.pager a:last-child{text-align:right;margin-left:auto}
.pager small{display:block;font-family:var(--font-mono);font-weight:500;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
</style>"""


def section_page(i):
    b = BLOCKS[i]
    steps = "".join(f"<li>{esc(s)}</li>" for s in b["steps"])
    tiles = "".join(f'<a class="tile" {_href(h)}><h3>{esc(t)}{" ↗" if h.startswith("http") else ""}</h3><p>{esc(d)}</p></a>'
                    for h, t, d in b["tiles"])
    note = f'<p class="note-q">{esc(b["note"])}</p>' if b.get("note") else ""
    body = f"""{CSS}
<div class="doc wide">
<p class="eyebrow"><a href="index.html">The day</a> · {b['start']} to {b['end']}</p>
<h1>{esc(b['title'])}</h1>
<p class="lede">{esc(b['desc'])}</p>
{note}
<h2>What we’ll do</h2>
<ol class="steps">{steps}</ol>
{b.get('embed', '')}
<h2>Materials</h2>
<div class="grid">{tiles}</div>
{pager(i)}
</div>"""
    return {"file": b["file"], "nav": "home",
            "title": f"{b['title']} · Teaching with, about, and without AI",
            "desc": b["desc"], "html": body}


SECTION_PAGES = [section_page(i) for i, b in enumerate(BLOCKS) if not b.get("existing")]

# The cases page is the 9:40 block's page: give it the block's time and the day's pager.
import scenarios  # noqa: E402
_i = next(i for i, b in enumerate(BLOCKS) if b["file"] == "scenarios.html")
_idx = scenarios.SCENARIO_PAGES[0]
_idx["html"] = _idx["html"].replace('<p class="eyebrow">Classroom situations</p>',
                                    f'<p class="eyebrow"><a href="index.html">The day</a> · {BLOCKS[_i]["start"]} to {BLOCKS[_i]["end"]} · Classroom situations</p>', 1)
_idx["html"] = _idx["html"][: _idx["html"].rindex("</div>")] + pager(_i) + "\n</div>"
