# Requirements Summary: AI Agents Learning Wiki (Phases P1 & P2)

## 1. Project Context & Objectives
- **Project Title:** AI Agents Learning Wiki
- **Target Audience:** AI Beginners with limited or no prior knowledge of AI agents.
- **Goal:** Build an authoritative, Karpathy-inspired persistent LLM Wiki that serves as a permanent knowledge base and foundation for an interactive educational HTML presentation in a subsequent phase.
- **Language Policy:** Strict academic English across all documentation, source cards, knowledge pages, and logs.
- **Execution Scope:** Phases P1 (Project Foundation & Documentation) and P2 (Source Ingestion & Wiki Construction). Phase P3 (HTML Presentation) is strictly deferred.

---

## 2. Requirement Verification Matrix

| Requirement Area | Specification | Implementation Artifact | Status |
| :--- | :--- | :--- | :---: |
| **Audience Level** | Beginner-friendly explanations with intermediate depth and Python code. | `wiki/overview.md`, `wiki/fundamentals/`, `wiki/implementation/` | **FULFILLED** |
| **Three-Layer Architecture** | Karpathy LLM Wiki pattern: Raw Sources, Wiki, Schema. | `raw/`, `wiki/`, `schemas/`, `AGENTS.md` | **FULFILLED** |
| **Source Collection** | Ingestion of 8 approved primary sources (S01–S08). | `raw/sources.json`, `raw/source-cards/` | **FULFILLED** |
| **Source Verification** | No fabricated sources; direct URL retrieval, HTTP 200, recorded access dates. | Network retrieval scripts, `raw/sources.json` | **FULFILLED** |
| **Claim-Level Traceability** | Factual statements must have traceable citations (`[S0x, Section ...]`). | `wiki/evidence-registry.md`, `raw/claims.json` | **FULFILLED** |
| **Disagreement Recording** | Explicitly record conflicting claims rather than silently merging. | Contradiction register in `wiki/evidence-registry.md` | **FULFILLED** |
| **Knowledge Coverage** | 21 required curriculum areas (Overview, Chatbot vs. Agent, ReAct, Graph Orchestration, etc.). | 24 content pages (21 topic articles plus 3 supporting pages) in `wiki/` (26 Markdown files total) | **FULFILLED** |
| **Framework Comparison** | OpenAI Agents SDK, LangGraph, CrewAI, MS Agent Fwk + AutoGen succession. | `wiki/frameworks/comparison.md` | **FULFILLED** |
| **Python Educational Code** | Runnable agent loop, no API key required, simulated vs. production distinction. | `wiki/implementation/python-agent-example.md` | **FULFILLED** |
| **Automated Quality Checks**| Runnable Python linter validating links, schemas, citations, and coverage. | `scripts/lint_wiki.py` (Current: 15/15 checks pass; Historical Phase P1/P2: 11/11) | **FULFILLED** |
| **Workflow Design** | Stateful graph with failure return paths, max 3 correction cycles, Mermaid diagram. | `workflow/graph.mmd`, `workflow/graph.md`, `prompts/` | **FULFILLED** |
| **Security & Governance** | No hardcoded keys, `.gitignore`, `.env.example`, no remote git push. | `.gitignore`, `.env.example`, local git init | **FULFILLED** |
| **Phase Boundary** | Complete P1 + P2 only; STOP and await PM approval before P3. | Maintained strict boundary. | **FULFILLED** |
