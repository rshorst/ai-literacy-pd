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
        "file": "welcome.html", "tab": "Welcome", "start": "9:00", "end": "9:15", "title": "Welcome",
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
        "file": "systems.html", "tab": "Strange systems", "start": "9:15", "end": "9:40", "title": "What are these strange systems, anyway?",
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
        "file": "scenarios.html", "tab": "Classroom situations", "start": "9:40", "end": "10:25", "title": "Classroom situations",
        "desc": "Small groups work through real and plausible situations involving generative AI in teaching and learning. We look closely at what is happening, what choices are available, and what different responses might mean for students, teachers, and the classroom.",
        "chips": [("scenarios.html", "Classroom situations"), ("responses.html", "Shared board")],
        "existing": True,  # the cases page is this block's page
    },
    {"pause": "Break", "start": "10:25"},
    {
        "file": "copilot.html", "tab": "Copilot", "start": "10:40", "end": "11:25", "title": "Some things worth trying in Copilot",
        "desc": "A hands-on look at a small number of useful things generative AI can do for teaching: generating alternatives, explaining something in different ways, creating examples and counterexamples, testing instructions, looking for gaps, and helping you see a lesson from another angle. Try a few with something you actually teach and decide what is useful, what is not, and what you would want to change.",
        "chips": [("copilot-and-prompting.html", "Copilot and prompting"), ("practical-moves.html", "Practical moves")],
        "steps": [
            "A short demo of a few things worth trying: generating alternatives, explaining something in different ways, examples and counterexamples, testing instructions, looking for gaps, and seeing a lesson from another angle.",
            "Try a few yourself with something you actually teach, using the links below.",
            "Decide what was useful, what was not, and what you would want to change.",
        ],
        "after_steps": "copilot_demo",
        "tiles": [
            ("copilot-and-prompting.html", "Copilot and prompting", "Prompting strategies, and the limits of Copilot in a school account."),
            ("practical-moves.html", "Practical moves", "What is worth doing, what to skip, and how to tell."),
        ],
    },
    {
        "file": "fit.html", "tab": "How AI fits", "start": "11:25", "end": "11:55", "title": "How should AI fit into classroom work?",
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
        "file": "rethinking.html", "tab": "Rethinking", "start": "12:45", "end": "1:45", "title": "Rethinking something you already teach",
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
        "file": "bigger-picture.html", "tab": "Bigger picture", "start": "1:45", "end": "2:15", "title": "Looking at the bigger picture",
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
        "file": "collective.html", "tab": "Collective decisions", "start": "2:25", "end": "2:50", "title": "From classroom choices to collective decisions",
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
        "file": "close.html", "tab": "Close", "start": "2:50", "end": "3:00", "title": "Close",
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


# ---------------------------------------------------------------- The Copilot demo (10:40)
MS = "https://support.microsoft.com/"
DEMOS = [
    ("Your notebook as a curated knowledge environment", "4 min", "Copilot app → Notebooks",
     "Open the AI Literacy Notebook. Show its sources, add one, and ask the same question again.",
     "What changed when the sources changed? What can it not say, because it isn’t in the notebook?",
     MS + "microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks"),
    ("Citation detective", "3 min", "Notebook → ask → open a citation",
     "Ask a question, then open the source Copilot cites.",
     "Does the source really support the answer, or only sit near it?",
     MS + "microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works"),
    ("Study guide", "3 min", "Notebook → Create → Study guide",
     "Turn the same readings into questions, quizzes and flashcards.",
     "What do these questions assess? What would a student learn by answering them?",
     MS + "microsoft-365-copilot/create-a-copilot-notebook-study-guide"),
    ("Infographic", "3 min", "Notebook → Create → Infographic",
     "Ask Copilot to visualize the main dimensions of AI literacy.",
     "What does it turn into simple categories? What relationships does it miss? Does the visual look more authoritative than its sources justify?",
     MS + "en-us/microsoft-365-copilot/infographics-copilot-notebooks"),
    ("Teach: a lesson plan", "3 min", "Copilot app → Teach → Lesson plan",
     "Create a lesson for something you teach.",
     "What does it assume about the students, the place and what counts as learning?",
     MS + "en-us/education/lesson-plan-creation-with-ai"),
    ("Teach: modify content", "4 min", "Copilot app → Teach → Modify content",
     "Change the reading level or language of a text.",
     "Did it make the text more accessible without removing the intellectual challenge?",
     "https://learn.microsoft.com/training/modules/create-instructional-materials-teach-microsoft-365-copilot/"),
    ("Study and Learn agent", "3 min", "Copilot app → Agents → Study and Learn",
     "Ask it the same question you asked Copilot Chat.",
     "How does question-led coaching differ from an answer-generating chatbot? Which one would your students choose?",
     MS + "en-us/education/copilot/study-learn-agent"),
]
TUTORIALS = [
    ("https://learn.microsoft.com/training/modules/enhance-teaching-learning-microsoft-copilot/", "Enhance teaching and learning with Copilot Chat", "Microsoft Learn. A beginner’s guide to prompting and evaluating responses."),
    ("https://learn.microsoft.com/training/modules/create-instructional-materials-teach-microsoft-365-copilot/", "Create instructional materials with Teach", "Microsoft Learn. Lesson plans, rubrics, quizzes, flashcards and differentiation."),
    (MS + "en-US/education/copilot/copilot-notebook-study-guide", "Copilot Notebook Study Guide", "Microsoft Support. Summaries, topic pages, quizzes and flashcards from your own materials."),
    (MS + "en-us/education/copilot/study-learn-agent", "Study and Learn agent", "Microsoft Support. What it is and who can use it."),
]


def copilot_demo_html():
    items = "".join(
        f'<li><div class="dh"><h3>{esc(t)}</h3><span class="dmin">{esc(m)}</span></div>'
        f'<p class="dpath">{esc(path)}</p><p>{esc(do)}</p><p class="dask"><b>Ask:</b> {esc(ask)}</p>'
        f'<p class="dlink"><a href="{url}" target="_blank" rel="noopener">How to do it ↗</a></p></li>'
        for t, m, path, do, ask, url in DEMOS)
    tut = "".join(f'<a class="tile" href="{h}" target="_blank" rel="noopener"><h3>{esc(t)} ↗</h3><p>{esc(d)}</p></a>' for h, t, d in TUTORIALS)
    return f"""<h2>The demo</h2>
<p>Seven short demonstrations, each followed straight away by a question. The centre is a Copilot Notebook on AI literacy: what changes when you choose the sources, how it represents knowledge, and how source material becomes a learning activity.</p>
<ol class="demos">{items}</ol>
<h2>Before you try it</h2>
<ul>
<li>Use your school Microsoft account. Notebooks, Teach and Study and Learn are in the Microsoft 365 Copilot app.</li>
<li>Your school’s IT has to turn on Copilot Chat. For students aged 13 to 17, IT also has to enable it before they can use Study and Learn.</li>
<li>Some notebook features, such as audio overviews, need a paid Copilot licence.</li>
<li>Don’t add personal or student information to a notebook or a chat.</li>
</ul>
<div class="tools"><a class="btn primary" href="{COPILOT_URL}" target="_blank" rel="noopener">Open Copilot ↗</a></div>
<h2>Tutorials</h2>
<div class="grid">{tut}</div>"""


BLOCKS = [b for b in DAY if "pause" not in b]

# Pages that sit inside a block, so its tab lights up there too.
BELONGS = {
    "metaphor.html": "welcome.html", "quickdraw.html": "welcome.html",
    "talk.html": "systems.html",
    "responses.html": "scenarios.html", "cards.html": "scenarios.html",
    "copilot-and-prompting.html": "copilot.html", "practical-moves.html": "copilot.html",
    "aias.html": "fit.html", "class-ai-agreement.html": "fit.html",
}


def block_of(file):
    if file.startswith("scenario-"):
        return "scenarios.html"
    return BELONGS.get(file, file if any(b["file"] == file for b in BLOCKS) else None)


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
.demos{list-style:none;counter-reset:dm;padding:0!important;margin:16px 0 10px;display:grid;gap:12px;max-width:none}
.demos li{counter-increment:dm;position:relative;background:var(--surface);border:1.5px solid var(--ink);border-radius:4px;padding:14px 16px 10px 64px}
.demos li::before{content:counter(dm,decimal-leading-zero);position:absolute;left:14px;top:12px;font-family:var(--font-display);font-weight:900;font-size:26px;line-height:1}
.demos .dh{display:flex;justify-content:space-between;gap:12px;align-items:baseline}
.demos h3{margin:0;font-size:18px}
.demos .dmin{font-family:var(--font-mono);font-size:12.5px;white-space:nowrap;background:var(--yellow);padding:1px 7px}
.demos .dpath{font-family:var(--font-mono);font-size:13px;color:var(--muted);margin:4px 0 6px}
.demos p{margin:0 0 6px}
.demos .dask{background:rgba(139,218,211,.35);padding:6px 9px;border-radius:3px}
.demos .dlink{font-size:14.5px}
.btn.primary{background:var(--yellow)}
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
{copilot_demo_html() if b.get('after_steps') == 'copilot_demo' else ''}
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
