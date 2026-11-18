"""Classroom cases: reads cases.md and builds scenarios.html, one page per case, and responses.html.

To change a case, edit cases.md and rebuild. Two links to set before the day:
"""
import re
import html
from pathlib import Path

# The Copilot your school has approved. Opens in a new tab from every case page.
COPILOT_URL = "https://copilot.cloud.microsoft/"
# The shared response board (for example a Microsoft Form with no name fields).
# Leave empty to show a placeholder on responses.html.
BOARD_URL = ""

SITE_URL = "https://rshorst.github.io/ai-literacy-pd/"
HERE = Path(__file__).resolve().parent
MD = (HERE / "cases.md").read_text(encoding="utf-8")


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- Parse cases.md
def _between(text, start, end=None):
    i = text.index(start) + len(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


INTRO = _between(MD, "## What would you do here?", "###").strip()
_lens_block = _between(MD, "### Learning · Knowing · Creating · Relating", "## Whole-room")
LENSES = re.findall(r"^- \*\*(\w+):\*\* (.+)$", _lens_block, re.M)
ACROSS = re.search(r"\*\*Across all four:\*\* (.+)$", _lens_block, re.M).group(1)

CASES = []
for block in re.split(r"^### ", MD, flags=re.M):
    head, _, body = block.partition("\n")
    m = re.match(r"(?:Sample|Case (\d\d)): (.+)$", head.strip())
    if not m:
        continue
    num = m.group(1)
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    CASES.append({
        "num": num,
        "id": num or "sample",
        "file": f"scenario-{num}.html" if num else "scenario-sample.html",
        "label": f"Case {num}" if num else "Whole-room sample",
        "title": m.group(2).strip(),
        "theme": re.search(r"^\*([^*].+)\*$", body, re.M).group(1),
        "text": next(p for p in paras if not p.startswith(("*", "[", "#"))),
        "questions": re.search(r"^\*\*Questions:\*\* (.+)$", body, re.M).group(1),
        "source": re.search(r"^\*\*Source context:\*\* (.+)$", body, re.M).group(1),
        "link": re.search(r"^\[Read the source\]\((.+?)\)", body, re.M).group(1),
    })

_exp = _between(MD, "## Copilot experiment", "## Group response")
COPILOT_INTRO = _exp.strip().split("\n")[0]
PROMPTS = re.findall(r"^### \d\. (.+?)\n\n```text\n(.+?)\n```", _exp, re.M | re.S)
FIELDS = [f.rstrip(":").strip() for f in re.findall(r"^- (.+)$", _between(MD, "## Group response"), re.M)]
FIELD_KEYS = ["first", "response"]
assert len(CASES) == 11 and len(LENSES) == 4 and len(PROMPTS) == 1 and len(FIELDS) == 2, (len(CASES), len(LENSES), len(PROMPTS), len(FIELDS))

LENS_TAPE = ["pink", "teal", "yellow", "blue"]

# ---------------------------------------------------------------- Shared CSS and script
CSS = """<style>
.situation{background:var(--surface);border:2px solid var(--ink);box-shadow:5px 5px 0 var(--pink);padding:16px 20px;margin:18px 0 8px;font-size:18px;line-height:1.6;max-width:68ch}
.situation p{margin:0}
.sit-with{font-size:17.5px}
.lens-list{list-style:none;padding:0!important;margin:14px 0}
.lens-list li{margin:0 0 10px}
.lens-list .tape,.lenses .tape{font-family:var(--font-display);font-weight:900;text-transform:uppercase;font-size:15px;letter-spacing:.01em;margin-right:6px}
.lenses details{background:var(--surface);border:1.5px solid var(--ink);border-radius:4px;margin:8px 0;padding:0 14px;max-width:68ch}
.lenses summary{cursor:pointer;padding:10px 0;font-size:16px}
.lenses details p{margin:0 0 12px}
.step{font-family:var(--font-mono);font-weight:500;font-size:14px;letter-spacing:.08em;background:var(--ink);color:var(--surface);padding:1px 8px;margin-right:8px;vertical-align:3px}
.prompt{background:var(--surface);border:1.5px solid var(--ink);border-radius:4px;padding:14px 16px 10px;margin:14px 0;max-width:72ch}
.prompt h3{margin:0 0 8px}
.prompt pre{white-space:pre-wrap;font-family:var(--font-mono);font-size:13.5px;line-height:1.55;background:var(--bg);border:1px dashed var(--muted);padding:10px 12px;margin:0}
.prompt .tools{margin:10px 0 0}
.field{display:block;margin:14px 0;max-width:68ch}
.field span{display:block;font-weight:700;margin-bottom:4px}
.field input,.field textarea{width:100%;font:inherit;font-size:16px;padding:8px 10px;border:1.5px solid var(--ink);border-radius:4px;background:#fff;color:var(--ink)}
.field textarea{min-height:88px;resize:vertical}
.field input.short{max-width:7em}
.status{font-size:14px;color:var(--muted);min-height:1.4em;margin:6px 0 0}
.manual{display:block;width:100%;max-width:68ch;min-height:120px;font-family:var(--font-mono);font-size:13px;margin:8px 0 0;padding:8px;border:1.5px solid var(--ink);border-radius:4px}
.btn.primary{background:var(--yellow)}
.pager{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:44px;border-top:2px solid var(--ink);padding-top:14px;max-width:none}
.pager a{text-decoration:none;font-weight:700;color:var(--ink);max-width:46%}
.pager a:last-child{text-align:right;margin-left:auto}
.pager small{display:block;font-family:var(--font-mono);font-weight:500;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.tile .num{font-family:var(--font-mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 4px}
.tile.sample{max-width:360px}
@media print{
  .case .respond,.case .try,.pager,.status,.manual{display:none!important}
  .situation{box-shadow:none;border:1px solid #888}
  .lenses details{border:none;padding:0}
}
</style>"""

JS = """<script>
(function(){
  var root=document.querySelector('.case'); if(!root) return;
  var key='aipd-case-'+root.getAttribute('data-case');
  var fields=[].slice.call(root.querySelectorAll('[data-field]'));
  var caseText=document.getElementById('case-text').textContent.trim();
  var store=null; try{store=window.localStorage;store.getItem(key);}catch(e){store=null;}
  try{var saved=store?JSON.parse(store.getItem(key)||'{}'):{};fields.forEach(function(f){if(saved[f.name])f.value=saved[f.name];});}catch(e){}
  function save(){if(!store)return;var d={},any=false;fields.forEach(function(f){if(f.value.trim()){d[f.name]=f.value;any=true;}});try{any?store.setItem(key,JSON.stringify(d)):store.removeItem(key);}catch(e){}}
  fields.forEach(function(f){f.addEventListener('input',save);});
  function val(name){var f=root.querySelector('[name="'+name+'"]');return f?f.value.trim():'';}
  function legacyCopy(text){var t=document.createElement('textarea');t.value=text;t.setAttribute('readonly','');t.style.position='fixed';t.style.top='-1000px';document.body.appendChild(t);t.select();var ok=false;try{ok=document.execCommand('copy');}catch(e){}document.body.removeChild(t);return ok;}
  function copy(text,btn,note){
    var box=btn.closest('[data-copybox]'),status=box.querySelector('.status'),manual=box.querySelector('.manual');
    if(manual)manual.remove();
    function done(ok){
      if(ok){var old=btn.textContent;btn.textContent='Copied';setTimeout(function(){btn.textContent=old;},1600);status.textContent=note||'Copied. Paste it into Copilot.';}
      else{var m=document.createElement('textarea');m.className='manual';m.readOnly=true;m.value=text;box.appendChild(m);m.focus();m.select();status.textContent='Copying is blocked here. Select this text and copy it.';}
    }
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(function(){done(true);},function(){done(legacyCopy(text));});}
    else done(legacyCopy(text));
  }
  root.addEventListener('click',function(e){
    var btn=e.target.closest('button[data-copy]'); if(!btn) return;
    var kind=btn.getAttribute('data-copy');
    if(kind==='response'){
      var lines=[root.getAttribute('data-label')+': '+root.getAttribute('data-title')];
      fields.forEach(function(f){lines.push(f.getAttribute('data-label')+': '+(f.value.trim()||''));});
      copy(lines.join('\\n'),btn,'Copied. Paste it into the shared board.');
      return;
    }
    var prompt=btn.closest('.prompt').querySelector('pre').textContent;
    if(kind==='prompt'){copy(prompt,btn);return;}
    var first=val('first'),text=prompt.replace('[PASTE CASE]',caseText);
    if(first)text=text.replace('[OUR THINKING]',first);
    var note='Copied with the case filled in.';
    if(prompt.indexOf('[OUR THINKING]')>-1)note=first?'Copied with the case and your first response filled in.':'Copied with the case filled in. Replace [OUR THINKING] in Copilot, or write your first response above first.';
    copy(text,btn,note);
  });
  var clear=root.querySelector('[data-clear]');
  if(clear)clear.addEventListener('click',function(){fields.forEach(function(f){f.value='';});save();clear.closest('[data-copybox]').querySelector('.status').textContent='Cleared.';});
  window.addEventListener('beforeprint',function(){[].forEach.call(document.querySelectorAll('details'),function(d){d.open=true;});});
})();
</script>"""


# ---------------------------------------------------------------- Pages
def lens_list():
    items = "".join(
        f'<li><span class="tape {LENS_TAPE[i]}">{esc(name)}</span> {esc(q)}</li>' for i, (name, q) in enumerate(LENSES)
    )
    return f'<ul class="lens-list">{items}</ul><p><strong>Across all four:</strong> {esc(ACROSS)}</p>'


def field(i, short=False):
    key, label = FIELD_KEYS[i], FIELDS[i]
    if short:
        return (f'<label class="field"><span>{esc(label)}</span>'
                f'<input class="short" name="{key}" data-field data-label="{attr(label)}" inputmode="numeric" autocomplete="off"></label>')
    return (f'<label class="field"><span>{esc(label)}</span>'
            f'<textarea name="{key}" data-field data-label="{attr(label)}" rows="3"></textarea></label>')


def case_page(i):
    c = CASES[i]
    prev_c = CASES[i - 1] if i > 0 else None
    next_c = CASES[i + 1] if i < len(CASES) - 1 else None
    name, text = PROMPTS[0]
    prompts = (f'<div class="prompt" data-copybox><pre>{esc(text)}</pre>'
               f'<div class="tools"><button class="btn primary" type="button" data-copy="case">Copy case + prompt</button>'
               f'<a class="btn" href="{COPILOT_URL}" target="_blank" rel="noopener">Open Copilot ↗</a></div>'
               f'<p class="status" aria-live="polite"></p></div>')
    lenses = "".join(
        f'<details><summary><span class="tape {LENS_TAPE[k]}">{esc(name)}</span></summary><p>{esc(q)}</p></details>'
        for k, (name, q) in enumerate(LENSES)
    )
    pager = '<nav class="pager" aria-label="Cases">'
    pager += (f'<a href="{prev_c["file"]}"><small>← {esc(prev_c["label"])}</small>{esc(prev_c["title"])}</a>'
              if prev_c else '<a href="scenarios.html"><small>← All cases</small>Classroom situations</a>')
    pager += (f'<a href="{next_c["file"]}"><small>{esc(next_c["label"])} →</small>{esc(next_c["title"])}</a>'
              if next_c else '<a href="responses.html"><small>Shared board →</small>See every group’s response</a>')
    pager += "</nav>"
    body = f"""{CSS}
<div class="doc case" data-case="{c['id']}" data-label="{attr(c['label'])}" data-title="{attr(c['title'])}">
<p class="eyebrow"><a href="scenarios.html">Classroom situations</a> · {esc(c['label'])} · {esc(c['theme'])}</p>
<h1>{esc(c['title'])}</h1>
<p class="meta">A fictional classroom adaptation grounded in published research or reporting.</p>
<div class="situation" id="case-text"><p>{esc(c['text'])}</p></div>
<h2>The question to sit with</h2>
<p class="sit-with">{esc(c['questions'])}</p>
<h2>The source</h2>
<p>{esc(c['source'])}</p>
<p><a href="{attr(c['link'])}">Read the source</a></p>
<h2>Four lenses</h2>
<div class="lenses">{lenses}</div>
<p><strong>Across all four:</strong> {esc(ACROSS)}</p>

<section class="respond">
<h2><span class="step">1</span>First response</h2>
<p>Talk it through as a group before you try Copilot.</p>
{field(0)}
</section>

<section class="try">
<h2><span class="step">2</span>Try Copilot</h2>
<p>{esc(COPILOT_INTRO)} The copy button puts the case and your first response into the prompt. You don’t need Copilot to work through the case.</p>
{prompts}
</section>

<section class="respond" data-copybox>
<h2><span class="step">3</span>Our response</h2>
<p>What do you think now?</p>
{field(1)}
<div class="tools"><button class="btn primary" type="button" data-copy="response">Copy our response</button><a class="btn" href="responses.html">Shared board</a><button class="btn" type="button" data-clear>Clear</button></div>
<p class="status" aria-live="polite"></p>
<p class="meta">Nothing here is sent anywhere. What you type stays in this browser until you clear it. No names or student information.</p>
</section>
{pager}
</div>
{JS}"""
    return {
        "file": c["file"], "nav": "scenarios",
        "title": f"{c['label']}: {c['title']} · Teaching with, about, and without AI",
        "desc": f"{c['label']}: {c['title']} A classroom case about AI for group discussion.",
        "html": body,
    }


def index_page():
    def tile(c):
        cls = "tile sample" if not c["num"] else "tile"
        return f'<a class="{cls}" href="{c["file"]}"><p class="num">{esc(c["label"])}</p><h3>{esc(c["title"])}</h3><p>{esc(c["theme"])}</p></a>'
    intro = esc(INTRO).replace("**fictional classroom adaptations grounded in published research or reporting**",
                               "<strong>fictional classroom adaptations grounded in published research or reporting</strong>")
    body = f"""{CSS}
<div class="doc wide">
<p class="eyebrow">Classroom situations</p>
<h1>What would you do here?</h1>
<p class="lede">{intro}</p>
<h2>Learning · Knowing · Creating · Relating</h2>
{lens_list()}
<h2>Whole-room sample case</h2>
<div class="grid">{tile(CASES[0])}</div>
<h2>Ten group cases</h2>
<div class="grid">{''.join(tile(c) for c in CASES[1:])}</div>
<h2>How each case works</h2>
<ol>
<li>Read the situation and the question to sit with. Talk first, and note your first response.</li>
<li>If you like, try the Copilot prompt. The copy button puts the case and your first response into it.</li>
<li>Write your group’s response and add it to the <a href="responses.html">shared board</a>.</li>
</ol>
<p>You don’t need a Copilot account to read the cases. Each case page prints on its own.</p>
<p class="meta">More to discuss: <a href="cards.html">ten more scenario cards</a>, each with a move to try in any chatbot.</p>
</div>"""
    return {"file": "scenarios.html", "nav": "scenarios",
            "title": "Classroom situations · Teaching with, about, and without AI",
            "desc": "Ten fictional classroom cases about AI, grounded in research and reporting, with Copilot prompts and a group response.",
            "html": body}


def responses_page():
    board = (f'<div class="tools"><a class="btn primary" href="{attr(BOARD_URL)}" target="_blank" rel="noopener">Open the shared board ↗</a></div>'
             if BOARD_URL else '<div class="note"><p>The link to the board will be added here before the day.</p></div>')
    body = f"""<div class="doc">
<p class="eyebrow">Classroom situations</p>
<h1>Shared board</h1>
<p class="lede">Where groups see each other’s thinking.</p>
{board}
<h2>Adding your group’s response</h2>
<ol>
<li>On your case page, fill in <strong>Our response</strong> and press <strong>Copy our response</strong>.</li>
<li>Open the board and paste it in.</li>
</ol>
<p>The board collects no names and no student information. Only post the fictional case text and your group’s own ideas.</p>
<p><a href="scenarios.html">Back to the cases</a></p>
</div>"""
    return {"file": "responses.html", "nav": "scenarios",
            "title": "Shared board · Teaching with, about, and without AI",
            "desc": "Where groups share their responses to the classroom cases.", "html": body}


SCENARIO_PAGES = [index_page()] + [case_page(i) for i in range(len(CASES))] + [responses_page()]
