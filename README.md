# AI Agents Learning Wiki

**Project:** AI Agents: Concepts, Architecture and Workflow  
**Audience:** AI beginners  
**Language:** English  
**Purpose:** A source-grounded, incrementally maintainable LLM Wiki that will serve as the knowledge base for an interactive teaching presentation.

## Project goals

1. Explain AI Agents from fundamentals through practical implementation.
2. Preserve source provenance and cite important claims.
3. Support incremental source ingestion, Wiki querying, and quality checks.
4. Generate a teaching-oriented HTML presentation using the Wiki as its knowledge source.
5. Document the workflow, actual execution evidence, and reflection.

## Planned repository structure

The implementation agent should preserve and extend this structure as needed:

- `raw/`: immutable source records and permitted source copies.
- `wiki/`: linked Markdown knowledge pages and indexes.
- `schemas/`: machine-readable source and claim schemas.
- `scripts/`: ingestion, query, and Wiki lint utilities.
- `workflow/`: Graph definition, prompts, and workflow explanation.
- `presentation/`: final HTML teaching slides and local assets.
- `reports/`: source ingestion, execution, validation, and reflection reports.
- `docs/`: supporting documentation.

## Required Wiki operations

- **Ingest:** retrieve and inspect a source, record provenance, extract supported evidence, update relevant Wiki pages, and append an ingestion log.
- **Query:** retrieve relevant Wiki pages and answer with traceable source references.
- **Lint:** detect invalid source IDs, missing citations, broken Wiki links, missing required topics, and unresolved contradictions.

## Source policy

Use the approved source list and record the actual retrieval and ingestion status for every item. A listed URL is not proof that a source was successfully ingested. Never fabricate source metadata, quotations, publication dates, or test results.

Do not copy or redistribute complete copyrighted works without permission. Store bibliographic metadata, links, concise notes, and permitted excerpts instead.

## Initial source plan

| ID | Source | URL |
|---|---|---|
| S01 | ReAct: Synergizing Reasoning and Acting in Language Models | https://arxiv.org/abs/2210.03629 |
| S02 | Toolformer: Language Models Can Teach Themselves to Use Tools | https://arxiv.org/abs/2302.04761 |
| S03 | Anthropic: Building Effective Agents | https://www.anthropic.com/engineering/building-effective-agents |
| S04 | Google Cloud: Choose your agentic AI architecture components | https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components |
| S05 | OpenAI Agents SDK guide | https://developers.openai.com/api/docs/guides/agents/sdk |
| S06 | LangGraph overview | https://docs.langchain.com/oss/python/langgraph/overview |
| S07 | CrewAI repository and documentation | https://github.com/crewAIInc/crewAI |
| S08 | Microsoft Agent Framework overview | https://learn.microsoft.com/en-us/agent-framework/overview |

**Methodology reference (not counted as a topic source):** Andrej Karpathy, LLM Wiki — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

AutoGen may be discussed for historical context, but its archived/maintenance status must be verified from current official sources before making claims about its successor or recommendation status.

## Definition of done

- At least five sources are genuinely retrieved and ingested.
- Source records contain verifiable metadata and retrieval status.
- Wiki pages are interconnected and cite evidence.
- Ingestion, query, and lint procedures are documented and runnable where feasible.
- A workflow Graph and its retry/return paths are documented.
- The HTML presentation uses the Wiki as its declared knowledge source.
- Execution and validation reports contain actual results.
- Reflection describes observed issues and workflow changes honestly.
- No secrets or private credentials are committed.

## Status

This README is a project starting point. Update it with actual implementation details, commands, test results, and the final published links after execution.