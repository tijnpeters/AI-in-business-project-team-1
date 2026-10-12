"""
publish_wiki.py - copies APPROVED pages from the handbook demo's wiki/ folder
into this website's docs/handbook/ folder, so GitHub can turn them into the
public handbook website.

Why a separate step? The demo's wiki/ folder is the platform's private memory:
it holds drafts, review notes and links to raw/ sources (which can include
local or confidential uploads). The website must only ever show pages a
researcher has approved. So this script:

  - only takes pages whose header says   status: APPROVED
    and that name who approved them      approved_by: <name>
    and when                             approved_on: YYYY-MM-DD
  - removes the "DRAFT - awaiting researcher review" label and the internal
    "Debates" review note
  - removes links into raw/ and hides local file paths (C:\\Users\\..., D:\\...)
    so nothing from your own computer ends up on the internet
  - warns you if an approved page cites a local upload, so you can double-check
    it contains nothing confidential
  - rebuilds docs/handbook/index.md (the list of pages on the website)
  - deletes pages from the website that are no longer approved

HOW TO APPROVE A PAGE (manual step, this is the human-review gate):
  Open wiki/<page>.md in a text editor. In the header between the two '---'
  lines, add three lines, e.g.:
      status: APPROVED
      approved_by: Kyran Weijman
      approved_on: 2026-10-12
  Save. Then run this script.

RUN (Windows, in the folder that contains this script):
    py publish_wiki.py --wiki "D:\\VSCode\\wiki"
  Then upload (commit + push) the changed docs/handbook/ files to GitHub.
  GitHub rebuilds the website automatically within a few minutes.

Only the Python standard library is used - nothing to install.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR_DEFAULT = HERE / "docs" / "handbook"
MARKER = "<!-- published-by: publish_wiki.py -->"


# ---------------------------------------------------------------------------
# Reading a wiki page
# ---------------------------------------------------------------------------
def split_frontmatter(text: str) -> tuple[dict, str]:
    """Returns (header fields, body). The demo writes a simple header:
    ---
    topic: ...
    confidence: HIGH
    updated: 2026-10-05T14:00:00
    sources: [id1, id2]
    ---"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}, text
    head = parts[0].lstrip("-").strip("\n")
    body = parts[1].lstrip("-").lstrip("\n")
    meta: dict = {}
    for line in head.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip().lower()] = value.strip()
    return meta, body


def source_ids(meta: dict) -> list[str]:
    raw = meta.get("sources", "").strip().strip("[]")
    return [s.strip() for s in raw.split(",") if s.strip()]


# ---------------------------------------------------------------------------
# Cleaning a page for the public website
# ---------------------------------------------------------------------------
LOCAL_PATH = re.compile(
    r"(?<![\w/])(?:[A-Za-z]:\\[^\s)|<>\"]+|/(?:home|Users|mnt)/[^\s)|<>\"]+)"
)
RAW_LINK = re.compile(r"\[([^\]]+)\]\((?:\.\./|\./)?raw/[^)]*\)")
DRAFT_LABEL = re.compile(r"^\**\s*DRAFT\s*[-–—:]\s*awaiting researcher review\.?\s*\**\s*$",
                         re.IGNORECASE | re.MULTILINE)


def remove_section(body: str, heading: str) -> str:
    """Removes a '## <heading>' section up to the next heading of level 1-2."""
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$.*?(?=^#{{1,2}}\s|\Z)",
                         re.IGNORECASE | re.MULTILINE | re.DOTALL)
    return pattern.sub("", body)


