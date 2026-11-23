# Academic Assignment Submission: AI Agents Learning Wiki

## 1. Project Identification & Web Resources
- **Project Title:** AI Agents: Concepts, Architecture, and Workflow — An LLM-Maintained Knowledge Base and Interactive Teaching Presentation
- **Official GitHub Repository:** [https://github.com/Mincow271104/LLM-Wiki](https://github.com/Mincow271104/LLM-Wiki)
- **Live Interactive Presentation (GitHub Pages):** [https://mincow271104.github.io/LLM-Wiki/](https://mincow271104.github.io/LLM-Wiki/)
- **Default Branch:** `main`

---

## 2. Student & Academic Institution Information
- **Institution:** National Chin-Yi University of Technology (NCUT)
- **Department:** Department of Computer Science and Information Engineering (CSIE)
- **Course Title:** [Course Name / e.g., Agentic AI & Advanced Language Models]
- **Student Name:** [Student Name / NCUT CSIE]
- **Student ID:** [Student ID / e.g., 3A... / 4A...]
- **Academic Advisor / Instructor:** [Instructor Name]
- **Submission Date:** November 24, 2026

---

## 3. Executive Abstract & Pedagogical Philosophy
This project delivers an authoritative, persistent **LLM Wiki** and a companion **12-slide interactive teaching presentation** exploring the theoretical foundations, architectural mechanisms, and practical workflows of agentic artificial intelligence. Tailored specifically for AI beginners, the curriculum bridges the conceptual gap between passive text-generating chatbots and autonomous problem-solving agents.

Following the methodology formalized by Andrej Karpathy (2026), the repository implements a strict three-layer knowledge architecture:
1. **Layer A — Immutable Evidence (`raw/`):** 8 canonical primary sources (`S01`–`S08`), bibliographic source cards, and a machine-validated registry of 18 empirical claims (`raw/claims.json`).
2. **Layer B — Synthesized Knowledge (`wiki/`):** 21 comprehensive conceptual articles across 6 domains, an evidence registry documenting 4 major architectural debates, a master glossary, and an append-only audit log.
3. **Layer C — Machine Validation Schemas (`schemas/`):** Formal JSON Schema specifications (`source.schema.json`, `claim.schema.json`) enforced by an automated 15-pass integrity linter (`scripts/lint_wiki.py`).

---

## 4. Key Deliverables & Architecture Overview

### A. The 12-Slide Interactive Teaching Presentation (`presentation/`)
Hosted natively on GitHub Pages, the presentation features:
- **Slide 01:** Title & Learning Objectives (Executive overview, navigation keymap, and 5 learning objectives).
- **Slide 02:** What Is an AI Agent? (Perception-Reasoning-Action-Feedback formula; Recipe Reader vs Executive Chef analogy).
- **Slide 03:** AI Agent vs. Traditional Chatbot (5-dimension comparative matrix covering objective, execution, agency, error handling, and memory).
- **Slide 04:** Core Agent Architecture (Responsive inline SVG diagram illustrating Foundation Model, Instructions, Tools, Memory, Environment, and Runtime).
- **Slide 05:** Planning and Reasoning (Task Decomposition, Plan-and-Solve, and Self-Reflection loops).
- **Slide 06:** Memory and Context (Short-term working context window vs long-term vector/key-value storage backends).
- **Slide 07:** Tools and Function Calling (4-step tool execution cycle, JSON Schema definitions, and Model Context Protocol).
- **Slide 08:** The ReAct Pattern (Tripartite `Thought -> Action -> Observation` cycle with a verified search/calculation trace).
- **Slide 09:** Agent Loops vs. Graph Orchestration (DAG workflows vs cyclic loops vs LangGraph state graphs; documenting the Anthropic/LangChain architectural debate).
- **Slide 10:** Single-Agent vs. Multi-Agent Systems (Specialization, sequential pipelines, supervisor routers, and peer handoffs).
- **Slide 11:** Frameworks & Python Implementation (Comparative matrix of OpenAI SDK, LangGraph, CrewAI, and MS Agent Framework; educational simulated loop vs production LLM pattern).
- **Slide 12:** Evaluation, Safety & Future Horizons (SWE-bench, GAIA, prompt injection guardrails, sandboxing, and core beginner takeaways).

### B. Automated Testing & Verification Suite
- **15-Pass Knowledge Linter (`scripts/lint_wiki.py`):** Runs `jsonschema` validation, checks source integrity, verifies live URLs (HTTP 200), validates non-empty locators, resolves 429 relative links, rejects non-portable paths, and verifies citation coverage.
- **Headless Browser Test Suite (`scripts/test_presentation.py`):** Executes Playwright Chromium tests across Desktop (1366x768) and Mobile (390x844) viewports. Asserts 0 console errors, 0 uncaught exceptions, and captures 6 visual evidence screenshots in `reports/evidence/`.
- **Controlled Negative Test Suite (`scripts/run_negative_tests.py`):** Injects 5 deliberate failure scenarios (missing locator, invalid source ID, non-portable link, schema violation, slide count mismatch) to prove the testing framework never emits false passes.
- **Audit Reports (`reports/`):** Includes the independent fidelity review (`fidelity-review.md`), execution log (`execution-log.md`), engineering reflection (`reflection.md`), and final validation summary (`final-validation-report.md`).

---

## 5. Curriculum & Source Coverage Summary

### Primary Sources Ingested:
1. `S01`: *ReAct: Synergizing Reasoning and Acting in Language Models* (Yao et al., ArXiv:2210.03629)
2. `S02`: *Toolformer: Language Models Can Teach Themselves to Use Tools* (Schick et al., ArXiv:2302.04761)
3. `S03`: *Building Effective Agents* (Anthropic Engineering Guide)
4. `S04`: *Choose your agentic AI architecture components* (Google Cloud Architecture)
5. `S05`: *Agents SDK Documentation* (OpenAI Developers)
6. `S06`: *LangGraph Overview & Persistence* (LangChain Documentation)
7. `S07`: *CrewAI Multi-Agent Framework* (CrewAI Inc.)
8. `S08`: *Microsoft Agent Framework Overview* (Microsoft Learn)

### Documented Architectural Disagreements Preserved:
1. **Workflows vs Agents (`CLM-008` vs `CLM-014`):** Anthropic's strict code-directed workflow preference vs. LangGraph's unified state graph architecture.
2. **Dynamic Interleaving vs Upfront Planning (`CLM-006` vs `CLM-011`):** Step-by-step ReAct loop vs. global Plan-and-Solve roadmaps.
3. **Memory Architectures (`CLM-004` vs `CLM-005`):** Bounded working context buffers vs. external vector/KV persistence tiers.
4. **Multi-Agent Coordination (`CLM-012` vs `CLM-016` / `CLM-017`):** Role-playing crew choreography vs. enterprise unified governance and AutoGen evolution.

---

## 6. Reproducibility & Verification Instructions

### 1. Environment Setup
```bash
git clone https://github.com/Mincow271104/LLM-Wiki.git
cd LLM-Wiki
pip install jsonschema playwright
playwright install chromium
```

### 2. Execute Automated Quality Linter
```bash
python scripts/lint_wiki.py --verify-live-urls
```
*Expected Result:* 15 Passed | 0 Failed | 0 Warnings.

### 3. Run Browser Testing & Screenshot Capture
```bash
python scripts/test_presentation.py
```
*Expected Result:* All presentation browser tests passed with 0 console errors and 0 uncaught exceptions. Screenshots saved to `reports/evidence/`.

### 4. Run Controlled Negative Tests
```bash
python scripts/run_negative_tests.py
```
*Expected Result:* All 5 negative test conditions correctly detected and rejected.

### 5. Query the Knowledge Base via CLI
```bash
python scripts/query.py "What is the ReAct pattern?"
python scripts/query.py "How does LangGraph differ from traditional workflows?"
```
