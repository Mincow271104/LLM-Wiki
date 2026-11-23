# Single-Agent Systems

## Summary
A **Single-Agent System** consists of a single primary autonomous loop where one foundation model—configured with system instructions, memory, and a designated set of tools—directs its own execution to accomplish a user's task. Single-agent architectures represent the baseline for agentic AI, offering simplicity, lower orchestration overhead, and straightforward debugging.

## Key Concepts
- **Unified Context:** A single agent maintains a single conversation and scratchpad stream, avoiding the communication overhead and state synchronization complexities of multi-agent topologies [[S03, When (and when not) to use agents](#)].
- **Generalist Scope:** The agent handles task planning, tool invocation, result interpretation, and final synthesis within one continuous execution thread [[S05, Core concepts: Agents](#)].
- **Operational Boundaries:** Understanding the exact complexity threshold where a single agent begins to degrade (due to tool bloat or context window saturation), indicating the need for multi-agent delegation [[S04, Tool bloat](#)].

---

## Anatomy of a Single-Agent Architecture

In a single-agent system, the agent acts as a unified operator:

```
               ┌───────────────────────────────────────────────┐
               │              Single-Agent System              │
               │                                               │
               │   ┌───────────────────────────────────────┐   │
               │   │           Unified LLM Core            │   │
               │   │    (Planning + Execution + Eval)      │   │
               │   └───────────────────┬───────────────────┘   │
               │                       │                       │
               │         ┌─────────────┼─────────────┐         │
               │         ▼             ▼             ▼         │
               │   ┌───────────┐ ┌───────────┐ ┌───────────┐   │
               │   │  Tool A   │ │  Tool B   │ │  Tool C   │   │
               │   │ (Search)  │ │ (Calc)    │ │ (Database)│   │
               │   └───────────┘ └───────────┘ └───────────┘   │
               └───────────────────────────────────────────────┘
```

### Key Advantages:
1. **Low Latency & Reduced Token Cost:** No inter-agent communication messages, hand-off protocols, or redundant context serialization.
2. **Deterministic Debugging:** The entire trajectory exists in a single sequential log (e.g., ReAct trace `Thought → Action → Observation`), making errors easily traceable.
3. **Architectural Simplicity:** Can be implemented in less than 50 lines of clean Python without complex third-party framework overhead [[S03, When and how to use frameworks](#)].

---

## Scaling Limits: When Does a Single Agent Fail?

While single agents excel at focused, well-scoped tasks (e.g., answering a multi-hop factual query or drafting an email using calendar tools), they degrade under three specific conditions:

1. **Tool Bloat:** If the agent is provided with dozens of disparate tools (e.g., Git commands, SQL queries, web search, email sending, math calculations), tool selection accuracy drops precipitously [[S04, Tool bloat](#)].
2. **Persona Conflict / Cognitive Overload:** An agent instructed to act simultaneously as an aggressive creative copywriter and a strict compliance auditor frequently produces diluted or contradictory outputs.
3. **Context Length Dilution:** Tasks requiring extended interactions (30+ steps) fill the context window with raw tool outputs, causing the model to forget initial constraints.

When these boundaries are reached, engineering teams transition to **Multi-Agent Systems** [[S07, Why CrewAI?](#)], [[S08, Agent Framework brings together four primary areas](#)].

---

## Citations & Evidence
- **[S03, When (and when not) to use agents & When and how to use frameworks]:** Anthropic advocates starting with single, simple agents before adding framework overhead.
- **[S04, Tool bloat]:** Google Cloud documents how single agents degrade when exposed to too many tool schemas.
- **[S05, Core concepts: Agents]:** OpenAI formalizes the single agent combining a model, instructions, and tools.

---

## Related Wiki Pages
- [What is an AI Agent?](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/what-is-an-agent.md)
- [The Agent Loop](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-loop.md)
- [Multi-Agent Systems](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/multi-agent-systems.md)
- [Educational Python Agent Example](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/implementation/python-agent-example.md)
- [Wiki Master Index](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/index.md)

*Last Updated: 2026-11-23*
