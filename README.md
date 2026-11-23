# AI Agents Learning Wiki

[![Wiki Lint Status](https://img.shields.io/badge/Wiki_Lint-11%2F11_PASS-brightgreen)](reports/wiki-lint-report.md)
[![Methodology](https://img.shields.io/badge/Architecture-Karpathy_LLM_Wiki-blue)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
[![Target Branch](https://img.shields.io/badge/Branch-main-orange)](https://github.com/Mincow271104/LLM-Wiki)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

**Project:** AI Agents: Concepts, Architecture and Workflow  
**Audience:** AI beginners with limited or no prior knowledge of AI Agents
**Language:** English  
**Purpose:** An authoritative, source-grounded, incrementally maintainable LLM Wiki that serves as the permanent knowledge base for an interactive teaching presentation.

---

## 1. Project Goals

1. **Explain AI Agents comprehensively:** From foundational definitions and LLM mechanics through cognitive architectures, memory, tools, orchestration, multi-agent systems, evaluation, and safety.
2. **Preserve source provenance & claim-level attribution:** Every important factual statement is backed by verifiable primary source evidence with traceable locators (`[S0x, Section ...]`).
3. **Support incremental Wiki operations:** Implement runnable CLI tools for Ingest, Query, and Lint following Andrej Karpathy's LLM Wiki methodology.
4. **Serve as knowledge base for teaching presentation:** Maintain an interlinked, rigorously verified markdown repository that will power the Phase P3 educational HTML presentation.
5. **Document workflow and real execution evidence:** Record actual retrieval results, execution logs, and honest contradiction registrations without fabricated tests or claims.

---

## 2. Karpathy LLM Wiki Architecture

Following Andrej Karpathy's LLM Wiki paradigm, this repository maintains a clean three-layer separation:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AI AGENTS LEARNING WIKI                         │
├────────────────────────────────────────────────────────────────────────┤
│ Layer A: Raw Sources (raw/)                                            │
│   Immutable source records, verified source cards (S01..S08), claims   │
├────────────────────────────────────────────────────────────────────────┤
│ Layer B: The Wiki (wiki/)                                              │
│   Interlinked Markdown knowledge pages, navigation index, audit log    │
├────────────────────────────────────────────────────────────────────────┤
│ Layer C: Schema & Operations (schemas/, scripts/, AGENTS.md)           │
│   JSON validation schemas, Ingest, Query, and Lint automation tools    │
└────────────────────────────────────────────────────────────────────────┘
```

### Core Wiki Operations
- **Ingest (`scripts/ingest.py`):** Retrieve and inspect a source, record provenance, extract supported evidence, update relevant Wiki pages, update index, and append to the chronological log.
- **Query (`scripts/query.py`):** Search the Markdown index and claims registry to answer questions with traceable source references without requiring complex vector databases.
- **Lint (`scripts/lint_wiki.py`):** Comprehensive automated audit checking source IDs, claim evidence, broken Markdown links, required topic coverage, and registered contradictions.

---

## 3. Curated Source Collection & Policy

All factual assertions in this Wiki are backed by eight verified primary sources:

| ID | Title | Publisher / Authors | Verified URL | Status |
| :---: | :--- | :--- | :--- | :---: |
| **S01** | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao et al. (Princeton / Google Brain) | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) | Verified (HTTP 200) |
| **S02** | Toolformer: Language Models Can Teach Themselves to Use Tools | Timo Schick et al. (Meta AI) | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) | Verified (HTTP 200) |
| **S03** | Building Effective Agents | Anthropic (Erik Schluntz & Barry Zhang) | [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents) | Verified (HTTP 200) |
| **S04** | Choose your agentic AI architecture components | Google Cloud Architecture Center | [docs.cloud.google.com](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components) | Verified (HTTP 200) |
| **S05** | Agents SDK | OpenAI Developer Platform Team | [developers.openai.com](https://developers.openai.com/api/docs/guides/agents/sdk) | Verified (HTTP 200) |
| **S06** | LangGraph Overview | LangChain Engineering Team | [docs.langchain.com](https://docs.langchain.com/oss/python/langgraph/overview) | Verified (HTTP 200) |
| **S07** | CrewAI Documentation & Repository | CrewAI Inc. (João Moura) | [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Verified (HTTP 200) |
| **S08** | Microsoft Agent Framework Overview | Microsoft Learn AI Team | [learn.microsoft.com](https://learn.microsoft.com/en-us/agent-framework/overview) | Verified (HTTP 200) |

- **Methodology Reference (Not a topic source):** [Andrej Karpathy - LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (Verified HTTP 200).
- **Source Policy:** Do not republish complete copyrighted articles without permission. Store bibliographic metadata, links, concise summaries, and permitted fair-use excerpts.
- **Historical Context on AutoGen:** AutoGen 0.2 has transitioned into legacy/maintenance status. As documented in S08, the Microsoft Agent Framework is the unified next-generation enterprise successor.

---

## 4. Wiki Navigation Map

Explore the interlinked knowledge base across six core domains:

- **Central Navigation Index:** [wiki/index.md](wiki/index.md)
- **Executive Overview & Roadmap:** [wiki/overview.md](wiki/overview.md)
- **Terminology Glossary:** [wiki/glossary.md](wiki/glossary.md)
- **Evidence & Disagreement Registry:** [wiki/evidence-registry.md](wiki/evidence-registry.md)
- **Chronological Operation Log:** [wiki/log.md](wiki/log.md)

### Curriculum Modules:
1. **Fundamentals:**
   - [What is an AI Agent?](wiki/fundamentals/what-is-an-agent.md) — Core definition, autonomy spectrum, and the simplicity rule.
   - [AI Agents vs. Traditional Chatbots](wiki/fundamentals/agents-vs-chatbots.md) — Passive text responders vs. active environment mutation.
   - [LLM Foundations for Agents](wiki/fundamentals/llm-foundations.md) — Autoregressive generation, context dynamics, function calling.
2. **Architecture:**
   - [Agent Architecture Stack](wiki/architecture/agent-architecture.md) — The Augmented LLM building block and enterprise multi-tier stack.
   - [Memory and Context Management](wiki/architecture/memory-and-context.md) — Short-term context buffers vs. long-term persistent storage.
   - [Tools and Function Calling](wiki/architecture/tools-and-function-calling.md) — Actuators, Toolformer lineage, JSON Schema, MCP standard, tool bloat.
   - [The Agent Loop](wiki/architecture/agent-loop.md) — Sense-Think-Act-Observe cycle, bounded iteration, and termination criteria.
3. **Concepts & Orchestration:**
   - [Planning and Reasoning](wiki/concepts/planning-and-reasoning.md) — Task decomposition, Plan-and-Solve, reflection loops.
   - [The ReAct Pattern](wiki/concepts/react-pattern.md) — Interleaved `Thought → Action → Observation` to eliminate hallucination.
   - [Workflows vs. Autonomous Agents](wiki/concepts/workflows-vs-agents.md) — 5 canonical workflow patterns vs. autonomous agent feedback loops.
   - [Graph-Based Orchestration](wiki/concepts/graph-orchestration.md) — State, Nodes, Edges, checkpointers, durable execution, time-travel debugging.
   - [Single-Agent Systems](wiki/concepts/single-agent-systems.md) — Unified context execution, cognitive limits, and architectural boundaries.
   - [Multi-Agent Systems](wiki/concepts/multi-agent-systems.md) — Collaboration topologies: sequential, supervisor, handoffs.
4. **Frameworks & AutoGen Transition:**
   - [Comprehensive Framework Comparison](wiki/frameworks/comparison.md) — Side-by-side comparative matrix.
   - [OpenAI Agents SDK Deep Dive](wiki/frameworks/openai-agents-sdk.md) — Minimal agent encapsulation, hand-offs, guardrails.
   - [LangGraph Deep Dive](wiki/frameworks/langgraph.md) — Low-level state graphs, persistence, interrupts, streaming.
   - [CrewAI Deep Dive](wiki/frameworks/crewai.md) — Role-playing agents (`role`, `goal`, `backstory`), sequential/hierarchical processes.
   - [Microsoft Agent Framework Deep Dive](wiki/frameworks/microsoft-agent-framework.md) — AutoGen & Semantic Kernel unification, Harness Agent.
5. **Practical Implementation:**
   - [Educational Python Agent Example](wiki/implementation/python-agent-example.md) — Fully runnable zero-dependency ReAct agent loop in pure standard Python.
6. **Safety, Evaluation & Limitations:**
   - [Agent Evaluation and Benchmarking](wiki/safety/evaluation.md) — Task success rate, trajectory efficiency, benchmarks (HotpotQA, ALFWorld).
   - [Safety, Guardrails, and Limitations](wiki/safety/safety-and-limitations.md) — Prompt injection defense, sandboxing, least privilege, compounding failure math.

---

## 5. Practical CLI Operations

The repository includes standard Python utilities in `scripts/` requiring no paid API keys:

### 1. Run Quality & Integrity Checks (Lint)
Audit schemas, link resolution, claim citations, topic coverage, and registered contradictions:
```bash
python scripts/lint_wiki.py
```
*Outputs execution results to `reports/wiki-lint-report.md`.*

### 2. Query the Knowledge Base (Search & Grounding)
Retrieve matched claims and relevant Markdown pages for any technical query:
```bash
python scripts/query.py "How does ReAct prevent hallucinations?"
```

### 3. Ingest a New Source Incrementally
Add a new paper or specification adhering to `schemas/source.schema.json` without rebuilding the Wiki:
```bash
python scripts/ingest.py --file raw/source-cards/S01-react.json --update
```

---

## 6. Definition of Done & Phase Status

- [x] **8/8 primary sources** retrieved, inspected, verified, and ingested.
- [x] **18/18 factual claims** registered with verified section locators and cross-referenced disagreements.
- [x] **24/24 knowledge pages** authored with structured headings, citations, and interlinks.
- [x] **11/11 automated lint checks** passing with zero defects.
- [x] **Zero secrets or private credentials** committed.
- [x] **Strict Phase Boundary:** Phases P1 and P2 complete. Phase P3 (HTML presentation) deferred until Project Manager review.

---

## 7. Future HTML Presentation & Publishing Plan

- **Presentation Location:** In Phase P3 (following Project Manager approval), an interactive 10–12 slide HTML presentation will be authored in `presentation/index.html`.
- **GitHub Pages Publishing:** The presentation deck and Wiki documentation will be deployed to GitHub Pages from the `main` or `gh-pages` branch for open educational access.
