# Procedure: Building the Teaching Slides Presentation

## 1. Overview
This procedure defines the exact, repeatable steps required for an AI agent or human engineer to build, test, and package the interactive HTML slide presentation (`presentation/`) from the foundational Wiki knowledge base.

---

## 2. Prerequisites
- **Python 3.10+** (verified on Python 3.14).
- Dependencies: `pip install jsonschema playwright`
- Playwright Chromium browser: `playwright install chromium`
- Official repository clone: Clean working tree at `E:\HƯ` (or project root).

---

## 3. Step-by-Step Build Procedure

### Step 1: Ingest and Verify Primary Sources
Ensure that all 8 primary sources (`S01` through `S08`) are registered, validated against `schemas/source.schema.json`, and summarized in canonical source cards:
```bash
python scripts/lint_wiki.py --verify-live-urls
```
Confirm that 15 test passes succeed with 0 failures.

### Step 2: Establish the 12-Slide Storyboard
Map the approved curriculum modules into `presentation/index.html`:
- **Slide 01:** Title and Learning Objectives (Analogy & Navigation Guide)
- **Slide 02:** What Is an AI Agent? (Perception, Reasoning, Action, Feedback; Recipe Reader vs Executive Chef)
- **Slide 03:** AI Agent vs. Traditional Chatbot (5-Dimension Comparative Matrix)
- **Slide 04:** Core Agent Architecture (Inline SVG Diagram of 6 Core Components)
- **Slide 05:** Planning and Reasoning (Decomposition, Plan-and-Solve, Self-Reflection)
- **Slide 06:** Memory and Context (Short-Term Working Memory vs Long-Term Vector/KV Stores)
- **Slide 07:** Tools and Function Calling (4-Step Actuator Cycle, JSON Schema, MCP)
- **Slide 08:** The ReAct Pattern (Tripartite Thought-Action-Observation Loop & Execution Trace)
- **Slide 09:** Agent Loops vs. Graph Orchestration (DAGs, Cyclic Loops, LangGraph State Graphs)
- **Slide 10:** Single-Agent vs. Multi-Agent Systems (Specialization, Sequential, Supervisor, Handoffs)
- **Slide 11:** Frameworks & Python Implementation (Comparative Matrix & Educational vs Production Code)
- **Slide 12:** Evaluation, Safety & Future Horizons (SWE-bench, GAIA, Guardrails, Summary Takeaways)

### Step 3: Implement Visual System and Responsive Styles
Ensure `presentation/styles.css` is loaded with:
- Academic Slate design tokens (`#0f172a`, `#1e293b`, `#38bdf8`, `#10b981`).
- Responsive flexbox/grid containers (`.columns-2`, `.columns-3`, `.table-container`).
- Mobile breakpoints (`@media (max-width: 768px)`).
- Accessibility attributes (aria labels, role definitions, high-contrast text).

### Step 4: Implement Controller and Navigation Engine
Verify `presentation/slides.js` supports:
- Keyboard event listeners (`ArrowRight`, `ArrowLeft`, `Space`, `PageUp`, `PageDown`, `Home`, `End`, `Escape`, `O`).
- Touch swipe gesture detection for mobile devices (`touchstart`, `touchend`).
- Dynamic progress bar calculation (`(current / total) * 100%`).
- Slide directory overview modal population and navigation.

### Step 5: Execute Automated Browser and Layout Testing
Run the automated Playwright test suite to verify navigation, mobile rendering, and capture screenshots:
```bash
python scripts/test_presentation.py
```
**Verification Criteria:**
- 12 slides detected.
- Desktop (1366x768) and Mobile (390x844) viewports render without horizontal page scroll.
- Exactly 0 console errors and 0 uncaught exceptions.
- 6 visual evidence screenshots generated in `reports/evidence/`.

### Step 6: Audit Citation Fidelity
Compare all citations in the slides against `raw/claims.json` and `wiki/evidence-registry.md`. Ensure that:
- Every slide contains valid source citations (`[S01]`, `[S03]`, etc.) with exact section locators.
- All 4 major architectural disagreement categories are documented.
- No phantom citations or unsupported facts exist.

### Step 7: Deploy to GitHub Pages
Commit all changes and push to `origin main`. The automated GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) will deploy the `presentation/` folder to GitHub Pages.
