# Source Evidence & Contradiction Registry

## Purpose
This registry provides an exhaustive mapping of factual claims, architectural assertions, and documented source disagreements across the AI Agents Learning Wiki. In compliance with the project's knowledge policy:
1. Every claim is assigned a persistent, traceable identifier (`CLM-001` through `CLM-018`).
2. Every claim links directly to a verified primary source and exact section locator.
3. Theoretical nuances and cross-source disagreements are recorded explicitly rather than silently merged.

---

## Master Claim Evidence Registry

| Claim ID | Source | Section Locator | Statement & Technical Finding | Claim Type | Disagreement Ref |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CLM-001** | [S01] | `2 ReAct: Synergizing Reasoning + Acting` | Interleaving reasoning traces ('thoughts') with task-specific actions ('actions') and external environment observations enables language models to overcome hallucination and maintain reliable multi-step plans. | Verified Fact | None |
| **CLM-002** | [S01] | `1 Introduction` | Chain-of-thought (CoT) reasoning without external action suffers from factual hallucination and error propagation in knowledge-intensive tasks. | Verified Fact | None |
| **CLM-003** | [S02] | `2 Approach` | Language models can learn to call external tools autonomously using self-supervised learning by generating potential API calls, executing them, and filtering based on whether tool outputs reduce language modeling perplexity on subsequent tokens. | Verified Fact | `CLM-008` |
| **CLM-004** | [S03] | `What are agents?` | Workflows and agents represent distinct architectural patterns: workflows orchestrate LLMs and tools via predefined, deterministic code paths, while agents dynamically direct their own processes and tool usage in autonomous loops. | Architectural Interpretation | `CLM-014` |
| **CLM-005** | [S03] | `When (and when not) to use agents` | Engineering teams should start with simple prompts, optimize with retrieval and few-shot examples, and only add agentic autonomy when deterministic workflows cannot handle the problem variability. | Verified Fact | None |
| **CLM-006** | [S03] | `Building block: The augmented LLM` | The foundational building block of agentic systems is the augmented LLM, which combines a core language model with retrieval capabilities, external tools, and memory. | Verified Fact | None |
| **CLM-007** | [S03] | `Building blocks, workflows, and agents` | Five core workflow patterns cover the majority of non-agentic LLM orchestration: Prompt Chaining, Routing, Parallelization (Sectioning/Voting), Orchestrator-Workers, and Evaluator-Optimizer. | Verified Fact | None |
| **CLM-008** | [S04] | `Agent architecture overview` | Production agentic AI architectures require modular enterprise layers: user interfaces, orchestration frameworks, tools and protocols (like MCP), short-term and long-term memory, foundation model runtimes, and governance/security controls. | Verified Fact | `CLM-003` (Qualified) |
| **CLM-009** | [S04] | `Agent memory` | Agent memory must be bifurcated into short-term memory (in-context conversation buffer and scratchpad) and long-term memory (external persistent storage such as vector, key-value, or document databases). | Verified Fact | None |
| **CLM-010** | [S04] | `Tool bloat` | Providing an agent with too many tools ('tool bloat') confuses model tool selection, increases token consumption and latency, and significantly expands the system attack surface. | Verified Fact | None |
| **CLM-011** | [S05] | `Core concepts: Agents` | An agent is defined as an autonomous entity encapsulating system instructions, a foundation model, and a scoped set of callable tools. | Verified Fact | None |
| **CLM-012** | [S05] | `Core concepts: Hand-offs` | Hand-offs enable multi-agent systems by allowing an active agent to pass conversation state and control authority directly to another specialized agent. | Verified Fact | `CLM-016` |
| **CLM-013** | [S05] | `Core concepts: Guardrails` | Guardrails execute programmatic safety checks before and after agent execution to detect malicious inputs, validate tool parameters, and sanitize generated outputs. | Verified Fact | None |
| **CLM-014** | [S06] | `Build with the Graph API` | LangGraph orchestrates stateful multi-actor applications by modeling workflows as graphs of shared typed state, compute nodes, and conditional edges. | Verified Fact | `CLM-004` |
| **CLM-015** | [S06] | `Capabilities: Persistence` | Durable execution with checkpointers allows graphs to snapshot state after every execution step, enabling automated recovery, time-travel debugging, and human-in-the-loop interruptions. | Verified Fact | None |
| **CLM-016** | [S07] | `Core Concepts: Agents, Tasks, Crews` | CrewAI models multi-agent collaboration through anthropomorphic role-playing personas defined by Role, Goal, and Backstory, organized into Crews that execute sequential or hierarchical processes. | Verified Fact | `CLM-012` |
| **CLM-017** | [S08] | `Why Agent Framework?` | Microsoft Agent Framework is the direct successor to both Semantic Kernel and AutoGen, unifying AutoGen's agent abstractions with Semantic Kernel's enterprise state management, telemetry, and middleware, while introducing graph workflows. | Verified Fact | AutoGen Legacy Note |
| **CLM-018** | [S08] | `When to use agents vs workflows` | If a task can be solved deterministically with a standard programmatic function, developers should use code rather than invoking an AI agent. | Verified Fact | None |

