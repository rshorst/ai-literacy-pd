"""Page content for the ai-literacy-pd site. Plain text and markdown, no school names."""
import html

SITE = {
    "name": "Teaching with, about, and without AI",
    "byline": "A professional learning day · Rachel Horst",
    "credit": '© 2026 Rachel Horst, University of British Columbia. Shared under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.',
    "updated": "Updated November 2026",
    "repo": "https://github.com/rshorst/ai-literacy-pd",
    "url": "https://rshorst.github.io/ai-literacy-pd/",
}

# Nav follows the order of the day.
NAV = [
    ("home", "The day", "index.html"),
    ("map", "AI map", "map.html"),
    ("scenarios", "Classroom situations", "scenarios.html"),
    ("policies", "Policy examples", "policies.html"),
    ("handouts", "Handouts", "handouts.html"),
    ("activities", "Activities", "activities.html"),
    ("frameworks", "Frameworks", "frameworks.html"),
    ("readings", "Readings", "readings.html"),
]

# Tape colour behind each page title, and one collage cut-out per page.
PAGE_STYLE = {
    "scenarios": {"tape": "pink", "deco": "lightbulb.webp"},
    "policies": {"tape": "teal", "deco": "sticker-collective.webp"},
    "handouts": {"tape": "yellow", "deco": "laptop.webp"},
    "activities": {"tape": "pink", "deco": "plant.webp"},
    "frameworks": {"tape": "yellow", "deco": "collage-ai.webp"},
    "readings": {"tape": "blue", "deco": "sticker-critical.webp"},
}

ZIP = "https://github.com/rshorst/ai-literacy-pd/archive/refs/heads/main.zip"
ED = "https://claude.ai/artifact/WSF2rJt3rngbyucXuhWF9N"  # interactive version
CSM = "https://rshorst.github.io/computational-sense-making/"
FUT = "https://rshorst.github.io/AI-Futures/"

PRINT = '<div class="tools no-print"><button class="btn" type="button" onclick="window.print()">Print this page</button></div>'


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- Home
HOME = f"""
<section class="hero">
<img class="deco-corner" src="assets/pink-paper-corner.webp" alt="">
<div class="hero-inner">
<div class="hero-text">
<h1 class="title"><span class="l">Teaching</span><span class="l tape pink">with,</span><span class="l tape teal">about,</span><span class="l and">and</span><span class="l tape yellow">without</span><span class="l ai">AI</span></h1>
<div class="hero-meta"><div>
<p class="byline"><span class="tape teal">with Dr. Rachel Horst</span></p>
<p class="kicker">A professional learning day for K-12 educators</p>
<p class="when">Friday 20 November 2026 · 9:00 to 3:00</p>
</div>
<figure class="access"><img src="assets/qr-materials.png" alt="QR code for bit.ly/ai-literacy-pd" width="132" height="132"><figcaption>Scan for the materials<br><a href="https://bit.ly/ai-literacy-pd">bit.ly/ai-literacy-pd</a></figcaption></figure></div>
</div>
<div class="hero-art" aria-hidden="true">
<img class="a-bulb" src="assets/lightbulb-with-rays.webp" alt="">
<img class="a-plant" src="assets/plant.webp" alt="">
<img class="a-laptop" src="assets/laptop.webp" alt="">
<img class="a-critical" src="assets/sticker-critical.webp" alt="">
<img class="a-creative" src="assets/sticker-creative.webp" alt="">
<img class="a-practical" src="assets/sticker-practical.webp" alt="">
<img class="a-collective" src="assets/sticker-collective.webp" alt="">
</div>
</div>
<img class="deco-mountains" src="assets/mountains-and-sun.webp" alt="">
<img class="deco-forest" src="assets/forest-corner.webp" alt="">
</section>

<div class="doc wide">
<p class="lede">Generative AI is already in classrooms, whether or not a school has decided anything about it. This professional development day will be about what these systems actually are and do, what this means for teaching and assessment, and how educators and students can make more deliberate choices about where and how AI belongs, and where it does not.</p>
<p>The day will be discussion-led. We’ll work through real classroom situations, try a few things in Microsoft Copilot, and reconsider something you already teach. We’ll also begin gathering questions and priorities that could inform future classroom- and school-level guidance around AI. (You’ll notice I don’t love the “tool” metaphor, but we’ll talk about that.)</p>

<h2>The day</h2>
<p>Every block has something to try and something to discuss. Timings and emphasis can shift in response to the pre-session input and the conversation in the room.</p>
<ol class="agenda">
<li><time>9:00</time><div><h3>Welcome</h3><p>A chance to reconnect, introduce the day, and begin with what matters to us in teaching and learning.</p><p class="res"><a href="metaphor.html">My AI Metaphor</a><a href="quickdraw.html">Quick, Draw!</a></p></div></li>
<li><time>9:15</time><div><h3>What are these strange systems, anyway?</h3><p>A plain-language introduction to how generative AI systems compose outputs, and the minimum technical background we need to make informed decisions about them. Then we experiment and see what happens.</p><p class="res"><a href="talk.html">Talk slides</a><a href="map.html">AI map</a></p></div></li>
<li><time>9:40</time><div><h3>Classroom situations</h3><p>Small groups work through real and plausible situations involving generative AI in teaching and learning. We look closely at what is happening, what choices are available, and what different responses might mean for students, teachers, and the classroom.</p><p class="res"><a href="scenarios.html">Classroom situations</a><a href="responses.html">Shared board</a></p></div></li>
<li class="pause"><time>10:25</time><span>Break</span></li>
<li><time>10:40</time><div><h3>How should AI fit into classroom work?</h3><p>A look at several ways educators and schools are approaching AI use in learning and assessment, from blanket rules to more nuanced frameworks such as the AI Assessment Scale. We consider what each approach makes possible, what assumptions it carries, and where it might break down in different K-12 contexts. Then we use a collaborative protocol to make decisions about AI use in a real classroom activity or assignment.</p><p class="res"><a href="policies.html">Policy examples</a><a href="class-ai-agreement.html">Collaborative protocol</a></p></div></li>
<li><time>11:25</time><div><h3>Some things worth trying in Copilot</h3><p>A hands-on look at a small number of useful things generative AI can do for teaching: generating alternatives, explaining something in different ways, creating examples and counterexamples, testing instructions, looking for gaps, and helping you see a lesson from another angle. Try a few with something you actually teach and decide what is useful, what is not, and what you would want to change.</p><p class="res"><a href="copilot-and-prompting.html">Copilot and prompting</a><a href="practical-moves.html">Practical moves</a></p></div></li>
<li class="pause"><time>11:55</time><span>Lunch</span></li>
<li><time>12:45</time><div><h3>Rethinking something you already teach</h3><p>Bring a lesson, activity, assignment, or unit you already teach. We use what we have explored so far to reconsider where AI might support the learning, where it might change or bypass something important, and where it may not belong at all.</p><p class="res"><a href="activities.html#activity-11">Activities for educators</a><a href="readings.html">Readings on assessment</a></p></div></li>
<li><time>1:45</time><div><h3>Looking at the bigger picture</h3><p>We use the Entangled Dimensions of AI Literacy framework to step back from individual classroom uses and explore some of the wider questions connected to AI: knowledge, relationships, institutions, resources, values, and planetary systems. Participants explore the framework themselves and use it to look at a classroom example, question, or concern from another angle.</p><p class="res"><a href="frameworks.html">Frameworks</a><a href="map.html#o-k-rec">Other kinds of AI</a></p></div></li>
<li class="pause"><time>2:15</time><span>Break</span></li>
<li><time>2:25</time><div><h3>From classroom choices to collective decisions</h3><p>We bring together the questions that have surfaced throughout the day and consider what can be decided by an individual educator, what may need shared school guidance, and what calls for broader community conversation. We look at emerging approaches elsewhere as possibilities to examine, not templates to adopt.</p><p><em>What needs to be decided here, who needs to be part of that decision, and what should remain open?</em></p><p class="res"><a href="policies.html">Policy examples</a><a href="activities.html#activity-13">The document audit</a></p></div></li>
<li><time>2:50</time><div><h3>Close</h3><p>We close by imagining the kinds of futures with AI we would want to move toward, and the ones we would want to resist.</p><p class="res"><a href="{FUT}">AI Futures map</a></p></div></li>
</ol>

<h2>What educators leave with</h2>
<ul class="leave">
<li>The Entangled Dimensions of AI Literacy framework with prompts for exploring AI as more than a tool. <a href="frameworks.html">Frameworks</a></li>
<li>A simple “with, about, or without?” planning guide for deciding whether, where, and why AI belongs in a particular learning activity.</li>
<li>A small collection of approaches for thinking about AI use in teaching and assessment including a collaborative decision-making protocol adaptable across grades and contexts. <a href="policies.html">Policy examples</a> · <a href="class-ai-agreement.html">Protocol</a></li>
<li>A set of practical Copilot ideas and prompts to experiment with in planning and teaching. <a href="copilot-and-prompting.html">Copilot and prompting</a></li>
<li>Adaptable K-12 activities for teaching about AI including options that do not require students to have AI accounts. <a href="activities.html">Activities</a></li>
<li>One lesson, activity, or assignment of their own reconsidered or redesigned in light of the day.</li>
<li>A staff-generated set of questions and priorities to carry forward into future classroom, school, and community conversations about AI guidance and policy.</li>
</ul>

<div class="two">
<div>
<h2>After the day</h2>
<p>If it would be useful, we can keep some of these conversations going after November. Possible next steps might include:</p>
<ul>
<li><strong>A policy session:</strong> a 60-90 minute online session in the new year, working from the questions that emerge during the day toward classroom- or school-level guidance.</li>
<li><strong>A short check-in:</strong> a few weeks later, a chance to share what you tried, what happened, and what questions are still hanging around.</li>
<li><strong>An ongoing AI literacy partnership:</strong> continued planning support, conversation, and another session later in the year.</li>
</ul>
</div>
<div>
<h2>A note on context</h2>
<p>I am coming to this as an educator, researcher, and lecturer in UBC’s Master of Educational Technology program. When I work with a school community I am not part of, questions involving local knowledge, language, data, and protocols carry particular significance. Some questions about AI can be worked through at the classroom level; others may belong at the school or community level. Where those boundaries arise, we can name them together, and leave them with the people they belong to.</p>
</div>
</div>

<h2>Frameworks we’ll use</h2>
<p>The day draws on two open frameworks developed through work at UBC:</p>
<div class="grid">
<a class="tile" href="{ED}"><h3>Entangled Dimensions of AI Literacy</h3><p>A way of looking beyond the immediate use of an AI system to the wider questions of knowledge, relationships, institutions, resources, values, and planetary systems.</p></a>
<a class="tile" href="{CSM}"><h3>Computational Sense-Making</h3><p>A way of looking more closely at what computational systems are doing, how they produce outputs, and how we make sense of them.</p></a>
</div>
<p>Both are freely available and will remain available after the session.</p>

<h2>Everything on this site</h2>
<div class="grid">
<a class="tile" href="map.html"><h3>AI map</h3><p>Who makes what in AI: companies, models, apps, and the other kinds of AI that rank, sort and predict.</p></a>
<a class="tile" href="scenarios.html"><h3>Classroom situations</h3><p>Ten fictional cases grounded in research and reporting, with Copilot prompts and a group response.</p></a>
<a class="tile" href="policies.html"><h3>Policy examples</h3><p>Twenty K to 12 AI policies to examine, not templates to adopt.</p></a>
<a class="tile" href="handouts.html"><h3>Handouts</h3><p>What these systems are, practical moves, the collaborative protocol, and Copilot and prompting.</p></a>
<a class="tile" href="activities.html"><h3>Activities</h3><p>Twenty short moves for students and for staff, about AI and with AI.</p></a>
<a class="tile" href="readings.html"><h3>Readings</h3><p>Fifteen recent readings on assessment, feedback, lesson planning, students’ use and refusal.</p></a>
</div>

<h2>Use it offline</h2>
<p>Every page works on its own: open it, save it from your browser, and it runs without an internet connection. To keep the whole site with its links and images, <a href="{ZIP}">download it as a zip</a>, unzip it, and open <code>index.html</code>. The cards, activities and handouts also print cleanly.</p>

<h2>Contact</h2>
<p class="contact">Rachel Horst, PhD<br>University of British Columbia<br>rachel.horst@ubc.ca</p>
</div>
"""

