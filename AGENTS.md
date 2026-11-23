# AGENTS.md: Project Instruction Manual & Operating Schema

## 1. Project Purpose & Philosophy
This repository implements an authoritative, persistent **LLM Wiki** on **"AI Agents: Concepts, Architecture, and Workflow"**, following the methodology outlined by Andrej Karpathy (2026). The Wiki serves as a structured, compounded knowledge base designed for AI beginners with limited or no prior background in agentic AI, while providing rigorous architectural clarity and educational Python implementations.

In Karpathy's architecture:
- **Raw Sources (`raw/`):** Immutable primary evidence.
- **The Wiki (`wiki/`):** Synthesized, interlinked Markdown knowledge layer maintained by AI agents.
- **The Schema (`schemas/`, `AGENTS.md`):** Rules, constraints, and instructions ensuring consistent, disciplined agent maintenance.

---

## 2. Directory Responsibilities & Structure
```
LLM-Wiki/                       # Repository Root
├── AGENTS.md                   # AI Agent operating manual & governance instructions
├── README.md                   # User-facing onboarding, navigation, and CLI guide
├── .gitignore                  # Git exclusions (private keys, scratch, cache)
├── .env.example                # Safe environment variable configuration template
│
├── raw/                        # LAYER A: Immutable raw source records
│   ├── README.md               # Raw layer rules & provenance guidelines
│   ├── sources.json            # Master source registry (validates against source.schema.json)
│   ├── claims.json             # Master claim evidence registry (validates against claim.schema.json)
│   └── source-cards/           # Markdown and JSON source cards for S01..S08
│
├── wiki/                       # LAYER B: Synthesized knowledge base
│   ├── index.md                # Central navigation index & mental map
│   ├── log.md                  # Chronological append-only audit log
│   ├── overview.md             # Executive overview & learning roadmap
│   ├── glossary.md             # Standardized academic terminology definitions
│   ├── evidence-registry.md    # Claim mapping & contradiction register
│   ├── fundamentals/           # Core beginner concepts (what is an agent, chatbots, LLM base)
│   ├── architecture/           # System components (stack, loop, memory, tools)
│   ├── concepts/               # Orchestration patterns (planning, ReAct, workflows, graphs, MAS)
│   ├── frameworks/             # Comparative analysis (OpenAI SDK, LangGraph, CrewAI, MS Agent Fwk)
│   ├── implementation/         # Educational Python agent implementations
│   └── safety/                 # Benchmarking, evaluation, guardrails, and limitations
│
├── schemas/                    # LAYER C: Machine-readable JSON validation schemas
│   ├── source.schema.json      # Schema for source metadata and status
│   └── claim.schema.json       # Schema for evidence claims and contradictions
│
├── workflow/                   # Workflow definitions and agent prompt templates
│   ├── graph.md                # Detailed orchestration graph specifications
│   ├── graph.mmd               # Mermaid visual workflow diagram
│   └── prompts/                # Ingest, query, and lint operational prompts
│
├── scripts/                    # Automation CLI tooling (Karpathy operations)
│   ├── ingest.py               # Incremental source ingestion tool
│   ├── query.py                # Keyword search and retrieval engine
│   └── lint_wiki.py            # Comprehensive 11-pass quality and integrity linter
│
├── reports/                    # Phase execution logs and validation artifacts
│   ├── requirements-summary.md # Comprehensive requirements analysis
│   ├── source-ingestion-report.md # Source-by-source retrieval and ingestion audit
│   ├── wiki-lint-report.md     # Real automated test execution report
│   └── implementation-log.md   # Chronological engineering log
│
└── docs/                       # Auxiliary documentation
    └── README.md               # Guide to project documentation and publishing
```

---

## 3. Agent Responsibilities & Rules of Engagement

