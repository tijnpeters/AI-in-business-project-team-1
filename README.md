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
| `py handbook_demo.py --add-doc "path-or-URL" --topic "..."` | Add a source to the wiki (password) |
| `py handbook_demo.py --remove-source <id>` / `--remove-page <slug>` | Remove from the wiki (password + typed "yes") |

---

## Important: your knowledge store starts empty

`wiki/` and `raw/` are **deliberately not on GitHub** (they can contain unreviewed drafts and confidential
sources). So after a fresh download, `--lookup` and `--ask` have nothing to search until you do a few runs
yourself. To get the team's existing material, ask a teammate to share their `wiki/` and `raw/` folders
directly (not via GitHub), and only if they contain no confidential Waterkracht or interview data.

## Publishing approved pages

Approved pages go to the website with `publish_wiki.py`. See **`SETUP.md`** for the approval header, the
dry-run check and the one-time GitHub Pages setup (repo owner only).

## Rules that always apply
1. Drafts stay DRAFT until a researcher approves them.
2. Never invent sources, numbers or quotes; every key claim needs a real, checkable source.
3. Confidential Waterkracht or interview data never goes into the AI or onto GitHub without consent/redaction.
4. Every automated step has a manual fallback (see `SETUP.md` → *Manual fallback*).