---

## Contradiction & Source Disagreement Register

When authoritative sources present conflicting terminologies, operational definitions, or architectural philosophies, the Wiki explicitly preserves both perspectives and explains the underlying drivers.

### Structure of the Disagreement Register:
The registry tracks **four thematic architectural disagreement categories**, spanning **five registered pairwise claim cross-references** (`CLM-003`, `CLM-004`, `CLM-012`, `CLM-014`, `CLM-016`) and **one historical succession qualification** (`CLM-017`):

### Disagreement Topic 1: Scope & Definition of "Agent" vs. "Workflow" (`CLM-004` vs. `CLM-014`)
- **Position A (Anthropic [S03, What are agents?], Microsoft [S08]):** Strict architectural dichotomy.
  - *Statement:* Workflows and agents are categorically distinct. Workflows are deterministic, predefined code execution paths; agents are autonomous model-driven execution loops. Anthropic and Microsoft urge engineers to prefer deterministic functions and workflows whenever possible.
- **Position B (LangChain / LangGraph [S06, Build with the Graph API]):** Unified continuum on a state graph.
  - *Statement:* Workflows and agents are not fundamentally distinct categories, but points on a single continuum implemented via the same computational primitives (State, Nodes, Edges). A deterministic workflow is simply a Directed Acyclic Graph (DAG), while an autonomous agent is a cyclical graph with conditional edges.
- **Synthesis & Technical Resolution:**
  - *Scope Difference:* Anthropic focuses on practical developer guidelines to avoid unnecessary autonomy. LangGraph provides an execution runtime capable of running both models.
  - *Conclusion:* In practice, production systems routinely blend both: deterministic DAGs route high-level stages, while cyclical agent loops handle sub-problems with open-ended search spaces.

### Disagreement Topic 2: Mechanism of Tool Usage (Inline Pretraining vs. Structured Function Calling) (`CLM-003` vs. `CLM-008`)
- **Position A (Toolformer [S02, Section 2]):** Self-supervised inline text tokens.
  - *Statement:* Tool calls are treated as continuous inline token sequences (e.g., `[Calculator(4*12) -> 48]`) learned during self-supervised model pretraining or fine-tuning based on language perplexity loss reduction.
  - *Limitation:* Does not support tool chaining or dynamic schema updates without model re-training.
- **Position B (Modern Industry Standard: Anthropic [S03], Google Cloud [S04], OpenAI [S05], LangGraph [S06], Microsoft [S08]):** Structured JSON Function Calling & Open Protocols (MCP).
  - *Statement:* Tool calling is handled dynamically at inference time using structured JSON schemas or standardized RPC protocols like Model Context Protocol (MCP). The model emits structured parameters, and an external host environment executes the tool.
- **Synthesis & Technical Resolution:**
  - *Evolutionary Shift:* Toolformer demonstrated the fundamental feasibility of self-taught tool use (2023). Industry practice (2024–2026) adopted runtime structured schema injection (Function Calling and MCP) to enable zero-shot tool addition without model fine-tuning.

### Disagreement Topic 3: Multi-Agent Organization Topologies (`CLM-016` vs. `CLM-012`)
- **Position A: Role-Playing Anthropomorphic Teams (CrewAI [S07, Core Concepts]):** Emphasizes natural-language personas (`role`, `goal`, `backstory`) executing sequential or hierarchical team plans. Highly intuitive for beginners and conceptual modeling.
- **Position B: Explicit Conversational Hand-offs (OpenAI Agents SDK [S05, Core concepts]):** Focuses on explicit delegation functions (`handoff_to_agent`) where control and context are routed cleanly between specialized agents without overhead.
- **Position C: Low-Level Stateful Graphs (LangGraph [S06, Build with the Graph API]):** Rejects rigid role-playing metaphors in favor of explicit state channels, conditional edge routers, and supervisor nodes.
- **Position D: Enterprise Middleware & Session Convergence (Microsoft Agent Framework [S08]):** Unifies AutoGen's conversational multi-agent patterns with Semantic Kernel's type-safe session management, OpenTelemetry, and enterprise guardrails.
- **Synthesis & Technical Resolution:**
  - These represent complementary layers of abstraction. Beginners often start with role-playing frameworks (CrewAI) for fast prototyping, while mission-critical enterprise systems favor explicit stateful graph orchestration (LangGraph) or enterprise-governed frameworks (Microsoft Agent Framework, OpenAI Agents SDK).

### Disagreement Topic 4: AutoGen Status & Legacy Migration (`CLM-017`)
- **Historical View (Archived Community Repositories / AutoGen 0.2):** AutoGen is frequently cited in earlier academic literature as an active multi-agent framework.
- **Authoritative Resolution (Microsoft Learn [S08, Why Agent Framework?]):** AutoGen (along with Semantic Kernel) has officially converged into the **Microsoft Agent Framework**. AutoGen 0.2 is in legacy maintenance; new enterprise developments are directed to Microsoft Agent Framework for unified state management, telemetry, and graph workflows.