# ---------------------------------------------------------------- Scenario cards
CARDS = [
    ("The helpful feedback",
     "A Grade 10 student shows you feedback a chatbot gave on their essay. It is specific, encouraging and mostly right. The student rewrote their essay to match it, and it is now smoother and less theirs.",
     "relational, creative, epistemic",
     "What did the student gain and what did they give up? Whose voice is the essay in now? What would feedback from you have done differently?",
     "Composition", "Ask for feedback on a short paragraph, then ask it to “argue with the writer rather than fix the writing”. Compare."),
    ("The class agreement",
     "Your department wants one AI rule for all courses. Your students want a say.",
     "political, relational, disciplinary",
     "Who gets to decide? Should the rule differ in art, science and English? What does a rule assume about students?",
     "Constraints", "Ask a chatbot to write a class AI policy. Note what it includes by default and what it leaves out: cost, data, refusal, community knowledge."),
    ("The grade it gave",
     "A colleague ran a stack of lab reports through a chatbot “just to check” their marks. The model's scores were close to theirs, with confident comments.",
     "epistemic, data, relational",
     "Is close agreement evidence of anything? What should students be told? What is assessment for, if a machine can mimic it?",
     "Calibration", "Grade the same sample three times. Compare scores and reasoning. Ask it how certain it is."),
    ("The un-AI-able task",
     "You redesign an assignment so it “can't be done with AI”: handwritten, in class, personal. A student with an IEP relied on AI-supported drafting.",
     "knowledge-construction, relational, political",
     "Who does structural redesign help and who does it exclude? What is the task protecting?",
     None, "None. Discuss without the machine, and notice what that is like."),
    ("Where it lives",
     "A student asks how much water their chatbot use takes. Another says it's tiny compared to video streaming.",
     "ecological, political, futures",
     "How do we teach cost when the numbers are contested and the companies don't publish them? Does this belong in every subject?",
     "Calibration", "Ask the chatbot the student's question. How confident does it sound? What sources can you find?"),
    ("The picture of us",
     "Students ask an image generator for “a family from our town”. The results look like nobody they know.",
     "data, creative, relational",
     "What does the system treat as normal? Whose absence is this? What would students make instead?",
     "Computation", "Add context step by step and watch what changes and what doesn't."),
    ("The confident history",
     "A chatbot gives a smooth, confident account of a local historical event. Parts of it are wrong, and it leaves out whose account it is.",
     "epistemic, knowledge-construction, political",
     "Whose knowledge is in the training data, and whose is not? What should never be asked of the machine?",
     "Computation", "Ask it where its account comes from and what it cannot know. Read the refusal or the invention."),
    ("The study buddy",
     "A student uses a chatbot every night to “explain things”. Their test scores are up. They say they have stopped asking you questions.",
     "relational, epistemic, futures",
     "What is lost if the relationship moves to the machine? What is gained? What would you say to this student?",
     "Constraints", "Ask the chatbot to disagree with you about something. Notice how it smooths."),
    ("The free tool",
     "A company offers your school free AI accounts for every student, with lesson plans included.",
     "political, data, futures",
     "What is the business model? What happens to student data? What future is being built, and who chose it?",
     None, "Ask the chatbot to summarise the tool's terms of service, then check it against the actual terms."),
    ("The lesson plan in thirty seconds",
     "A new teacher generates a full unit plan in half a minute. It is tidy, aligned to curriculum, and generic.",
     "disciplinary, creative, knowledge-construction",
     "What does planning do for a teacher beyond producing a plan? Where is the time better spent?",
     "Composition", "Regenerate twice. What stays the same? That sameness is the average."),
]


def cards_html():
    out = []
    for i, (title, scen, threads, ask, c, move) in enumerate(CARDS, 1):
        label = f"Try it ({c})" if c else "Try it"
        out.append(
            f'<article class="card" id="card-{i}"><p class="num">Card {i}</p><h3>{esc(title)}</h3><p>{esc(scen)}</p>'
            f'<dl><dt>Threads</dt><dd>{esc(threads)}</dd><dt>Ask</dt><dd>{esc(ask)}</dd><dt>{label}</dt><dd>{esc(move)}</dd></dl></article>'
        )
    return "\n".join(out)


CARDS_PAGE = f"""
<div class="doc wide">
<p class="eyebrow">Classroom situations</p>
<h1>More scenario cards</h1>
<p class="lede">Ten classroom situations for discussion. Each pulls on two or three dimensions of the <a href="frameworks.html">Entangled Dimensions</a> framework and suggests one move to try with a chatbot, read through one of the four Cs of Computational Sense-Making.</p>
<p><strong>How to run them.</strong> Groups of three or four take one card each. Discuss for ten minutes, try the move for five, then report one tension back to the room in two. If there is no connection, run the move on one screen, read out a saved output, or skip it.</p>
{PRINT}
<div class="cards">
{cards_html()}
</div>
<p class="meta">Free to reuse and adapt under CC BY 4.0. Cards to write next: a parent who forbids AI.</p>
</div>
"""

