# Memory and Context Management

## Summary
Memory enables AI agents to transcend stateless forward passes, allowing them to recall historical interactions, maintain intermediate task progress, track entity states, and accumulate knowledge over time. Production agent architectures bifurcate memory into **Short-Term Memory** (in-context buffers and scratchpads) and **Long-Term Memory** (external persistent databases), each serving distinct operational roles.

## Key Concepts
- **Short-Term Memory:** Transient working context maintained within the model's active context window, capturing immediate conversation turns and execution scratchpads [[S04, Short-term memory](#)].
- **Long-Term Memory:** Persistent storage maintained across sessions and threads using vector databases, key-value stores, or knowledge graphs [[S04, Long-term memory](#)], [[S07, Key Features: Memory](#)].
- **Checkpointers & Thread State:** Deterministic state snapshots saved after every execution step, enabling crash resilience, time-travel debugging, and state inspection [[S06, Capabilities: Persistence](#)].
- **Context Compaction & Summarization:** Techniques to compress or prune old conversational tokens to prevent context window saturation while preserving critical task variables [[S08, In this article: Harness Agent](#)].

---

## The Two-Tier Memory Architecture

Google Cloud's reference architecture [[S04, Agent memory](#)] and modern agent frameworks establish a clear separation of memory tiers:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           AI Agent Execution                            │
└───────────────────┬─────────────────────────────────┬───────────────────┘
                    │                                 │
     Active Context Window (RAM)           External Persistence (Disk/DB)
                    ▼                                 ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────┐
│           Short-Term Memory           │ │       Long-Term Memory        │
│  - System Prompt & Active Tools       │ │  - Vector Database (RAG)      │
│  - Working Scratchpad (Thoughts)      │ │  - Key-Value User Store       │
│  - Recent Tool Observations           │ │  - Entity Knowledge Graph     │
│  - Checkpointer State Snapshots       │ │  - Historical Task Logs       │
└───────────────────────────────────────┘ └───────────────────────────────┘
```

### 1. Short-Term Memory (In-Context Working Memory)
Short-term memory corresponds to the model's immediate working consciousness:
- **Scope:** Bounded strictly by the model's context window limit (e.g., 128k, 1M, or 2M tokens).
- **Contents:** Current user request, active tool schemas, intermediate thought traces, and the raw outputs of recent tool calls [[S01, Section 2](#)].
- **Lifespan:** Active execution session or thread.
- **Management Techniques:**
  - *Sliding Windows:* Discarding older interaction turns when approaching token thresholds.
  - *Compaction & Summarization:* Periodically prompting an LLM to distill the preceding 20 turns into a concise factual summary [[S08, In this article: Harness Agent](#)].
  - *Selective Pruning:* Retaining tool call definitions while truncating voluminous tool outputs (such as massive JSON payloads).

### 2. Long-Term Memory (Persistent Storage)
Long-term memory provides durability across restarts, sessions, and multi-day workflows:
- **Semantic / Episodic Memory:** Storing prior task summaries, user preferences, and solutions in a vector database. When a new prompt arrives, the agent queries the vector store to retrieve semantically relevant historical context [[S04, Long-term memory](#)], [[S07, Key Features: Memory](#)].
- **Entity Memory:** Tracking attributes of specific real-world entities (users, project names, servers, code modules) across time, frequently implemented via key-value stores or knowledge graphs [[S07, Key Features: Memory](#)].
- **Thread Stores:** As implemented in LangGraph, cross-thread stores allow one agent execution thread to write persistent memories that other threads or future sessions can retrieve [[S06, Capabilities: Persistence](#)].

---

## Comparison of Memory Implementations Across Frameworks

| Framework | Short-Term Memory Mechanism | Long-Term Memory Mechanism |
| :--- | :--- | :--- |
| **LangGraph** [S06] | Checkpointers (Sqlite, Postgres) saving TypedDict/Pydantic graph state at every super-step. | BaseStore / Cross-thread key-value and document namespaces. |
| **CrewAI** [S07] | In-memory message history and local short-term RAG buffer. | Chroma/embedding-backed persistent episodic storage and entity memory. |
| **Microsoft Agent Framework** [S08] | Session-based state management, Harness Agent context compaction. | Context providers interfacing with vector stores and Azure AI Search. |
| **OpenAI Agents SDK** [S05] | In-memory conversation state passed along hand-off chains. | External database integration via custom tools or developer storage. |

---

## Engineering Challenges in Agent Memory

1. **Memory Drift & Poisoning:** If an agent encounters a hallucinated or erroneous tool output and persists it into long-term memory, future agent runs will treat the corrupted data as verified truth.
2. **Context Dilution ("Lost in the Middle"):** While context windows have expanded dramatically, empirical research reveals that model attention and reasoning quality degrade when key information is buried within hundreds of thousands of irrelevant tokens.
3. **Privacy & Data Governance:** Long-term memory stores must respect user data deletion requests (GDPR right to be forgotten) and enforce strict tenant isolation in enterprise deployments [[S04, Agent security and governance](#)].

---

## Citations & Evidence
- **[S01, Section 2]:** Yao et al. emphasize how observation tokens in short-term context enable dynamic plan adjustments.
- **[S04, Short-term memory & Long-term memory]:** Google Cloud establishes the architectural taxonomy separating in-context memory from persistent database memory.
- **[S06, Capabilities: Persistence]:** LangGraph specifies checkpointers for step-by-step durable state and thread recovery.
- **[S07, Key Features: Memory]:** CrewAI documents short-term, long-term, and entity memory systems.
- **[S08, In this article: Harness Agent]:** Microsoft highlights automated context compaction for long-running agent tasks.

---

## Related Wiki Pages
- [Agent Architecture Stack](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-architecture.md)
- [The Agent Loop](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-loop.md)
- [Graph-Based Orchestration](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/graph-orchestration.md)
- [Wiki Master Index](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/index.md)

*Last Updated: 2026-11-23*
