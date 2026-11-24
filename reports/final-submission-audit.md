# Final Academic Submission Audit Report
**Project:** AI Agents: Concepts, Architecture, and Workflow — An LLM-Maintained Knowledge Base and Interactive Teaching Presentation  
**Institution:** National Chin-Yi University of Technology (NCUT) — Department of Computer Science and Information Engineering (CSIE)  
**Student:** PHUONG KHANG MINH (Student ID: 4B517024)  
**Audit Date:** November 24, 2026  
**Auditor:** Senior Implementation Engineer  

---

## 1. Overall Readiness Status
**VERDICT: READY FOR FINAL SUBMISSION**

- **Six Instructor Requirements:** 100% Satisfied and Grounded in Repository Evidence.
- **Student Information:** University (NCUT), Student ID (4B517024), Department (CSIE / 資訊工程系), and Student Name (PHUONG KHANG MINH) verified and preserved.
- **GitHub Repository:** Unstaged local documentation modifications present on branch `main` at `https://github.com/Mincow271104/LLM-Wiki`; zero commits or pushes performed.
- **Live Interactive Presentation:** Deployed and operational on GitHub Pages at `https://mincow271104.github.io/LLM-Wiki/` (HTTP 200 OK verified).
- **Automated Verification:** 15/15 Linter Passes, Playwright Browser Suite (0 errors), 6 Visual Screenshots, and 5 Controlled Negative Tests verified.

---

## 2. What Was Automatically Completed by Agent
1. **Verified Student Metadata Integration:** Confirmed and preserved the student's personal information (`PHUONG KHANG MINH`, `4B517024`, `NCUT`, `CSIE`) in [SUBMISSION.md](../SUBMISSION.md).
2. **Metadata Synchronization:** Verified and embedded official URLs across all user-facing documentation ([README.md](../README.md), [SUBMISSION.md](../SUBMISSION.md), [submission-checklist.md](submission-checklist.md)).
3. **Teacher Reflection Questions Supplementation:** Rewrote [reflection.md](reflection.md) to directly answer the instructor's three questions:
   - *Node with highest error frequency:* Markdown Link Resolution / Portability in Stage 7 (qualitatively observed as the most repetitive troubleshooting check across development iterations; exact per-node numerical retry telemetry was not recorded).
   - *Left-shifted validation:* Canonical slug enforcement and source schema validation shifted upstream into the earlier source-ingestion process ([ingest.py](../scripts/ingest.py)), and authoring-time link portability guidelines into [AGENTS.md](../AGENTS.md). (Claim validation, locator checks, and link resolution remain enforced at Stage 7 in [lint_wiki.py](../scripts/lint_wiki.py)).
   - *Graph modification:* Expansion from Batch 1 linear 8-node pipeline to Batch 2 10-stage presentation-generation graph with 3 bounded cyclic loops: Loop A (Stage 7 &rarr; Stage 3), Loop B (Stage 8 &rarr; Stage 5), and Loop C (Stage 9 &rarr; Stage 3), with maximum 3 cycles per gate, supported by an offline supplementary negative test suite.
4. **Live Deployment Verification:** Tested GitHub Actions workflow run `45215603066` (`completed` / `success`) and validated live HTTP 200 response of `https://mincow271104.github.io/LLM-Wiki/`.
5. **Checklist Standardization:** Updated [submission-checklist.md](submission-checklist.md) to reflect all six requirements and the exact Moodle title ordering.

---