# ---------------------------------------------------------------- Activities
STUDENT_ACTS = [
    ("Unaided first", "With AI", "25 min. Any subject.", "Students do the task cold: a summary, an explanation, a set of predictions. Then they run the same task through the model and mark up the difference in two colours: what it added, what it flattened. The comparison is the assignment, not either version.", "What did it make smoother, and what did that smoothing cost?", "Knowledge-construction, epistemic."),
    ("Read the hidden prompt", "About AI", "20 min. Teacher screen.", "Ask an image tool for a group of people, then show students the expanded prompt the system actually sent, which usually contains descriptions nobody typed. The system edited the request before answering it.", "Who decided what to add, and what would you have asked for instead?", "Algorithmic, data. Computation and Constraints."),
    ("Critique the critique", "With AI", "30 min. English, Social Studies.", "The model drafts a critique of a text students know well. Students then critique the critique, line by line, against the text itself.", "Where was it right for the wrong reason?", "Epistemic, knowledge-construction."),
    ("The refusal log", "About AI", "One week. 10 min to set up, 20 min to debrief.", "Students keep a running log of every time a model refuses, hedges, softens or changes the subject. In the debrief they sort the entries: safety, liability, politeness, vagueness, no idea.", "What is this system protecting, and from whom?", "Political, epistemic. Constraints."),
    ("Translate and check", "With AI", "40 min. Languages, any class with multilingual students.", "Translate a short passage into a language someone in the room speaks. Check it sentence by sentence with that speaker, not with the model.", "What went missing that was not a word?", "Relational, epistemic, data."),
    ("Source trail", "With AI", "30 min. Any research task.", "Ask for five sources on a topic. Students verify each: does it exist, does it say what the model claims, is the author real. Tally the results on the board across the class.", "What would it take for you to trust a reference you did not check?", "Knowledge-construction, epistemic. Calibration."),
    ("Three drafts, one page", "With AI", "35 min plus homework. Any writing task.", "Students keep their original draft, the model's suggestions and their final revision on one page, side by side, and write a short note on what they accepted and why.", "Which suggestion did you refuse, and what were you protecting?", "Creative, relational."),
    ("Whose hands", "About AI", "40 min. Art, Social Studies, Careers.", "Students read a short account of data labelling and content moderation work, then map the chain behind one output: who wrote the training text, who labelled it, who paid, who profits.", "Which part of that chain is invisible in the interface, and why might that be?", "Political, ecological."),
    ("Ask it about here", "About AI", "25 min.", "Students ask the model detailed questions about their own community: local history, a recent event, a place only locals would know. They mark what it invented and what it generalised.", "What did it replace local knowledge with?", "Epistemic, data."),
    ("Rewrite the assignment", "With AI", "30 min. Any subject.", "Give the model your actual assignment sheet and ask it to complete the task. The class reads the output against the criteria and decides what mark it would get, and what the task was really asking for.", "What would we have to change so that answer would not be enough?", "Knowledge-construction, disciplinary."),
]
STAFF_ACTS = [
    ("Run your own task through it", None, "45 min. Staff meeting or workshop block.", "Everyone brings a current assessment task. Run each through a model, read the output against your own criteria, then change one structural thing about the task, not the wording of the rules.", "What part of this task was never really about the writing?", "Assessment. Knowledge-construction."),
    ("One task, three levels", None, "30 min.", "Take a single task and write three versions: no AI, AI for planning only, AI throughout with the process shown. Decide which you would actually run and what you would tell students about why.", "What is the reason, in a sentence a student would accept?", "Assessment, political."),
    ("The document audit", None, "30 min.", "Before anyone writes an AI policy, list the documents that already exist: integrity, devices, privacy, assessment, home communication. Mark which need one new line rather than a new document.", "What do we already say that covers this?", "Political."),
    ("Show one, refuse one", None, "20 min. Pairs.", "Each teacher demonstrates one thing they do with AI, and one thing they will not use it for, with the reason. Collect the refusals on the board. The refusals are the more interesting list.", "Which refusals do we share, and which are personal?", "Relational, creative."),
    ("Ask the families first", None, "20 min to design, then run it.", "Draft five questions for parents and caregivers about where AI may and may not be used in their child's learning. Schools that have done this find support for short updates and resistance to anything high-stakes.", "Which answer would change what we do?", "Relational, political."),
    ("The wrong answer bank", None, "15 min, then ongoing.", "Every teacher brings one confidently wrong output in their own subject. Keep them in a shared folder and use them with students, since a generic error is not as convincing as one in your own field.", "How would a student in your class have spotted this?", "Epistemic, disciplinary. Calibration."),
    ("Marking the boundary", None, "25 min.", "Each teacher names one piece of work in their course that should stay unmediated, and says what it protects. Then: what would you do if you found it had been outsourced anyway?", "Was the rule the point, or the relation?", "Relational, creative."),
    ("What are we scoring", None, "30 min.", "Hand out a published set of questions for deciding whether a school should adopt an AI tool. Groups answer them for a tool the school already uses, then list what the questions never ask about.", "Who would have to be in the room for those missing questions to get asked?", "Political, futures."),
    ("Where does it run", None, "25 min.", "Find out where the data centres behind the school's approved tools are, what they use, and who lives near them. The numbers will conflict and most will be estimates.", "What would you need to know to say this is worth it?", "Ecological, political."),
    ("The register", None, "20 min to start.", "Begin a shared list of every AI tool staff and students actually use, including the ones nobody approved. Keep it open to families.", "What is on this list that we did not know about?", "Data, political."),
]


def acts_html(acts, start):
    out = []
    for i, (title, kind, time, text, ask, dims) in enumerate(acts, start):
        k = f'<span class="tag">{kind}</span>' if kind else ""
        out.append(
            f'<article class="card" id="activity-{i}"><p class="num">{i}</p><h3>{esc(title)}</h3>'
            f'<p>{k}<span class="tag">{esc(time)}</span></p><p>{esc(text)}</p>'
            f'<dl><dt>Ask</dt><dd>{esc(ask)}</dd><dt>Dimensions</dt><dd>{esc(dims)}</dd></dl></article>'
        )
    return "\n".join(out)


ACTIVITIES_PAGE = f"""
<div class="doc wide">
<p class="eyebrow">Short moves</p>
<h1>Activities</h1>
<p class="lede">Quick activities to drop into a class, a staff meeting or a workshop block. Each says whether it is <strong>about AI</strong>, where AI is the thing being studied, or <strong>with AI</strong>, where AI serves learning something else.</p>
<p>Nothing here needs student accounts. Every student activity runs on a teacher's screen, and Translate and check needs a speaker, not a tool.</p>
{PRINT}
<h2>For students</h2>
<div class="cards">
{acts_html(STUDENT_ACTS, 1)}
</div>
<h2>For educators</h2>
<div class="cards">
{acts_html(STAFF_ACTS, 11)}
</div>
</div>
"""

# ---------------------------------------------------------------- Handouts
HANDOUTS_INDEX = """
<div class="doc">
<p class="eyebrow">Print or share</p>
<h1>Handouts</h1>
<p class="lede">Short handouts for teachers. Each one is its own page, prints on its own, and works offline once saved.</p>
<div class="grid">
<a class="tile" href="what-these-systems-are.html"><h3>What these systems are</h3><p>Eight things educators need to know about chatbots, in plain language.</p></a>
<a class="tile" href="practical-moves.html"><h3>Practical moves</h3><p>Moves for teachers and for students, tied to the four Cs.</p></a>
<a class="tile" href="class-ai-agreement.html"><h3>The class AI agreement</h3><p>A protocol for writing a class AI agreement with students in one or two lessons.</p></a>
<a class="tile" href="copilot-and-prompting.html"><h3>Copilot and prompting</h3><p>What Copilot is in a school, what it is good for, and six prompting strategies.</p></a>
</div>
</div>
"""

SYSTEMS_MD = """
<p class="eyebrow">Handout</p>

# What these systems are

<p class="lede">Eight things educators need to know about chatbots and the models behind them. The tags in brackets point to the four Cs of <a href="frameworks.html">Computational Sense-Making</a> and the dimensions they touch.</p>

<div class="tools no-print"><button class="btn" type="button" onclick="window.print()">Print this page</button><a class="btn" href="map.html">Open the AI map</a></div>

1. **A chatbot predicts the next word.** It generates text from patterns in a very large body of text. Fluency is not understanding. (Computation)
2. **It knows within the borders of its data.** It has a cutoff date, filters and exclusions, and it leans toward what was most often written, by whom and in which languages. (Computation; data, epistemic)
3. **The prompt shapes the answer.** How a question is framed sets what counts as a possible answer. (Composition)
4. **It is tuned to be agreeable.** Training smooths conflict, favours consensus and refuses some requests. Those are choices someone made. (Constraints; political)
5. **Confidence is performed, not earned.** A precise grade or a confident claim is a style, not a judgement. Run it twice and compare. (Calibration)
6. **It has material costs.** Energy, water, minerals and hidden human labour in data labelling and moderation. (Ecological, relational, political)
7. **Your data goes somewhere.** What students type may leave the country and train future models. Check what your district has approved. (Data, political)
8. **Detectors do not work reliably.** Several districts have rejected them. Design the task instead. (Knowledge-construction) See [AI detectors on the map](map.html#o-k-detect).

<p class="meta">The app is not the model, and one model often sits behind many apps. The <a href="map.html">AI map</a> shows who makes what.</p>
"""

MOVES_MD = """
<p class="eyebrow">Handout</p>

# Practical moves

<p class="lede">Small habits that make AI use more honest, for teachers and for students. Pick one to try this week.</p>

<div class="tools no-print"><button class="btn" type="button" onclick="window.print()">Print this page</button></div>

## For teachers

- **Run it twice.** Compare before trusting any output. (Calibration)
- **Ask for what is uncertain or debated,** not just an explanation. (Computation)
- **Change the frame** and watch the answer change. (Composition)
- **Ask what it left out.** (Constraints)
- **Keep AI out of relational feedback** you would want to give yourself.
- **Design structurally:** process, in-class drafting, oral defence, reflection.
- **Check your district's approved tools** and data rules before students log in.

## For students

- “Show me where you might be wrong.”
- “Argue with me.”
- “Who would disagree with this, and why?”
- Keep your own draft first. Use AI after, not instead.
- Say when you used it, and how. Include the chat if asked.
- It is fine to choose not to use it.
"""

AGREEMENT_MD = """
<p class="eyebrow">Handout</p>

# The class AI agreement

<p class="lede">A protocol you can run with students in one or two lessons. In a workshop, teachers run it themselves, taking the student role.</p>

<div class="tools no-print"><button class="btn" type="button" onclick="window.print()">Print this page</button></div>

1. **Surface (5 min).** Each person writes three things: one way AI helps me learn; one way it gets in the way; one thing I don't want it used for.
2. **Sort (5 min).** Groups cluster the notes, then name each cluster with a dimension, for example data, relational or creative.
3. **Machine draft (5 min).** Ask a chatbot for a class AI policy. Read it together. What did it assume? What is missing from our clusters? (Constraints)
4. **Draft our own (10 min).** Three short sections: *We will. We won't. We'll ask first.* Every line names why.
5. **Agree how to revisit.** Set a date to review it, and post it in the room.

## What you end up with

- A class agreement in students' own words.
- A record of the reasoning behind each line.

<div class="note">What a chatbot writes as a class policy is usually all permission and detection. Cost, data, refusal and student voice tend to be missing. That gap is a good place to start the discussion.</div>

See the <a href="policies.html">policy examples</a> for twenty published school and district policies to compare with.
"""

