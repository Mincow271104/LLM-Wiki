# AI Agents Learning Wiki: Master Index

Welcome to the **AI Agents Learning Wiki**, an authoritative, beginner-friendly, and technically grounded knowledge base covering the concepts, architectures, and workflows of **AI Agents**.

Built upon the **Karpathy-inspired LLM Wiki architecture**, this repository maintains an interlinked compilation of verified academic literature, enterprise cloud architecture standards, and official framework documentation.

---

## Quick Navigation Hub

| Section | Key Topic Areas | Target Audience |
| :--- | :--- | :--- |
| **[Overview](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/overview.md)** | Executive Summary, Wiki Architecture, Learning Roadmap | All Readers |
| **[Evidence Registry](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/evidence-registry.md)** | Claim-Level Citations (`CLM-001`–`CLM-018`), Contradiction Register | Researchers & Reviewers |
| **[Terminology Glossary](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/glossary.md)** | Standard Definitions (ReAct, Loop, Checkpointer, MCP, Bloat) | Beginners |
| **[Operation Log](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/log.md)** | Append-only Chronological Audit Log of Wiki Modifications | Developers & Auditors |

---

## Structured Knowledge Map

```
AI AGENTS LEARNING WIKI
│
├── 1. FUNDAMENTALS
│   ├── [What is an AI Agent?](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/what-is-an-agent.md)
│   │   └─ Definition, agency spectrum, when to use (and when not to use) agents.
│   ├── [AI Agents vs. Traditional Chatbots](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/agents-vs-chatbots.md)
│   │   └─ Passive text generation vs. active environment mutation.
│   └── [LLM Foundations for Agents](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/llm-foundations.md)
│       └─ Autoregressive prediction, context windows, in-context learning, function calling.
│
├── 2. ARCHITECTURE
│   ├── [Agent Architecture Stack](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-architecture.md)
│   │   └─ The Augmented LLM building block and the multi-tier enterprise stack.
│   ├── [Memory and Context Management](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/memory-and-context.md)
│   │   └─ Short-term in-context buffers vs. persistent long-term storage (RAG, checkpointers).
│   ├── [Tools and Function Calling](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/tools-and-function-calling.md)
│   │   └─ Actuators, Toolformer lineage, JSON Schemas, MCP protocol, tool bloat risks.
│   └── [The Agent Loop: Control Flow](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/agent-loop.md)
│       └─ Sense-Think-Act-Observe cycle, bounded iteration limits, termination logic.
│
├── 3. CONCEPTS & ORCHESTRATION
│   ├── [Planning and Reasoning](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/planning-and-reasoning.md)
│   │   └─ Decomposition, Plan-and-Solve, reflection, evaluator-optimizer loops.
│   ├── [The ReAct Pattern](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/react-pattern.md)
│   │   └─ Synergizing reasoning traces with environmental actions to eliminate hallucination.
│   ├── [Workflows vs. Autonomous Agents](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/workflows-vs-agents.md)
│   │   └─ 5 canonical workflow patterns (chaining, routing, parallel, etc.) vs. agent loops.
│   ├── [Graph-Based Orchestration](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/graph-orchestration.md)
│   │   └─ State, Nodes, Edges, checkpointers, durable execution, time-travel debugging.
│   ├── [Single-Agent Systems](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/single-agent-systems.md)
│   │   └─ Unified context execution, cognitive limits, and architectural boundaries.
│   └── [Multi-Agent Systems](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/multi-agent-systems.md)
│       └─ Collaboration topologies (sequential, hierarchical, handoffs, group chats).
│
├── 4. FRAMEWORKS & COMPARISONS
│   ├── [Comprehensive Framework Comparison](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/comparison.md)
│   │   └─ Master matrix comparing OpenAI Agents SDK, LangGraph, CrewAI, and MS Agent Fwk.
│   ├── [OpenAI Agents SDK Deep Dive](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/openai-agents-sdk.md)
│   │   └─ Minimal agent encapsulation, function-driven hand-offs, native guardrails.
│   ├── [LangGraph Deep Dive](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/langgraph.md)
│   │   └─ Low-level state graphs, persistence, human-in-the-loop interrupts, streaming.
│   ├── [CrewAI Deep Dive](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/crewai.md)
│   │   └─ Role-playing agents (role, goal, backstory), sequential and hierarchical crews.
│   └── [Microsoft Agent Framework Deep Dive](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/microsoft-agent-framework.md)
│       └─ AutoGen & Semantic Kernel unification, Harness Agent, enterprise governance.
│
├── 5. PRACTICAL IMPLEMENTATION
│   └── [Educational Python Agent Example](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/implementation/python-agent-example.md)
│       └─ Runnable zero-dependency ReAct agent loop in pure standard-library Python.
│
└── 6. EVALUATION, SAFETY & LIMITATIONS
    ├── [Agent Evaluation and Benchmarking](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/safety/evaluation.md)
    │   └─ Task success rate, trajectory efficiency, benchmarks (HotpotQA, ALFWorld).
    └── [Safety, Guardrails, and Limitations](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/safety/safety-and-limitations.md)
        └─ Prompt injection defense, sandboxing, least privilege, compounding failure math.
```

---

## Curated Sources & Citation Identifiers

The knowledge in this Wiki is compiled strictly from the following eight verified primary sources:

1. **[S01] ReAct: Synergizing Reasoning and Acting in Language Models** — Yao et al., ICLR 2023. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S01-react.md)]
2. **[S02] Toolformer: Language Models Can Teach Themselves to Use Tools** — Schick et al., NeurIPS 2023. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S02-toolformer.md)]
3. **[S03] Building Effective Agents** — Anthropic Engineering, 2024. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S03-building-effective-agents.md)]
4. **[S04] Choose your agentic AI architecture components** — Google Cloud Architecture Center, 2024/2025. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S04-cloud-architecture-components.md)]
5. **[S05] Agents SDK** — OpenAI Developer Platform, 2025. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S05-openai-agents-sdk.md)]
6. **[S06] LangGraph Overview** — LangChain Engineering, 2024/2025. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S06-langgraph-overview.md)]
7. **[S07] CrewAI Documentation & Repository** — CrewAI Inc., 2023–2026. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S07-crewai-documentation.md)]
8. **[S08] Microsoft Agent Framework Overview** — Microsoft Learn, 2025/2026. [[Source Card](file:///e:/HƯ/ai-agents-wiki-assignment/raw/source-cards/S08-microsoft-agent-framework.md)]

Methodology Reference: **Andrej Karpathy - LLM Wiki** ([GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)).

---

## Operating on the Wiki

CLI automation scripts located in `scripts/`:
- **Query the Wiki:** `python scripts/query.py "How does ReAct prevent hallucinations?"`
- **Verify Integrity:** `python scripts/lint_wiki.py`
- **Ingest a Source:** `python scripts/ingest.py --source <source_json_or_url>`

*Last Updated: 2026-11-23*
