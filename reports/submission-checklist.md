# Assignment Submission Checklist & Verification Audit

## 1. Moodle Submission Title Format
```text
[Assignment Submission] AI Agents: Concepts, Architecture and Workflow - NCUT CSIE - [Student ID] - [Student Name]
```

---

## 2. Comprehensive Deliverables Checklist

### Core Repository Files
- [x] `PROJECT_BRIEF.md`: Preserved from official repository initialization.
- [x] `AGENTS.md`: Operating schema, academic rules, traceable citation conventions, governance.
- [x] `README.md`: Student onboarding, curriculum roadmap, CLI instructions, GitHub Pages link.
- [x] `SUBMISSION.md`: Formal assignment package covering all 6 instructor requirements and NCUT CSIE placeholders.
- [x] `.env.example`: Safe environment configuration template with zero exposed credentials.
- [x] `.gitignore`: Excludes virtual environments, Python caches, temporary scratch files, and nested repos.

### Layer A: Immutable Raw Layer (`raw/`)
- [x] `raw/README.md`: Provenance rules, immutability guidelines, and citation standards.
- [x] `raw/sources.json`: 8 approved primary sources (`S01` through `S08`), valid against `source.schema.json`.
- [x] `raw/claims.json`: 18 primary empirical claims (`CLM-001` through `CLM-018`), valid against `claim.schema.json`.
- [x] `raw/source-cards/`: Exactly 16 canonical files (8 JSON + 8 Markdown pairs) with unique IDs and slugs.

### Layer B: Synthesized Knowledge Base (`wiki/`)
- [x] `wiki/index.md`: Central navigation directory, curriculum roadmap, and source cross-index.
- [x] `wiki/overview.md`: Executive summary of agentic AI concepts and learning pathway.
- [x] `wiki/glossary.md`: Academic terminology definitions with exact source citations.
- [x] `wiki/evidence-registry.md`: Claim mapping, evidence grounding, and 4 documented architectural debates.
- [x] `wiki/log.md`: Chronological append-only record of ingestion and curation events.
- [x] `wiki/fundamentals/`: 3 modules (What is an Agent, Agents vs Chatbots, LLM Foundations).
- [x] `wiki/architecture/`: 4 modules (Agent Architecture, Agent Loop, Memory & Context, Tools & Functions).
- [x] `wiki/concepts/`: 5 modules (Planning & Reasoning, ReAct, Workflows vs Agents, Single-Agent, Multi-Agent).
- [x] `wiki/frameworks/`: 5 modules (OpenAI SDK, LangGraph, CrewAI, MS Agent Framework, Comparison).
- [x] `wiki/implementation/`: 1 educational module (Python Agent Example).
- [x] `wiki/safety/`: 2 modules (Evaluation & Benchmarks, Safety & Limitations).

### Layer C: Machine-Readable Schemas (`schemas/`)
- [x] `schemas/source.schema.json`: Formal JSON Schema for source records.
- [x] `schemas/claim.schema.json`: Formal JSON Schema for empirical claims and contradiction links.

### Interactive Presentation Layer (`presentation/`)
- [x] `presentation/index.html`: Complete 12-slide educational deck with inline SVG diagram, comparative tables, and ReAct loop.
- [x] `presentation/styles.css`: Responsive Academic Slate styling, card components, and mobile layout.
- [x] `presentation/slides.js`: Keyboard navigation, touch gestures, dynamic progress bar, and slide directory modal.
- [x] `presentation/assets/`: Presentation assets directory.

### Automation Tooling (`scripts/`)
- [x] `scripts/lint_wiki.py`: 15-pass automated integrity linter (`jsonschema`, live URLs, link resolution).
- [x] `scripts/ingest.py`: Incremental ingestion CLI tool with canonical slug enforcement.
- [x] `scripts/query.py`: Search and retrieval engine for terminal exploration.
- [x] `scripts/test_presentation.py`: Playwright Chromium test runner for headless verification and screenshot capture.
- [x] `scripts/run_negative_tests.py`: Controlled negative test suite injecting 5 deliberate failure scenarios.

### Workflow & Governance (`workflow/`)
- [x] `workflow/graph.mmd`: 10-stage presentation generation graph showing DAG flow and cyclic loops (max 3 retries).
- [x] `workflow/graph.md`: Formal specification of the 10 stages, verification gates, and telemetry.
- [x] `workflow/build-teaching-slides.md`: Step-by-step reproduction guide.
- [x] `workflow/prompts/fidelity-review-prompt.md`: Operational prompt for auditing slide citation fidelity.
- [x] `workflow/prompts/ingest-prompt.md`, `lint-prompt.md`, `query-prompt.md`: Operational prompt templates.

### Continuous Deployment (`.github/workflows/`)
- [x] `.github/workflows/deploy-pages.yml`: Automated GitHub Pages deployment pipeline.

### Quality Reports & Evidence (`reports/`)
- [x] `reports/fidelity-review.md`: Complete Slide $\to$ Claim $\to$ Wiki $\to$ Source mapping and audit verdict.
- [x] `reports/execution-log.md`: Chronological engineering log of Batch 1 and Batch 2.
- [x] `reports/reflection.md`: In-depth analysis answering all 6 mandatory architectural questions.
- [x] `reports/final-validation-report.md`: Complete summary of 15-pass linter, Playwright tests, and negative tests.
- [x] `reports/wiki-lint-report.md`: Real execution output of 15-pass linter.
- [x] `reports/evidence/`: 6 high-resolution PNG screenshots verifying desktop and mobile presentation rendering.

---

## 3. Final Verification Sign-Off
- **Status:** **ALL DELIVERABLES READY FOR SUBMISSION**
- **Git State:** Clean working tree, official clone at `E:\HƯ`, remote tracking `origin/main`.