1. **Academic English Exclusivity:** All documentation, Wiki articles, logs, source cards, and code comments must be written in clear, precise academic English.
2. **Never Fabricate Content:** Under no circumstances should an agent invent facts, fabricate author names, cite phantom page numbers, or create fictitious source cards. Every non-trivial assertion must have source evidence.
3. **Immutability of Raw Sources:** Never modify original source text files or historical source cards in `raw/` once verified.
4. **Incremental Ingestion:** When new sources are introduced, do not rebuild the entire Wiki. Perform incremental updates to affected concept pages, update `wiki/index.md`, and append an entry to `wiki/log.md`.
5. **Preserve Disagreements:** When sources present conflicting definitions (e.g., Anthropic's strict agent/workflow dichotomy vs. LangGraph's unified state graph), explicitly document both positions in `wiki/evidence-registry.md`. Never silently merge contradictory positions.

---

## 4. Naming & Citation Conventions

### Naming Conventions:
- **Source IDs:** `S` followed by a two-digit zero-padded number (`S01`, `S02`, ..., `S08`).
- **Claim IDs:** `CLM-` followed by a three-digit zero-padded number (`CLM-001`, `CLM-002`, ...).
- **Filenames:** Lowercase kebab-case (`react-pattern.md`, `source.schema.json`).

### Traceable Citation Format:
In-text citations must use traceable brackets specifying the source ID and exact locator:
- `[S01, Section 2]`
- `[S03, What are agents?]`
- `[S04, Agent memory]`
- `[S05, Core concepts: Agents]`
- `[S06, Build with the Graph API]`
- `[S07, Core Concepts: Agents, Tasks, Crews]`
- `[S08, Why Agent Framework?]`

---

## 5. Standard Operating Protocols

### Protocol A: Ingest
1. Retrieve canonical source via HTTP. Verify status is 200.
2. Verify metadata (title, authors, publisher, date, section headings).
3. Validate against `schemas/source.schema.json`.
4. Generate `raw/source-cards/<ID>-<slug>.json` and `.md`.
5. Extract key claims to `raw/claims.json` and `wiki/evidence-registry.md`.
6. Update affected concept pages in `wiki/`.
7. Update `wiki/index.md` and append entry to `wiki/log.md`.
8. Execute `python scripts/lint_wiki.py` to confirm zero regressions.

### Protocol B: Query
1. Run `python scripts/query.py "<terms>"`.
2. Retrieve matched claims and relevant Markdown pages.
3. Synthesize beginner-friendly answers citing exact locators without hallucination.

### Protocol C: Lint
1. Execute `python scripts/lint_wiki.py`.
2. Ensure all 11 automated test passes succeed.
3. Output updated execution results to `reports/wiki-lint-report.md`.

---

## 6. Security and Git Governance

1. **No Hardcoded Secrets:** Never hardcode API keys, access tokens, or private credentials in scripts, Wiki pages, or tests.
2. **Environment Variable Configuration:** All optional cloud integrations must read from environment variables (see `.env.example`).
3. **No External Pushes:** Do not push to remote repositories during local assignment execution.
4. **Scope Isolation:** Modify only files inside this official repository workspace.
5. **Authorized Remote Operations:** Remote Git pushes are performed only when explicitly reviewed and authorized by the Project Manager.

---

## 7. Definition of Done (Phases P1 & P2)
A task within Phase P1 + P2 is marked **DONE** only when:
- [x] All 8 curated sources are verified and ingested.
- [x] All schemas (`source.schema.json`, `claim.schema.json`) validate.
- [x] All 21 required curriculum topics are covered in comprehensive Wiki pages.
- [x] Master index (`wiki/index.md`), glossary (`wiki/glossary.md`), and operation log (`wiki/log.md`) are current.
- [x] Contradiction and evidence registry (`wiki/evidence-registry.md`) is populated.
- [x] Automated linter (`scripts/lint_wiki.py`) runs and passes with zero failures.
- [x] Real execution logs and reports are saved in `reports/`.
- [x] Phase boundary respected: **HTML presentation is deferred until PM approval.**
