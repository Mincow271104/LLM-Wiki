# Source Card: S08

## Metadata
- **Source ID:** S08
- **Title:** Microsoft Agent Framework Overview
- **Authors:** Microsoft Learn AI Team
- **Publisher / Organization:** Microsoft Learn
- **Publication Date:** 2025-02-18 (Updated 2026)
- **URL:** [https://learn.microsoft.com/en-us/agent-framework/overview](https://learn.microsoft.com/en-us/agent-framework/overview)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Official documentation

## Summary
Microsoft Agent Framework is Microsoft's next-generation, enterprise-grade framework for building and orchestrating AI agents and multi-agent workflows. It explicitly represents the convergence and direct successor to two seminal open-source projects: **AutoGen** and **Semantic Kernel**.

Key architectural features and pillars:
1. **Convergence and Succession:**
   - AutoGen pioneered conversational multi-agent patterns and dynamic group chats.
   - Semantic Kernel established enterprise patterns: session-based state management, strong type safety, middleware filters, telemetry (OpenTelemetry), and broad model support.
   - Microsoft Agent Framework merges both codebases and conceptual models into a unified framework, adding explicit graph-based workflows and robust state persistence.
   - *Status of AutoGen:* AutoGen (especially 0.2) is recognized as a pioneering foundation that has transitioned into legacy/maintenance status, with the Microsoft Agent Framework serving as the forward-looking production standard.
2. **Four Primary Areas:**
   - *Agents:* Individual agents that use LLMs to process inputs, invoke tools, and connect to MCP servers.
   - *Harness Agent:* An opinionated, batteries-included agent specialized for long, multi-step tasks (planning, todo tracking, context compaction, file access, and persistent memory).
   - *Workflows:* Explicit functional and graph-based execution paths connecting agents and deterministic functions.
   - *Integrations & Enterprise Features:* Native model clients (OpenAI, Azure OpenAI, Anthropic, Ollama), session state management, middleware for intercepting actions, and OpenTelemetry instrumentation.
3. **Guidance on Agents vs. Workflows:**
   - *Use an agent when:* The task is open-ended or conversational, autonomous tool selection and planning are needed, and execution paths cannot be hardcoded.
   - *Use a workflow when:* The process has well-defined sequential steps, explicit execution order is required, and multiple agents or functions coordinate deterministically.
   - Explicit architectural rule: *"If you can write a function to handle the task, do that instead of using an AI agent."*

## Verified Section Structure
- **In this article** — Summary of the four primary areas (Agents, Harness Agent, Workflows, Integrations).
- **Get started** — Quickstart examples in .NET (`Microsoft.Agents.AI`), Python (`agent-framework`), and Go (`agent-framework-go`).
- **When to use agents vs workflows** — Pragmatic decision matrix comparing autonomy versus deterministic orchestration.
- **Why Agent Framework?** — Detailed historical lineage, explaining the synthesis of AutoGen's agent patterns with Semantic Kernel's enterprise foundation, and migration pathways.
- **Next steps** — Tutorials, documentation links, and enterprise governance guidelines.

## Key Claims & Evidence Locators
- **[S08, Why Agent Framework?]:** Microsoft Agent Framework is the direct successor to both Semantic Kernel and AutoGen, combining AutoGen's agent abstractions with Semantic Kernel's enterprise state management, middleware, and telemetry.
- **[S08, When to use agents vs workflows]:** Use agents for open-ended conversational tasks requiring dynamic planning; use workflows when execution order must be deterministic and predictable.
- **[S08, When to use agents vs workflows]:** "If you can write a function to handle the task, do that instead of using an AI agent."
- **[S08, In this article: Description]:** Agent Framework provides foundational building blocks including model clients, agent sessions for state management, context providers for memory, and MCP clients for tool integration.
- **[S08, In this article: Harness Agent]:** The Harness Agent provides batteries-included capabilities for complex multi-step tasks, including todo tracking, context compaction, and memory.
