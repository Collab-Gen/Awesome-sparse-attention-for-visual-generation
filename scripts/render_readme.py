#!/usr/bin/env python3
"""Update the generated bibliography blocks in README.md."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
BLOCK = re.compile(
    r"^<!-- BEGIN PAPERS: (?P<name>[a-z0-9-]+) -->\n"
    r"(?P<body>.*?)"
    r"^<!-- END PAPERS: (?P=name) -->$",
    re.MULTILINE | re.DOTALL,
)
PAPER_REFERENCE = re.compile(r"(?<!!)\[[^\[\]\n]+\]\[paper:([^\[\]\s]+)\]")
ARXIV_ID = re.compile(r"arxiv:(\d{4}\.\d{4,5})")
DOI = re.compile(r"doi:(10\.\d{4,9}/[a-z0-9._;()/:+-]+)", re.IGNORECASE)
VENUE_ID = re.compile(r"venue:[a-z0-9]+(?:-[a-z0-9]+)+")
PUBLIC_DATE = re.compile(r"\d{4}-\d{2}(?:-\d{2})?")
SECTION = re.compile(r"(?:mechanism|application|related)-[a-z0-9-]+")


def paper_url(paper):
    if "url" in paper:
        return paper["url"]
    identifier = paper["id"]
    if arxiv := ARXIV_ID.fullmatch(identifier):
        return f"https://arxiv.org/abs/{arxiv[1]}"
    if doi := DOI.fullmatch(identifier):
        return f"https://doi.org/{doi[1]}"
    raise ValueError(f"{identifier}: missing paper URL")


def require_url(url, field):
    if not isinstance(url, str) or any(char.isspace() or char in "<>" for char in url):
        raise ValueError(f"{field}: expected an HTTPS URL")
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError(f"{field}: expected an HTTPS URL")


def require_text(value, field):
    if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value:
        raise ValueError(f"{field}: expected nonempty text on one line")


def load_catalog(sections):
    entries = json.loads(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        raise ValueError("papers.json must contain an array of paper records")

    papers = {}
    urls = set()
    titles = {}
    for paper in entries:
        identifier = paper["id"]
        if not any(pattern.fullmatch(identifier) for pattern in (ARXIV_ID, DOI, VENUE_ID)):
            raise ValueError(f"{identifier}: use an arXiv, DOI, or venue ID")
        key = identifier.casefold()
        if key in papers:
            raise ValueError(f"{identifier}: duplicate paper ID")
        url = paper_url(paper)
        require_url(url, identifier)
        if url in urls:
            raise ValueError(f"{identifier}: duplicate paper URL: {url}")
        urls.add(url)
        require_text(paper["title"], f"{identifier} title")
        title_key = "".join(
            char for char in unicodedata.normalize("NFKC", paper["title"]).casefold()
            if char.isalnum()
        )
        if title_key in titles:
            raise ValueError(f"{identifier}: duplicate title also listed as {titles[title_key]}")
        titles[title_key] = identifier

        published = paper["first_public"]
        if not PUBLIC_DATE.fullmatch(published):
            raise ValueError(f"{identifier}: first_public must use YYYY-MM-DD or YYYY-MM")
        try:
            date.fromisoformat(published if len(published) == 10 else f"{published}-01")
        except ValueError as error:
            raise ValueError(f"{identifier}: invalid first_public date {published!r}") from error
        if type(paper["year"]) is not int or not int(published[:4]) <= paper["year"] <= 9999:
            raise ValueError(f"{identifier}: invalid bibliographic year")

        tags = paper["sections"]
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise ValueError(f"{identifier}: sections must be a list of section names")
        if len(tags) != len(set(tags)):
            raise ValueError(f"{identifier}: duplicate section names")
        if unknown := set(tags) - sections:
            raise ValueError(f"{identifier}: unknown sections: {', '.join(sorted(unknown))}")

        if "code" in paper:
            require_url(paper["code"]["url"], f"{identifier} code")
            require_text(paper["code"]["label"], f"{identifier} code label")
        if "featured" in paper:
            require_text(paper["featured"]["name"], f"{identifier} featured name")
            require_text(paper["featured"]["note"], f"{identifier} featured note")
        papers[key] = paper
    return papers


def cell(text):
    return text.replace("|", r"\|")


def link(label, url):
    label = cell(label.replace("[", r"\[").replace("]", r"\]"))
    return f"[{label}](<{url}>)" if "(" in url or ")" in url else f"[{label}]({url})"


def render_readme(source):
    matches = list(BLOCK.finditer(source))
    names = {match["name"] for match in matches}
    if (
        len(names) != len(matches)
        or source.count("<!-- BEGIN PAPERS: ") != len(matches)
        or source.count("<!-- END PAPERS: ") != len(matches)
        or not {"featured", "references"} <= names
    ):
        raise ValueError("README paper blocks must have unique, matching markers")
    sections = names - {"featured", "references"}
    if invalid := sorted(name for name in sections if not SECTION.fullmatch(name)):
        raise ValueError(f"Invalid README paper blocks: {', '.join(invalid)}")

    papers = load_catalog(sections)
    referenced = {key.casefold() for key in PAPER_REFERENCE.findall(BLOCK.sub("", source))}
    if unknown := referenced - papers.keys():
        raise ValueError(f"README cites unknown papers: {', '.join(sorted(unknown))}")
    unlisted = {
        key for key, paper in papers.items()
        if not paper["sections"] and "featured" not in paper and key not in referenced
    }
    if unlisted:
        raise ValueError(f"Papers need a section or a README citation: {', '.join(sorted(unlisted))}")
    newest_first = sorted(
        papers.values(), key=lambda paper: (paper["first_public"], paper["id"].casefold()),
        reverse=True,
    )

    def replace_block(match):
        name = match["name"]
        if name == "references":
            lines = [f"[paper:{key}]: <{paper_url(papers[key])}>" for key in sorted(referenced)]
        elif name == "featured":
            lines = ["| Method | What to look for | Paper | Official code |", "| --- | --- | --- | --- |"]
            for paper in newest_first:
                if featured := paper.get("featured"):
                    code = paper.get("code")
                    implementation = link(code["label"], code["url"]) if code else "—"
                    lines.append(
                        f"| {cell(featured['name'])} | {cell(featured['note'])} | "
                        f"{link('Paper', paper_url(paper))} | {implementation} |"
                    )
        else:
            lines = ["| Year | Paper |", "| ---: | --- |"]
            lines.extend(
                f"| {paper['year']} | {link(paper['title'], paper_url(paper))} |"
                for paper in newest_first if name in paper["sections"]
            )
        return f"<!-- BEGIN PAPERS: {name} -->\n\n" + "\n".join(lines) + f"\n\n<!-- END PAPERS: {name} -->"

    return BLOCK.sub(replace_block, source)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if README.md needs regeneration")
    args = parser.parse_args()
    try:
        source = README.read_text(encoding="utf-8")
        expected = render_readme(source)
        if expected != source:
            if args.check:
                print("README.md is out of date. Run python3 scripts/render_readme.py.", file=sys.stderr)
                return 1
            README.write_text(expected, encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Cannot render bibliography: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
