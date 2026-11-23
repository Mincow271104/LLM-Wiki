# Source Card: S03

## Metadata
- **Source ID:** S03
- **Title:** Building Effective Agents
- **Authors:** Erik Schluntz, Barry Zhang
- **Publisher / Organization:** Anthropic Engineering
- **Publication Date:** 2024-12-19
- **URL:** [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Engineering guide / Technical blog
- **Note on Scope:** Used for fundamental architectural principles and design patterns. Historical tooling references from Dec 2024 are acknowledged as evolved.

## Summary
Anthropic's "Building Effective Agents" provides pragmatic engineering guidance distilled from working with dozens of production AI teams. The core thesis is that teams should **start with the simplest possible solution** and only add complexity when demonstrably required. The authors draw an essential architectural distinction between **workflows** (predictable, deterministic code-orchestrated pipelines) and **agents** (autonomous, model-driven feedback loops).

Key contributions:
1. **The Augmented LLM:** The foundational building block consisting of an LLM enhanced with retrieval, external tools, and memory.
2. **Core Workflow Patterns:**
   - *Prompt Chaining:* Sequential LLM calls where each step processes the output of the prior step.
   - *Routing:* Classification stage that directs an input to specialized downstream prompts or tools.
   - *Parallelization:* Running multiple LLM calls concurrently, either by sectioning (independent subtasks) or voting (generating diverse outputs for consensus/filtering).
   - *Orchestrator-Workers:* A central orchestrator dynamically decomposes tasks, delegates subtasks to parallel workers, and synthesizes results.
   - *Evaluator-Optimizer:* Two LLM roles where one generates candidate solutions and the other provides critique in an iterative refinement loop.
3. **Autonomous Agents:** Systems where the LLM maintains control over the execution loop, choosing tools and deciding when tasks are complete. Recommended only when open-ended exploration and unpredictable branching are strictly necessary.
4. **Tool Engineering Best Practices:** Formulating clear tool definitions, providing few-shot usage examples, and investing in robust guardrails.

## Verified Section Structure
- **01 What are agents?** — Conceptual distinction between deterministic workflows and autonomous agent loops.
- **02 When (and when not) to use agents** — Decision criteria; trade-offs between flexibility, latency, cost, and predictability.
- **03 When and how to use frameworks** — Critique of framework overhead; recommendation to write transparent native code first.
- **04 Building blocks, workflows, and agents** — Detailed architectural diagrams and breakdowns of the five workflow patterns and the autonomous agent loop.
- **05 Combining and customizing these patterns** — Hybrid designs combining deterministic routing with agentic execution.
- **06 Summary** — Key takeaways and architectural checklist.
- **Appendix 1: Agents in practice** — Production case studies (customer support, coding agents).
- **Appendix 2: Prompt engineering your tools** — Practical advice on tool schema design, descriptions, and error formatting.

## Key Claims & Evidence Locators
- **[S03, What are agents?]:** Workflows orchestrate LLMs and tools through predefined code paths, whereas agents dynamically direct their own processes and tool usage.
- **[S03, When (and when not) to use agents]:** Start with simple prompts, optimize with retrieval and few-shot examples, and only add agentic autonomy when deterministic workflows cannot handle the problem variability.
- **[S03, Building block: The augmented LLM]:** The core building block of all modern agentic systems is an LLM augmented with retrieval, tools, and memory.
- **[S03, Workflow: Evaluator-optimizer]:** Combining a generator model with an evaluator model in a feedback loop improves output quality on complex drafting and code generation tasks.
- **[S03, Appendix 2: Prompt engineering your tools]:** Tool definitions require the same prompt engineering care as user prompts; clear descriptions, edge-case documentation, and realistic examples prevent tool misuse.
