# Chronological Engineering Execution Log

## 1. Project Overview & Scope
- **Project Title:** AI Agents Learning Wiki: Concepts, Architecture, and Workflow
- **Methodology:** Karpathy-Inspired LLM Wiki Knowledge Architecture & Educational HTML Presentation
- **Official Repository:** `https://github.com/Mincow271104/LLM-Wiki.git`
- **Active Branch:** `main`
- **Execution Phases:**
  - **Batch 1 (Phases P1 & P2):** Repository discovery, source ingestion (`S01`–`S08`), schema validation, 21-topic knowledge base authoring, evidence registration, automated linter creation, and safe Git integration.
  - **Batch 2 (Phase P3 & Final Delivery):** Batch 1 bug fixes, `jsonschema` engine integration, portable relative link conversion, canonical source card deduplication, 12-slide interactive presentation authoring, Playwright automated testing, workflow graph formalization, fidelity review, GitHub Pages deployment workflow, and complete final reporting.

---

## 2. Chronological Milestones & Actions

### Phase A: Batch 1 Initial Implementation & Gate 2 Push
*Recorded Timeline: November 23, 2026, 21:00 – 23:45 UTC+8*

- **Step 1: Workspace & Git Discovery:**
  - Identified initial workspace at `E:\HƯ\ai-agents-wiki-assignment` on branch `master` with 66 unpushed committed files.
  - Inspected root directory `E:\HƯ` and discovered official Git clone tracking `origin: https://github.com/Mincow271104/LLM-Wiki.git` on branch `main`.
  - Reconciled directories: Safely transferred project files from nested folder to official root `E:\HƯ`, excluding `.git/` to avoid git submodule conflicts. Added `ai-agents-wiki-assignment/` to `.gitignore`.
- **Step 2: Source Ingestion & Claim Extraction:**
  - Sequentially ingested 8 approved primary sources (`S01` through `S08`).
  - Extracted 18 primary claims into `raw/claims.json` and `wiki/evidence-registry.md`.
  - Authored 21 comprehensive Wiki articles across 6 topic domains (`fundamentals/`, `architecture/`, `concepts/`, `frameworks/`, `implementation/`, `safety/`).
- **Step 3: Initial Linter Creation:**
  - Authored `scripts/lint_wiki.py` with 11 structural integrity passes.
  - Resolved contradiction counting discrepancy by establishing reciprocal pointers between conflicting claims.
- **Step 4: Batch 1 Git Integration:**
  - Removed trailing whitespace in `README.md`.
  - Committed and pushed initial 66 files to `origin main` (Commit `fc5865e`).

---

### Phase B: Batch 2 Defect Remediation & Core Tooling Upgrades
*Recorded Timeline: November 23, 2026, 23:45 – November 24, 2026, 00:15 UTC+8*

- **Defect 1: JSON Schema Validation Incompleteness:**
  - *Root Cause:* Initial linter only verified key presence without checking types, enums, URI formats, or regex patterns.
  - *Fix:* Integrated official `jsonschema` package. Updated `scripts/lint_wiki.py` Pass 1 and Pass 2 to run `jsonschema.validate(instance, schema)`.
- **Defect 2: Source Integrity False-Pass Logic Bug:**
  - *Root Cause:* Historical HTTP status was evaluated without returning an explicit FAIL when required fields were missing.
  - *Fix:* Rewrote source integrity verification to assert all required conditions. Added `--verify-live-urls` flag with `urllib.request` timeouts (5s) to separate historical records from live network verification.
- **Defect 3: Duplicate S01 Source Card Generation:**
  - *Root Cause:* `ingest.py` truncated title slugs differently across runs, creating `S01-react.json`/`.md` and `S01-react-synergizing-reasoning-a.json`/`.md`.
  - *Fix:* Enforced a hardcoded `CANONICAL_SLUGS` dictionary in `scripts/ingest.py`. Deleted duplicate files, leaving exactly 16 files (8 JSON + 8 MD pairs).
- **Defect 4: Machine-Specific Local File Links:**
  - *Root Cause:* Batch 1 markdown files used absolute `file:///e:/HƯ/...` links which fail on GitHub web UI and other developer machines.
  - *Fix:* Executed systematic relative path conversion across all 24 content pages (and operational Markdown files). Updated linter Pass 12 to reject `file:///` and Windows drive letter patterns.
