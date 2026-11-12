"""Publish the paper from its Google Doc into the three repos.

The doc is the one source. This script turns it into:

- this repo's README.md: the overview, up to "The sections below take each
  module in turn.", then a link to each module's chapter, the glossary and
  the earlier versions;
- each module's chapter in the README of the repo that holds its code
  (CHAPTERS below), between the markers <!-- paper:start --> and
  <!-- paper:end -->. Whatever the README holds outside the markers (how to
  run, the repo map, license) is the repo's own and is kept;
- the whole paper as one PDF in this repo (Drive's own export of the doc).

Usage:
    python publish/publish.py DOC_JSON [--pdf PDF] [--version 4]
        [--date "November 2026"] [--node PATH] [--governance PATH]

DOC_JSON is the doc as documents.get returns it (bare, or wrapped as
{"content": ...}). PDF is Drive's export of the same revision
(application/pdf), copied in as the_on_chain_jurisdiction_v<version>.pdf.
Nothing is committed: review the diffs in each repo, then commit there.
"""
import argparse
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doc_to_md import convert  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPLIT = "The sections below take each module in turn."
START, END = "<!-- paper:start -->", "<!-- paper:end -->"

WRAPPER_URL = "https://github.com/autonet-code/whitepaper"
# Each module chapter (a "### <name>" heading after SPLIT) and the repo whose
# README holds it. Chapters for one repo appear there in the doc's order.
CHAPTERS = {
    "Governance": "governance",
    "Projects": "governance",
    "Autonet": "node",
}
REPOS = {
    "governance": "https://github.com/autonet-code/governance",
    "node": "https://github.com/autonet-code/node",
}


def slug(title):
    """GitHub's heading anchor."""
    s = re.sub(r"[*_`]", "", title).strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def heading(line):
    m = re.match(r"^(#{1,6}) (.*)$", line)
    return (len(m.group(1)), m.group(2).strip()) if m else None


def split(md):
    """(overview, {repo: [chapter lines]}, glossary) from the whole paper."""
    lines = md.split("\n")
    cut = next(i for i, l in enumerate(lines) if l.strip() == SPLIT)
    gloss = next(i for i, l in enumerate(lines) if heading(l) == (1, "Glossary"))
    overview = lines[: cut + 1]
    parts, repo = {}, None
    for line in lines[cut + 1 : gloss]:
        h = heading(line)
        if h and h[0] == 3 and h[1] in CHAPTERS:
            repo = CHAPTERS[h[1]]
        elif h and h[0] <= 3 and repo is not None and h[1] not in CHAPTERS:
            sys.exit(f"unexpected heading between chapters: {line!r}")
        if repo is None:
            if line.strip():
                sys.exit(f"text after the split line before any chapter: {line!r}")
            continue
        parts.setdefault(repo, []).append(line)
    return overview, parts, lines[gloss:]


def promote(lines):
    """A chapter's '### Autonet' becomes its README's '# Autonet'."""
    out = []
    for line in lines:
        h = heading(line)
        out.append("#" * max(1, h[0] - 2) + " " + h[1] if h else line)
    return out


def link_refs(text, here, where):
    """'(see X)' becomes a link when X is a heading: within the page, or to
    the README that holds it."""
    def repl(m):
        title = m.group(2).strip("*")
        if title.endswith(" below"):
            title = title[: -len(" below")]
        target = where.get(title)
        if target is None:
            return m.group(0)
        page, anchor = target
        href = f"#{anchor}" if page == here else f"{page}#{anchor}"
        return f"{m.group(1)}[{title}]({href})"
    return re.sub(r"(\(see )([^)]+?)(?=\))", repl, text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc_json")
    ap.add_argument("--pdf")
    ap.add_argument("--version", default="4")
    ap.add_argument("--date", default="November 2026")
    ap.add_argument("--node", default=r"C:\code\autonet")
    ap.add_argument("--governance", default=r"C:\code\dao\trustless-contracts")
    a = ap.parse_args()
    paths = {"node": a.node, "governance": a.governance}

    md = convert(json.load(open(a.doc_json, encoding="utf-8")))
    overview, parts, glossary = split(md)
    parts = {repo: promote(lines) for repo, lines in parts.items()}

    # Where every heading lives, for the cross-references.
    where = {}
    for line in overview + glossary:
        h = heading(line)
        if h:
            where.setdefault(h[1], (WRAPPER_URL, slug(h[1])))
    for repo, lines in parts.items():
        for line in lines:
            h = heading(line)
            if h:
                where.setdefault(h[1], (REPOS[repo], slug(h[1])))

    pdf_name = f"the_on_chain_jurisdiction_v{a.version}.pdf"

    # This repo's README.
    chapters = []
    for name, repo in CHAPTERS.items():
        if repo in parts and any(heading(l) == (1, name) for l in parts[repo]):
            chapters.append(f"- [{name}]({REPOS[repo]}#{slug(name)}), in the README of "
                            f"[{REPOS[repo].rsplit('/', 1)[1]}]({REPOS[repo]}), "
                            "next to its code.")
    wrapper = "\n".join(overview) + "\n\n" + "\n".join(chapters) + "\n\n"
    wrapper += "\n".join(glossary).rstrip("\n") + "\n\n---\n\n"
    wrapper += "## Earlier versions and related papers\n\n"
    wrapper += (f"This paper is version {a.version} ({a.date}). The whole paper, "
                f"chapters included, is also one file: [{pdf_name}]({pdf_name}).\n\n")
    wrapper += (
        "- [Autonet: The Recursive Principial Body](legacy/autonet_paper_v3.md), version 3 (2026).\n"
        "- [Emergent Alignment: Economic Mechanisms for the Peaceful Transfer of Work from "
        "Humans to AI](emergent_alignment.md) (February 2026), the theoretical framework.\n"
        "- [Autonet: Economy-as-a-Service](legacy/autonet_2021.pdf), the original whitepaper (2021).\n")
    wrapper = link_refs(wrapper, WRAPPER_URL, where)
    open(os.path.join(HERE, "README.md"), "w", encoding="utf-8", newline="\n").write(wrapper)
    print("whitepaper/README.md:", len(wrapper.split()), "words")

    # Each module repo's README, between the markers.
    for repo, lines in parts.items():
        readme = os.path.join(paths[repo], "README.md")
        text = open(readme, encoding="utf-8").read()
        if START not in text or END not in text:
            sys.exit(f"{readme}: add {START} and {END} where the chapter goes")
        chapter = (f"*A chapter of [The On-Chain Jurisdiction]({WRAPPER_URL}), version "
                   f"{a.version} ({a.date}). Its terms are defined in the paper's "
                   f"[Glossary]({WRAPPER_URL}#glossary).*\n\n" + "\n".join(lines).strip("\n"))
        chapter = link_refs(chapter, REPOS[repo], where)
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        new = f"{head}{START}\n\n{chapter}\n\n{END}{tail}"
        open(readme, "w", encoding="utf-8", newline="\n").write(new)
        print(f"{repo}/README.md: chapter of", len(chapter.split()), "words")

    if a.pdf:
        shutil.copyfile(a.pdf, os.path.join(HERE, pdf_name))
        print("copied", pdf_name)


if __name__ == "__main__":
    main()
