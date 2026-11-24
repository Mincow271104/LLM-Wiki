# Assignment Submission Checklist & Verification Audit

## 1. Moodle Submission Title Format
The instructor requires the submission title to follow this order:
**School + Student ID + Department + Name + Topic**

### Recommended Standard Chinese Format:
```text
國立勤益科技大學 4B517024 資工系 PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow
```

### English Variant:
```text
NCUT 4B517024 CSIE PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow
```

---

## 2. Six Instructor Requirements Compliance Audit

| Requirement # | Instructor Requirement | Implementation & Repository Location | Status |
|:---:|:---|:---|:---:|
| **Req 1** | LLM Wiki topic and short introduction | `README.md`, `SUBMISSION.md`, `wiki/index.md`, `wiki/overview.md` | **VERIFIED (PASS)** |
| **Req 2** | LLM Wiki link or deliverable | GitHub Repository: `https://github.com/Mincow271104/LLM-Wiki`<br>Wiki Knowledge Base: `wiki/` (24 content pages [21 topic articles plus 3 supporting pages], 26 Markdown files total, Layer A/B/C) | **VERIFIED (PASS)** |
| **Req 3** | Teaching HTML presentation link | Live Presentation URL: `https://mincow271104.github.io/LLM-Wiki/`<br>Local Source: `presentation/index.html` (12 slides, responsive) | **VERIFIED (PASS)** |
| **Req 4** | Loop / Graph diagram or explanation | Workflow Graph: `workflow/graph.mmd` & `workflow/graph.md`<br>Presentation Diagrams: Slide 04, Slide 08 (ReAct), Slide 09 | **VERIFIED (PASS)** |
| **Req 5** | Actual execution results or validation records | 15-Pass Linter: `reports/wiki-lint-report.md`<br>Playwright Browser Test: `reports/final-validation-report.md`<br>Visual Screenshots: `reports/evidence/` (6 PNGs)<br>Controlled Negative Tests: `scripts/run_negative_tests.py` | **VERIFIED (PASS)** |
| **Req 6** | Reflection on errors and workflow improvements | Engineering Reflection: `reports/reflection.md`<br>Chronological Log: `reports/execution-log.md` | **VERIFIED (PASS)** |

---

## 3. Comprehensive Deliverables Checklist

### Core Repository Files
- [x] `PROJECT_BRIEF.md`: Preserved from official repository initialization.
- [x] `AGENTS.md`: Operating schema, academic rules, citation conventions, governance.
- [x] `README.md`: Student onboarding, curriculum roadmap, CLI instructions, GitHub Pages link.
- [x] `SUBMISSION.md`: Formal assignment package covering all 6 instructor requirements and verified student info.
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
- [x] `wiki/log.md`: Chronological append-only record of ingestion, upgrade, presentation, and testing events.
- [x] `wiki/fundamentals/`: 3 modules (`what-is-an-agent.md`, `agents-vs-chatbots.md`, `llm-foundations.md`).
- [x] `wiki/architecture/`: 4 modules (`agent-architecture.md`, `agent-loop.md`, `memory-and-context.md`, `tools-and-function-calling.md`).
- [x] `wiki/concepts/`: 6 modules (`graph-orchestration.md`, `planning-and-reasoning.md`, `react-pattern.md`, `workflows-vs-agents.md`, `single-agent-systems.md`, `multi-agent-systems.md`).
- [x] `wiki/frameworks/`: 5 modules (`openai-agents-sdk.md`, `langgraph.md`, `crewai.md`, `microsoft-agent-framework.md`, `comparison.md`).
- [x] `wiki/implementation/`: 1 educational module (`python-agent-example.md`).
- [x] `wiki/safety/`: 2 modules (`evaluation.md`, `safety-and-limitations.md`).

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
- [x] Verified Live GitHub Actions Run: ID `45215603066`, Status: `completed`, Conclusion: `success`, Event: `push`.
- [x] Verified Live URL: `https://mincow271104.github.io/LLM-Wiki/` responds with HTTP 200 OK.

### Quality Reports & Evidence (`reports/`)
- [x] `reports/fidelity-review.md`: Complete Slide $\to$ Claim $\to$ Wiki $\to$ Source mapping and audit verdict.
- [x] `reports/execution-log.md`: Chronological engineering log of Batch 1 and Batch 2.
- [x] `reports/reflection.md`: In-depth analysis answering the 3 required questions directly.
- [x] `reports/final-validation-report.md`: Complete summary of 15-pass linter, Playwright tests, and negative tests.
- [x] `reports/submission-checklist.md`: Assignment verification checklist & Moodle title format.
- [x] `reports/wiki-lint-report.md`: Real execution output of 15-pass linter.
- [x] `reports/final-submission-audit.md`: Formal audit report for PM review.
- [x] `reports/evidence/`: 6 high-resolution PNG screenshots verifying desktop and mobile presentation rendering.

---

## 4. Final Submission Action for Student
The student has confirmed that all metadata is complete and no class designation or academic year is needed. The submission text is 100% copy-ready:
1. **Copy Final Submission Text into Moodle:** Copy the pre-formatted submission block from `reports/final-submission-audit.md` Section 7 into the NCUT Moodle submission portal.
2. **Set Moodle Submission Title:** Use the verified title format: `國立勤益科技大學 4B517024 資工系 PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow` (or the English variant `NCUT 4B517024 CSIE PHUONG KHANG MINH - AI Agents: Concepts, Architecture and Workflow`).
