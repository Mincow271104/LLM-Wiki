#!/usr/bin/env python3
"""
scripts/query.py - Local Search and Synthesis Engine for AI Agents Learning Wiki
Implements the Karpathy LLM Wiki QUERY operation:
Searches the Markdown index, Wiki pages, and Claims Registry without requiring
vector databases or external API keys.
"""

import os
import sys
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR = BASE_DIR / "raw"
CLAIMS_FILE = RAW_DIR / "claims.json"
SOURCES_FILE = RAW_DIR / "sources.json"

def load_claims():
    if not CLAIMS_FILE.exists():
        return []
    with open(CLAIMS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_sources():
    if not SOURCES_FILE.exists():
        return []
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def search_claims(query_tokens, claims):
    matched_claims = []
    for c in claims:
        text = f"{c.get('claim_id', '')} {c.get('statement', '')} {c.get('category', '')} {c.get('source_id', '')}".lower()
        score = sum(1 for token in query_tokens if token in text)
        if score > 0:
            matched_claims.append((score, c))
    matched_claims.sort(key=lambda x: x[0], reverse=True)
    return [c for score, c in matched_claims]

def search_wiki_pages(query_tokens):
    matched_pages = []
    for md_file in WIKI_DIR.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else md_file.name
                lower_content = content.lower()
                score = sum(1 for token in query_tokens if token in lower_content)
                if score > 0:
                    # Find snippet around first match
                    first_pos = -1
                    matched_token = ""
                    for token in query_tokens:
                        pos = lower_content.find(token)
                        if pos != -1 and (first_pos == -1 or pos < first_pos):
                            first_pos = pos
                            matched_token = token
                    
                    snippet = ""
                    if first_pos != -1:
                        start = max(0, first_pos - 60)
                        end = min(len(content), first_pos + 140)
                        snippet = content[start:end].replace("\n", " ").strip()
                        snippet = f"...{snippet}..."
                    
                    rel_path = md_file.relative_to(BASE_DIR)
                    matched_pages.append((score, title, str(rel_path), snippet))
        except Exception as e:
            continue
    matched_pages.sort(key=lambda x: x[0], reverse=True)
    return matched_pages

def query_wiki(query_str):
    print("=" * 75)
    print(f"AI AGENTS LEARNING WIKI - SEARCH ENGINE")
    print(f"Query: \"{query_str}\"")
    print("=" * 75)
    
    tokens = [t.lower().strip() for t in query_str.split() if len(t) > 2]
    if not tokens:
        print("Please provide a search query with terms longer than 2 characters.")
        return

    claims = load_claims()
    sources = load_sources()
    source_map = {s["id"]: s for s in sources}
    
    # 1. Matched Claims
    matched_claims = search_claims(tokens, claims)
    print(f"\n[1] MATCHED FACTUAL CLAIMS ({len(matched_claims)} found):")
    if matched_claims:
        for c in matched_claims[:5]:
            src_info = source_map.get(c['source_id'], {})
            src_title = src_info.get('title', 'Unknown Source')
            print(f"  * [{c['claim_id']}] ({c['source_id']}: {c['locator']}) [{c['claim_type']}]")
            print(f"    Statement: {c['statement']}")
            if c.get("disagreement_with"):
                print(f"    Notice: Differs with {c['disagreement_with']}: {c.get('disagreement_notes')}")
            print(f"    Source: {src_title}")
            print()
    else:
        print("  No direct claims matched the search terms.")

    # 2. Matched Wiki Pages
    matched_pages = search_wiki_pages(tokens)
    print(f"\n[2] MATCHED WIKI KNOWLEDGE PAGES ({len(matched_pages)} found):")
    if matched_pages:
        for score, title, path, snippet in matched_pages[:6]:
            print(f"  * {title} (Relevance Score: {score})")
            print(f"    Path: {path}")
            print(f"    Snippet: {snippet}")
            print()
    else:
        print("  No Wiki pages matched the query.")
        
    print("=" * 75)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_text = " ".join(sys.argv[1:])
    else:
        query_text = "ReAct loop reasoning and acting"
    query_wiki(query_text)
