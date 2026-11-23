# Agent Architecture: The Systems Blueprint

## Summary
Building effective AI agents requires looking beyond the foundation model to the entire computational architecture. Modern agent architectures combine the **Augmented LLM** building block with modular multi-tier enterprise systems encompassing orchestration runtimes, standardized tool protocols, tiered memory, and security governance layers.

## Key Concepts
- **The Augmented LLM:** The foundational building block combining an LLM core with retrieval, tool execution interfaces, and memory buffers [[S03, Building block: The augmented LLM](#)].
- **Multi-Tier Agent Stack:** The end-to-end infrastructure stack spanning frontend interfaces, orchestration frameworks, model runtimes, and enterprise data backends [[S04, Agent architecture overview](#)].
- **Separation of Concerns:** Decoupling the reasoning model from deterministic tool execution, state persistence, and telemetry [[S06, LangGraph overview](#)], [[S08, Agent Framework brings together four primary areas](#)].
- **Governance & Sandboxing:** Security boundaries that isolate agent code execution, enforce identity-based permissions (IAM), and apply guardrails [[S04, Agent security and governance](#)], [[S05, Core concepts: Guardrails](#)].

---

## The Foundational Building Block: The Augmented LLM

As articulated in Anthropic's architectural guide [[S03, Building block: The augmented LLM](#)], every agentic system—regardless of framework complexity—is assembled from a single primary building block:

```
               ┌───────────────────────────────────────────────┐
               │                Augmented LLM                  │
               │                                               │
               │   ┌───────────────────────────────────────┐   │
               │   │         Foundation Model Core         │   │
               │   │        (Reasoning & Planning)         │   │
               │   └───────────────────┬───────────────────┘   │
               │                       │                       │
               │         ┌─────────────┼─────────────┐         │
               │         ▼             ▼             ▼         │
               │   ┌───────────┐ ┌───────────┐ ┌───────────┐   │
               │   │ Retrieval │ │   Tools   │ │  Memory   │   │
               │   │  (Search) │ │   (APIs)  │ │  (Context)│   │
               │   └───────────┘ └───────────┘ └───────────┘   │
               └───────────────────────────────────────────────┘
```

This building block augments the model's static training weights with three vital capabilities:
1. **Retrieval:** Fetching domain-specific facts or document passages dynamically.
2. **Tools:** Calling external APIs, database queries, calculators, or terminal commands.
3. **Memory:** Maintaining state and learning across interactions.

---

## Enterprise Multi-Tier Agent Architecture

Google Cloud's reference architecture [[S04, Agent architecture overview](#)] outlines the full enterprise stack required to run agents reliably at scale:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. User Interaction Layer                                               │
│    Chat interfaces, web applications, IDE extensions, CLI tools         │
├─────────────────────────────────────────────────────────────────────────┤
│ 2. Agent Orchestration Layer                                            │
│    - Frameworks: LangGraph, OpenAI Agents SDK, CrewAI, MS Agent Fwk     │
│    - Execution engine: State management, graph routing, error retry     │
├─────────────────────────────────────────────────────────────────────────┤
│ 3. Tool & Protocol Layer                                                │
│    - Model Context Protocol (MCP) servers, REST APIs, GraphQL, SQL      │
│    - Function calling schemas & parameter validators                    │
├─────────────────────────────────────────────────────────────────────────┤
│ 4. Memory & Storage Layer                                               │
│    - Short-term: Context scratchpad, in-memory thread checkpointers     │
│    - Long-term: Vector databases, relational DBs, graph stores         │
├─────────────────────────────────────────────────────────────────────────┤
│ 5. Foundation Model & Runtime Layer                                     │
│    - Inference endpoints (Vertex AI, Azure AI, OpenAI, Ollama)          │
│    - Model types: Fast routing models, reasoning models, multimodal     │
├─────────────────────────────────────────────────────────────────────────┤
│ 6. Governance, Safety & Observability Layer                             │
│    - Input/output guardrails, IAM least-privilege, audit logging        │
│    - OpenTelemetry, LangSmith tracing, execution sandboxing             │
└─────────────────────────────────────────────────────────────────────────┘
```

### Layer Breakdown & Responsibilities
1. **User Interaction Layer:** Translates user goals into agent sessions and renders step-by-step progress, tool outputs, and confirmations.
2. **Agent Orchestration Layer:** Maintains the execution loop, evaluates termination criteria, passes state between steps, and handles retries [[S06, Build with the Graph API](#)].
3. **Tool & Protocol Layer:** Standardizes how tools are discovered and invoked. Rather than custom bespoke wrappers, industry standards like **Model Context Protocol (MCP)** provide universal interoperability [[S04, Agent tools: MCP](#)], [[S08, In this article: Description](#)].
4. **Memory Layer:** Persists working context and enables retrieval across user sessions [[S04, Agent memory](#)].
5. **Model Runtime Layer:** Provides low-latency, scalable inference with appropriate context length and structured decoding support.
6. **Governance Layer:** Protects the host infrastructure from unauthorized commands, data leakage, and prompt injection attacks [[S04, Agent security and governance](#)], [[S05, Core concepts: Guardrails](#)].

---

## Citations & Evidence
- **[S03, Building block: The augmented LLM]:** Defines the augmented LLM combining foundational reasoning with retrieval and tools.
- **[S04, Agent architecture overview]:** Specifies the multi-layer enterprise architecture for robust agent systems.
- **[S05, Core concepts: Guardrails]:** Highlights the necessity of programmatic safety checks in the architecture stack.
- **[S06, LangGraph overview]:** Articulates low-level orchestration separated into state, nodes, and edges.

---

## Related Wiki Pages
- [What is an AI Agent?](../fundamentals/what-is-an-agent.md)
- [The Agent Loop](agent-loop.md)
- [Tools & Function Calling](tools-and-function-calling.md)
- [Memory & Context Management](memory-and-context.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