COPILOT_MD = """
<p class="eyebrow">Handout</p>

# Copilot and prompting

<p class="lede">A working handout for schools that use Microsoft 365. Microsoft renames and relicenses these products often, so what is on your screen may not match this page. Check details with your district's IT team.</p>

<div class="tools no-print"><button class="btn" type="button" onclick="window.print()">Print this page</button></div>

## What Copilot is in a school

There are two products sharing one name.

**Microsoft 365 Copilot Chat** is the free one. It comes with the standard school licences at no extra cost. It works from the web, not from your school's files.

**Microsoft 365 Copilot** is the paid add-on. What you get for the money is grounding in your own work, meaning your files, mail, calendar and Teams content, plus drafting features inside Word, Excel and PowerPoint.

In practice, the side panel that answers questions is free. Features that rewrite the document in front of you are paid, and some may not be available on education licences at all. Check before you rely on them.

### Data protection, honestly described

Microsoft commits that prompts and responses in a work or school account are not used to train its models, and that data stays inside your organization's permissions, retention and audit systems. Three things that commitment does not cover:

1. **It follows the account, not the app.** Sign in with a personal Microsoft account and you are under consumer terms.
2. **Web search is different.** When Copilot searches the web, the query goes out under Microsoft's ordinary service agreement.
3. **Where the data lives.** Don't assume your prompts stay in Canada. When this was written, Microsoft's data residency pages did not commit to that for Copilot Chat. Check your district's position under FIPPA.

### Students

In a K to 12 setup, Microsoft's defaults block students under 13 from Copilot Chat, and 13 to 17 year olds are off unless an administrator sets age groups and records consent. Staff-only is the default, not a local restriction. Check what your school has enabled.

### Education tools worth knowing

- **Teach in Microsoft 365 Copilot.** Lesson plans, quizzes, rubrics, and adapting material by reading level, language or difficulty. For staff only, included with education licences.
- **Learning Zone.** Builds interactive lessons from your materials. Creating lessons needs a Copilot+ PC; students can open finished lessons on any device.
- **Learning Accelerators.** Reading Progress, Reading Coach, Search Coach, Speaker Coach, Math Progress and Reflect. These are longstanding tools, not new AI.
- **Elevate for Educators.** A free Microsoft educator credential launched with ISTE and ASCD in January 2026. Worth knowing about, and worth discussing: free vendor training is not neutral training.

## Good uses, and what to skip

**Reasonable uses**

- First drafts of routine writing: newsletters, permission letters, a description of an assignment.
- Reformatting and restructuring something you already wrote.
- Variations: three versions of a task at different reading levels, ten practice questions to choose from.
- Summarising a long document you already understand, so you can find the part you need.
- Getting unstuck on a lesson idea.

**Skip or be careful**

- **Grading.** That is your professional judgement and your district's policy. Run the same piece of work through twice and see how stable the mark is before trusting it with anyone's grade.
- **Writing about identifiable people,** whether students, colleagues or families. The Dutch education sector's assessment of Copilot found it inventing biographical details about real people.
- **Anything factual that goes to students unverified.** The same assessment found fabricated articles and court cases.
- **Feedback you would want to give yourself.** The relationship is the point.
- **Transcribing meetings with students or parents.** That is a consent question for your district, not a feature question.

**What the evidence says about time.** The best trial so far randomised 259 science teachers across 68 schools using a chatbot for lesson preparation. They saved about 25 minutes a week, roughly a third of their preparation time, and independent reviewers found no difference in the quality of what they produced. It can save time. It does not obviously make the work better.

## Prompting strategies

These are reasonable heuristics. Research on prompting is thin, so treat them as craft, not method.

**Six that do most of the work**

1. **Say who and what for.** Grade, subject, length, what the students already know. Most disappointing output is a missing-context problem.
2. **Show it an example.** Paste one of your own handouts and ask for something that matches it.
3. **Ask for options, not an answer.** Three versions, and you pick.
4. **Work in steps.** Outline first, agree the outline, then the content.
5. **Say what the output should look like.** A table with these columns, six bullets, under 200 words.
6. **Make it argue.** “What is wrong with this?” “What would a skeptical colleague say?” The default setting is agreeable, which is not useful.

**Three habits that matter more than any prompt**

- **Run it twice.** Two fresh chats, same question. What changes is what it was never sure about.
- **Ask what it left out.** The smoothing is where the interesting material went.
- **Verify anything factual.** Every name, date, number and citation, before it reaches a student.

<div class="note">One question to keep asking: what am I giving up by handing this over? Sometimes nothing. Sometimes the thinking was the job.</div>

## Sources

- Microsoft, [Copilot licensing](https://learn.microsoft.com/en-us/copilot/manage) and [enterprise data protection](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)
- Microsoft, [education AI features and Teach in Copilot](https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/manage-microsoft-365-education-ai-features) and [enabling Copilot Chat for learners](https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/enable-copilot-chat-for-learners)
- SURF, [data protection impact assessment on Microsoft 365 Copilot for Education](https://www.surf.nl/files/2025-09/20250911-surf-public-update-dpia-on-m365-copilot-for-education-website.pdf) (September 2025)
- EEF and NFER, [teacher choices trial on lesson preparation](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/choices-in-edtech-using-generative-ai-chatgpt-for-ks3-science-lesson-preparation-2024-teacher-choices-trial)

<p class="meta">Checked September 2026.</p>
"""

