# Workflows vs. Autonomous Agents

## Summary
A foundational architectural question in modern AI engineering is choosing between **deterministic workflows** and **autonomous agents**. While the terms are often used interchangeably in marketing discourse, engineering literature (Anthropic, Google Cloud, Microsoft) establishes a rigorous technical distinction: workflows orchestrate LLMs and tools along predefined, deterministic code paths, whereas agents dynamically govern their own process flow in iterative feedback loops.

## Key Concepts
- **Deterministic Workflows:** Systems where the sequence of execution steps, routing decisions, and tool calls are governed by hardcoded application logic [[S03, What are agents?](#)].
- **Autonomous Agents:** Systems where the language model dynamically decides which actions to take, inspects results, and determines when the process is complete [[S03, What are agents?](#)], [[S08, When to use agents vs workflows](#)].
- **Trade-off Dimensions:** Predictability, latency, cost, and debugging ease vs. flexibility, open-ended problem solving, and error recovery [[S03, When (and when not) to use agents](#)].
- **The Graph Continuum:** As modeled in LangGraph, workflows (DAGs) and agents (cyclic graphs) exist on a unified continuum of stateful graph orchestration [[S06, Patterns: Workflows + agents](#)].

---

## The Architectural Spectrum

Anthropic's seminal guide [[S03, Building blocks, workflows, and agents](#)] categorizes orchestration patterns into two clear paradigms:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Workflows vs. Agents                            │
├───────────────────────────────────┬────────────────────────────────────┤
│ Workflows (Code Orchestrated)     │ Agents (Model Orchestrated)        │
├───────────────────────────────────┼────────────────────────────────────┤
│ - Execution path is hardcoded     │ - Execution path is dynamic        │
│ - Predictable, deterministic      │ - Flexible, non-deterministic      │
│ - Fixed token cost and latency    │ - Variable token cost and latency  │
│ - Straightforward unit testing    │ - Requires trajectory evaluation   │
│ - Best for well-defined pipelines │ - Best for open-ended exploration  │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## The Five Canonical Workflow Patterns

Anthropic [[S03, Building blocks, workflows, and agents](#)] identifies five core design patterns that cover the vast majority of non-agentic LLM implementations:

### 1. Prompt Chaining
Decomposes a complex task into a fixed linear pipeline where each LLM call processes the output of the previous step.
$$\text{Input} \longrightarrow [\text{Step 1: Extract Data}] \longrightarrow [\text{Step 2: Transform}] \longrightarrow [\text{Step 3: Format Output}]$$
- *Best for:* Data extraction, multi-stage summarization, translation with quality checks.

### 2. Routing
A lightweight classification model inspects the user input and directs it to a specialized downstream prompt, model, or tool.
$$\text{Input} \longrightarrow [\text{Router}] \overset{\text{Category A}}{\longrightarrow} [\text{Specialized Handler A}]$$
- *Best for:* Customer support triage, separating simple queries from complex reasoning tasks.

### 3. Parallelization
Executing multiple LLM calls concurrently. Divided into two subtypes:
- **Sectioning:** Splitting an input into independent chunks (e.g., chapters or files) processed in parallel.
- **Voting:** Executing the same prompt multiple times with temperature $> 0$ to sample diverse perspectives, extract consensus, or filter malicious outputs.
- *Best for:* Guardrails, multi-perspective reviews, bulk document analysis.

### 4. Orchestrator-Workers
A central orchestrator LLM analyzes a complex goal, breaks it down into dynamic subtasks, assigns them to parallel worker models, and synthesizes their returned deliverables.
- *Best for:* Research synthesis, multi-source competitive analysis, large-scale code refactoring.

### 5. Evaluator-Optimizer
One LLM role generates candidate outputs, while another LLM role acts as a critic/evaluator, testing results against specific criteria and requesting revisions in a loop until quality standards are met.
- *Best for:* High-stakes drafting, code synthesis with unit tests, translation polishing.

---

## Decision Matrix: Choosing the Right Approach

Microsoft Learn [[S08, When to use agents vs workflows](#)] and Anthropic [[S03, When (and when not) to use agents](#)] provide pragmatic guidance:

| Use a Workflow When: | Use an Autonomous Agent When: |
| :--- | :--- |
| The business process has known, deterministic steps. | The task is open-ended, conversational, or exploratory. |
| Strict latency, cost, and compliance SLAs must be guaranteed. | The sequence of steps cannot be predicted beforehand. |
| Errors can be avoided by programmatic validation and unit tests. | The system must adapt to unpredictable environment feedback. |
| A deterministic code function can accomplish the goal. | Tool usage, search paths, and exceptions must be self-directed. |

> **Architectural Rule:** *"If you can write a function to handle the task, do that instead of using an AI agent."* — Microsoft Agent Framework [[S08, When to use agents vs workflows](#)].

---

## Citations & Evidence
- **[S03, What are agents? & Building blocks]:** Anthropic outlines the definition of workflows vs. agents and documents the five canonical workflow patterns.
- **[S03, When (and when not) to use agents]:** Advises starting with simple workflows and only introducing agents when justified.
- **[S06, Patterns: Workflows + agents]:** LangGraph models workflows and agents on a shared graph runtime.
- **[S08, When to use agents vs workflows]:** Microsoft provides the enterprise decision matrix and golden rule for choosing workflows over agents.

---

## Related Wiki Pages
- [What is an AI Agent?](../fundamentals/what-is-an-agent.md)
- [The Agent Loop](../architecture/agent-loop.md)
- [Graph-Based Orchestration](graph-orchestration.md)
- [Master Evidence & Disagreement Registry](../evidence-registry.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
