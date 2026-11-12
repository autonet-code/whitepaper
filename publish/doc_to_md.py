"""Google Doc JSON (documents.get) -> GitHub Markdown, for the whitepaper.

Headings keep the doc's levels; empty paragraphs and empty headings are
dropped; bullets become '- ' (nested by level); the glossary table becomes a
Markdown table; bold, italic, links and subscripts are kept."""
import json
import re
import sys

PREFIX = {"TITLE": "# ", "SUBTITLE": "", "HEADING_1": "# ", "HEADING_2": "## ",
          "HEADING_3": "### ", "HEADING_4": "#### ", "HEADING_5": "##### ",
          "HEADING_6": "###### "}


def run_md(r, in_heading):
    tr = r.get("textRun")
    if not tr:
        return ""
    text = tr.get("content", "").replace("\n", "").replace("\u000b", " ")
    if not text:
        return ""
    st = tr.get("textStyle", {})
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    core = text.strip()
    if not core:
        return text
    core = core.replace("*", "\\*").replace("_", "\\_") if not st.get("link") else core
    SUB = {"i": "ᵢ", "j": "ⱼ", "n": "ₙ", "0": "₀", "1": "₁", "2": "₂"}
    if st.get("baselineOffset") == "SUBSCRIPT":
        # Unicode subscripts render in GitHub and in the app's Markdown
        # widget alike (the widget shows <sub> tags as text).
        core = ("".join(SUB[ch] for ch in core) if all(ch in SUB for ch in core)
                else f"<sub>{core}</sub>")
    elif st.get("baselineOffset") == "SUPERSCRIPT":
        core = f"<sup>{core}</sup>"
    if st.get("bold") and not in_heading:
        core = f"**{core}**"
    if st.get("italic") and not st.get("baselineOffset"):
        core = f"*{core}*"
    link = (st.get("link") or {}).get("url")
    if link:
        core = f"[{core}]({link})"
    return lead + core + trail


def para_md(p):
    style = p.get("paragraphStyle", {}).get("namedStyleType", "NORMAL_TEXT")
    in_heading = style in PREFIX and style != "SUBTITLE"
    # Merge consecutive runs with the same formatting, so a phrase split
    # over several runs becomes one span.
    merged = []
    for r in p.get("elements", []):
        tr = r.get("textRun")
        if not tr:
            continue
        st = tr.get("textStyle", {})
        key = (bool(st.get("bold")), bool(st.get("italic")),
               st.get("baselineOffset"), (st.get("link") or {}).get("url"))
        if merged and merged[-1][0] == key:
            merged[-1][1]["textRun"]["content"] += tr.get("content", "")
        else:
            merged.append([key, {"textRun": {"content": tr.get("content", ""),
                                             "textStyle": st}}])
    body = "".join(run_md(r, in_heading) for _, r in merged)
    body = body.strip()
    if not body:
        return None
    if "bullet" in p:
        level = p["bullet"].get("nestingLevel", 0)
        return "  " * level + "- " + body
    if style == "SUBTITLE":
        return f"*{body}*"
    return PREFIX.get(style, "") + body


def cell_text(cell):
    parts = []
    for e in cell.get("content", []):
        if "paragraph" in e:
            t = para_md(e["paragraph"])
            if t:
                parts.append(t.lstrip("#- ").strip())
    return " ".join(parts).replace("|", "\\|")


def convert(d):
    """The whole doc as Markdown. `d` is a documents.get result, bare or
    wrapped as {"content": ...}."""
    c = d.get("content", d)
    body = c["tabs"][0]["documentTab"]["body"]["content"]
    blocks = []          # list of (kind, text)
    for e in body:
        if "paragraph" in e:
            t = para_md(e["paragraph"])
            if t is None:
                continue
            if re.fullmatch(r"-{3,}", t.strip()):
                blocks.append(("hr", "---"))
            else:
                blocks.append(("bullet" if t.lstrip().startswith("- ") else "p", t))
        elif "table" in e:
            rows = [[cell_text(cell) for cell in row["tableCells"]]
                    for row in e["table"]["tableRows"]]
            lines = ["| " + " | ".join(rows[0]) + " |",
                     "|" + "|".join("---" for _ in rows[0]) + "|"]
            lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
            blocks.append(("table", "\n".join(lines)))
    out = []
    prev = None
    for kind, t in blocks:
        if out:
            out.append("\n" if (kind == "bullet" and prev == "bullet") else "\n\n")
        out.append(t)
        prev = kind
    return "".join(out) + "\n"


def main(src, dst):
    text = convert(json.load(open(src, encoding="utf-8")))
    open(dst, "w", encoding="utf-8", newline="\n").write(text)
    print(len(text.split()), "words")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
