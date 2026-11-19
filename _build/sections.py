"""The day, block by block: the home page agenda and one page per block.

Edit a block here and rebuild. Each block has the plan's description (word for word),
"What we'll do" steps (draft), and the materials for that block.
"""
import html
from scenarios import COPILOT_URL

FIT_PDF = "assets/how-ai-fits-handout.pdf"
ED_PDF = "assets/entangled-dimensions-handout.pdf"
ESSAY_PDF = "assets/one-essay-many-outcomes.pdf"
TASK_PDF = "assets/what-is-your-task-assessing.pdf"

ED = "https://rshorst.github.io/Entangled-Dimensions-of-AI-Literacy/interactive.html"  # the K-12 interactive
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
        "file": "welcome.html", "tab": "Welcome", "start": "8:30", "end": "8:50", "title": "Welcome",
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
        "file": "systems.html", "tab": "Strange systems", "start": "8:50", "end": "9:25", "title": "What are these strange systems, anyway?",
        "desc": "A plain-language introduction to how generative AI systems compose outputs, and the minimum technical background we need to make informed decisions about them. Then we experiment and see what happens.",
        "chips": [("systems.html#slides", "Talk slides"), ("map.html", "AI map")],
        "steps": [],
        "tiles": [],
        "after_steps": "talk_slides",
    },
    {
        "file": "scenarios.html", "tab": "Classroom situations", "start": "9:25", "end": "10:15", "title": "Classroom situations",
        "desc": "Small groups work through real and plausible situations involving generative AI in teaching and learning. We look closely at what is happening, what choices are available, and what different responses might mean for students, teachers, and the classroom.",
        "chips": [("scenarios.html", "Classroom situations"), ("responses.html", "Shared board")],
        "existing": True,  # the cases page is this block's page
    },
    {"pause": "Break", "start": "10:15"},
    {
        "file": "copilot.html", "tab": "Copilot", "start": "10:30", "end": "11:15", "title": "Some things worth trying in Copilot",
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
        "file": "fit.html", "tab": "How AI fits", "start": "11:15", "end": "12:00", "title": "How should AI fit into classroom work?",
        "desc": "A look at several ways educators and schools are approaching AI use in learning and assessment, from blanket rules to more nuanced frameworks such as the AI Assessment Scale. We consider what each approach makes possible, what assumptions it carries, and where it might break down in different K-12 contexts. Then we try configuring a chatbot to support learning without doing the thinking.",
        "chips": [("aias.html", "AI Assessment Scale"), ("fit.html#configure", "Configure the machine")],
        "steps": [
            "Approaches, quickly: ban, allow everything, traffic lights, the AI Assessment Scale, a class agreement.",
            "In pairs, one person plays the student. Configure the machine with the tutor, the student who gets it wrong, or the skeptic, then test it.",
            "Talk it over: what thinking was left to you, what difficulty was kept or removed, what the machine couldn’t know.",
        ],
        "extra": "configure",
        "tiles": [
            (FIT_PDF, "How AI fits handout", "What kind of task is this, assessing the process, and the prompts. Two pages to print."),
            ("aias.html", "What kind of task is this?", "Our summary of the AI Assessment Scale, with questions for it and ways to assess the process."),
            ("https://aiassessmentscale.com/", "The AI Assessment Scale", "By Leon Furze, with Mike Perkins, Jasper Roe and Jason MacVaugh. The scale itself, with translations and resources."),
        ],
    },
    {"pause": "Lunch", "start": "12:00"},
    {
        "file": "bigger-picture.html", "tab": "Bigger picture", "start": "1:00", "end": "1:30", "title": "Looking at the bigger picture",
        "desc": "We use the Entangled Dimensions of AI Literacy framework to step back from individual classroom uses and explore some of the wider questions connected to AI: knowledge, relationships, institutions, resources, values, and planetary systems. Participants explore the framework themselves and use it to look at a classroom example, question, or concern from another angle.",
        "chips": [(ED, "Entangled Dimensions"), ("bigger-picture.html#threads", "Pull the threads")],
        "steps": [
            "A short introduction to the Entangled Dimensions of AI Literacy.",
            "Take the task you worked on this morning. Which threads did your thinking already pull?",
            "Pick one you didn’t, ask its question of your task, and share what it opened up.",
        ],
        "extra": "threads",
        "embed": f'<div class="board ed"><iframe src="{ED}" title="Entangled Dimensions of AI Literacy: in the classroom" loading="lazy"></iframe></div><p class="meta"><a href="{ED}" target="_blank" rel="noopener">Open it in its own tab ↗</a></p>',
        "tiles": [
            (ED_PDF, "Entangled Dimensions handout", "The diagram on one side, the ten threads on the other. Landscape, to print."),
        ],
    },
    {
        "file": "rethinking.html", "tab": "Rethinking", "start": "1:30", "end": "2:30", "title": "Rethinking something you already teach",
        "desc": "Bring a lesson, activity, assignment, or unit you already teach. We use what we have explored so far to reconsider where AI might support the learning, where it might change or bypass something important, and where it may not belong at all.",
        "chips": [("bigger-picture.html#threads", "Pull the threads"), ("readings.html", "Readings on assessment")],
        "steps": [
            "Bring a lesson, activity, assignment or unit you already teach.",
            "Where might AI support the learning? Where might it change or bypass something important? Where may it not belong at all?",
            "Redesign one part, and name what the redesign protects.",
        ],
        "extra": "rethink",
        "tiles": [
            (ESSAY_PDF, "One essay, many outcomes", "The worked example: eight Grade 9 standards, and how the assessment changes for each."),
            (TASK_PDF, "What is your task assessing?", "The worksheet: the same layout, blank, for a task you teach."),
            ("aias.html", "AI Assessment Scale", "Which kind of task is this, and why?"),
            (FIT_PDF, "How AI fits handout", "The scale, assessing the process, and the prompts, to print."),
            (ED_PDF, "Entangled Dimensions handout", "The ten threads and their questions, to keep beside the worksheet."),
            ("readings.html", "Readings on assessment", "Research and practice to draw on."),
        ],
    },
    {"pause": "Break", "start": "2:30"},
    {
        "file": "collective.html", "tab": "Collective decisions", "start": "2:45", "end": "3:15", "title": "From classroom choices to collective decisions",
        "desc": "We bring together the questions that have surfaced throughout the day and consider what can be decided by an individual educator, what may need shared school guidance, and what calls for broader community conversation. We look at emerging approaches elsewhere as possibilities to examine, not templates to adopt.",
        "note": "What needs to be decided here, who needs to be part of that decision, and what should remain open?",
        "chips": [("policies.html", "Policy examples"), ("class-ai-agreement.html", "Collaborative protocol"), ("activities.html#activity-13", "The document audit")],
        "steps": [
            "Gather the questions that came up through the day.",
            "Sort them: what an individual educator can decide, what may need shared school guidance, and what calls for broader community conversation.",
            "Look at approaches from elsewhere as possibilities to examine, not templates to adopt.",
        ],
        "tiles": [
            ("responses.html", "Shared board", "The groups’ responses from the morning."),
            ("policies.html", "Policy examples", "What other schools and districts have written."),
            ("class-ai-agreement.html", "Collaborative protocol", "Deciding together, with students, how AI is used in the room."),
            ("activities.html#activity-13", "The document audit", "What do we already say that covers this?"),
        ],
    },
    {
        "file": "close.html", "tab": "Close", "start": "3:15", "end": "3:30", "title": "Close",
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
    "aias.html": "fit.html", "class-ai-agreement.html": "collective.html",
}


