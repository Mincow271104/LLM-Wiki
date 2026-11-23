#!/usr/bin/env python3
"""
scripts/ingest.py - Incremental Source Ingestion Tool
Implements the Karpathy LLM Wiki INGEST operation:
- Validates metadata using jsonschema against schemas/source.schema.json.
- Optionally performs live HTTP GET verification of canonical URLs (--verify-online).
- Enforces stable canonical card naming (one card per source ID) to prevent duplicates.
- Updates master raw/sources.json registry.
- Updates wiki/index.md and appends structured entries to wiki/log.md.
- Explicitly documents the boundary between automated CLI bookkeeping and LLM cognitive extraction.
"""

import os
import sys
import json
import argparse
import re
import urllib.request
from datetime import date
from pathlib import Path

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw"
CARDS_DIR = RAW_DIR / "source-cards"
SOURCES_FILE = RAW_DIR / "sources.json"
SCHEMA_FILE = BASE_DIR / "schemas" / "source.schema.json"
LOG_FILE = BASE_DIR / "wiki" / "log.md"
INDEX_FILE = BASE_DIR / "wiki" / "index.md"

CANONICAL_SLUGS = {
    "S01": "S01-react",
    "S02": "S02-toolformer",
    "S03": "S03-building-effective-agents",
    "S04": "S04-cloud-architecture-components",
    "S05": "S05-openai-agents-sdk",
    "S06": "S06-langgraph-overview",
    "S07": "S07-crewai-documentation",
    "S08": "S08-microsoft-agent-framework"
}

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def get_canonical_card_name(source_id, title):
    if source_id in CANONICAL_SLUGS:
        return CANONICAL_SLUGS[source_id]
    # Check if an existing card for this ID already exists
    existing = list(CARDS_DIR.glob(f"{source_id}-*.md"))
    if existing:
        return existing[0].stem
    return f"{source_id}-{slugify(title[:30])}"

def validate_source_schema(source_dict):
    schema = load_json(SCHEMA_FILE)
    if HAS_JSONSCHEMA:
        try:
            jsonschema.validate(instance=source_dict, schema=schema)
            return True, "Valid (jsonschema verified)"
        except jsonschema.ValidationError as ve:
            return False, f"Schema validation error: {ve.message}"
    else:
        for field in schema.get("required", []):
            if field not in source_dict or source_dict[field] is None or source_dict[field] == "":
                return False, f"Missing required field: '{field}'"
        if not re.match(r"^S[0-9]{2,}$", source_dict.get("id", "")):
            return False, f"Invalid ID format: '{source_dict.get('id')}'"
        return True, "Valid (basic check)"

def verify_url_live(url, timeout=7):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status == 200, resp.status, None
    except Exception as e:
        return False, None, str(e)

def append_to_log(source, verified_live=False):
    today = date.today().isoformat()
    status_note = "Verified live via HTTP 200" if verified_live else "Recorded metadata validated against schema"
    log_entry = f"""
## [{today}] ingest | {source['id']}: {source['title']}
- **Source ID:** {source['id']}
- **Publisher / Authors:** {', '.join(source.get('authors', [])) or source.get('publisher')}
- **URL:** {source['url']}
- **Document Type:** {source.get('document_type', 'unknown')}
- **Status:** {status_note}.
"""
    if LOG_FILE.exists():
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"Appended ingestion audit entry to {LOG_FILE.name}")

def append_to_index(source, card_stem):
    if not INDEX_FILE.exists():
        return
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if f"[{source['id']}]" in content:
        print(f"Source {source['id']} already present in index.")
        return

    rel_card_path = f"../raw/source-cards/{card_stem}.md"
    entry_line = f"\n- **[{source['id']}] {source['title']}** — {source.get('publisher', 'Unknown')} ({source.get('publication_date', 'N/A')}). [Source Card]({rel_card_path})"

    if "## Operating on the Wiki" in content:
        parts = content.split("## Operating on the Wiki")
        new_content = parts[0].rstrip() + "\n" + entry_line + "\n\n## Operating on the Wiki" + parts[1]
    else:
        new_content = content + "\n" + entry_line

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {INDEX_FILE.name} with source index entry.")

