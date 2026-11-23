# Source Card: S05

## Metadata
- **Source ID:** S05
- **Title:** Agents SDK
- **Authors:** OpenAI Developer Platform Team
- **Publisher / Organization:** OpenAI
- **Publication Date:** 2025-03-01
- **URL:** [https://developers.openai.com/api/docs/guides/agents/sdk](https://developers.openai.com/api/docs/guides/agents/sdk)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Official API documentation

## Summary
The OpenAI Agents SDK is an official multi-language library (Python and TypeScript) designed to help developers build, orchestrate, and deploy robust multi-agent systems. The SDK formalizes agents around explicit, minimal abstractions rather than complex nested wrappers.

Core abstractions and capabilities:
1. **Agent Definition:** An agent encapsulates instructions (system prompts), a target model (e.g., GPT-4o, o3-mini), and a list of callable tools (Python functions or schema-defined tools).
2. **Hand-offs:** A native mechanism enabling an agent to transfer control of a conversation or workflow to another specialized agent. Hand-offs preserve context while scoping tool access to the active agent.
3. **Guardrails:** Pre-execution and post-execution validation functions to enforce safety, check user permissions, validate outputs, and prevent prompt injection before calling tools or returning responses.
4. **Tracing & Observability:** Built-in tracing hooks to inspect agent loops, tool invocations, execution latency, and error states without requiring third-party modifications.
5. **Runtime Flexibility:** Supports running agents locally in native application code or hosting them on OpenAI-managed agent infrastructure.

## Verified Section Structure
- **Get your first agent running** — Quickstart walk-through defining a basic agent and executing a run.
- **Get the Agents SDK** — Links and installation guides for Python (`openai-agents-python`) and TypeScript (`openai-agents-js`).
- **Choose your starting point** — Comparative table recommending architecture paths based on use cases (single agent, multi-agent hand-offs, evaluations).
- **Build with the SDK** — In-depth guidance on tools, agent loops, hand-off mechanics, and context state management.
- **Compare agent runtime options** — Trade-offs between self-hosted agent runners and managed cloud agent infrastructure.
- **Core concepts** — Fundamental definitions of Agents, Hand-offs, Guardrails, and Tracing.

## Key Claims & Evidence Locators
- **[S05, Core concepts: Agents]:** An agent is a configured instance combining a model, specific instructions, and a scoped set of tools.
- **[S05, Core concepts: Hand-offs]:** Hand-offs allow an agent to transfer conversation state and execution authority directly to another specialized agent.
- **[S05, Core concepts: Guardrails]:** Guardrails provide programmatic safety boundaries that execute before or after an agent turn to detect jailbreaks, check policy compliance, or validate tool arguments.
- **[S05, Build with the SDK: Tracing]:** Built-in tracing captures every intermediate reasoning step, tool call, and hand-off transition for debugging and compliance.
