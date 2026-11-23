# Source Card: S04

## Metadata
- **Source ID:** S04
- **Title:** Choose your agentic AI architecture components
- **Authors:** Google Cloud Architecture Center Contributors
- **Publisher / Organization:** Google Cloud Documentation
- **Publication Date:** 2024-11-15 (Updated 2025/2026)
- **URL:** [https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Official enterprise architecture guidance

## Summary
Google Cloud's reference architecture provides an exhaustive taxonomy of components required to build, deploy, and govern agentic AI systems at enterprise scale. Rather than viewing agents as simple prompt wrappers, this architecture dissects the system into modular infrastructure layers.

Core architectural components:
1. **Agent Development Frameworks:** Evaluates LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, and Vertex AI Agent Builder.
2. **AI Models & Model Runtime:** Selecting foundation models (multimodal capabilities, context windows) and hosting infrastructure (Vertex AI, Cloud Run, GKE) with SLA, latency, and cost considerations.
3. **Agent Tools:**
   - Built-in tools vs. custom function tools.
   - Standardized tool protocols such as Model Context Protocol (MCP) and enterprise API gateways (Apigee).
   - **Tool Bloat:** Explicitly warns against offering too many tools to an LLM, which degrades selection accuracy, inflates token overhead, and introduces security attack surfaces.
4. **Agent Memory:**
   - *Short-Term Memory:* In-context conversation history and scratchpad buffers within an active execution session.
   - *Long-Term Memory:* External persistent stores (vector databases, relational databases, key-value stores, graph databases) for cross-session knowledge retention.
5. **Agent Design Patterns:** ReAct, Plan-and-Solve, Reflection, and Multi-Agent Collaboration.
6. **Agent Security & Governance:** Sandboxed runtimes, IAM least-privilege policies, prompt injection defenses, audit logging, and human-in-the-loop validation.

## Verified Section Structure
- **Agent architecture overview** — The systemic multi-tier stack for enterprise agent applications.
- **Agent development frameworks** — Comparative criteria for framework selection.
- **Frontend framework** — User interaction patterns and conversational interfaces.
- **Agent security and governance** — Isolation, identity management, and compliance controls.
- **Agent tools** — Subsections on Built-in tools, MCP, API management platform, Custom function tool, and Tool bloat.
- **Agent memory** — Subsections on Short-term memory and Long-term memory.
- **Agent design patterns** — ReAct, planning, reflection, and collaborative agent topologies.
- **AI models & Model runtime** — Model capabilities, inference scaling, and deployment runtimes.
- **Agent runtime** — Orchestration engines, state persistence, and operational monitoring.

## Key Claims & Evidence Locators
- **[S04, Agent architecture overview]:** Production agentic systems require a multi-layer stack encompassing user interfaces, orchestration frameworks, tools, memory stores, model runtimes, and governance infrastructure.
- **[S04, Short-term memory]:** Short-term memory resides within the model's active context window to maintain immediate conversation turns and working scratchpad data.
- **[S04, Long-term memory]:** Long-term memory requires external persistent data stores (such as vector databases or document stores) to persist user preferences and domain facts across sessions.
- **[S04, Tool bloat]:** Providing an agent with an excessive number of tools degrades tool selection accuracy, increases prompt latency, and expands the system's attack surface.
- **[S04, Agent security and governance]:** Agents executing arbitrary tools or code must operate in sandboxed environments with strict IAM permissions and human oversight.
