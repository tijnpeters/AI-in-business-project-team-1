# AI-in-business-project-team-1

HAN Minor DDDM – *AI in Business*, team 1. A demo platform that helps student researchers turn a research
question into a reviewed, plain-language handbook page for Dutch technical SMEs (case company: Waterkracht B.V.).

Pipeline: research question → source search → AAOCC source evaluation → draft page → quality check →
**human review** → publication on the handbook website.

> Everything the scripts produce is a **DRAFT**. Nothing is published until a researcher approves it.

---

## Getting started (about 15 minutes)

### 1. What you need
- **Python 3.10 or newer** – check with `py --version`.
- **A Claude subscription** (Pro or Max) for `handbook_demo.py`
  *or* a ChatGPT Plus/Pro/Business account for `handbook_demo_codex.py`.
- This repo on your computer (green **Code** button → *Download ZIP*, or `git clone`).

### 2. Install the Python packages
Open a terminal in the repo folder and run:

```
py -m pip install claude-agent-sdk python-docx pypdf youtube-transcript-api
```

| Package | Needed for | Without it |
|---|---|---|
| `claude-agent-sdk` | Running the pipeline at all | Script won't start |
| `python-docx` | Word export, **and reading `Handbook_criteria.docx`** | No .docx output; team weights/gates are ignored and the built-in defaults are used |
| `pypdf` | PDF sources (`--file`, `--add-doc`) | PDFs can't be evaluated |
| `youtube-transcript-api` | YouTube sources | YouTube links can't be evaluated |

(`requirements.txt` is only for building the website – see `SETUP.md`.)

### 3. Install Claude Code and log in once
Follow the official guide: <https://code.claude.com/docs/en/setup>. Log in with your **Claude subscription**.

⚠️ **Do not set `ANTHROPIC_API_KEY`.** If it is set, you pay per token instead of using your subscription.

If the script says it can't find Claude Code, open `handbook_demo.py` and set `CLI_PATH` near the top
to your install path, e.g. `r"C:\Users\<you>\.local\bin\claude.exe"`.

*Using ChatGPT instead?* Install Node.js (LTS), run `npm install -g @openai/codex`, run `codex` once to sign in,
then use `handbook_demo_codex.py` with the same commands below.

### 4. Check these files are next to the script
- `Handbook_criteria.docx` – the team's AAOCC weights and quality-gate rules (in the repo).
- `handbook_template.docx` – the Word layout for exported pages. *Optional:* without it, exports use plain Word styling.

### 5. Set your wiki password
The first time you use `--add-doc`, `--remove-source` or `--remove-page`, the script creates
`wiki_password.txt` with the password `changeme`. Open it and set your own. This file is never uploaded to GitHub.

### 6. First run
```
py handbook_demo.py "How should Dutch technical SMEs assess AI suppliers?"
```
You get progress per stage, a timestamped `.html` result, a `.docx` draft, and a new page in `wiki/` with its
sources in `raw/`.

---

## Commands

| Command | What it does |
|---|---|
| `py handbook_demo.py "question"` | Full run: search, evaluate, draft, quality check, save to wiki |
| `... --file "path-or-URL"` | Also evaluate one source you supply (.pdf, .docx, .txt, .md, .html, web link, YouTube link) |
| `... --skip-gate` | Skip the go/no-go pause before drafting |
| `py handbook_demo.py --lookup "question"` | Answer using only what's already in your wiki (no new search) |
| `py handbook_demo.py --ask` | Interactive Q&A on your wiki |
| `py handbook_demo.py --health-check` | Check that the stored data is consistent (changes nothing) |
| `... --confidential` (with `--file` or `--add-doc`) | Source is sensitive (e.g. an interview): the AI may use its content, but its name, company, person and exact quotes are kept out of the draft and all exports – see below |
| `... --score-only` | **Demo/testing only:** still shows every AAOCC score but keeps low-scoring web sources instead of replacing them. Never for real handbook pages |
| `py handbook_demo.py --add-doc "path-or-URL" --topic "..."` | Add a source to the wiki (password) |
| `py handbook_demo.py --remove-source <id>` / `--remove-page <slug>` | Remove from the wiki (password + typed "yes") |
| `py handbook_demo.py --help` | Show all options |

Every full run also writes `wiki/<page>.claims.json`: one entry per key finding with an exact quote from its
source, checked by the script (not the AI) – shown as "Claim quote verification" in the quality check.

> All of this works the same in `handbook_demo_codex.py` (the ChatGPT version).

---

## Confidential sources (`--confidential`)

```
py handbook_demo.py "question" --file "C:\path\interview.docx" --confidential
py handbook_demo.py --add-doc "C:\path\interview.docx" --topic "..." --confidential
```
- The source is shown everywhere as *"Confidential source (anonymized, ref xxxxxx)"* – go/no-go check,
  source list, `.html`, `.docx`, wiki page. The real file name stays only in your local `raw/`.
- The AI is told never to name, quote or identify the company or person and to generalise instead
  ("an SME in a similar sector reported…"). Exact quotes appear only in the local `.claims.json`, never in
  the exports.

**What it does NOT do:**
1. **The full text is still sent to the AI.** Turn off *"Improve the model"* in your Claude account
   (claude.ai → Settings → Privacy), or *"Improve the model for everyone"* in ChatGPT (Settings → Data controls)
   for the Codex version, if you don't want it used for training. Get the company's consent first.
2. **The hiding is an instruction to the AI, not a hard filter.** Specific facts (numbers, events, suppliers)
   are still used and can make a company recognisable to insiders. The human reviewer must check every
   page that cites a confidential source before approving it.

---

## Sharing one wiki with the team (`wiki_location.txt`)

`wiki/` and `raw/` are **deliberately not on GitHub** (they can contain unreviewed drafts and confidential
sources), so a fresh download starts with an empty knowledge store – `--lookup` and `--ask` have nothing to
search yet.

To share one store instead: create a file `wiki_location.txt` next to the script containing one line – the
path to a shared, synced folder (e.g. the team's Teams/OneDrive folder):
```
C:\Users\<you>\OneDrive - HAN\<team folder>\AI-Wiki
```
Everyone whose copy points at the same folder adds to and asks from the same wiki. If the folder doesn't
exist on your computer (not synced), the script warns you and uses the local store next to the script.
Only use a folder that only the team can access, because confidential sources are stored there too.

## Publishing approved pages

Approved pages go to the website with `publish_wiki.py`. See **`SETUP.md`** for the approval header, the
dry-run check and the one-time GitHub Pages setup (repo owner only).

## Rules that always apply
1. Drafts stay DRAFT until a researcher approves them.
2. Never invent sources, numbers or quotes; every key claim needs a real, checkable source.
3. Confidential Waterkracht or interview data never goes into the AI or onto GitHub without consent/redaction.
4. Every automated step has a manual fallback (see `SETUP.md` → *Manual fallback*).