def clean_body(body: str) -> tuple[str, int]:
    body = DRAFT_LABEL.sub("", body)
    body = remove_section(body, "Debates")
    body = RAW_LINK.sub(r"\1", body)
    body, n_paths = LOCAL_PATH.subn("(local document - not public)", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return body, n_paths


def info_box(meta: dict) -> str:
    conf = meta.get("confidence", "not stated").upper()
    kind = {"HIGH": "success", "MEDIUM": "warning", "LOW": "danger"}.get(conf, "info")
    updated = meta.get("updated", "")[:10]
    lines = [f'!!! {kind} "Overall confidence: {conf}"',
             f"    Approved by **{meta['approved_by']}** on {meta['approved_on']}."]
    if updated:
        lines.append(f"    Research last updated {updated}.")
    if meta.get("next_review"):
        lines.append(f"    Next review planned {meta['next_review']}.")
    return "\n".join(lines) + "\n"


def build_page(meta: dict, body: str) -> tuple[str, int]:
    body, n_paths = clean_body(body)
    box = info_box(meta)
    # Put the info box right under the page title (first '# ' line).
    m = re.search(r"^# .+$", body, re.MULTILINE)
    if m:
        body = body[:m.end()] + "\n\n" + box + body[m.end():]
    else:
        body = f"# {meta.get('topic', 'Untitled')}\n\n{box}\n{body}"
    header = (f"---\ntitle: {meta.get('topic', '').replace(':', ' -')}\n"
              f"status: APPROVED\n---\n{MARKER}\n\n")
    return header + body, n_paths


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def check_approval(meta: dict) -> str | None:
    """Returns None if the page may be published, else the reason it may not."""
    if meta.get("status", "").upper() != "APPROVED":
        return f"status is '{meta.get('status') or 'missing'}' (needs: APPROVED)"
    if not meta.get("approved_by"):
        return "approved_by is missing"
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta.get("approved_on", "")):
        return "approved_on is missing or not YYYY-MM-DD"
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Publish approved wiki pages to the website folder.")
    ap.add_argument("--wiki", default=str(HERE / "wiki"),
                    help="path to the demo's wiki/ folder (default: wiki/ next to this script)")
    ap.add_argument("--raw", default=None,
                    help="path to the demo's raw/ folder (default: raw/ next to the wiki folder)")
    ap.add_argument("--out", default=str(OUT_DIR_DEFAULT), help="website folder for handbook pages")
    ap.add_argument("--dry-run", action="store_true", help="only report, change nothing")
    args = ap.parse_args()

    wiki = Path(args.wiki)
    raw = Path(args.raw) if args.raw else wiki.parent / "raw"
    out = Path(args.out)
    if not wiki.is_dir():
        print(f"No wiki folder found at {wiki}. Use --wiki \"D:\\path\\to\\wiki\".")
        return 1

    published, skipped, warnings = [], [], []
    pages_out: dict[str, str] = {}
    for page in sorted(wiki.glob("*.md")):
        if page.name.lower() == "index.md":
            continue
        meta, body = split_frontmatter(page.read_text(encoding="utf-8"))
        reason = check_approval(meta)
        if reason:
            skipped.append((page.name, reason))
            continue
        uploads = [sid for sid in source_ids(meta) if (raw / "upload" / f"{sid}.json").exists()]
        if uploads:
            warnings.append(f"{page.name}: cites local upload(s) {', '.join(uploads)} - make sure the "
                            f"page text contains nothing confidential before you push it.")
        text, n_paths = build_page(meta, body)
        if n_paths:
            warnings.append(f"{page.name}: hid {n_paths} local file path(s).")
        pages_out[page.name] = text
        published.append((page.stem, meta))

    print(f"Wiki folder: {wiki}")
    print(f"Approved and published: {len(published)}")
    for slug, meta in published:
        print(f"  + {slug}  (confidence {meta.get('confidence', '?')}, approved by {meta['approved_by']})")
    print(f"Not published: {len(skipped)}")
    for name, reason in skipped:
        print(f"  - {name}: {reason}")
    for w in warnings:
        print(f"  ! {w}")

    if args.dry_run:
        print("\n--dry-run: nothing was changed.")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    # Remove pages this script published earlier that are no longer approved.
    for old in out.glob("*.md"):
        if old.name == "index.md" or old.name in pages_out:
            continue
        if MARKER in old.read_text(encoding="utf-8", errors="replace"):
            old.unlink()
            print(f"  removed from website (no longer approved): {old.name}")
    for name, text in pages_out.items():
        (out / name).write_text(text, encoding="utf-8")

    # The list of pages on the website.
    rows = ["# Handbook pages", "",
            "Every page below has been reviewed and approved by a researcher. "
            "Each one ends with one concrete next step.", ""]
    if published:
        rows += ["| Page | Confidence | Approved |", "|---|---|---|"]
        for slug, meta in sorted(published, key=lambda p: p[1].get("topic", p[0]).lower()):
            rows.append(f"| [{meta.get('topic', slug)}]({slug}.md) | "
                        f"{meta.get('confidence', '?').upper()} | {meta['approved_on']} |")
    else:
        rows.append("*No pages have been approved yet.*")
    rows += ["", f"*List generated {date.today().isoformat()}.*", ""]
    (out / "index.md").write_text("\n".join(rows), encoding="utf-8")
    print(f"\nWebsite folder updated: {out}")
    print("Next: commit + push the docs/ folder to GitHub; the website updates by itself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
