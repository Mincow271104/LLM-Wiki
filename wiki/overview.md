# AI Agents: Concepts, Architecture, and Workflow

## Executive Summary
This Wiki is a structured, persistent knowledge base designed to teach **AI Agents** to beginners while providing intermediate-level technical clarity and Python implementation insights. Built upon the **Karpathy-inspired LLM Wiki architecture**, this repository serves as an evolving, compounding knowledge layer connecting raw academic literature and official industry documentation to accessible educational content.

## What is an AI Agent?
At its core, an **AI Agent** is an autonomous or semi-autonomous software system driven by a foundation model (such as a Large Language Model) that perceives its environment, reasons about objectives, formulates plans, executes actions using external tools, and iterates based on environmental feedback until a goal is satisfied [[S03, What are agents?](#)], [[S05, Core concepts: Agents](#)].

Unlike traditional static software programs that execute rigid algorithmic instructions, an AI agent exhibits dynamic problem-solving capabilities. Unlike simple conversational chatbots that respond passively turn-by-turn without modifying external systems, an agent actively alters environment state and gathers new information to solve multi-step problems [[S01, Section 1](#)], [[S04, Agent architecture overview](#)].

## The Karpathy LLM Wiki Architecture
Following Andrej Karpathy's methodology, this knowledge repository is structured into three distinct layers:
1. **Layer A: Raw Sources (`raw/`)** — An immutable archive of verified primary evidence, including peer-reviewed papers (ReAct, Toolformer) and authoritative engineering documentation (Anthropic, Google Cloud, OpenAI, LangChain, CrewAI, Microsoft).
2. **Layer B: The Wiki (`wiki/`)** — An interlinked network of conceptual synthesis pages, entity breakdowns, architectural blueprints, framework matrices, and runnable educational examples.
3. **Layer C: Schema & Operations (`schemas/`, `scripts/`, `AGENTS.md`)** — Machine-readable validation schemas and CLI automation tools for three core operations:
   - **Ingest:** Reading new sources, extracting claims, updating synthesis pages, and logging entries.
   - **Query:** Fast, keyword-grounded retrieval across the knowledge base without costly or opaque vector databases.
   - **Lint:** Continuous automated verification of citation integrity, orphan page detection, link resolution, and contradiction tracking.

```
       ┌────────────────────────┐
       │   Curated Sources      │  (ArXiv, Anthropic, Google, OpenAI,
       │      (Layer A)         │   LangChain, CrewAI, Microsoft)
       └───────────┬────────────┘
                   │  Ingest Pipeline
                   ▼
       ┌────────────────────────┐
       │     The LLM Wiki       │  (Concepts, Architecture, Loops,
       │      (Layer B)         │   Frameworks, Safety, Registry)
       └───────────┬────────────┘
                   │  Query & Lint
                   ▼
       ┌────────────────────────┐
       │  Educational Delivery  │  (Beginner Wiki, Future HTML Deck,
       │      (Later Phase)     │   Runnable Code Artifacts)
       └────────────────────────┘
```

## Learning Roadmap for Beginners
For readers new to agentic artificial intelligence, the following sequential learning path is recommended:

1. **Foundations:**
   - [What is an AI Agent?](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/what-is-an-agent.md) — Fundamental definitions, autonomy spectrum, and foundational characteristics.
   - [AI Agents vs. Traditional Chatbots](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/agents-vs-chatbots.md) — Understanding the shift from passive text generation to active environmental agency.
   - [LLM Foundations for Agents](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/llm-foundations.md) — Context windows, token prediction, in-context learning, and instruction adherence.
2. **Architecture & Core Mechanics:**
   - [Agent Architecture Stack](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-architecture.md) — The Augmented LLM building block and the enterprise multi-tier infrastructure.
   - [The Agent Loop](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-loop.md) — The core perception-reasoning-action-observation feedback cycle.
   - [Tools & Function Calling](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/tools-and-function-calling.md) — Extending LLM reach with APIs, Model Context Protocol (MCP), and tool bloat mitigation.
   - [Memory & Context Management](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/memory-and-context.md) — Differentiating short-term working context from persistent long-term storage.
3. **Advanced Concepts & Orchestration:**
   - [Planning & Reasoning](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/planning-and-reasoning.md) — Task decomposition, reflection, and error recovery.
   - [The ReAct Pattern](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/react-pattern.md) — Synergizing reasoning traces with environment actions.
   - [Workflows vs. Autonomous Agents](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/workflows-vs-agents.md) — When to use deterministic pipelines versus autonomous loops.
   - [Graph-Based Orchestration](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/graph-orchestration.md) — Stateful orchestration using nodes, edges, checkpointers, and human-in-the-loop gates.
   - [Single-Agent vs. Multi-Agent Systems](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/multi-agent-systems.md) — Hand-offs, supervisor patterns, and role-playing crews.
4. **Frameworks & Practical Python Implementation:**
   - [Comprehensive Framework Comparison](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/comparison.md) — Side-by-side analysis of OpenAI Agents SDK, LangGraph, CrewAI, and Microsoft Agent Framework (with AutoGen succession analysis).
   - [Educational Python Agent Example](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/implementation/python-agent-example.md) — A self-contained, API-key-free educational Python script illustrating the agent loop.
5. **Safety, Evaluation, and Limitations:**
   - [Agent Evaluation & Benchmarking](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/safety/evaluation.md) — How to measure task success, trajectory efficiency, and tool precision.
   - [Safety, Guardrails, and Limitations](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/safety/safety-and-limitations.md) — Addressing prompt injection, sandboxing, tool limits, and operational boundaries.

## Metadata & Navigation
- **Primary Sources Cited:** [S01], [S03], [S04], [S05], [S06], [S07], [S08]
- **Evidence Registry:** [Master Evidence & Disagreement Registry](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/evidence-registry.md)
- **Terminology Glossary:** [Agent Concepts Glossary](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/glossary.md)
- **Index:** [Wiki Master Index](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/index.md)
- **Last Updated:** 2026-11-23