# ---------------------------------------------------------------- Readings
READINGS = [
    ("Assessment and feedback", [
        ("Corbin, T., Dawson, P., & Liu, D. (2025). Talk is cheap: Why structural assessment changes are needed for a time of GenAI. <em>Assessment & Evaluation in Higher Education, 50</em>, 1087–1097.", "https://doi.org/10.1080/02602938.2025.2503964", "Open access",
         "Separates discursive changes to assessment (telling students what is allowed, declarations, honour statements) from structural ones (changing what the task is, where and when it happens, with whom). Argues the discursive kind depends on students following instructions nobody can enforce, so only structural change holds. Written for higher education, but the distinction transfers directly to a secondary classroom and is the cleanest way to explain why “just tell them not to” fails.", "relational + creative"),
        ("Bearman, M., Tai, J., Dawson, P., Boud, D., & Ajjawi, R. (2024). Developing evaluative judgement for a time of generative artificial intelligence. <em>Assessment & Evaluation in Higher Education, 49</em>(6), 893–905.", "https://doi.org/10.1080/02602938.2024.2335321", "Open access",
         "The positive answer to “what do we assess, then?” The capacity students most need is evaluative judgement: telling good work from bad, including AI output, and knowing why. Offers design moves teachers can use tomorrow: exemplars, feedback on students' judgements, calibration against criteria.", "epistemic + knowledge construction"),
        ("Webb, M., & Galamba, A. (2026). Transforming pedagogy with GenAI-supported formative assessment: Challenges for teacher education. <em>British Journal of Educational Technology, 57</em>(3), 690–706.", "https://doi.org/10.1111/bjet.70051", "May need library access",
         "Written for teacher educators. Reads GenAI against established formative assessment theory and asks what teacher preparation now has to include. Their line that “AI agency is agency without intelligence” is a good provocation for a room. Also honest that digital technologies have historically had only moderate effects on learning.", "epistemic + knowledge construction; disciplinary + futures"),
        ("Meyer, J., Steinbach, M., Schiller, R., Mertens, U., Schaller, N.-J., Horbach, A., Fleckenstein, J., Köller, O., Kizilcec, R. F., & Jansen, T. (2026). Comparing teacher and AI-generated feedback in the writing classroom: Experimental results from secondary school classrooms. <em>Proceedings of the Thirteenth ACM Conference on Learning @ Scale</em>.", "https://doi.org/10.1145/3774398.3811602", "Open access",
         "Secondary English-as-a-foreign-language classrooms, 391 students. Teacher-written feedback was compared with immediate and delayed AI feedback on essay revision and later writing. The differences were small and not significant; students rated immediate feedback as more useful and motivating. The authors see the value of AI feedback in redistributing teacher effort, not in beating teachers. Worth reading against the grain: what counts as feedback here, and what is missing from the measure?", "relational + creative"),
        ("Zhan, Y., & Yan, Z. (2025). Students' engagement with ChatGPT feedback: Implications for student feedback literacy in the context of generative artificial intelligence. <em>Assessment & Evaluation in Higher Education</em>. Advance online publication.", "https://doi.org/10.1080/02602938.2025.2471821", "May need library access",
         "Watched 16 undergraduates use ChatGPT feedback on writing tasks, then interviewed them. Most accepted suggestions without judging them. Proposes an AI feedback literacy (prompting, evaluative judgement, emotional reflexivity, ethical decision-making, metacognition) that reads as a list of what to teach students before they ask a bot for feedback.", "epistemic + knowledge construction"),
    ]),
    ("Lesson planning and teachers' own use", [
        ("National Foundation for Educational Research. (2024, December). <em>ChatGPT in lesson preparation: A Teacher Choices trial</em>. Education Endowment Foundation.", "https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/choices-in-edtech-using-generative-ai-chatgpt-for-ks3-science-lesson-preparation-2024-teacher-choices-trial", "Free",
         "A randomised trial with 259 science teachers in 68 English secondary schools. ChatGPT plus a short guide cut weekly planning time by 31 percent, about 25 minutes, and an expert panel judging resources blind found no drop in quality. The best current evidence for the time-saving claim. Pair it with Selwyn and colleagues below: the number, and what the number leaves out.", "data + algorithmic; political + ecological"),
        ("Selwyn, N., Ljungqvist, M., & Sonesson, A. (2025). When the prompting stops: Exploring teachers' work around the educational frailties of generative AI tools. <em>Learning, Media and Technology, 50</em>(3), 310–323.", "https://doi.org/10.1080/17439884.2025.2537959", "May need library access",
         "Interviews with 57 teachers across eight schools in Sweden and Australia. Teachers spend real time reviewing, repairing and reworking AI output. The paper reads this as hidden labour that props up the illusion of automation, not as a prompting problem. The clearest recent statement of the labour question.", "political + ecological; relational"),
        ("Common Sense Media. (2025, August). <em>AI risk assessment: AI teacher assistants</em>.", "https://www.commonsensemedia.org/sites/default/files/featured-content/files/csm-ai-risk-assessment-ai-teacher-assistants-final.pdf", "Free",
         "Assessed Gemini in Google Classroom, Khanmigo Teacher Assistant, Curipod and MagicSchool, with an overall rating of moderate risk. Two findings matter for teachers: the tools quietly shape what gets taught, and their IEP and behaviour-plan generators are not fit for high-stakes use and show bias tied to perceived student background.", "data + algorithmic"),
    ]),
    ("Guiding students' use", [
        ("Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. <em>Proceedings of the National Academy of Sciences, 122</em>(26), e2422633122.", "https://doi.org/10.1073/pnas.2422633122", "Open access",
         "A randomised trial with nearly 1,000 high school students in Turkey. Unrestricted GPT-4 access improved practice performance, but students then did about 17 percent worse on the unassisted exam than peers with no AI. A version with tutor-style guardrails (hints, no direct answers) removed the harm but produced no gain. The most useful single study for the “how should students use it” conversation.", "epistemic + knowledge construction"),
        ("Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. <em>Scientific Reports, 15</em>.", "https://doi.org/10.1038/s41598-025-97652-6", "Open access",
         "Introductory university physics. An AI tutor built on explicit teaching principles (answers held back, load managed, scripted scaffolding) produced larger gains than active-learning classes covering the same content, in less time. Read alongside Bastani: what matters is the design of the constraint, not AI yes or no. One course, one discipline, university students.", "data + algorithmic"),
        ("Fan, Y., Tang, L., Le, H., Shen, K., Tan, S., Zhao, Y., Shen, Y., Li, X., & Gašević, D. (2025). Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance. <em>British Journal of Educational Technology, 56</em>(2), 489–530.", "https://doi.org/10.1111/bjet.13544", "Open access",
         "Compared ChatGPT, a human expert, a checklist and no support on an essay task. ChatGPT raised essay scores but not knowledge gain or transfer, and learners handed off the work of managing their own learning. Gives teachers a vocabulary for what students can lose, without the neuro-hype of some recent preprints.", "epistemic + knowledge construction"),
    ]),
    ("Not using AI: refusal and critique", [
        ("Sano-Franchini, J., McIntyre, M., & Fernandes, M. (2024, November). <em>Refusing GenAI in writing studies: A quickstart guide</em>.", "https://refusal.blog/", "Free",
         "Short, practical and principled. Frames refusal as an informed teaching position rather than technophobia, with reasons (labour, environment, bias, surveillance, the economics of the tools) and concrete classroom moves. Written for university writing teachers and transferable to secondary English and humanities.", "political + ecological; relational"),
        ("Warner, J. (2025). <em>More than words: How to think about writing in the age of AI</em>. Basic Books.", "https://teachinginhighered.com/podcast/564-how-to-think-about-writing-in-the-age-of-ai/", "Book; link is a podcast interview",
         "The strongest long-form argument that writing is thinking and feeling, and that automating it hollows out the practice it claims to assist. The later chapters are practical: process, reflection, unassisted writing, what to stop assigning. Pairs with <a href=\"cards.html#card-4\">scenario card 4</a>, the un-AI-able task.", "relational + creative"),
        ("Costa, C., & Murphy, M. (2025). Generative artificial intelligence in education: (What) are we thinking? <em>Learning, Media and Technology</em>. Advance online publication.", "https://doi.org/10.1080/17439884.2025.2518258", "Open access",
         "Uses Arendt on thoughtlessness and Freire on critical pedagogy to argue that GenAI puts intellectual development at risk unless education makes thinking itself a form of accountability. Theoretical but short and usable.", "epistemic + knowledge construction; political"),
        ("Worrell, T., & Roberts, Z. (2026). Bringing Uncle Chatty Gee (ChatGPT) into the classroom: A lens from Critical Indigenous Studies. <em>Curriculum Perspectives</em>.", "https://doi.org/10.1007/s41297-026-00321-5", "Open access",
         "Two Indigenous academics in Australia, three classroom cases. Argues AI is not neutral, that it threatens Indigenous cultural and intellectual property through misappropriation and homogenisation, and models critiquing outputs and relational learning over convenience. Tertiary and Australian, so not a template for Canadian schools, but the clearest recent statement of the knowledge-sovereignty problem from Indigenous educators.", "political + ecological; disciplinary + futures"),
    ]),
]
BENCH = [
    ("Knox, J. (2025). Critiquing AI in education. <em>Postdigital Science and Education</em>.", "https://doi.org/10.1007/s42438-025-00606-4", "Why critique should aim at education's own infrastructures and not only at the technology."),
    ("UNESCO. (2025). <em>AI and the future of education: Disruptions, dilemmas and directions</em>.", "https://www.unesco.org/en/articles/ai-and-future-education-disruptions-dilemmas-and-directions-0", "A policy collection from Digital Learning Week 2025, useful for its framing of dilemmas."),
    ("OECD. (2026). <em>OECD Digital Education Outlook 2026: Exploring effective uses of generative AI in education</em>.", "https://doi.org/10.1787/062a7394-en", "The most current policy view of effective uses."),
    ("Doss, C. J., Bozick, R., Schwartz, H. L., Chu, L., Rainey, L. R., Woo, A., Reich, J., & Dukes, J. (2025). <em>AI use in schools is quickly increasing but guidance lags behind</em>. RAND.", "https://www.rand.org/pubs/research_reports/RRA4180-1.html", "US figures: about half of students and teachers used AI for school in 2025, and over 80 percent of students had no explicit instruction on it."),
    ("Williamson, B., Molnar, A., & Boninger, F. (2024). <em>Time for a pause: Without effective public oversight, AI in schools will do more harm than good</em>. National Education Policy Center.", "https://nepc.colorado.edu/publication/ai", "The case for a pause, made at policy level."),
    ("BC Ministry of Education and Child Care. (n.d.). <em>Considerations for using AI tools in K-12 schools</em>.", "https://www2.gov.bc.ca/assets/gov/education/administration/kindergarten-to-grade-12/ai-in-education/considerations-for-using-ai-tools-in-k-12-schools.pdf", "The BC context. Short."),
]


def readings_html():
    parts = []
    n = 0
    for heading, items in READINGS:
        parts.append(f"<h2>{esc(heading)}</h2>")
        for ref, url, access, note, knot in items:
            n += 1
            parts.append(
                f'<article class="card" id="reading-{n}"><p class="num">{n}</p><p><strong>{ref}</strong></p>'
                f'<p>{note}</p><p><a href="{url}">{esc(url)}</a></p>'
                f'<p><span class="tag">{esc(access)}</span><span class="tag">{esc(knot)}</span></p></article>'
            )
    parts.append("<h2>Six more worth knowing</h2><ul>")
    for ref, url, note in BENCH:
        parts.append(f'<li>{ref} <a href="{url}">Link</a>. {esc(note)}</li>')
    parts.append("</ul>")
    return "\n".join(parts)


READINGS_PAGE = f"""
<div class="doc">
<p class="eyebrow">Reading list</p>
<h1>Readings</h1>
<p class="lede">Fifteen recent readings on AI in teaching, from 2024 to 2026: assessment and feedback, lesson planning, guiding students' use, and the case for not using it. A mix of studies, practitioner pieces and one book.</p>
<p>Each entry notes the pair of <a href="frameworks.html">Entangled Dimensions</a> it touches most. Open access is noted where it could be confirmed.</p>
{readings_html()}
<p class="meta">Compiled September 2026. Each reference was checked against the publisher or repository page.</p>
</div>
"""