## 3. What Was Corrected
1. **Preserved Student Edits in `SUBMISSION.md`:** Ensured the student's manual update to [SUBMISSION.md](../SUBMISSION.md) (adding their name and student ID while removing unnecessary placeholders) was preserved without conflict or overwrite.
2. **Eliminated Optional Placeholders:** Removed optional placeholders for *Course Title* and *Academic Advisor / Instructor* from [SUBMISSION.md](../SUBMISSION.md), ensuring only mandatory academic fields remain.
3. **Regex False-Positive Fix:** Resolved a linter issue in [lint_wiki.py](../scripts/lint_wiki.py) where inline code examples formatted in backticks were matched as active markdown links.
4. **Standardized Moodle Title Ordering:** Corrected the title structure in the submission checklist to match the instructor's mandatory ordering: **School + Student ID + Department + Name + Topic**.
5. **Portability of Documentation Links:** Replaced local file URLs with valid repository-relative Markdown links throughout all audit documentation.

---

## 4. Manual Inputs Classification Table

| Field / Requirement | Current Value or Status | Supporting Evidence | Can Agent Complete It? | Student Action Required? | Classification |
|:---|:---|:---|:---:|:---:|:---:|
| **University / School** | National Chin-Yi University of Technology (NCUT) | Student prompt & [SUBMISSION.md](../SUBMISSION.md) | Yes (Completed) | No | **A (Completed)** |
| **Student ID** | `4B517024` | Student prompt & [SUBMISSION.md](../SUBMISSION.md) | Yes (Completed) | No | **A (Completed)** |
| **Department** | CSIE (Computer Science & Information Engineering) | Student prompt & [SUBMISSION.md](../SUBMISSION.md) | Yes (Completed) | No | **A (Completed)** |
| **Student Name** | `PHUONG KHANG MINH` | Student prompt & [SUBMISSION.md](../SUBMISSION.md) | Yes (Completed) | No | **A (Completed)** |
| **Class / Year (系級)** | Intentionally Omitted | Student explicitly confirmed class/year designation is not needed for submission | Yes (Completed per Owner Decision) | No | **A (Completed)** |
| **Repository URL** | `https://github.com/Mincow271104/LLM-Wiki` | Official Git remote origin | Yes (Completed) | No | **A (Completed)** |
| **Live Presentation URL** | `https://mincow271104.github.io/LLM-Wiki/` | GitHub Actions Run 45215603066 | Yes (Completed) | No | **A (Completed)** |
| **Submission Date** | `November 24, 2026` | Current calendar date | Yes (Completed) | No | **A (Completed)** |
| **Course Title** | Removed | Not required by instructor | Yes (Removed) | No | **C (Optional Removed)**|
| **Instructor Name** | Removed | Not required by instructor | Yes (Removed) | No | **C (Optional Removed)**|

---

## 5. Evidence Supporting Each Requirement

### Requirement 1: LLM Wiki Topic & Short Introduction
- **Evidence:** [README.md](../README.md) Section 1, [SUBMISSION.md](../SUBMISSION.md) Section 3, [overview.md](../wiki/overview.md), [index.html](../presentation/index.html) Slide 01.
- **Summary:** Authoritative, persistent Karpathy-inspired LLM Wiki exploring "AI Agents: Concepts, Architecture, and Workflow" for AI beginners.

### Requirement 2: LLM Wiki Link / Deliverable
- **Evidence:** Official GitHub Repository: `https://github.com/Mincow271104/LLM-Wiki`.
- **Knowledge Base Deliverables:** 8 canonical sources in `raw/`, 18 validated empirical claims in [claims.json](../raw/claims.json), 24 content pages (21 topic articles plus 3 supporting pages) in `wiki/` (26 Markdown files total).

### Requirement 3: Teaching HTML Presentation Link
- **Evidence:** Public live URL: `https://mincow271104.github.io/LLM-Wiki/`.
- **Local Deliverables:** [index.html](../presentation/index.html), [styles.css](../presentation/styles.css), [slides.js](../presentation/slides.js) (12 slides, responsive, inline SVG diagram, ReAct loop trace, keyboard/touch navigation).

### Requirement 4: Loop / Graph Diagram & Explanation
- **Evidence:** [graph.mmd](../workflow/graph.mmd) (Mermaid visual graph), [graph.md](../workflow/graph.md) (Formal 10-stage specification).
- **Distinction Grounding:** Clearly differentiates macro DAG pipelines from local bounded cyclic correction loops (max 3 retries). Also illustrated on Slide 04, Slide 08, and Slide 09 of the presentation.

