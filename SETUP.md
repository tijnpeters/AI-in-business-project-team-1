# Handbook website on GitHub Pages - setup

This folder turns the handbook demo's wiki into a public website, hosted free by
GitHub Pages. Only pages a researcher has **approved** ever reach the website.

## What is in this folder

| File | What it does |
|---|---|
| `mkdocs.yml` | Website settings (name, colours, menu). Normally no need to edit. |
| `docs/` | The website's pages. `index.md` = home, `about.md` = how pages are made, `handbook/` = the approved handbook pages (filled by the script below). |
| `publish_wiki.py` | Copies approved pages from the demo's `wiki/` folder into `docs/handbook/`. Removes draft labels, review notes, links into `raw/` and local file paths. |
| `.github/workflows/deploy-wiki.yml` | Tells GitHub to rebuild the website whenever `docs/` changes. It refuses to publish any page that is not marked APPROVED. |
| `requirements.txt` | The two tools GitHub installs to build the site (MkDocs + Material theme). |
| `.gitignore` | Already contains `site/`, `wiki/`, `raw/` and `wiki_password.txt`, so drafts, sources and the wiki password are never uploaded by accident. |

## One-time setup (repo owner - Tijn)

1. Copy everything in this folder into the root of the repo
   `tijnpeters/AI-in-business-project-team-1` (keep the `.github` folder - it may be hidden in File Explorer;
   turn on View > Show > Hidden items).
2. Commit and push.
3. On github.com: repo > **Settings** > **Pages** > under "Build and deployment", set **Source** to **GitHub Actions**.
4. Repo visibility: GitHub Pages is free for **public** repos. For a **private** repo, the owner needs
   GitHub Pro (free for students via the GitHub Student Developer Pack). In both cases **the website itself
   is public** - anyone with the address can read it.
5. Go to the **Actions** tab > "Publish handbook website" > **Run workflow**. After 1-2 minutes the site is
   live at `https://tijnpeters.github.io/AI-in-business-project-team-1/`.

## Every time a page is approved

1. Researcher reads the draft in `wiki/<page>.md` and, if approved, adds three lines to the header
   between the `---` lines:
   ```
   status: APPROVED
   approved_by: <full name>
   approved_on: 2026-10-12
   ```
   Optional: `next_review: 2026-12-14`.
2. Check first without changing anything:
   ```
   py publish_wiki.py --wiki "D:\VSCode\wiki" --dry-run
   ```
   Read the `!` warnings - e.g. a page that cites a local upload (could be confidential).
3. Publish into the website folder:
   ```
   py publish_wiki.py --wiki "D:\VSCode\wiki"
   ```
4. Commit + push `docs/handbook/`. The website updates itself within a few minutes.

To take a page offline: remove `status: APPROVED` from its header, run step 3 again, and push.

## Manual fallback

If the script or the AI pipeline is not available, write or edit a page directly in `docs/handbook/`
(on github.com: open the file > pencil icon). Put this at the top so the safety check accepts it:
```
---
title: Page title
status: APPROVED
---
```
Only do this for pages a researcher has actually approved.

## Test locally before pushing (optional)

```
py -m pip install -r requirements.txt
py -m mkdocs serve
```
Then open http://127.0.0.1:8000 in your browser. Ctrl+C stops it.