# ---------------------------------------------------------------- Policy examples
SECONDARY = [
    ("Seaquam Secondary School (Delta SD37), Academic Honesty", "Delta, BC. Secondary, grades 8 to 12. November 2024. Governs students.", "https://se.deltasd.bc.ca/our-school/academic-honesty/",
     "A school academic-integrity page that adds copying from AI, or using AI content without sourcing it, to the list of plagiarism offences. Consequences include a mark of zero, a call home and referral to administration. No guidance on permitted use, no disclosure format, no tool list.",
     "The typical BC bolt-on: AI handled as a plagiarism category inside an existing honesty policy rather than as its own framework. A good contrast case."),
    ("School District No. 5 (Southeast Kootenay), Policy 24: Generative Artificial Intelligence", "Cranbrook and Fernie, BC. District K to 12. Adopted May 2024. Governs students, staff and others.", "https://media.sd5.bc.ca/media/Default/medialib/policy-24-generative-artificial-intelligence.b0134e9115.pdf",
     "A formal board-adopted governance policy covering how AI tools are acquired and used: transparency, human verification of every output, bias evaluation of tools, training before deployment, privacy compliance and non-discrimination. Principles rather than classroom rules; the operational detail sits in an administrative procedure.",
     "One of the few BC districts with an adopted board policy, not just guidelines. Shows the governance layer above classroom practice."),
    ("York Region District School Board, Student AI Guidelines (Grades 7 to 12)", "York Region, Ontario. Grades 7 to 12. January 2026. Governs students, with a companion page for educators.", "https://www2.yrdsb.ca/student-support/artificial-intelligence/student-ai-guidelines-grades-7-12",
     "Permissive but structured. Board-approved tools may be used for brainstorming, tutoring, study notes, proofreading and organising research, always with the teacher's permission for each assignment. Disclosure and citation in the bibliography are mandatory, and students stay responsible for everything they submit. The educator page adds that student work should not be entered into AI for assessment.",
     "Pairs a student page with an educator page so the obligations mirror each other."),
    ("Canadian Rockies Public Schools, Administrative Procedure 140", "Canmore and Banff, Alberta. K to 12 with grade 9 to 12 provisions. August 2026. Governs students and staff.", "https://www.crps.ca/download/344210",
     "Folds AI into the technology acceptable-use procedure. Students may use AI to generate ideas, practise skills or deepen understanding, and must disclose it and mark which parts were AI-assisted. Only district-approved tools with privacy agreements may be used. Staff are steered away from AI detectors toward conversations with students. Deepfakes of any person without permission are banned.",
     "An explicit anti-deepfake rule and an explicit stance against detection software, with the preferred alternative named."),
    ("Snohomish High School, AI Code of Conduct", "Snohomish, Washington. Grades 9 to 12. October 2024. Governs students.", "https://shs.sno.wednet.edu/student-life/ai-code-of-conduct",
     "Teachers label each assignment AI recommended, AI permitted or AI restricted. The default is no use without teacher approval; attribution is required, no personal information may be entered, and misuse may be treated as cheating.",
     "The clearest school-level traffic-light scheme."),
    ("Park East High School (NYC), AI and Academic Integrity Policies", "New York. Grades 9 to 12. 2026–27 school year. Governs students.", "https://www.parkeasths.org/apps/pages/index.jsp?uREC_ID=4428131&type=d&pREC_ID=2698883",
     "Restrictive by default: every assignment is red (no AI) unless the teacher makes it yellow or green. Where AI is allowed, students disclose what it generated and how they used it. A consequence ladder runs from a call home to a redo under a strict timeframe, then a zero.",
     "The clearest red-by-default policy, with a fully specified discipline ladder. A useful contrast to permissive-by-default models."),
    ("Wyndham College (NSW), Generative AI in assessment", "Quakers Hill, New South Wales. Years 11 and 12. September 2024. Governs students, with teacher duties.", "https://assets.schools.nsw.gov.au/content/dam/doe/sws/schools/w/wyndhamcol-h/Docs/Policy_for_use_of_Generative_AI_in_Assesment_at_Wyndham_College.2024.pdf",
     "Every assessment notification declares one of four levels, from no AI to sanctioned tools generating content. Students keep evidence of their AI use and cite it; suspected malpractice goes through a review panel with a right of appeal. Tasks can never require AI, because that would conflict with equity.",
     "Combines a scale with an equity rule and a due-process chain."),
    ("Harristown State High School, Artificial Intelligence policy", "Toowoomba, Queensland. Years 7 to 12. July 2025. Governs students, with teacher duties.", "https://harristownshs.eq.edu.au/SupportAndResources/FormsAndDocuments/Documents/3.curriculum/senior-secondary/HSHS-AI-policy-2025.pdf",
     "AI is allowed for brainstorming, research, clarifying concepts, flashcards and summaries, and banned for anything the marking guide assesses. Students keep and supply their prompt transcripts. Senior work suspected of prohibited use is not marked.",
     "Ties the line between allowed and prohibited to the marking guide itself, and uses prompt transcripts as evidence rather than detectors."),
    ("Tudor Grange Academies Trust, AI Policy", "West Midlands and Worcestershire, England. Primary and secondary. April 2026. Governs staff and pupils.", "https://www.tgacademy.org.uk/files/2026/04/AI-Policy-v1.0.pdf",
     "Staff-focused. Authorised tools only; AI may draft resources, mark objective items and help write reports, with human review and disclosure of where AI was used. A data protection assessment is required before AI note-takers, and emotion-recognition AI is banned. Pupils may use authorised, age-appropriate tools.",
     "Treats teacher and administrative AI use as the main governance risk."),
    ("Gwinnett County Public Schools, Guidance for Human-Centered AI Use", "Gwinnett County, Georgia. District K to 12. September 2025. Governs students, staff and parents.", "https://www.gcpsk12.org/programs-and-services/college-and-career-development/academies-and-career-technical-and-agricultural-education/artificial-intelligence-and-computer-science/guidance-for-human-centered-ai-use",
     "Principle-based guidance from a large, AI-forward district: humans in the loop for all uses, encouraged student uses, a definition of AI plagiarism, citation when allowed, and staff instructions never to enter personal information or rely on unreviewed output. Using AI to impersonate, bully or harass is banned.",
     "Treats AI-enabled bullying and impersonation as a conduct issue, not only an integrity issue."),
]
ELEMENTARY = [
    ("BC Ministry of Education and Child Care, What you need to know about AI (Elementary)", "British Columbia. Provincial, one of three versions. Written directly to children.", "https://www2.gov.bc.ca/assets/gov/education/administration/kindergarten-to-grade-12/ai-in-education/what-you-need-to-know-about-ai-elementary.pdf",
     "A one-page set of norms for children rather than a rule book: AI as a helper, not a replacement for your own thinking; add your own ideas; double-check everything; protect personal information; ask your teacher; tell a trusted adult if something feels wrong. A companion parent sheet comes in eight languages.",
     "The only provincial document in Canada written in age-differentiated language for elementary children. Several BC districts reproduce it."),
    ("Vancouver School Board, AI guidelines and Copilot 13+", "Vancouver, BC. K to 12; the age gate excludes elementary. May 2026.", "https://www.vsb.bc.ca/ai-guidelines-for-educators",
     "Copilot 13+ is available inside the district tenant only to secondary students aged 13 and older, so elementary use is teacher-mediated. Educator guidelines permit planning, feedback and differentiation, with review of AI output, disclosure to students and no identifiable student data. The student guidelines were developed with educators and secondary students.",
     "The most current BC example of a hard no-accounts-under-13 line. A parent-led campaign is contesting it, which makes it good discussion material."),
    ("Langley School District (SD35), AI Guidelines", "Langley, BC. K to 12; Copilot for staff, student access planned for grades 9 to 12. Spring 2025.", "https://www.sd35.bc.ca/instructionalservices/sd35-ai-guidelines",
     "Teacher-facing. Staff may use the district Copilot for planning, assignments, rubrics and family communications, and must tell students when and how AI is permitted. At the request of the district's Aboriginal Program, teachers are asked not to use AI to create Indigenous learning opportunities, which the guidelines name as cultural appropriation.",
     "The only policy found that explicitly prohibits using AI to generate Indigenous learning content."),
    ("Central Okanagan Public Schools (SD23), Guidelines for the Responsible Use of Generative AI", "Kelowna, BC. K to 12. April 2025. Governs educators, students and parents.", "https://lts.sd23.bc.ca/documents/a8e0b7b4-1b65-45da-8273-5852d036518d/1-Central-Okanagan-Public-Schools-Guidelines-for-Responsible-use-of-Gen-AI.pdf",
     "Puts the onus on teachers: check the approved tools list, respect vendor age minimums, judge developmental appropriateness for younger students, and send a parent consent form when data leaves Canada. Recommends against AI writing detectors.",
     "Frames age limits and parental consent as legal obligations under FIPPA, and rejects detectors outright."),
    ("Halton District School Board, Generative AI Staff and Student Use Guidelines", "Halton Region, Ontario. K to 12 with tiers. August 2025.", "https://www.myhdsb.ca/media/bhtc22om/generative-ai-staff-and-student-use-guidelines.pdf",
     "The clearest tiered model found: no student tools for K to 6, a short vetted list for grades 7 and 8 with signed parental consent and an alternate assignment for anyone without it, and a broader list for 9 to 12. Staff may use AI for planning and report-card drafting as a supplement to professional judgement, and must disclose AI-generated lesson content.",
     "An explicit K to 6 prohibition, per-class consent letters and mandatory alternate assignments."),
    ("Waterloo Region District School Board, GenAI Student Guidelines", "Waterloo Region, Ontario. Grades 7 to 12. May 2026.", "https://www.wrdsb.ca/learning/digital-citizenship/genai-student-guidelines/",
     "Two board-licensed tools for grades 7 and up, always optional and teacher-guided. Teachers can include, limit or leave out AI for each task using a four-level scale, with worked citation examples. Copying without citation is plagiarism.",
     "A grade 7 floor with teacher opt-out, and a ready-made student-facing scale."),
    ("Peel District School Board, Interim Guidance on Generative AI", "Peel Region, Ontario. K to 12 with an under-13 provision. May 2024, reaffirmed December 2025.", "https://www.peelschools.org/documents/47dd02f9-5574-4671-8c10-10d644747cf7/SAW1207B-Interim-Guidance-on-Generative-AI-in-PDSB.pdf",
     "Rather than banning, Peel allows students under 13 to use generative AI only with supervision, and all students only with educator approval. Staff review all AI output, attribute it, and keep personal data out.",
     "A supervised-not-prohibited stance for under-13s. A useful contrast to Halton."),
    ("Joy Lane Primary School, Acceptable Use of Generative AI", "Whitstable, Kent, England. Ages 4 to 11. March 2026.", "https://www.joylane.kent.sch.uk/attachments/download.asp?file=1187&type=pdf",
     "Pupils may use AI only when supervised by an adult, as a research tool, or when studying AI itself; never in assessments or for homework passed off as their own. Staff may use approved tools for planning, resources, marking support and parent letters, and must keep personal data out of prompts.",
     "A complete, current primary policy with a named list of approved tools."),
    ("Manly Village Public School (NSW), Generative AI Implementation Procedures", "Manly, New South Wales. K to 6; AI limited to Years 5 and 6. 2025.", "https://assets.schools.nsw.gov.au/content/dam/doe/sws/schools/m/manlyvill-p/Documents/Manly%20Village%20Generative%20AI%20Procedures%202025.pdf",
     "Prohibited by default, with one exception: Years 5 and 6 may use the state-built, filtered chatbot under teacher supervision. No AI for homework or assessment.",
     "A school layering stricter procedures on top of a state-provided tool."),
    ("Central Elementary School (CCSD 62), AI in Education", "Des Plaines, Illinois. K to 8 district. September 2025.", "https://central.d62.org/families-community/ai-in-education",
     "Permissive but teacher-controlled: two vetted tools approved for teacher-directed activities, contracts that restrict data collection from under-13s and bar vendors from training on student data, AI literacy lessons at every grade, and a signed student expectations document.",
     "A family-facing page that names the tools, the legal basis for under-13 protection and the permitted uses."),
]


