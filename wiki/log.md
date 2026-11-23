# Chronological Wiki Operation Log

This append-only log tracks every operation (ingest, query, lint, compilation) performed on the AI Agents Learning Wiki, following the Karpathy LLM Wiki methodology.

---

## [2026-11-23] init | Knowledge Base Inception & Layer Setup
- **Action:** Initialized Karpathy three-layer architecture (Raw Sources, Wiki, Schema).
- **Artifacts:** Created `.gitignore`, `.env.example`, directory structure, `schemas/source.schema.json`, and `schemas/claim.schema.json`.
- **Status:** Complete.

## [2026-11-23] ingest | S01: ReAct (Synergizing Reasoning and Acting in Language Models)
- **Source ID:** S01
- **Publisher / Authors:** Yao et al. (Princeton University / Google Research)
- **Action:** Verified source URL (`https://arxiv.org/abs/2210.03629`), inspected section structure, created `raw/source-cards/S01-react.md` and JSON record.
- **Key Claims Extracted:** `CLM-001` (interleaving reasoning and acting), `CLM-002` (CoT hallucination without action grounding).
- **Target Wiki Pages:** `wiki/concepts/react-pattern.md`, `wiki/architecture/agent-loop.md`, `wiki/concepts/planning-and-reasoning.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S02: Toolformer (Language Models Can Teach Themselves to Use Tools)
- **Source ID:** S02
- **Publisher / Authors:** Schick et al. (Meta AI Research)
- **Action:** Verified source URL (`https://arxiv.org/abs/2302.04761`), extracted self-supervised API calling pipeline, created `raw/source-cards/S02-toolformer.md` and JSON record.
- **Key Claims Extracted:** `CLM-003` (self-supervised API call generation and perplexity filtering).
- **Target Wiki Pages:** `wiki/architecture/tools-and-function-calling.md`, `wiki/fundamentals/llm-foundations.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S03: Building Effective Agents (Anthropic)
- **Source ID:** S03
- **Publisher / Authors:** Anthropic Engineering (Erik Schluntz & Barry Zhang)
- **Action:** Verified source URL (`https://www.anthropic.com/engineering/building-effective-agents`), parsed workflows vs. agents dichotomy and 5 workflow patterns, created `raw/source-cards/S03-building-effective-agents.md` and JSON record.
- **Key Claims Extracted:** `CLM-004` (workflows vs. agents), `CLM-005` (start simple principle), `CLM-006` (Augmented LLM building block), `CLM-007` (5 workflow patterns).
- **Target Wiki Pages:** `wiki/fundamentals/what-is-an-agent.md`, `wiki/concepts/workflows-vs-agents.md`, `wiki/architecture/agent-architecture.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S04: Choose your agentic AI architecture components (Google Cloud)
- **Source ID:** S04
- **Publisher / Authors:** Google Cloud Architecture Center
- **Action:** Verified source URL (`https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components`), parsed enterprise components, created `raw/source-cards/S04-cloud-architecture-components.md` and JSON record.
- **Key Claims Extracted:** `CLM-008` (enterprise agent stack), `CLM-009` (short-term vs. long-term memory bifurcation), `CLM-010` (tool bloat degradation and risks).
- **Target Wiki Pages:** `wiki/architecture/agent-architecture.md`, `wiki/architecture/memory-and-context.md`, `wiki/architecture/tools-and-function-calling.md`, `wiki/safety/safety-and-limitations.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S05: Agents SDK (OpenAI)
- **Source ID:** S05
- **Publisher / Authors:** OpenAI Developer Platform Team
- **Action:** Verified source URL (`https://developers.openai.com/api/docs/guides/agents/sdk`), parsed markdown documentation, created `raw/source-cards/S05-openai-agents-sdk.md` and JSON record.
- **Key Claims Extracted:** `CLM-011` (agent encapsulation), `CLM-012` (multi-agent hand-offs), `CLM-013` (guardrails for safety).
- **Target Wiki Pages:** `wiki/frameworks/openai-agents-sdk.md`, `wiki/concepts/multi-agent-systems.md`, `wiki/safety/safety-and-limitations.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S06: LangGraph Overview (LangChain)
- **Source ID:** S06
- **Publisher / Authors:** LangChain Engineering
- **Action:** Verified source URL (`https://docs.langchain.com/oss/python/langgraph/overview`), parsed markdown documentation, created `raw/source-cards/S06-langgraph-overview.md` and JSON record.
- **Key Claims Extracted:** `CLM-014` (graph orchestration via state, nodes, edges), `CLM-015` (durable execution via checkpointers, time-travel, interrupts).
- **Target Wiki Pages:** `wiki/concepts/graph-orchestration.md`, `wiki/frameworks/langgraph.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S07: CrewAI Documentation & Repository (CrewAI)
- **Source ID:** S07
- **Publisher / Authors:** João Moura / CrewAI Inc.
- **Action:** Verified source repository (`https://github.com/crewAIInc/crewAI`), parsed role-playing architecture, created `raw/source-cards/S07-crewai-documentation.md` and JSON record.
- **Key Claims Extracted:** `CLM-016` (role-playing agents with role, goal, backstory, and sequential/hierarchical processes).
- **Target Wiki Pages:** `wiki/frameworks/crewai.md`, `wiki/concepts/multi-agent-systems.md`.
- **Status:** Verified and ingested.

