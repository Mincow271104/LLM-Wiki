# Multi-Agent Systems: Collaboration and Topologies

## Summary
When tasks exceed the cognitive capacity, context budget, or tool scope of an individual agent, systems scale horizontally into **Multi-Agent Systems (MAS)**. In a multi-agent architecture, specialized autonomous agents collaborate, negotiate, and divide labor. This page analyzes the primary multi-agent organizational topologies, communication protocols, and engineering trade-offs across leading frameworks.

## Key Concepts
- **Specialized Personas & Scoping:** Distributing responsibility across focused agents with distinct roles, goals, and scoped tools to eliminate tool bloat and cognitive overload [[S04, Tool bloat](#)], [[S07, Core Concepts: Agents, Tasks, Crews](#)].
- **Hand-offs:** Explicit delegation primitives where one agent transfers execution control and context to another specialized agent [[S05, Core concepts: Hand-offs](#)].
- **Organizational Topologies:** Architectural coordination patterns including Sequential chains, Hierarchical supervisor-worker trees, and dynamic Group Chats [[S07, Processes](#)], [[S08, Agent Framework brings together four primary areas](#)].
- **Inter-Agent Communication Overhead:** The latency, token cost, and state synchronization penalties inherent to multi-agent architectures [[S03, When and how to use frameworks](#)].

---

## Architectural Topologies in Multi-Agent Systems

Multi-agent architectures coordinate collaboration through four primary structural topologies:

```
1. Sequential Pipeline (CrewAI, Workflows)
   Agent A (Researcher) ──> Agent B (Writer) ──> Agent C (Editor)

2. Hierarchical / Supervisor (LangGraph, CrewAI Hierarchical)
                    ┌────────────────────────┐
                    │    Supervisor Agent    │
                    └───────────┬────────────┘
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
           ┌───────────┐  ┌───────────┐  ┌───────────┐
           │ Worker A  │  │ Worker B  │  │ Worker C  │
           └───────────┘  └───────────┘  └───────────┘

3. Handoff Network (OpenAI Agents SDK)
           ┌───────────┐  handoff   ┌───────────┐
           │ Triage    ├───────────>│ Billing   │
           │ Agent     │<───────────┤ Agent     │
           └─────┬─────┘  handoff   └───────────┘
                 │
                 │ handoff
                 ▼
           ┌───────────┐
           │ Technical │
           │ Support   │
           └───────────┘

4. Collaborative Group Chat / Blackboard (AutoGen, Microsoft Agent Framework)
   All agents share a unified message bus or blackboard, with speaker selection
   governed by an orchestrator or round-robin protocol.
```

### 1. Sequential Pipeline
Tasks flow in a predetermined linear sequence. Agent A completes its deliverable and writes its output into shared state; Agent B consumes Agent A's output as its starting prompt [[S07, Processes: Sequential Process](#)].
- *Best for:* Content production, ETL pipelines, standardized compliance reviews.

### 2. Hierarchical / Supervisor Model
A central manager agent inspects the user goal, formulates a project plan, assigns subtasks to specialized subordinate agents, inspects worker deliverables, and requests revisions if necessary [[S03, Workflow: Orchestrator-workers](#)], [[S07, Processes: Hierarchical Process](#)].
- *Best for:* Complex software development, comprehensive research reports, multi-modal analysis.

### 3. Handoff Network
Popularized by the OpenAI Agents SDK [[S05, Core concepts: Hand-offs](#)], agents are connected as a graph of peers. A front-facing triage agent assesses the user's intent and executes an explicit handoff function (e.g., `handoff_to_billing_agent()`). Control and conversation history shift completely to the recipient agent, which possesses only billing-specific tools.
- *Best for:* Enterprise customer support, multi-department enterprise assistants.

### 4. Group Chat & Blackboard
Pioneered in AutoGen and unified in the Microsoft Agent Framework [[S08, Why Agent Framework?](#)], multiple agents participate in a shared conversational thread. A speaker selection model or rule-based orchestrator selects which agent speaks next based on current conversational context.
- *Best for:* Brainstorming, multi-perspective debates, adversarial red-teaming.

---

## Multi-Agent Paradigms: Framework Approaches

| Feature / Dimension | CrewAI [S07] | OpenAI Agents SDK [S05] | LangGraph [S06] | Microsoft Agent Framework [S08] |
| :--- | :--- | :--- | :--- | :--- |
| **Agent Metaphor** | Anthropomorphic role-playing (`role`, `goal`, `backstory`). | Explicit functional units (model, instructions, tools). | Graph compute nodes operating on shared typed state. | Converged agents with enterprise session state and harness. |
| **Coordination Model** | Sequential or Hierarchical Crews. | Function-driven hand-offs. | Conditional edges, supervisor nodes, or subgraphs. | Workflows, group chat, and supervisor topologies. |
| **Tool Scoping** | Attached directly to individual agent instances. | Scoped to active agent; switched upon hand-off. | Bound to tool-executing graph nodes. | Bound to agents via MCP clients and middleware. |
| **State Sharing** | In-memory task output cascading. | Transferred conversation messages. | Explicit typed state schema with state reducers. | Enterprise session state management with type safety. |

---

## The Engineering Realities of Multi-Agent Systems

While multi-agent systems offer remarkable architectural modularity, Anthropic [[S03, When and how to use frameworks](#)] and Google Cloud [[S04, Agent design patterns](#)] emphasize key operational trade-offs:
1. **Compounding Latency:** If three agents must converse sequentially to solve a query, total latency is the sum of all individual inference times and tool calls.
2. **Exponential Token Costs:** Context is often duplicated across agent boundaries, leading to rapid token consumption.
3. **Cascading Hallucinations:** If Agent 1 makes an unverified assumption, downstream agents (Agent 2 and Agent 3) treat that error as an established ground truth, compounding mistakes.

---

## Citations & Evidence
- **[S03, When and how to use frameworks & Workflow: Orchestrator-workers]:** Analyzes the trade-offs of multi-agent orchestration.
- **[S04, Agent design patterns & Tool bloat]:** Documents multi-agent collaboration as a defense against single-agent tool bloat.
- **[S05, Core concepts: Hand-offs]:** Formulates hand-offs as the primary multi-agent delegation mechanism.
- **[S07, Core Concepts: Agents, Tasks, Crews]:** Outlines role-playing multi-agent crews and sequential/hierarchical execution.
- **[S08, Why Agent Framework?]:** Documents the unification of conversational multi-agent systems with enterprise telemetry and graph workflows.

---

## Related Wiki Pages
- [Single-Agent Systems](single-agent-systems.md)
- [Workflows vs. Autonomous Agents](workflows-vs-agents.md)
- [Comprehensive Framework Comparison](../frameworks/comparison.md)
- [CrewAI Framework Deep Dive](../frameworks/crewai.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