def policies_html(items, prefix):
    out = []
    for i, (name, meta, url, summary, notable) in enumerate(items, 1):
        out.append(
            f'<article class="card" id="{prefix}-{i}"><h3>{esc(name)}</h3><p class="meta">{esc(meta)}</p>'
            f'<p>{esc(summary)}</p><p><strong>Notable:</strong> {esc(notable)}</p><p><a href="{url}">Read the policy</a></p></article>'
        )
    return "\n".join(out)


POLICIES_PAGE = f"""
<div class="doc">
<p class="eyebrow">Positions to argue with</p>
<h1>Policy examples</h1>
<p class="lede">Twenty published K to 12 AI policies, ten secondary and ten elementary, from BC, the rest of Canada, the US, the UK and Australia. They are here as positions to argue with, not templates to adopt.</p>
<div class="note">Read in September 2026. Policies in this area change quickly, so check the link before putting one in front of a room.</div>

<h2>Two ways to use them</h2>
<p><strong>Critique.</strong> Give small groups three contrasting documents, such as Seaquam's bolt-on, Park East's red-by-default and Waterloo's scale. Read each through the <a href="frameworks.html">dimensions</a>: what does it assume about data and where it goes, about authorship and relation, whose labour does it move, and what future does it take for granted? Then: which would you want to teach under, and what would you add?</p>
<p><strong>Build your own.</strong> Use the lists as positions to argue with while writing your own guidance. Langley's line on Indigenous content, Central Okanagan's framing of consent as a legal duty, Halton's tiers, Peel's supervised-not-prohibited stance and Wyndham's equity rule are good starting points. For a class version, see <a href="class-ai-agreement.html">the class AI agreement</a>.</p>

<h2>Secondary</h2>
{policies_html(SECONDARY, "secondary")}

<h2>Elementary</h2>
{policies_html(ELEMENTARY, "elementary")}

<h2>Patterns across the twenty</h2>
<ul>
<li><strong>Disclosure and citation</strong> is the near-universal student rule. Few say what a good disclosure looks like; Waterloo and York give worked examples.</li>
<li><strong>Teacher discretion, task by task,</strong> is the default mechanism. Scales make it visible: Waterloo's and Wyndham's four levels, Snohomish's and Park East's traffic lights. Park East is the only one that names the default.</li>
<li><strong>Age gates</strong> do most of the elementary work. Thirteen is the usual line, or a grade floor. Peel is the exception: supervised use rather than prohibition.</li>
<li><strong>No personal information</strong> goes into the tool, in almost every document, for students and staff alike.</li>
<li><strong>Teacher use</strong> is governed less often than student use. When it is, the rules are approved tools only, review every output, disclose AI-generated materials, and never enter student work for assessment.</li>
<li><strong>Consequences</strong> range from nothing stated to bolt-on plagiarism penalties, progressive ladders and due-process chains.</li>
<li><strong>Detectors:</strong> three documents reject them, and none endorse them.</li>
<li><strong>Equity</strong> appears once as a rule: Wyndham says AI can never be required for a task.</li>
<li><strong>Indigenous knowledge</strong> is named only by Langley. Nothing else in the twenty touches knowledge sovereignty.</li>
<li><strong>Labour, environment and cost</strong> are almost absent, and none ask what futures the policy assumes.</li>
</ul>
<p>Every policy here is about permission and detection. None is about what AI does to the conditions of meaning-making in a classroom. That gap is where an entangled policy starts.</p>
</div>
"""

# ---------------------------------------------------------------- Frameworks
FRAMEWORKS_PAGE = f"""
<div class="doc">
<p class="eyebrow">Behind the resources</p>
<h1>Frameworks</h1>
<p class="lede">The day draws on two open frameworks developed through work at UBC. Both are freely available.</p>

<h2>Entangled Dimensions of AI Literacy</h2>
<p>A way of looking beyond the immediate use of an AI system to the wider questions of knowledge, relationships, institutions, resources, values, and planetary systems. There are ten dimensions, and they work as threads, not a checklist. Each classroom situation card pulls on two or three.</p>
<p><span class="tag">data</span><span class="tag">algorithmic</span><span class="tag">knowledge-construction</span><span class="tag">disciplinary</span><span class="tag">epistemic</span><span class="tag">political</span><span class="tag">ecological</span><span class="tag">relational</span><span class="tag">creative</span><span class="tag">futures</span></p>
<p><a class="btn" href="{ED}">Open the interactive Entangled Dimensions</a></p>

<h2>Computational Sense-Making</h2>
<p>A way of looking more closely at what computational systems are doing, how they produce outputs, and how we make sense of them. The four Cs give the practical moves when a chatbot is brought into the conversation.</p>
<table>
<thead><tr><th>C</th><th>What it reads</th></tr></thead>
<tbody>
<tr><td><strong>Computation</strong></td><td>Meaning assembled by probability: prediction and repetition, the boundaries of the training data, centring the normal, what is inherited.</td></tr>
<tr><td><strong>Composition</strong></td><td>How outputs are built: one word after another, framing, layering, style.</td></tr>
<tr><td><strong>Constraints</strong></td><td>What can be said: filtering, smoothing, consensus, refusal.</td></tr>
<tr><td><strong>Calibration</strong></td><td>Confidence and trust: confidence signals, error, verification, knowing what you don't know.</td></tr>
</tbody>
</table>
<p><a class="btn" href="{CSM}">Open the Computational Sense-Making site</a></p>

<h2>Used together</h2>
<p>The dimensions give a discussion its questions. The four Cs give the moves to try. In the <a href="cards.html">classroom situation cards</a>, each card names its threads and pairs a question with a move.</p>

<h2>Related</h2>
<p><a href="{FUT}">AI Futures</a>: an interactive map of positions on AI's future, from automated utopia to defiant resistance, built from published quotations.</p>
</div>
"""

# ---------------------------------------------------------------- My AI Metaphor (9:00)
PADLET = "https://padlet.com/embed/s025k2ljostv9t2zbjfr"

METAPHOR_PAGE = f"""
<style>
.board{{border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);background:#f4f4f4;overflow:hidden;margin:20px 0 10px}}
.board iframe{{display:block;width:100%;height:640px;border:0}}
@media (max-width:700px){{.board iframe{{height:520px}}}}
.btn.primary{{background:var(--yellow)}}
</style>
<div class="doc wide">
<p class="eyebrow">9:00 · Welcome</p>
<h1>My AI Metaphor</h1>
<p class="lede">AI is like… because… Add your metaphor to the board and place it where it sits for you: personal or collective, opening possibilities or raising concerns.</p>
<div class="tools"><a class="btn primary" href="{PADLET}" target="_blank" rel="noopener">Open the board ↗</a><a class="btn" href="assets/my-ai-metaphor-paper.pdf">Paper version (PDF)</a></div>
<div class="board"><iframe src="{PADLET}" title="My AI Metaphor board" allow="camera;microphone;geolocation;display-capture;clipboard-write" loading="lazy"></iframe></div>
<p class="meta">On a phone, the board is easier to use in its own tab.</p>
<h2>On paper</h2>
<p>The paper version has the same board as a poster and a card for each table. Write your metaphor on a sticky note and place it on the poster. The table card also has a QR code to the online board.</p>
</div>
"""

# ---------------------------------------------------------------- Quick, Draw! (9:00)
QD = "https://quickdraw.withgoogle.com/"