### Requirement 5: Actual Execution Results & Validation Records
- **Evidence:**
  - [wiki-lint-report.md](wiki-lint-report.md): Real execution log of 15 automated lint passes (15 Passed, 0 Failed, 0 Warnings; 198 local relative links resolved out of 198 checked, 465 total references scanned, 24 external URI links (HTTP(S)/mailto) skipped, 243 fragment-only links skipped, 0 broken, 0 non-portable paths).
  - [final-validation-report.md](final-validation-report.md): Playwright Chromium test execution log, desktop and mobile viewport verification, 0 console errors.
  - [evidence/](evidence/): 6 high-resolution visual evidence screenshots.
  - [run_negative_tests.py](../scripts/run_negative_tests.py): Real execution log of 5 controlled negative test passes (supplementary verification suite).

### Requirement 6: Reflection on Errors & Workflow Improvements
- **Evidence:** [reflection.md](reflection.md) Section 2 directly answers the three teacher questions:
  1. *Most error-prone stage:* Markdown Link Resolution and Path Portability in Stage 7 (qualitatively observed as the most recurring troubleshooting check; exact per-node retry telemetry was not recorded).
  2. *Shift-left validation:* Moved canonical slug enforcement and source metadata schema validation to the earlier ingestion process ([ingest.py](../scripts/ingest.py)), and documented link portability authoring standards in [AGENTS.md](../AGENTS.md). Automated link resolution and claim checks remain at Stage 7.
  3. *Workflow graph modification:* Expanded to 10 stages with 3 bounded cyclic loops: Loop A (Stage 7 &rarr; Stage 3), Loop B (Stage 8 &rarr; Stage 5), and Loop C (Stage 9 &rarr; Stage 3), capped at &le; 3 retries each; with the controlled negative test suite serving as an independent supplementary verification harness.

---

## 6. Exact Final Moodle Submission Title

The teacher's mandatory title format is:
**School + Student ID + Department + Name + Topic**

### Recommended Chinese/Standard Format:
```text
國立勤益科技大學 4B517024 資工系 PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow
```

### English Format:
```text
NCUT 4B517024 CSIE PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow
```

---

## 7. Final English Submission Text (Ready to Copy into Moodle)

Copy the text block below directly into the Moodle assignment submission box:

```markdown
# AI Agents: Concepts, Architecture and Workflow
**Course Assignment Submission — National Chin-Yi University of Technology (NCUT)**

- **University:** National Chin-Yi University of Technology (NCUT)
- **Department:** Department of Computer Science and Information Engineering (CSIE) / 資訊工程系
- **Student ID:** 4B517024
- **Student Name:** PHUONG KHANG MINH
- **Submission Date:** November 24, 2026

---

### 1. Project Overview & Deliverables
This project implements an authoritative, persistent **LLM Wiki** and an interactive **12-slide educational presentation** on **"AI Agents: Concepts, Architecture, and Workflow"**, following Andrej Karpathy's LLM Wiki methodology. Designed for AI beginners, it bridges the gap between passive chatbots and autonomous agentic systems.

- **Official GitHub Repository:** https://github.com/Mincow271104/LLM-Wiki
- **Live Interactive Presentation (GitHub Pages):** https://mincow271104.github.io/LLM-Wiki/

---

### 2. Fulfillment of the Six Instructor Requirements

1. **Topic and Introduction:**
   Comprehensive curriculum covering What AI Agents are, Agents vs. Chatbots, Agent Architecture (6 core pillars), Planning/Reasoning (ReAct, Plan-and-Solve, Reflection), Memory (Context window vs Vector/KV stores), Tools/MCP, Graph Orchestration (DAGs vs Loops vs LangGraph State Graphs), Multi-Agent Topologies, 4 Production Frameworks, and Safety/Evaluation Benchmarks (SWE-bench, GAIA).
   - *Reference:* `README.md`, `SUBMISSION.md`, `wiki/index.md`, `wiki/overview.md`.

2. **LLM Wiki Deliverable:**
   Built on Karpathy's 3-layer architecture:
   - *Layer A (Raw Sources):* 8 canonical sources (`S01`–`S08`), source cards, and 18 machine-validated empirical claims (`raw/claims.json`).
   - *Layer B (Wiki):* 24 content pages (21 topic articles plus 3 supporting pages) across 6 domains, evidence registry preserving 4 architectural debates, glossary, and audit log (26 Markdown files total).
   - *Layer C (Schemas):* `source.schema.json` and `claim.schema.json` enforced via `jsonschema`.
   - *Reference:* `https://github.com/Mincow271104/LLM-Wiki/tree/main/wiki`