def block_of(file):
    if file.startswith("scenario-"):
        return "scenarios.html"
    return BELONGS.get(file, file if any(b["file"] == file for b in BLOCKS) else None)


def _href(h):
    if h.endswith(".pdf"):
        return f'href="{h}" download'
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
.board.ed{background:#fff}
.board.ed iframe{height:1140px}
@media (max-width:700px){.board.ed iframe{height:1100px}}
.pager{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:44px;border-top:2px solid var(--ink);padding-top:14px;max-width:none}
.pager a{text-decoration:none;font-weight:700;color:var(--ink);max-width:46%}
.pager a:last-child{text-align:right;margin-left:auto}
.pager small{display:block;font-family:var(--font-mono);font-weight:500;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
</style>"""


# ---- 11:25 "Configure the machine to help you learn" (matches the How AI fits handout, side 2)
def _b(id_, ph, cls="blank"):
    return f'<input class="{cls}" id="cf-{id_}" type="text" placeholder="{esc(ph)}" aria-label="{esc(ph)}" autocomplete="off">'


def _prompt(pid, title, tag, items, full=False):
    lis = "".join(f"<li>{it}</li>" for it in items)
    return (f'<div class="prompt{" full" if full else ""}" data-prompt="{pid}">'
            f'<div class="ph"><h4>{esc(title)}</h4>{f"<span class=tag>{esc(tag)}</span>" if tag else ""}</div>'
            f'<ul>{lis}</ul>'
            f'<div class="pa"><button class="btn primary copy" type="button">Copy prompt</button><span class="ok" aria-live="polite"></span></div></div>')


def configure_html():
    tutor = _prompt("tutor", "The tutor who won’t answer", "Learning", [
        f"You are my tutor for {_b('tutor-topic', 'topic')} at a Grade {_b('tutor-grade', 'grade')} level. Help me figure it out myself. Don’t do it for me.",
        "Start by asking what I already know.",
        "Ask one question at a time, then wait for my answer.",
        "If I’m stuck, give the smallest hint that helps. Get more specific only if I’m still stuck.",
        "If I’m wrong, don’t correct me. Ask me to explain my thinking.",
        "If I ask for the answer, say no and give me a hint.",
        "At the end, ask me to explain it back in my own words, then name one thing I still need to work on.",
    ], full=True)
    student = _prompt("student", "The student who gets it wrong", "Teaching it back", [
        f"You are a Grade {_b('student-grade', 'grade')} student who has just learned {_b('student-topic', 'topic')} but misunderstood part of it.",
        "Explain it to me in a short paragraph with one example. Include one or two mistakes a real student might make. Don’t point them out.",
        "Then I’ll teach you. Ask questions when I’m unclear, and only change your mind when I give you a good reason.",
    ])
    skeptic = _prompt("skeptic", "The skeptic", "Arguing", [
        f"I’m going to argue that {_b('skeptic-claim', 'your claim')}. Play {_b('skeptic-who', 'who disagrees')}, who disagrees.",
        "Give me one objection at a time and wait for my reply.",
        "Don’t make my arguments for me, and don’t agree just to be nice. Push me to use evidence.",
        "After three objections, tell me which of my answers was weakest.",
    ])
    own = _prompt("own", "Your own", "", [
        f"For this conversation, you are {_b('own-role', 'a role', 'blank line')}",
        f"Your job is to help me {_b('own-job', 'do what', 'blank line')}",
        f"Never {_b('own-never', 'a rule', 'blank line')}",
        f"Always {_b('own-always', 'a rule', 'blank line')}",
        f"End by {_b('own-end', 'how it should finish', 'blank line')}",
    ], full=True)
    return f"""<style>
.cfg-intro{{max-width:68ch}}
.cfg-part{{display:flex;align-items:baseline;flex-wrap:wrap;gap:4px 12px;margin:30px 0 12px;font-size:21px;text-transform:uppercase}}
.cfg-part .pn{{background:var(--ink);color:var(--surface);padding:0 9px}}
.cfg-part em{{font-family:var(--font-body);font-weight:400;font-size:15.5px;font-style:italic;color:var(--muted);text-transform:none}}
.prompts{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;max-width:none}}
.prompt{{background:var(--surface);border:2px solid var(--ink);border-radius:4px;box-shadow:4px 4px 0 var(--ink);padding:16px 18px 14px}}
.prompt.full{{grid-column:1/-1}}
.prompt .ph{{display:flex;align-items:center;flex-wrap:wrap;gap:6px 10px}}
.prompt h4{{margin:0;font-family:var(--font-display);font-size:16px;text-transform:uppercase}}
.prompt .tag{{font-family:var(--font-mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;border:1.5px solid var(--ink);padding:1px 7px}}
.prompt ul{{margin:12px 0 14px;padding-left:20px}}
.prompt li{{margin:5px 0;line-height:1.55}}
.prompt[data-prompt=own] ul{{list-style:none;padding-left:0}}
.prompt[data-prompt=own] li{{display:flex;align-items:baseline;gap:10px;margin:10px 0}}
.blank{{font:inherit;color:var(--ink);background:#fff6cc;border:0;border-bottom:2px solid var(--ink);border-radius:2px 2px 0 0;padding:0 5px;width:12ch;max-width:100%}}
.blank.line{{flex:1;width:0;min-width:0}}
.blank::placeholder{{color:#8a8274;font-style:italic}}
.blank:focus{{outline:2px solid var(--accent);outline-offset:1px}}
.prompt .pa{{display:flex;align-items:center;gap:12px}}
.prompt .ok{{font-family:var(--font-mono);font-size:12.5px;color:var(--muted)}}
@media (max-width:760px){{.prompts{{grid-template-columns:minmax(0,1fr)}}}}
</style>
<h2 id="configure">Configure the machine to help you learn</h2>
<p class="cfg-intro">Using these systems well means knowing how you learn. Setting one up yourself is a way to find out. Paste instructions at the top of a new chat, in Copilot or any chatbot, and fill in the blanks.</p>
<h3 class="cfg-part"><span class="pn">1</span>Use one as given <em>the teacher sets the conditions</em></h3>
<div class="prompts">{tutor}{student}{skeptic}</div>
<h3 class="cfg-part"><span class="pn">2</span>Write your own <em>the student designs</em></h3>
<div class="prompts">{own}</div>
<h3 class="cfg-part"><span class="pn">3</span>Test it <em>the student checks</em></h3>
<p class="cfg-intro">Does it keep to your rules after five turns? What happens when you ask it to break one? Open a new chat: what’s left? <strong>What did writing the rules show you about how you learn?</strong></p>
<p><strong>Use fictional material only, and leave out student information.</strong></p>
<p class="meta">Prompts by Rachel Horst, drawing on Mollick &amp; Mollick (2023). CC BY 4.0.</p>
<script>
(function(){{
  var KEY='aipd-configure', saved={{}};
  try{{ saved=JSON.parse(localStorage.getItem(KEY)||'{{}}'); }}catch(e){{}}
  var blanks=document.querySelectorAll('.prompt .blank');
  function size(el){{ if(!el.classList.contains('line')) el.style.width=(Math.max(el.value.length, el.placeholder.length)+3)+'ch'; }}
  blanks.forEach(function(el){{
    if(saved[el.id]) el.value=saved[el.id];
    size(el);
    el.addEventListener('input',function(){{
      size(el); saved[el.id]=el.value;
      try{{ localStorage.setItem(KEY, JSON.stringify(saved)); }}catch(e){{}}
    }});
  }});
  function textOf(node){{
    var out='';
    node.childNodes.forEach(function(c){{
      if(c.nodeType===3) out+=c.textContent;
      else if(c.tagName==='INPUT') out+=(c.value.trim()||'___');
      else out+=textOf(c);
    }});
    return out;
  }}
  function copy(text, done){{
    if(navigator.clipboard && window.isSecureContext){{ navigator.clipboard.writeText(text).then(done, fallback); }} else fallback();
    function fallback(){{
      var t=document.createElement('textarea'); t.value=text; t.setAttribute('readonly',''); t.style.position='fixed'; t.style.opacity='0';
      document.body.appendChild(t); t.select(); try{{ document.execCommand('copy'); done(); }}catch(e){{}} t.remove();
    }}
  }}
  document.querySelectorAll('.prompt .copy').forEach(function(btn){{
    btn.addEventListener('click',function(){{
      var card=btn.closest('.prompt'), ok=card.querySelector('.ok');
      var text=Array.prototype.map.call(card.querySelectorAll('li'), function(li){{ return textOf(li).replace(/\\s+/g,' ').trim(); }}).join('\\n');
      copy(text, function(){{ ok.textContent='Copied. Paste it into a new chat.'; setTimeout(function(){{ ok.textContent=''; }}, 4000); }});
    }});
  }});
}})();
</script>"""


# ---- 1:45 "Pull the threads" (matches the Entangled Dimensions handout, side 2)
THREADS = [
    ("data", "Data", "#59a34f", "What will students type or upload, and where does it go once they press enter?"),
    ("algorithmic", "Algorithmic", "#eec949", "The tool is built to sound helpful and keep you going. Is that what this task needs?"),
    ("futures", "Futures", "#b07ba3", "If students did this task this way every year, what would they get better at, and what would they lose?"),
    ("creative", "Creative", "#f59ba8", "In the finished work, which choices were the student’s and which were the tool’s defaults?"),
    ("relational", "Relational", "#9d7661", "Who would a student have asked for help before, and what happens to that conversation now?"),
    ("political", "Political", "#bcb0ac", "Who decided this tool is allowed here, and what happens to a student who says no?"),
    ("disciplinary", "Disciplinary", "#507aa9", "Would someone who works in your subject accept the way this was made?"),
    ("epistemic", "Epistemic", "#f3902a", "If the tool gets something wrong, how would the student notice?"),
    ("knowledge", "Knowledge-construction", "#e3585b", "What can the student do on their own after this task that they couldn’t before?"),
    ("ecological", "Ecological", "#77b8b3", "Is this use worth the energy, water and hidden labour behind it, or would a pencil do?"),
]


def threads_html():
    cards = "".join(
        f'<label class="thread" style="--c:{c}"><input type="checkbox" id="th-{k}" style="accent-color:{c}">'
        f'<span class="tn">{esc(n)}</span><span class="tq">{esc(q)}</span></label>'
        for k, n, c, q in THREADS)
    return f"""<style>
.threads-intro{{max-width:68ch}}
.th-field{{display:block;font-weight:700;margin:16px 0 18px;max-width:68ch}}
.th-field input,.th-field textarea{{display:block;width:100%;margin-top:6px;font:inherit;font-weight:400;background:var(--surface);border:2px solid var(--ink);border-radius:4px;padding:8px 10px;color:var(--ink)}}
.th-field textarea{{min-height:96px;resize:vertical}}
.threads{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;max-width:none;margin:0 0 6px}}
.thread{{position:relative;display:flex;flex-direction:column;gap:8px;background:var(--surface);border:2px solid var(--ink);border-radius:4px;box-shadow:3px 3px 0 var(--ink);padding:12px 12px 14px;cursor:pointer;line-height:1.45}}
.thread input{{position:absolute;top:12px;right:10px;width:20px;height:20px;margin:0;cursor:pointer}}
.thread .tn{{align-self:flex-start;background:var(--c);font-family:var(--font-display);font-weight:800;font-size:13px;letter-spacing:.03em;text-transform:uppercase;padding:2px 7px;margin-right:24px}}
.thread .tq{{font-size:15px}}
.thread:has(input:checked){{background:color-mix(in srgb,var(--c) 22%,var(--surface))}}
.thread:has(input:focus-visible){{outline:3px solid var(--accent);outline-offset:2px}}
@media (max-width:1100px){{.threads{{grid-template-columns:repeat(2,1fr)}}}}
@media (max-width:560px){{.threads{{grid-template-columns:1fr}}}}
</style>
<h2 id="threads">Pull the threads</h2>
<p class="threads-intro">Each dimension is a thread, and they’re tangled together. Take a task you’ve worked on today. Tick the threads your thinking already pulled. Then pick one you didn’t, ask its question of your task, and note what it opens up.</p>
<label class="th-field">The task<input id="th-task" type="text" autocomplete="off"></label>
<div class="threads">{cards}</div>
<label class="th-field">The thread I’ll pull next, and why<textarea id="th-next"></textarea></label>
<p class="meta">Your ticks and notes stay in this browser.</p>
<script>
(function(){{
  var KEY='aipd-threads', saved={{}};
  try{{ saved=JSON.parse(localStorage.getItem(KEY)||'{{}}'); }}catch(e){{}}
  document.querySelectorAll('.threads input, #th-task, #th-next').forEach(function(el){{
    var cb=el.type==='checkbox';
    if(el.id in saved){{ if(cb) el.checked=!!saved[el.id]; else el.value=saved[el.id]; }}
    el.addEventListener(cb?'change':'input',function(){{
      saved[el.id]=cb?el.checked:el.value;
      try{{ localStorage.setItem(KEY, JSON.stringify(saved)); }}catch(e){{}}
    }});
  }});
}})();
</script>"""


EXTRAS = {"configure": configure_html, "threads": threads_html}


# ---- 12:45 "Rethinking something you already teach": a guide
REREAD = {
    "fppl": "https://www.fnesc.ca/first-peoples-principles-of-learning/",
    "kdu": "https://curriculum.gov.bc.ca/curriculum/overview",
    "dawson_talk": "https://www.timeshighereducation.com/news/ai-cheating-matters-redrawing-assessment-matters-most",
    "dawson": "https://doi.org/10.1080/02602938.2024.2386662",
    "corbin": "https://doi.org/10.1080/02602938.2025.2503964",
    "sydney": "https://educational-innovation.sydney.edu.au/teaching@sydney/?p=21264",
    "sydney_values": "https://needednowlt.substack.com/p/why-banning-ai-in-assessment-is-all",
    "lane_critique": "https://themindfile.substack.com/p/the-off-ramp-obstructs-learning",
    "furze_cheat": "https://leonfurze.com/2024/08/09/can-the-ai-assessment-scale-stop-students-cheating-with-ai/",
    "teqsa": "https://www.teqsa.gov.au/about-us/news-and-events/latest-news/assessment-reform-age-artificial-intelligence",
    "teqsa25": "https://www.teqsa.gov.au/sites/default/files/2025-09/enacting-assessment-reform-in-a-time-of-artificial-intelligence.pdf",
    "furze_k12": "https://durham-repository.worktribe.com/output/3355831/the-ai-assessment-scale-aias-in-australian-k-12-education",
    "beyond": "https://leonfurze.com/2026/05/25/beyond-scales-in-practice/",
    "bc_ai": "https://www2.gov.bc.ca/gov/content/education-training/k-12/administration/program-management/ai-in-education",
    "kentz": "https://mikekentz.substack.com/p/a-new-assessment-design-framework",
    "kentz_seven": "https://mikekentz.substack.com/p/the-ai-era-demands-curriculum-redesign",
    "math9": "https://www2.gov.bc.ca/assets/gov/education/administration/kindergarten-to-grade-12/ai-in-education/math-9-teaching-and-learning-story-exploring-ai-and-dodging-bias.pdf",
    "bcfp12": "https://www2.gov.bc.ca/assets/gov/education/administration/kindergarten-to-grade-12/ai-in-education/bcfp-12-teaching-and-learning-story-ethics-of-generating-ai-images-of-bc-first-peoples-and-local-indigenous-art.pdf",
    "reuters": "https://www.thestar.com.my/tech/tech-news/2026/10/28/how-teachers-are-remaking-classrooms-for-the-ai-age",
}

TEACHER_EXAMPLES = [
    ("Open", "Grade the chats", "Mike Kentz, Grade 9 English, United States",
     "He assesses students’ conversations with the chatbot alongside the essay, so the thinking is visible. In one project he marked only the first seven prompts, and many students began drafting their prompts before typing them.",
     REREAD["kentz"]),
    ("Open", "Recreate the shape", "Mathematics 9, BC (a Ministry teaching and learning story)",
     "The teacher made 14 geometric images with AI. In pairs, students try to recreate them, which only works when their math vocabulary is precise.",
     REREAD["math9"]),
    ("Keep out", "Whose images are these?", "BC First Peoples 12 (a Ministry teaching and learning story)",
     "Students generate images of First Peoples and local Indigenous art, then judge them for stereotypes, protocol and appropriation, drawing on the First Peoples Principles of Learning.",
     REREAD["bcfp12"]),
    ("Protect", "Fifteen questions, five minutes", "Tristen Chang, Grade 6 humanities, San Francisco",
     "She dropped take-home essays for short oral exams: fifteen questions on character, plot, theme and metaphor.",
     REREAD["reuters"]),
    ("Change the question", "Which method, and why?", "Bobson Wong, high school mathematics, New York",
     "AI can show every step of a solution, so Wong asks students which problem-solving method they prefer and why. Practice moved from homework into class.",
     REREAD["reuters"]),
    ("Protect", "A month on one essay", "Rusty Shabe, middle school English, San Francisco",
     "He found students turn to AI at home when they feel overwhelmed. So the writing happens in class: a month on one essay with his Grade 7s.",
     REREAD["reuters"]),
]


ESSAY_ROWS = [
    ("Opinion and evidence", "Express an opinion and support it with credible evidence.",
     "Write a one-page position, then defend it live: answer three questions the page doesn’t.",
     "Spar with AI playing a skeptic, one objection at a time. Students note the strongest objection and how they answered it."),
    ("Judging sources", "Find information and judge how relevant, accurate and reliable it is.",
     "Collect five sources and rank them by how much you trust them. Explain each ranking in a sentence.",
     "Ask AI for sources on the issue, then check each one: does it exist, and does it say what AI claims? The checking is what’s assessed."),
    ("Synthesis", "Bring ideas from several sources together to build understanding.",
     "Map three sources in conversation: where they agree, where they clash. Then write one paragraph in class.",
     "Give AI the sources and ask for a summary. Students mark what it flattened or missed, and their paragraph does better."),
    ("Revision", "Refine a text for clarity and impact, for its purpose and audience.",
     "Draft in class and keep the drafts. Hand in the best page with a note on two changes and why.",
     "Ask AI for feedback against the class criteria. Students take or refuse each suggestion and give a reason. Assess the reasons."),
    ("Audience and form", "Choose the form and features that fit the audience and purpose.",
     "Write it twice: a letter to council and a post for classmates. Assess what changed between them.",
     "Ask AI to rewrite one paragraph for three audiences. Students name what changed, then apply it to their own writing."),
    ("Transformation", "Turn ideas and information into an original text.",
     "Turn the argument into a radio piece, poster or comic, and explain the choices in a two-minute talk.",
     "Use AI to rough out two or three forms quickly. Students choose one, make it themselves, and explain the choice."),
    ("Oral storytelling", "Use and experiment with oral storytelling.",
     "Interview one person affected and, with their permission, retell their story aloud as part of the argument.",
     "Brainstorm interview questions with AI, then revise them together: which are respectful, which are leading? The story itself stays out of the chatbot."),
    ("Perspectives", "Big Idea: people read texts differently, depending on worldview and perspective.",
     "Write the strongest case for the side you disagree with. Someone who holds that view reads it: is it fair?",
     "AI argues the other side first. Then students talk with someone who holds that view. What did AI get right, miss or caricature?"),
]


LESSONS_SECONDARY = [
    ("Break the Fake: Verifying information online", "Grades 6 to 9 · Digital literacy · MediaSmarts",
     "https://mediasmarts.ca/teacher-resources/break-fake-lesson-plan-verifying-information-online",
     "Four quick steps for checking information online, practised on real examples, then a media piece students make.",
     "Adapt it for AI-generated misinformation without losing the original fact-checking steps."),
    ("What is Poetry? Contrasting Poetry and Prose", "Grades 6 to 8 · English · ReadWriteThink",
     "https://readwritethink.org/classroom-resources/lesson-plans/what-poetry-contrasting-poetry",
     "Tennyson’s “The Eagle” beside an informational article about eagles, read closely and discussed in groups.",
     "Ask for reading supports that keep both texts, and the differences between them, intact."),
    ("Perspective drawing, slope and equations of lines", "Grades 7 to 11 · Math and art · Art Canada Institute",
     "https://aci-iac.ca/education/teacher-resource-guides/perspective-drawing-slope-and-equations-of-lines-through-the-art-of-kazuo-nakamura",
     "The paintings of Kazuo Nakamura as a way into one- and two-point perspective, slope and the equations of lines.",
     "Ask it to explain slope through the artwork, then find the visual and mathematical reasoning it misses."),
    ("Understanding Ocean and Coastal Acidification", "Grades 9 to 12 · Science · NOAA Data in the Classroom",
     "https://dataintheclassroom.noaa.gov/content/ocean-acidification",
     "A five-level module on carbon dioxide, ocean pH and marine life, built on real NOAA data. Updated in 2025.",
     "Turn one level into a 50-minute lesson, then check whether it reads the graphs and claims correctly."),
    ("Primary sources relating to Canadians of Chinese ancestry", "Grades 5 to 10 · History · Canada’s History, Flora Fung",
     "https://www.canadashistory.ca/getmedia/e111c303-b817-45ba-b20d-b7010c14f9d5/EduLesBeyondGoldMountainEduGuideEN.pdf",
     "Photographs, letters and documents analysed and built into a concept map. Some sources contain racist language and images; the guide explains how to handle them.",
     "Ask for evidence-based questions, then separate what a source shows from what the model infers."),
    ("(re)Mapping Place", "Grades 7 to 12 · Art, geography, Indigenous studies · Ottawa Art Gallery, Barry Ace",
     "https://oaggao.ca/learn/educational-programs-and-resources/contemporary-indigenous-artists-in-the-classroom/",
     "Anishinaabe artist Barry Ace’s lesson on maps as colonial authority, with students making their own mapping of place.",
     "Ask it to adapt the lesson for your place. Does it invent teachings, flatten the artist’s intent, or assume knowledge it doesn’t have?"),
]

LESSONS_PRIMARY = [
    ("Seasonal changes through the art of Maud Lewis", "Grades 1 to 3 · Art, language arts, science · Art Canada Institute",
     "https://aci-iac.ca/education/teacher-resource-guides/seasonal-changes-through-the-art-of-maud-lewis",
     "Maud Lewis’s paintings as a way into how the seasons change, ending in a class mural."),
    ("Watering Your Plants", "Grades K to 4 · Science and engineering · NASA",
     "https://www.nasa.gov/stem-content/lesson-4-watering-your-plants/",
     "Students look at how watering systems work, then design one for plants growing on the moon."),
    ("To the Number Line", "Grade 3 · Math · Illustrative Mathematics",
     "https://curriculum.illustrativemathematics.org/k5/teachers/grade-3/unit-5/lesson-5/preparation.html",
     "From fraction strips to placing fractions on a number line."),
]

LESSON_PROMPT = """Using the uploaded lesson and accompanying student materials:
1. Identify what students are actually expected to learn and do.
2. Identify the parts of the lesson that require direct experience, interpretation, discussion, or productive struggle.
3. Propose one meaningful adaptation for a mixed-ability classroom.
4. Explain what your adaptation changes about the original learning experience.
5. Refer to the source documents and flag anything you cannot verify.
Do not replace the original learning task simply because you can generate a faster alternative."""


def lessons_html():
    sec = "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)} ↗</a><span class="lmeta">{esc(m)}</span>'
        f'<span>{esc(d)}</span><span class="try"><b>Try in Copilot:</b> {esc(c)}</span></li>'
        for t, m, u, d, c in LESSONS_SECONDARY)
    pri = "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)} ↗</a><span class="lmeta">{esc(m)}</span><span>{esc(d)}</span></li>'
        for t, m, u, d in LESSONS_PRIMARY)
    return f"""<style>
.lessons{{list-style:none;padding:0!important;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;max-width:none;margin:10px 0 18px}}
.lessons li{{background:var(--surface);border:2px solid var(--ink);border-radius:4px;box-shadow:3px 3px 0 var(--ink);padding:12px 14px;margin:0;display:flex;flex-direction:column;gap:4px}}
.lessons a{{font-family:var(--font-display);font-weight:800;font-size:15.5px;line-height:1.25}}
.lessons .lmeta{{font-family:var(--font-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.lessons .try{{font-size:14px;color:var(--muted);margin-top:2px}}
.lprompt{{background:var(--surface);border:2px dashed var(--ink);border-radius:4px;padding:12px 16px;max-width:72ch;margin:8px 0 6px}}
.lprompt pre{{white-space:pre-wrap;font-family:var(--font-body);font-size:15px;margin:0 0 10px}}
.lprompt .ok{{font-family:var(--font-mono);font-size:12.5px;color:var(--muted);margin-left:10px}}
@media (max-width:760px){{.lessons{{grid-template-columns:minmax(0,1fr)}}}}
</style>
<h2 id="lessons">Or start from a real lesson</h2>
<p class="rt">No task to hand? Pick a lesson an educator or organization has published, open its materials, and work it through the worksheet. Each one comes with what students actually use: readings, sources, artwork or data.</p>
<h3>Grades 6 to 12</h3>
<ul class="lessons">{sec}</ul>
<h3>Younger students</h3>
<ul class="lessons">{pri}</ul>
<h3>A prompt for any of them</h3>
<p class="rt">Upload the lesson to Copilot, or paste in its text, then use this. The point is not a new lesson. It is to see what happens when a machine interprets work a teacher has already made with care.</p>
<div class="lprompt"><pre id="lesson-prompt">{esc(LESSON_PROMPT)}</pre><button class="btn primary" type="button" id="copy-lesson-prompt">Copy prompt</button><span class="ok" aria-live="polite"></span></div>
<p class="rt meta">Publicly downloadable doesn’t mean openly licensed for uploading to an AI service. Check the materials’ terms, and what your school’s Copilot agreement covers, before you upload someone else’s text or artwork.</p>
<script>
(function(){{
  var b=document.getElementById('copy-lesson-prompt'); if(!b) return;
  b.addEventListener('click',function(){{
    var text=document.getElementById('lesson-prompt').textContent, ok=b.nextElementSibling;
    function done(){{ ok.textContent='Copied. Paste it into Copilot.'; setTimeout(function(){{ ok.textContent=''; }},4000); }}
    function fallback(){{ var t=document.createElement('textarea'); t.value=text; t.style.position='fixed'; t.style.opacity='0'; document.body.appendChild(t); t.select(); try{{ document.execCommand('copy'); done(); }}catch(e){{}} t.remove(); }}
    if(navigator.clipboard && window.isSecureContext){{ navigator.clipboard.writeText(text).then(done,fallback); }} else fallback();
  }});
}})();
</script>"""


def rethink_html():
    R = REREAD
    rows = "".join(
        f'<tr><th scope="row"><span class="n">{i}</span><b>{esc(lab)}</b><small>{esc(std)}</small></th><td>{esc(a)}</td><td>{esc(ai)}</td></tr>'
        for i, (lab, std, a, ai) in enumerate(ESSAY_ROWS, 1))
    stories = "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener">{esc(h)} ↗</a> <span class="who">{esc(w)}.</span> {esc(d)}</li>'
        for _, h, w, d, u in TEACHER_EXAMPLES)
    return f"""<style>
.rt{{max-width:68ch}}
.essay{{width:100%;border-collapse:collapse;background:var(--surface);border:2px solid var(--ink);box-shadow:4px 4px 0 var(--ink);margin:14px 0 18px}}
.essay th,.essay td{{border-bottom:1.5px solid var(--line);border-right:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}}
.essay thead th{{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;border-bottom:2px solid var(--ink);background:var(--bg)}}
.essay tbody th{{width:26%;font-weight:400;background:var(--bg)}}
.essay tbody th b{{display:block;font-family:var(--font-display);text-transform:uppercase;font-size:15px}}
.essay tbody th small{{display:block;margin-top:3px;font-family:var(--font-body);font-size:13px;font-weight:400;text-transform:none;letter-spacing:0;color:var(--muted);line-height:1.35}}.essay tbody th{{font-family:var(--font-body);text-transform:none;letter-spacing:0}}
.essay .n{{display:inline-block;background:var(--ink);color:var(--surface);font-family:var(--font-display);font-weight:800;font-size:12px;padding:0 6px;margin-bottom:4px}}
.essay tr:last-child th,.essay tr:last-child td{{border-bottom:0}}
.prio{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;max-width:none;margin:14px 0 14px}}
.prio > div{{position:relative;background:#fffdf7;border:1.5px solid var(--line);border-radius:3px;box-shadow:0 2px 6px rgba(0,0,0,.12);padding:18px 16px 16px}}
.prio > div::before{{content:"";position:absolute;top:-9px;left:28px;width:84px;height:18px;background:rgba(214,205,187,.85);transform:rotate(-2deg)}}
.prio .pn{{display:inline-block;background:var(--yellow);font-family:var(--font-display);font-weight:900;font-size:15px;padding:0 7px;margin-bottom:6px}}
.prio h3{{margin:0 0 4px;font-size:20px;text-transform:uppercase}}
.prio .kw{{margin:0 0 6px;font-weight:700}}
.prio p{{margin:0}}
.prio-line{{font-size:18px;margin-top:4px}}
@media (max-width:900px){{.prio{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:520px){{.prio{{grid-template-columns:minmax(0,1fr)}}}}
.teacher-idea{{background:var(--yellow);border:2px solid var(--ink);border-radius:4px;padding:12px 16px;max-width:none;margin:0 0 10px}}
.teacher-idea b{{font-family:var(--font-display);text-transform:uppercase}}
.stories li{{margin:8px 0}}
.stories .who{{color:var(--muted)}}
.refs li{{margin:6px 0}}
@media (max-width:760px){{.essay thead{{display:none}}.essay tr{{display:block;border-bottom:1.5px solid var(--line)}}.essay th,.essay td{{display:block;border:0;width:auto!important}}
.essay td:nth-of-type(1)::before{{content:"Instead of the essay: ";font-weight:700}}.essay td:nth-of-type(2)::before{{content:"Bringing AI in: ";font-weight:700}}}}
</style>
<p class="tools no-print"><a class="btn primary" href="{ESSAY_PDF}" download>The essay example (PDF)</a><a class="btn" href="{TASK_PDF}" download>Your worksheet (PDF)</a></p>

<h2 id="priorities">Four priorities</h2>
<p class="rt">Keep these in view as you rethink a task.</p>
<div class="prio">
<div><span class="pn">1</span><h3>Learning</h3><p class="kw">Experience, patience, time</p><p>What do we need to experience and practise to learn?</p></div>
<div><span class="pn">2</span><h3>Knowing</h3><p class="kw">Memory, history, story</p><p>Whose knowledge matters, and who has permission to share it?</p></div>
<div><span class="pn">3</span><h3>Creating</h3><p class="kw">Exploration, identity, responsibility</p><p>What do we discover about ourselves through making?</p></div>
<div><span class="pn">4</span><h3>Relating</h3><p class="kw">Reciprocity, connection, place</p><p>How do our relationships make learning possible?</p></div>
</div>
<p class="rt prio-line">An answer can be correct and still wrong for this class, this purpose or this community.</p>
<p class="meta">In conversation with the <a href="{R['fppl']}" target="_blank" rel="noopener">First Peoples Principles of Learning</a> (FNESC).</p>

<h2 id="essay">What is this essay assessing?</h2>
<p class="rt">Take an ordinary task: a Grade 9 essay arguing a position on a local issue. It could be assessing any of the standards below, from BC’s English Language Arts 9 curriculum. Once you name the one you mean, the assessment changes, and so does the place AI might have in it.</p>
<table class="essay">
<thead><tr><th scope="col">The standard</th><th scope="col">Instead of the essay</th><th scope="col">A meaningful way to bring AI in</th></tr></thead>
<tbody>{rows}</tbody>
</table>
<p class="teacher-idea"><b>Teacher idea: use AI to develop a class-wide plan.</b> Ask Copilot: “Give me ten whole-class games or activities where Grade 9s practise backing an opinion with evidence. No devices needed.” Then pick one and make it yours. It might suggest four corners, a source tournament or a mock town hall.</p>
<p class="meta">Standards in plain words, from <a href="{R['kdu']}" target="_blank" rel="noopener">BC’s English Language Arts 9 curriculum</a>.</p>

<h2 id="yours">Now your task</h2>
<p class="rt">Bring the thread you chose at the end of the last block, and keep the <a href="bigger-picture.html#threads">ten threads</a> and the <a href="{ED}" target="_blank" rel="noopener">Entangled Dimensions</a> close by as you work.</p>
<p class="rt">Write a task you already teach in the middle of the worksheet. Around it, name the standards it could be assessing, and circle the one you actually mean. Then redesign the assessment for two or three of them: what students could do instead, and how they could use AI without it doing the learning. Last question: is there any part AI should stay out of, and why?</p>
<p class="rt">The First Peoples Principles of Learning are a good check here. Learning takes patience and time, and it serves more than the learner. Some knowledge, in FNESC’s words, is “sacred and only shared with permission and/or in certain situations.” (<a href="{R['fppl']}" target="_blank" rel="noopener">the full principles ↗</a>)</p>

{lessons_html()}

<h2 id="stories">Teachers who changed the task</h2>
<ul class="stories rt">{stories}</ul>

<h2 id="research">What the research says</h2>
<p class="rt">Assessment researchers keep coming back to the same few points. Ask what a task lets you say about a student’s learning before asking how to stop cheating; Phillip Dawson and colleagues argue that <a href="{R['dawson']}" target="_blank" rel="noopener">validity matters more than cheating</a>. Rules about AI only work if students read and follow them, so <a href="{R['corbin']}" target="_blank" rel="noopener">change the task itself</a>, not only its instructions. The University of Sydney protects some tasks and opens others to AI on purpose, in what it calls a <a href="{R['sydney']}" target="_blank" rel="noopener">two-lane approach</a>; critics say that is <a href="{R['sydney_values']}" target="_blank" rel="noopener">too binary</a> and can <a href="{R['lane_critique']}" target="_blank" rel="noopener">undo gains in equity</a>. And the authors of the AI Assessment Scale say <a href="{R['furze_cheat']}" target="_blank" rel="noopener">no framework can stop dishonest use</a>. It is a way to talk about a task, not a lock.</p>

<h2 id="resources">Readings</h2>
<ul class="refs meta">
<li>TEQSA (2023). <a href="{R['teqsa']}">Assessment reform for the age of artificial intelligence</a>. And the follow-up, <a href="{R['teqsa25']}">Enacting assessment reform in a time of artificial intelligence</a> (2025).</li>
<li>Dawson, P., Bearman, M., Dollinger, M., &amp; Boud, D. (2024). <a href="{R['dawson']}">Validity matters more than cheating</a>. <em>Assessment &amp; Evaluation in Higher Education, 49</em>(7).</li>
<li>Corbin, T., Dawson, P., &amp; Liu, D. (2025). <a href="{R['corbin']}">Talk is cheap: Why structural assessment changes are needed for a time of GenAI</a>. <em>Assessment &amp; Evaluation in Higher Education</em>.</li>
<li>University of Sydney. <a href="{R['sydney']}">The two-lane approach to assessment</a>. With Liu and Bridgeman’s <a href="{R['sydney_values']}">case for it</a> and <a href="{R['lane_critique']}">a critique</a>.</li>
<li>Furze, L., &amp; Roe, J. (2024). <a href="{R['furze_k12']}">The AI Assessment Scale (AIAS) in Australian K-12 education</a>. And Furze (2026), <a href="{R['beyond']}">Beyond scales: in practice</a>, including Saskatoon Public Schools.</li>
<li>BC Ministry of Education and Child Care. <a href="{R['bc_ai']}">Digital literacy and the use of AI in education</a>. Teaching and learning stories from BC classrooms, Grade 3 to 12.</li>
<li>Kentz, M. <a href="{R['kentz']}">Stop grading essays, start grading chats</a>.</li>
<li>Coster, H. (2026, October 28). <a href="{R['reuters']}">How teachers are remaking classrooms for the AI age</a>. Reuters.</li>
<li>First Nations Education Steering Committee. <a href="{R['fppl']}">First Peoples Principles of Learning</a>.</li>
</ul>"""


EXTRAS["rethink"] = rethink_html


# ---- 9:15 talk slides: slides 6 to 23 of the deck, rendered to assets/talk/NN.webp ----
TALK_SLIDES = [
    (6, "What are these strange systems, anyway? Plain language, the minimum we need, then we experiment."),
    (7, "What are we calling AI? Many things. Nested circles since the 1950s: AI (route planning, chess engines) contains machine learning (spam filters, recommendations), deep learning (face unlock, translation), generative AI (image makers) and language models (chatbots), where Copilot sits. AI is a big field with a long history. Chatbots like Copilot are a small, recent slice of it. Keep in mind: when someone says “AI”, ask: which one?"),
    (8, "The AI landscape: who makes what. A screenshot of the AI map on this site. Companies train models. Apps put those models in front of you. One model often sits behind many apps. Keep in mind: the app is not the model."),
    (9, "Under the interface, 1 of 8. What we see: Copilot. Microsoft’s AI assistant. Or several, wearing one name. Copilot snowmen stand on the tip of an iceberg outline. Keep in mind: “Copilot” is the tip of a very huge iceberg."),
    (10, "Under the interface, 2 of 8. Where do we meet it? Apps. Built into Word, Teams, Edge and Windows, with hidden instructions behind each. Keep in mind: built to feel helpful. That’s design, not evidence."),
    (11, "Under the interface, 3 of 8. What generates the text? Models. OpenAI, Anthropic or Microsoft. You don’t see which. Your prompt, plus web results and files, goes in between the app and the model. Keep in mind: models have cutoffs and keep changing."),
    (12, "Models, with a screenshot of the Copilot model menu: Auto, Quick response, Think deeper, and GPT models. Keep in mind: the application is not the model. The models keep changing."),
    (13, "Under the interface, 4 of 8. What shapes the model? Training. Learns to predict text, then gets tuned by human ratings. Keep in mind: tuned to please. Pleasing isn’t the same as right."),
    (14, "Under the interface, 5 of 8. What does it learn from? Data and training. Models learn patterns from large collections of data. Further training shapes which kinds of responses they are encouraged to produce. Keep in mind: what’s common in the data isn’t necessarily true. What’s rewarded in the training isn’t necessarily good for learning."),
    (15, "Under the interface, 6 of 8. Who makes it work? Human labour. Creators, annotators, moderators, maintainers. Keep in mind: “automatic” rests on hidden, low-paid work."),
    (16, "Under the interface, 7 of 8. What does it run on? Material infrastructure. Chips, data centres, energy, water, minerals. Keep in mind: the real costs are mostly undisclosed."),
    (17, "Under the interface, 8 of 8. Who decides? Power shapes every layer: ownership, incentives, rules, values. Keep in mind: Microsoft sets most of the rules. Schools still decide how, and whether. Ask the room: what else comes into the classroom with AI?"),
    (18, "How does it work? How does an output get made? The word “answer” is crossed out and replaced with “output”."),
    (19, "One token at a time. 1, context: hidden instructions, the chat so far, files, web results, memory, and the words so far. 2, the model looks at all the tokens so far, using patterns from training. 3, prediction: a score for every possible next token, for example write 31%, read 22%, share 14%, and thousands more. 4, pick one: usually a likely one, not always the top, and add it to the context. Then do it again, and again."),
    (20, "A probability, not an answer. It predicts what’s likely to come next, one piece at a time. Several answers are possible, and how we ask changes which one we get. Keep in mind: it doesn’t have an answer. It has a probability."),
    (21, "Before the cases: three questions. 1, accurate? What evidence could we check? 2, appropriate? What does it assume about these learners and this place? 3, worthwhile? Does it support the work we want students to do? An answer can be correct and still wrong for this class, this purpose or this community."),
    (22, "Try it live in Copilot: two framings. A: Explain photosynthesis in three sentences. B: What do scientists still disagree about when it comes to photosynthesis? Run A twice. Same answer? Then try B. What changed?"),
    (23, "What sounds right: plausible isn’t true. A model can explain something clearly without having checked it, or sound sure while hiding real disagreement. Keep in mind: fluent and confident isn’t the same as checked."),
]


def talk_slides_html():
    import json
    data = json.dumps([{"src": f"assets/talk/{n:02d}.webp", "alt": a} for n, a in TALK_SLIDES], ensure_ascii=False)
    first = TALK_SLIDES[0]
    total = len(TALK_SLIDES)
    return f"""<style>
.deck{{margin:20px 0 8px}}
.deck-frame{{position:relative;aspect-ratio:16/9;border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);background:#f3eee6;overflow:hidden}}
.deck-frame img{{display:block;width:100%;height:100%;object-fit:contain}}
.deck-hit{{position:absolute;top:0;bottom:0;width:30%;background:none;border:0;padding:0;cursor:pointer}}
.deck-hit.prev{{left:0;cursor:w-resize}}.deck-hit.next{{right:0;cursor:e-resize}}
.deck-hit:focus-visible{{outline:3px solid var(--ink);outline-offset:-6px}}
.deck-bar{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:14px}}
.deck-count{{font-family:var(--font-mono,monospace);min-width:6ch;text-align:center}}
.deck-bar .fs{{margin-left:auto}}
.deck-frame:fullscreen{{border:0;border-radius:0;box-shadow:none;background:#000}}
</style>
<figure class="deck" id="slides" aria-roledescription="carousel" aria-label="Talk slides">
<div class="deck-frame">
<img id="deck-img" src="assets/talk/{first[0]:02d}.webp" alt="{esc(first[1])}" width="1920" height="1080">
<button class="deck-hit prev" type="button" aria-label="Previous slide"></button>
<button class="deck-hit next" type="button" aria-label="Next slide"></button>
</div>
<figcaption class="deck-bar">
<button class="btn" type="button" data-go="-1">← Previous</button>
<span class="deck-count" aria-live="polite">1 / {total}</span>
<button class="btn" type="button" data-go="1">Next →</button>
<button class="btn fs" type="button" hidden>Full screen</button>
</figcaption>
</figure>
<script>
(function(){{
  var S={data}, i=0, img=document.getElementById('deck-img'), deck=document.getElementById('slides'),
      frame=deck.querySelector('.deck-frame'), count=deck.querySelector('.deck-count'), fs=deck.querySelector('.fs');
  function show(n){{
    i=Math.max(0,Math.min(S.length-1,n));
    img.src=S[i].src; img.alt=S[i].alt; count.textContent=(i+1)+' / '+S.length;
    if(S[i+1]){{ new Image().src=S[i+1].src; }}
  }}
  deck.querySelector('.prev').onclick=function(){{show(i-1);}};
  deck.querySelector('.next').onclick=function(){{show(i+1);}};
  deck.querySelectorAll('[data-go]').forEach(function(b){{ b.onclick=function(){{show(i+Number(b.dataset.go));}}; }});
  document.addEventListener('keydown',function(e){{
    var t=e.target; if(t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.isContentEditable)) return;
    if(e.key==='ArrowRight'||e.key==='PageDown'){{show(i+1);e.preventDefault();}}
    else if(e.key==='ArrowLeft'||e.key==='PageUp'){{show(i-1);e.preventDefault();}}
    else if(e.key==='Home'){{show(0);}} else if(e.key==='End'){{show(S.length-1);}}
  }});
  var x0=null;
  frame.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX;}},{{passive:true}});
  frame.addEventListener('touchend',function(e){{ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40) show(i+(dx<0?1:-1)); x0=null; }});
  if(document.fullscreenEnabled){{
    fs.hidden=false;
    fs.onclick=function(){{ if(document.fullscreenElement) document.exitFullscreen(); else frame.requestFullscreen(); }};
    document.addEventListener('fullscreenchange',function(){{ fs.textContent=document.fullscreenElement?'Exit full screen':'Full screen'; }});
  }}
}})();
</script>"""


def section_page(i):
    b = BLOCKS[i]
    steps = "".join(f"<li>{esc(s)}</li>" for s in b["steps"])
    tiles = "".join(f'<a class="tile" {_href(h)}><h3>{esc(t)}{" ↗" if h.startswith("http") else ""}{" (PDF)" if h.endswith(".pdf") else ""}</h3><p>{esc(d)}</p></a>'
                    for h, t, d in b["tiles"])
    note = f'<p class="note-q">{esc(b["note"])}</p>' if b.get("note") else ""
    body = f"""{CSS}
<div class="doc wide">
<p class="eyebrow"><a href="index.html">The day</a> · {b['start']} to {b['end']}</p>
<h1>{esc(b['title'])}</h1>
<p class="lede">{esc(b['desc'])}</p>
{note}
{EXTRAS[b['extra']]() if b.get('extra') else ''}
{b.get('embed', '')}
{copilot_demo_html() if b.get('after_steps') == 'copilot_demo' else ''}
{talk_slides_html() if b.get('after_steps') == 'talk_slides' else ''}
{f'<h2>Materials</h2><div class="grid">{tiles}</div>' if tiles else ''}
{pager(i)}
</div>"""
    return {"file": b["file"], "nav": "home",
            "title": f"{b['title']} · Teaching with, about, and without AI",
            "desc": b["desc"], "html": body}


SECTION_PAGES = [section_page(i) for i, b in enumerate(BLOCKS) if not b.get("existing")]

# The cases page is the 9:25 block's page: give it the block's time and the day's pager.
import scenarios  # noqa: E402
_i = next(i for i, b in enumerate(BLOCKS) if b["file"] == "scenarios.html")
_idx = scenarios.SCENARIO_PAGES[0]
_idx["html"] = _idx["html"].replace('<p class="eyebrow">Classroom situations</p>',
                                    f'<p class="eyebrow"><a href="index.html">The day</a> · {BLOCKS[_i]["start"]} to {BLOCKS[_i]["end"]} · Classroom situations</p>', 1)
_idx["html"] = _idx["html"][: _idx["html"].rindex("</div>")] + pager(_i) + "\n</div>"