QUICKDRAW_PAGE = f"""
<style>
.launch{{display:block;text-decoration:none;color:var(--ink);background:var(--yellow);border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);padding:34px 24px;margin:22px 0 10px;text-align:center;transition:transform .12s}}
.launch:hover{{transform:translate(-2px,-2px);box-shadow:7px 7px 0 var(--ink)}}
.launch .big{{display:block;font-family:var(--font-display);font-weight:900;text-transform:uppercase;font-size:clamp(26px,4vw,40px);line-height:1.05}}
.launch .small{{display:block;margin-top:10px;font-size:14.5px}}
.shot{{margin:28px auto 8px;max-width:560px}}
.shot img{{display:block;width:100%;height:auto;border:2px solid var(--ink);box-shadow:5px 5px 0 var(--ink)}}
.shot figcaption{{margin-top:12px;font-size:15px;color:var(--muted)}}
.facts li{{margin-bottom:10px}}
.sources{{font-size:14px;color:var(--muted)}}
.sources li{{margin-bottom:4px}}
</style>
<div class="doc">
<p class="eyebrow">9:00 · Welcome</p>
<h1>Quick, Draw!</h1>
<p class="lede">You get a word and 20 seconds to draw it. While you draw, a neural network guesses what it is.</p>
<a class="launch" href="{QD}" target="_blank" rel="noopener"><span class="big">Play Quick, Draw! ↗</span><span class="small">Opens in a new tab. Google doesn't let the game run inside other sites.</span></a>
<figure class="shot"><img src="assets/quickdraw-palms.webp" width="900" height="889" loading="lazy" alt="Quick, Draw! results screen. Asked to draw palms, the drawing of palm trees and two hands was not recognized. Its closest matches were glove, campfire and shrub. The examples it learned from are all palm trees."><figcaption>One round. Asked to draw “palms”, I drew palm trees and the palms of hands. The network didn’t recognize it, and its closest matches were glove, campfire and shrub. Every example it learned from was a palm tree.</figcaption></figure>

<h2>Why we play it</h2>
<p>It is a quick way to watch machine learning work, with no account needed. It also shows what that learning takes: millions of people drawing for free, and a system that learns the most common way to draw a thing.</p>

<h2>How it learns</h2>
<p>The game does not see your drawing the way a person would. It compares your strokes with the patterns in drawings other players made for the same word. Google Creative Lab launched it in 2016, and it has collected over a billion drawings across 345 words. Each one was saved with the word, the order of the strokes, whether the game guessed it, and the player’s country.</p>

<h2>What gets lost or left out</h2>
<ul class="facts">
<li><strong>The usual way wins.</strong> When Google looked at more than 115,000 shoe drawings, one style that looks like a sneaker dominated. The game struggled to recognize high heels or sandals as shoes.</li>
<li><strong>Culture is in the strokes.</strong> In the data, 86% of circles drawn in the US went counterclockwise, while 80% of circles drawn in Japan went clockwise. Players in Korea and Russia were more likely to draw a chair sideways.</li>
<li><strong>Someone chose the words.</strong> The game asks for 345 things that can be drawn in 20 seconds. Whatever is not on the list, or is drawn differently here, is not what the system learns.</li>
<li><strong>Odd drawings get corrected.</strong> A drawing network trained on these doodles, given a cat with three eyes, draws it back with two.</li>
</ul>

<h2>What Google did with the drawings</h2>
<p>In 2017 Google released 50 million of them as an open dataset, with each player’s country and the time of each drawing. Its researchers trained Sketch-RNN, a network that draws and can finish your doodles, on millions of them. Google also used the dataset to study how representative large datasets are, which is where the shoe finding comes from.</p>

<h2>Games that train machines</h2>
<p>Getting people to play so a system can learn is an old move. In 2004 the ESP Game paired strangers to type words for the same image, and Google licensed it as the Google Image Labeler to improve image search. reCAPTCHA, which Google bought in 2009, had people type words from scanned books and newspapers to prove they were human, which helped digitize Google Books. From 2012 it showed house numbers from Street View, and later it asked people to click on crosswalks and traffic lights.</p>

<h2>To talk about</h2>
<ul>
<li>Who did the work in this game, and who benefits from it?</li>
<li>What did the game reward you for drawing?</li>
<li>What would it fail to recognize from here?</li>
</ul>

<h2>Sources</h2>
<ul class="sources">
<li><a href="https://opensource.googleblog.com/2018/11/introducing-web-component-and-data-api-for-quick-draw.html">Google Open Source Blog (2018), Quick, Draw! web component and data API</a></li>
<li><a href="https://research.google/blog/exploring-and-visualizing-an-open-global-dataset/">Google Research (2017), Exploring and visualizing an open global dataset</a></li>
<li><a href="https://github.com/googlecreativelab/quickdraw-dataset">The Quick, Draw! dataset on GitHub</a></li>
<li><a href="https://qz.com/994486/the-way-you-draw-circles-says-a-lot-about-you/">Quartz (2017), How do you draw a circle?</a></li>
<li><a href="https://techcrunch.com/2017/08/25/google-releases-millions-of-bad-drawings-for-you-and-your-ai-to-paw-through">TechCrunch (2017), Google releases millions of bad drawings</a></li>
<li><a href="https://magenta.tensorflow.org/sketch-rnn-demo">Magenta, Sketch-RNN demo</a> and <a href="https://thenextweb.com/news/google-used-your-pictionary-sketches-to-teach-its-ai-to-draw">The Next Web (2017)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human-based_computation_game">Games with a purpose and the ESP Game</a> (von Ahn and Dabbish, 2004, 2008)</li>
<li><a href="https://en.wikipedia.org/wiki/ReCAPTCHA">reCAPTCHA</a></li>
</ul>
</div>
"""

# ---------------------------------------------------------------- Talk slides (9:15)
# Paste the slides' embed link (the src of the iframe your slide tool gives you) into
# SLIDES_EMBED. SLIDES_FILE is optional: a link to a PDF copy for offline or printing.
SLIDES_EMBED = ""
SLIDES_FILE = ""

if SLIDES_EMBED:
    _slides = f'<div class="slides"><iframe src="{html.escape(SLIDES_EMBED)}" title="Talk slides" allowfullscreen loading="lazy"></iframe></div>'
else:
    _slides = '<div class="slides empty"><p>The slides will be added here before the day.</p></div>'
_slides_file = f'<div class="tools"><a class="btn" href="{html.escape(SLIDES_FILE)}">Download the slides</a></div>' if SLIDES_FILE else ""

TALK_PAGE = f"""
<style>
.slides{{position:relative;aspect-ratio:16/9;width:100%;border:2px solid var(--ink);border-radius:4px;box-shadow:5px 5px 0 var(--ink);background:var(--surface);margin:22px 0 10px}}
.slides iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
.slides.empty{{display:grid;place-items:center;text-align:center;padding:20px}}
.slides.empty p{{font-family:var(--font-mono);font-size:14px;letter-spacing:.06em;color:var(--muted);margin:0}}
</style>
<div class="doc wide">
<p class="eyebrow">9:15 · Talk slides</p>
<h1>What are these strange systems, anyway?</h1>
<p class="lede">A plain-language introduction to how generative AI systems compose outputs, and the minimum technical background we need to make informed decisions about them. Then we experiment and see what happens.</p>
{_slides}
{_slides_file}
<p class="res"><a href="map.html">AI map</a><a href="scenarios.html">Next: Classroom situations</a></p>
</div>
"""

PAGES = [
    {"file": "index.html", "nav": "home", "title": "Teaching with, about, and without AI", "desc": "A professional learning day for K-12 educators, with Dr. Rachel Horst: the day, an AI map, classroom situations, activities, handouts, readings and policy examples.", "html": HOME},
    {"file": "cards.html", "nav": "scenarios", "title": "More scenario cards · Teaching with, about, and without AI", "desc": "Ten more classroom scenarios about AI for small-group discussion.", "html": CARDS_PAGE},
    {"file": "metaphor.html", "nav": "home", "title": "My AI Metaphor · Teaching with, about, and without AI", "desc": "Opening activity: add a metaphor for AI to the shared board.", "html": METAPHOR_PAGE},
    {"file": "quickdraw.html", "nav": "home", "title": "Quick, Draw! · Teaching with, about, and without AI", "desc": "A sketch game with a neural network, and what it shows about how machine learning learns.", "html": QUICKDRAW_PAGE},
    {"file": "talk.html", "nav": "home", "title": "Talk slides · Teaching with, about, and without AI", "desc": "Slides for the opening talk: what are these strange systems, anyway?", "html": TALK_PAGE},
    {"file": "activities.html", "nav": "activities", "title": "Activities · Teaching with, about, and without AI", "desc": "Twenty short activities about AI and with AI, for students and educators.", "html": ACTIVITIES_PAGE},
    {"file": "handouts.html", "nav": "handouts", "title": "Handouts · Teaching with, about, and without AI", "html": HANDOUTS_INDEX},
    {"file": "what-these-systems-are.html", "nav": "handouts", "title": "What these systems are · Teaching with, about, and without AI", "md": '<div class="doc" markdown="1">\n' + SYSTEMS_MD + "\n</div>"},
    {"file": "practical-moves.html", "nav": "handouts", "title": "Practical moves · Teaching with, about, and without AI", "md": '<div class="doc" markdown="1">\n' + MOVES_MD + "\n</div>"},
    {"file": "class-ai-agreement.html", "nav": "handouts", "title": "The class AI agreement · Teaching with, about, and without AI", "md": '<div class="doc" markdown="1">\n' + AGREEMENT_MD + "\n</div>"},
    {"file": "copilot-and-prompting.html", "nav": "handouts", "title": "Copilot and prompting · Teaching with, about, and without AI", "md": '<div class="doc" markdown="1">\n' + COPILOT_MD + "\n</div>"},
    {"file": "readings.html", "nav": "readings", "title": "Readings · Teaching with, about, and without AI", "html": READINGS_PAGE},
    {"file": "policies.html", "nav": "policies", "title": "Policy examples · Teaching with, about, and without AI", "html": POLICIES_PAGE},
    {"file": "frameworks.html", "nav": "frameworks", "title": "Frameworks · Teaching with, about, and without AI", "html": FRAMEWORKS_PAGE},
]