3. **Teaching HTML Presentation:**
   Responsive 12-slide web presentation built in vanilla HTML/CSS/JS with an Academic Slate design system:
   - Includes inline SVG architecture diagram, ReAct execution trace, comparative matrices, and beginner analogies.
   - Fully interactive: keyboard navigation, touch swipe gestures, dynamic progress bar, and slide directory modal.
   - *Live Link:* https://mincow271104.github.io/LLM-Wiki/

4. **Workflow Graph & Loop Explanation:**
   Formalized as a 10-stage stateful orchestration graph:
   - Distinguishes macro Directed Acyclic Graph (DAG) pipelines from local cyclic correction loops.
   - Formalizes 3 bounded correction loops with strict retry limits (`<= 3` cycles per gate): Loop A (Stage 7 &rarr; Stage 3: Repair Syntax/Links), Loop B (Stage 8 &rarr; Stage 5: Refactor CSS/JS), and Loop C (Stage 9 &rarr; Stage 3: Refine Content/Cards).
   - *Reference:* `workflow/graph.mmd` and `workflow/graph.md`.

5. **Actual Execution & Validation Evidence:**
   - *Automated Linter:* 15/15 passes clean (`reports/wiki-lint-report.md`). All 8 source URLs return HTTP 200 OK. All 198 local relative links resolve cleanly (465 total references scanned: 198 local checked, 24 external URI links (HTTP(S)/mailto) skipped, 243 fragment skipped, 0 non-portable paths, 0 broken).
   - *Browser Verification:* Playwright Chromium headless tests passing with 0 console errors and 0 exceptions across desktop (1366x768) and mobile (390x844) viewports (`reports/final-validation-report.md`).
   - *Visual Evidence:* 6 high-resolution screenshots in `reports/evidence/`.
   - *Controlled Negative Tests:* Supplementary test suite verifying 5 injected failure scenarios (missing locator, unknown source, machine link, schema error, slide count mismatch) are reliably detected and rejected.

6. **Reflection on Errors & Workflow Improvements:**
   Directly addresses the teacher's three required questions in `reports/reflection.md`:
   - *Node with highest error frequency:* Markdown Link Resolution and Path Portability at Stage 7 (qualitatively observed as the most recurring troubleshooting check; exact numerical retry telemetry was not recorded).
   - *Shift-left validation:* Enforced canonical card slugs and source metadata schema validation directly in the earlier source-ingestion process (`ingest.py`), and documented link portability authoring standards in `AGENTS.md`. (Claim schema validation, locator checks, and link resolution remain enforced at Stage 7 via `lint_wiki.py`).
   - *Workflow graph modification:* Expanded to 10 stages with 3 bounded cyclic loops: Loop A (Stage 7 &rarr; Stage 3), Loop B (Stage 8 &rarr; Stage 5), Loop C (Stage 9 &rarr; Stage 3) with `max_retries <= 3`, supported by Playwright browser testing and an offline negative testing harness.
```