- **Defect 5: License Badge Misalignment:**
  - *Root Cause:* `README.md` displayed an MIT License badge while the repository contained no LICENSE file.
  - *Fix:* Removed misleading badge; updated documentation to reflect academic assignment governance.

---

### Phase C: Interactive Presentation Development (`presentation/`)
*Recorded Timeline: November 24, 2026, 00:15 – 00:45 UTC+8*

- **Styling Architecture (`presentation/styles.css`):**
  - Implemented the Academic Slate design system using CSS custom properties (`--bg-primary: #0f172a`, `--accent-primary: #38bdf8`, `--text-main: #f8fafc`).
  - Created responsive grid components (`.columns-2`, `.columns-3`), card containers (`.card-highlight`, `.card-success`, `.card-warning`), code blocks, high-contrast tables, and modal overlay.
  - Implemented mobile breakpoint `@media (max-width: 768px)` with vertical column collapse and responsive font scaling.
- **Controller Logic (`presentation/slides.js`):**
  - Authored zero-dependency vanilla JavaScript controller.
  - Implemented keyboard event listener (`ArrowRight`, `ArrowLeft`, `Space`, `PageUp`, `PageDown`, `Home`, `End`, `Escape`, `O`).
  - Added touch swipe gesture recognizer (`touchstart`, `touchend` delta detection).
  - Wired dynamic top progress bar (`width: (current / total) * 100%`) and slide counter.
  - Implemented Slide Directory overview modal populated dynamically from `.slide-title` nodes.
- **HTML Content Authoring (`presentation/index.html`):**
  - Authored all 12 slides fulfilling curriculum objectives.
  - Added custom inline SVG architecture diagram on Slide 04.
  - Included side-by-side comparative tables on Slide 03 and Slide 11.
  - Formatted ReAct tripartite loop and trace on Slide 08.
  - Embedded exact source citations (`[S01]`, `[S03]`, `CLM-001`–`CLM-018`) in footer badges on every slide.

---

### Phase D: Automated Headless Browser Testing & Screenshot Evidence
*Recorded Timeline: November 24, 2026, 00:45 – 01:10 UTC+8*

- **Script Development (`scripts/test_presentation.py`):**
  - Integrated Playwright Chromium headless engine.
  - Set up console error interceptor (`page.on('console', ...)`) and exception monitor (`page.on('pageerror', ...)`).
- **Desktop Execution (1366 x 768):**
  - Verified title, total slides (12), initial active slide.
  - Tested navigation via UI Next/Prev buttons, keyboard shortcuts, and overview modal.
  - Captured evidence screenshots:
    - `reports/evidence/slide-01-desktop.png`
    - `reports/evidence/slide-04-architecture.png`
    - `reports/evidence/slide-08-react.png`
    - `reports/evidence/slide-09-orchestration.png`
    - `reports/evidence/slide-12-summary.png`
- **Mobile Execution (390 x 844):**
  - Tested touch viewport responsiveness and navigation.
  - Captured `reports/evidence/slide-01-mobile.png`.
- **Integrity Result:** Exactly 0 console errors, 0 uncaught exceptions, 0 layout overflow errors.

---

### Phase E: Workflow Documentation & Independent Verification
*Recorded Timeline: November 24, 2026, 01:10 – 01:35 UTC+8*

- **Workflow Formalization:**
  - Authored `workflow/graph.mmd` and `workflow/graph.md` specifying the 10-stage presentation generation pipeline and distinguishing DAG flow from 3 cyclic correction loops (max 3 retries).
  - Authored `workflow/build-teaching-slides.md` providing step-by-step reproduction instructions.
  - Authored `workflow/prompts/fidelity-review-prompt.md` defining reviewer audit criteria.
- **Fidelity Review (`reports/fidelity-review.md`):**
  - Created complete Slide $\to$ Claim $\to$ Wiki $\to$ Source mapping table covering all 12 slides, 8 sources, and 18 claims.
  - Verified preservation of all 4 major architectural debates.
  - Issued formal `PASS` audit sign-off.
- **Deployment & Submission Package:**
  - Configured `.github/workflows/deploy-pages.yml` targeting `https://mincow271104.github.io/LLM-Wiki/`.
  - Authored `SUBMISSION.md` addressing all 6 instructor requirements with NCUT CSIE placeholders.
  - Compiled final validation reports and controlled negative test suite.