def generate_markdown_card(source):
    authors_str = ", ".join(source.get("authors", [])) if source.get("authors") else source.get("publisher", "N/A")
    sections_str = "\n".join([f"- **{sec}**" for sec in source.get("verified_sections", ["General Overview"])])
    topics_str = ", ".join(source.get("key_topics", []))

    md = f"""# Source Card: {source['id']}

## Metadata
- **Source ID:** {source['id']}
- **Title:** {source['title']}
- **Authors / Contributors:** {authors_str}
- **Publisher / Venue:** {source.get('publisher', 'N/A')}
- **Publication Date:** {source.get('publication_date', 'N/A')}
- **Access Date:** {source.get('access_date', date.today().isoformat())}
- **Canonical URL:** [{source['url']}]({source['url']})
- **Retrieval Status:** {source.get('retrieval_status', 'accessible')} (HTTP {source.get('http_status', 200)})
- **Document Type:** {source.get('document_type', 'N/A')}

## Summary
{source.get('summary', 'No summary provided.')}

## Key Topics Covered
{topics_str}

## Verified Section Structure
{sections_str}

## Copyright & Fair Use Notice
{source.get('copyright_notice', 'Metadata and excerpts stored under educational fair use guidelines.')}
"""
    return md

def ingest_source(source_data, verify_online=False, force_update=False):
    is_valid, msg = validate_source_schema(source_data)
    if not is_valid:
        print(f"ERROR: {msg}")
        return False

    url_verified = False
    if verify_online:
        print(f"Performing live URL check for: {source_data['url']}")
        ok, code, err = verify_url_live(source_data["url"])
        if not ok:
            print(f"ERROR: Live URL verification failed (Code: {code}, Error: {err})")
            print("Aborting ingestion: Source must be accessible to be marked verified.")
            return False
        url_verified = True
        source_data["http_status"] = 200
        source_data["retrieval_status"] = "accessible"
        source_data["access_date"] = date.today().isoformat()
        print("Live URL check: HTTP 200 OK")

    sources = load_json(SOURCES_FILE) if SOURCES_FILE.exists() else []
    existing_idx = next((i for i, s in enumerate(sources) if s["id"] == source_data["id"]), None)

    if existing_idx is not None and not force_update:
        print(f"WARNING: Source {source_data['id']} already exists in registry. Use --update to overwrite.")
        return False

    if existing_idx is not None:
        sources[existing_idx] = source_data
        print(f"Updating existing source record for {source_data['id']}.")
    else:
        sources.append(source_data)
        print(f"Adding new source record for {source_data['id']}.")

    save_json(SOURCES_FILE, sources)

    card_stem = get_canonical_card_name(source_data["id"], source_data["title"])
    json_card_path = CARDS_DIR / f"{card_stem}.json"
    md_card_path = CARDS_DIR / f"{card_stem}.md"

    save_json(json_card_path, source_data)
    with open(md_card_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown_card(source_data))

    print(f"Wrote canonical source cards:\n  - {json_card_path.name}\n  - {md_card_path.name}")

    append_to_log(source_data, verified_live=url_verified)
    append_to_index(source_data, card_stem)

    print(f"\nSUCCESS: Source {source_data['id']} ingested and indexed cleanly.")
    print("\nNOTE: Automated ingestion handles metadata, cards, schemas, and indexing.")
    print("Extracting semantic claims, resolving contradictions, and writing synthesis pages")
    print("requires subsequent cognitive analysis conforming to schemas/claim.schema.json.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a source into AI Agents Learning Wiki.")
    parser.add_argument("--file", help="Path to JSON file containing source metadata.")
    parser.add_argument("--verify-online", action="store_true", help="Perform live HTTP GET check before ingestion.")
    parser.add_argument("--update", action="store_true", help="Allow updating an existing source ID.")
    args = parser.parse_args()

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"File not found: {args.file}")
            sys.exit(1)
        data = load_json(file_path)
        success = ingest_source(data, verify_online=args.verify_online, force_update=args.update)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
