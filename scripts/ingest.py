#!/usr/bin/env python3
"""
scripts/ingest.py - Incremental Source Ingestion Tool
Implements the Karpathy LLM Wiki INGEST operation:
Ingests new sources incrementally, validates metadata against schemas/source.schema.json,
generates raw source cards, updates the master registry, and appends to the chronological log.
"""

import os
import sys
import json
import argparse
import re
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw"
CARDS_DIR = RAW_DIR / "source-cards"
SOURCES_FILE = RAW_DIR / "sources.json"
SCHEMA_FILE = BASE_DIR / "schemas" / "source.schema.json"
LOG_FILE = BASE_DIR / "wiki" / "log.md"
INDEX_FILE = BASE_DIR / "wiki" / "index.md"

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

def validate_source(source_dict, schema_dict):
    required = schema_dict.get("required", [])
    for field in required:
        if field not in source_dict or not source_dict[field]:
            return False, f"Missing required field: '{field}'"
    # Validate ID pattern
    if not re.match(r"^S[0-9]{2,}$", source_dict.get("id", "")):
        return False, f"Invalid ID format: '{source_dict.get('id')}'. Must match ^S[0-9]{{2,}}$"
    return True, "Valid"

def append_to_log(source):
    today = date.today().isoformat()
    log_entry = f"""
## [{today}] ingest | {source['id']}: {source['title']}
- **Source ID:** {source['id']}
- **Publisher / Authors:** {', '.join(source.get('authors', [])) or source.get('publisher')}
- **URL:** {source['url']}
- **Document Type:** {source.get('document_type', 'unknown')}
- **Status:** Ingested and validated against schema.
"""
    if LOG_FILE.exists():
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"Appended ingestion entry to {LOG_FILE.name}")

def append_to_index(source):
    if not INDEX_FILE.exists():
        return
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if ID already in index
    if f"[{source['id']}]" in content:
        print(f"Source {source['id']} is already referenced in wiki/index.md")
        return
    
    entry_line = f"\n- **[{source['id']}] {source['title']}** — {source.get('publisher', 'Unknown')} ({source.get('publication_date', 'N/A')}). [Source Card](file:///raw/source-cards/{source['id']}-{slugify(source['title'][:30])}.md)"
    # Append right before Operating on the Wiki
    if "## Operating on the Wiki" in content:
        parts = content.split("## Operating on the Wiki")
        new_content = parts[0].rstrip() + "\n" + entry_line + "\n\n## Operating on the Wiki" + parts[1]
    else:
        new_content = content + "\n" + entry_line
        
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {INDEX_FILE.name} with source entry.")

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

def ingest_source(source_data, force_update=False):
    schema = load_json(SCHEMA_FILE)
    is_valid, err_msg = validate_source(source_data, schema)
    if not is_valid:
        print(f"ERROR: Schema validation failed: {err_msg}")
        return False

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

    # Save master sources registry
    save_json(SOURCES_FILE, sources)

    # Save individual source cards (JSON and MD)
    slug = slugify(source_data["title"][:30])
    json_card_path = CARDS_DIR / f"{source_data['id']}-{slug}.json"
    md_card_path = CARDS_DIR / f"{source_data['id']}-{slug}.md"

    save_json(json_card_path, source_data)
    with open(md_card_path, "w", encoding="utf-8") as f:
        f.write(generate_markdown_card(source_data))

    print(f"Generated source cards:\n  - {json_card_path.relative_to(BASE_DIR)}\n  - {md_card_path.relative_to(BASE_DIR)}")

    # Update Log and Index
    append_to_log(source_data)
    append_to_index(source_data)

    print(f"\nSUCCESS: Source {source_data['id']} successfully ingested into Wiki!")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a new source into the AI Agents Learning Wiki.")
    parser.add_argument("--file", help="Path to JSON file containing source metadata.")
    parser.add_argument("--update", action="store_true", help="Overwrite existing source if ID already exists.")
    args = parser.parse_args()

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"File not found: {args.file}")
            sys.exit(1)
        data = load_json(file_path)
        success = ingest_source(data, force_update=args.update)
        sys.exit(0 if success else 1)
    else:
        print("Incremental Ingest CLI:")
        print("Usage: python scripts/ingest.py --file <path_to_source.json> [--update]")
        print("Example: python scripts/ingest.py --file raw/source-cards/S01-react.json --update")