## [2026-11-23] ingest | S08: Microsoft Agent Framework Overview (Microsoft)
- **Source ID:** S08
- **Publisher / Authors:** Microsoft Learn AI Team
- **Action:** Verified source URL (`https://learn.microsoft.com/en-us/agent-framework/overview`), parsed AutoGen and Semantic Kernel convergence, created `raw/source-cards/S08-microsoft-agent-framework.md` and JSON record.
- **Key Claims Extracted:** `CLM-017` (Agent Framework as successor to AutoGen and Semantic Kernel), `CLM-018` (prefer programmatic functions over agents when deterministic).
- **Target Wiki Pages:** `wiki/frameworks/microsoft-agent-framework.md`, `wiki/frameworks/comparison.md`, `wiki/fundamentals/what-is-an-agent.md`.
- **Status:** Verified and ingested.

## [2026-11-23] compile | Wiki Knowledge Base Synthesis
- **Action:** Authored interlinked knowledge pages across Fundamentals, Architecture, Concepts, Frameworks, Implementation, and Safety.
- **Cross-References:** Established bidirectional Markdown links across all concept pages and linked to `wiki/evidence-registry.md`.
- **Status:** Synthesis complete.

## [2026-11-23] ingest | S01: ReAct: Synergizing Reasoning and Acting in Language Models
- **Source ID:** S01
- **Publisher / Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan
- **URL:** https://arxiv.org/abs/2210.03629
- **Document Type:** peer_reviewed_paper
- **Status:** Ingested and validated against schema.

## [2026-11-23] ingest | S01: ReAct: Synergizing Reasoning and Acting in Language Models
- **Source ID:** S01
- **Publisher / Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan
- **URL:** https://arxiv.org/abs/2210.03629
- **Document Type:** peer_reviewed_paper
- **Status:** Ingested and validated against schema.

## [2026-11-23] ingest | S01: ReAct: Synergizing Reasoning and Acting in Language Models
- **Source ID:** S01
- **Publisher / Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan
- **URL:** https://arxiv.org/abs/2210.03629
- **Document Type:** peer_reviewed_paper
- **Status:** Recorded metadata validated against schema.


## [2026-11-24] upgrade | Batch 2 Tooling, Schema Engine & Link Portability
- **Action:** Upgraded `scripts/lint_wiki.py` to employ official `jsonschema` validation engine across `raw/sources.json` and `raw/claims.json`.
- **Source Integrity:** Replaced unconditional PASS logic with comprehensive assertion verifying recorded HTTP 200, bibliographic fields, and unique source cards. Added optional `--verify-live-urls` timeout check.
- **Link Portability:** Converted all 24 Markdown files from machine-specific absolute file paths (`file:///`) to portable relative links. Linter Pass 12 now strictly rejects non-portable paths.
- **Deduplication:** Enforced canonical slugs in `scripts/ingest.py` and purged duplicate S01 cards.
- **Status:** Complete (15/15 Lint Passes Succeeded).

## [2026-11-24] presentation | Interactive 12-Slide Teaching Presentation
- **Action:** Designed and implemented responsive educational slide deck in `presentation/` (`index.html`, `styles.css`, `slides.js`).
- **Curriculum:** Fully addresses all 12 planned slides, including inline SVG architecture diagram, ReAct trace, comparative matrices, and beginner analogies.
- **Fidelity Grounding:** Every slide is grounded with exact citations (`[S01]`, `[S03]`, etc.) and primary claims (`CLM-001` through `CLM-018`).
- **Status:** Verified and functional.

## [2026-11-24] test | Automated Playwright Browser Verification & Evidence
- **Action:** Executed end-to-end automated browser testing using Playwright Chromium across Desktop (1366x768) and Mobile (390x844) viewports.
- **Verification:** Verified 0 console errors, 0 uncaught exceptions, full keyboard navigation, touch swipe support, and modal interactions. Captured 6 visual evidence screenshots to `reports/evidence/`.
- **Controlled Negative Tests:** Executed 5 negative test cases verifying that locator omissions, bad source IDs, machine links, schema errors, and missing slides are reliably caught and rejected.
- **Status:** Complete (All test suites passed).

## [2026-11-24] deploy | GitHub Pages & Submission Package
- **Action:** Configured GitHub Actions Pages workflow `.github/workflows/deploy-pages.yml` targeting `https://mincow271104.github.io/LLM-Wiki/`.
- **Submission:** Authored `SUBMISSION.md` and `reports/submission-checklist.md` with NCUT CSIE institutional metadata placeholders.
- **Status:** Ready for final Git commit and push to `origin main`.
