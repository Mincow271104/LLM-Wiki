# Glossary of AI Agent Concepts

## Purpose
This glossary provides clear, standardized academic and engineering definitions for essential concepts across the AI Agent landscape. Each entry includes its standard definition, operational role, and source citations.

---

### A
- **Agent:** An autonomous or semi-autonomous software system combining a foundation model (LLM), instructions, and a set of tools to pursue specified goals across multiple interaction turns [[S03, What are agents?](#)], [[S05, Core concepts: Agents](#)].
- **Agent Loop:** The iterative execution cycle (Sense → Plan/Reason → Act → Observe) through which an agent evaluates current state, selects an action or tool, executes it, inspects the result, and repeats until the objective is accomplished or terminated [[S01, Section 2](#)], [[S04, Agent design patterns](#)].
- **Augmented LLM:** The foundational computational building block consisting of a core language model enhanced with external tools, retrieval mechanisms, and persistent memory [[S03, Building block: The augmented LLM](#)].
- **AutoGen:** A pioneering open-source multi-agent framework developed by Microsoft that introduced conversational multi-agent patterns. Currently transitioned into legacy/maintenance status, succeeded by the Microsoft Agent Framework [[S08, Why Agent Framework?](#)].

### C
- **Checkpointer:** A state persistence mechanism (prominently implemented in LangGraph) that saves complete state snapshots after every graph step, enabling crash resilience, human approval pauses, and time-travel debugging [[S06, Capabilities: Persistence](#)].
- **Conditional Edge:** In graph-based orchestration, a control-flow route whose destination node is evaluated dynamically at runtime based on the contents of the shared graph state [[S06, Build with the Graph API: Graph API](#)].
- **Context Window:** The maximum token capacity a language model can process in a single inference call, encompassing system prompts, memory, retrieved documents, and tool outputs [[S04, Agent memory](#)].
- **Crew:** In CrewAI, the top-level container encapsulating a set of specialized agents, their assigned tasks, and an execution process (Sequential or Hierarchical) [[S07, Core Concepts: Agents, Tasks, Crews](#)].

### E
- **Evaluator-Optimizer Pattern:** A dual-LLM architectural workflow where a generator model produces an output or solution, and an evaluator model critiques it, driving iterative refinement until quality thresholds are met [[S03, Workflow: Evaluator-optimizer](#)].

### F
- **Function Calling:** A mechanism whereby a language model outputs a structured JSON object specifying an API or function name and its arguments, allowing an external execution runtime to execute real code on the model's behalf [[S04, Agent tools](#)], [[S05, Build with the SDK](#)].

### G
- **Guardrail:** Programmatic safety, security, and schema validation checks executed immediately before an agent turn (input guardrail) or after an agent turn (output guardrail) to intercept prompt injection, policy violations, or unsafe tool parameters [[S05, Core concepts: Guardrails](#)], [[S04, Agent security and governance](#)].

### H
- **Handoff:** A pattern and SDK primitive enabling an active agent to transfer conversation state and execution authority directly to another specialized agent [[S05, Core concepts: Hand-offs](#)].
- **Harness Agent:** An opinionated, batteries-included agent implementation within Microsoft Agent Framework equipped with native planning, todo tracking, context compaction, and memory for long-running tasks [[S08, In this article: Harness Agent](#)].
- **Human-in-the-Loop (HITL):** An architectural design pattern where execution is deterministically paused before sensitive actions (e.g., executing code, modifying databases, making financial transactions) so a human operator can inspect, approve, edit, or reject the action [[S06, Capabilities: Human-in-the-loop](#)], [[S04, Agent security and governance](#)].

### L
- **Long-Term Memory:** Persistent storage (such as vector databases, relational databases, or document stores) maintained outside the active LLM context window to retain facts, user preferences, and historical task executions across distinct sessions [[S04, Long-term memory](#)], [[S07, Key Features: Memory](#)].

### M
- **Model Context Protocol (MCP):** An open standard protocol for securely connecting AI models and agents to external data sources, enterprise tools, and environment services without writing custom bespoke glue code [[S04, Agent tools: MCP](#)], [[S08, In this article: Description](#)].
- **Multi-Agent System (MAS):** An architecture in which multiple specialized agents collaborate, communicate, or divide labor to solve complex problems beyond the scope of a single generalist agent [[S07, Why CrewAI?](#)], [[S08, Agent Framework brings together four primary areas](#)].

### O
- **Orchestration:** The coordination layer that controls how agents and workflows invoke models, call tools, transition state, and handle errors [[S04, Agent runtime](#)], [[S06, LangGraph overview](#)].
- **Orchestrator-Workers Pattern:** A workflow pattern where a central supervisor LLM dynamically breaks a complex task into discrete subtasks, dispatches them to parallel worker LLMs, and synthesizes the returned results [[S03, Workflow: Orchestrator-workers](#)].

### P
- **Prompt Chaining:** A sequential workflow pattern where a complex task is decomposed into fixed steps, with the output of one LLM call acting as the input to the next [[S03, Workflow: Prompt chaining](#)].

### R
- **ReAct (Reasoning + Acting):** A paradigm combining chain-of-thought reasoning with external environment actions. The model alternates between generating thoughts (to track and update plans) and actions (to query external systems), receiving environment observations before taking subsequent steps [[S01, Section 2](#)].
- **Routing Pattern:** A workflow pattern that classifies incoming requests and directs them to specialized downstream prompts, agents, or tools [[S03, Workflow: Routing](#)].

### S
- **Short-Term Memory:** Working memory maintained within the model's active context window, including the current conversation thread, scratchpad observations, and recent tool outputs [[S04, Short-term memory](#)].
- **State:** A shared, typed data structure (e.g., Pydantic schema or TypedDict in LangGraph) representing the current knowledge, history, and variables of an agentic workflow [[S06, Build with the Graph API: Graph API](#)].

### T
- **Time Travel:** A capability provided by stateful graph runtimes (such as LangGraph) allowing developers or humans-in-the-loop to inspect past states, modify state variables, and re-execute execution branches from any historical checkpoint [[S06, Capabilities: Persistence](#)].
- **Tool Bloat:** A pathological condition where an agent is configured with too many tools, resulting in degraded reasoning, increased tool selection errors, higher token costs, and increased security exposure [[S04, Tool bloat](#)].
- **Toolformer:** A pioneering self-supervised training approach where language models learn when and how to call external APIs by inserting candidate calls into text and filtering based on language modeling loss reduction [[S02, Section 2](#)].

### W
- **Workflow:** An LLM-powered system where execution paths and tool invocations are orchestrated through deterministic, predefined code paths rather than open-ended model self-direction [[S03, What are agents?](#)], [[S08, When to use agents vs workflows](#)].
