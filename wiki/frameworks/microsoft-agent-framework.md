# Microsoft Agent Framework

## Summary
The **Microsoft Agent Framework** is Microsoft's next-generation, enterprise-grade platform for building, orchestrating, and securing AI agents and multi-agent workflows. Developed by the engineering teams behind **AutoGen** and **Semantic Kernel**, the framework represents the official convergence and direct successor to both pioneering projects. It combines AutoGen's flexible multi-agent conversational patterns with Semantic Kernel's enterprise state management, type safety, middleware filters, and OpenTelemetry instrumentation, while adding native graph-based workflows.

## Key Concepts
- **Convergence & Succession:** The official evolutionary transition from AutoGen and Semantic Kernel into a single unified enterprise standard [[S08, Why Agent Framework?](#)].
- **Four Primary Pillars:** Individual Agents, the opinionated Harness Agent, deterministic Workflows, and comprehensive Integrations [[S08, In this article: Description](#)].
- **Harness Agent:** A batteries-included agent specialized for complex, multi-step tasks equipped with native planning, todo tracking, context compaction, and memory [[S08, In this article: Harness Agent](#)].
- **The Pragmatic Workflow Rule:** An explicit architectural directive: *"If you can write a function to handle the task, do that instead of using an AI agent"* [[S08, When to use agents vs workflows](#)].

---

## Architectural Breakdown

### 1. The Four Primary Pillars
As documented in the official architecture [[S08, In this article: Description](#)], Microsoft Agent Framework organizes enterprise capabilities into four pillars:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      Microsoft Agent Framework                         │
├──────────────────┬──────────────────┬─────────────────┬────────────────┤
│ 1. Agents        │ 2. Harness Agent │ 3. Workflows    │ 4. Integrations│
│ Single LLM units │ Batteries-inc.   │ Functional and  │ Azure AI,      │
│ calling tools &  │ long-running     │ graph execution │ Foundry, MCP,  │
│ MCP servers      │ tasks & todos    │ paths & routers │ OTEL, Auth     │
└──────────────────┴──────────────────┴─────────────────┴────────────────┘
```

1. **Agents:** Individual autonomous agents supporting multiple providers (Azure OpenAI, OpenAI, Anthropic, Ollama) and standardized protocols (MCP).
2. **Harness Agent:** An opinionated agent with built-in planning, task checklist (todo) tracking, context compaction, persistent memory, and "don't-ask-again" tool approvals [[S08, In this article: Harness Agent](#)].
3. **Workflows:** Graph-based and functional pipelines that connect agents and deterministic code functions through explicit execution order.
4. **Integrations:** Enterprise middleware, identity providers (Azure Identity / IAM), OpenTelemetry tracing, and user interface connectors.

### 2. Multi-Language SDK Ecosystem
Unlike frameworks restricted to Python, Microsoft Agent Framework provides enterprise first-class support across three major languages [[S08, Get started](#)]:
- **C# / .NET:** (`Microsoft.Agents.AI`) with strong type safety, ASP.NET Core integration, and dependency injection.
- **Python:** (`agent-framework`) for rapid data science and AI development.
- **Go:** (`agent-framework-go`) for high-concurrency cloud infrastructure and microservices.

### 3. Python Quickstart Example
```python
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

agent = Agent(
    client=FoundryChatClient(
        project_endpoint="https://your-foundry-service.services.ai.azure.com/api/projects/sample",
        model="gpt-5.4-mini",
        credential=AzureCliCredential()
    ),
    name="EnterpriseSupportAgent",
    instructions="You are an enterprise support assistant. Keep answers concise."
)

result = await agent.run("What are the company's retention guidelines?")
print(result)
```

---

## AutoGen Lineage, Historical Context, and Legacy Status

Understanding the transition from AutoGen is critical for technical teams:

1. **Pioneering Innovations of AutoGen (0.2):** Introduced multi-agent conversation patterns (`AssistantAgent`, `UserProxyAgent`, `GroupChatManager`), demonstrating that collaborative LLMs could solve coding benchmarks autonomously.
2. **Enterprise Limitations of Legacy AutoGen:** Early AutoGen suffered from conversational deadlocks, unconstrained looping, lack of strict type safety, missing enterprise telemetry, and fragile session state persistence.
3. **The Unification:** Microsoft engineered the Agent Framework to combine AutoGen's conversational simplicity with Semantic Kernel's enterprise backbone (sessions, middleware, filters, vector stores).
4. **Current Status:** AutoGen 0.2 is in legacy maintenance. Microsoft explicitly directs new enterprise development to the **Microsoft Agent Framework** [[S08, Why Agent Framework?](#)].

---

## Citations & Evidence
- **[S08, Why Agent Framework?]:** Explicitly designates Agent Framework as the direct successor to both Semantic Kernel and AutoGen.
- **[S08, In this article: Description & Harness Agent]:** Details the four pillars, MCP client integration, and Harness Agent capabilities.
- **[S08, When to use agents vs workflows]:** Documents the decision matrix and rule prioritizing programmatic functions over agents.
- **[S08, Get started]:** Specifies installation and code samples across .NET, Python, and Go.

---

## Related Wiki Pages
- [Comprehensive Framework Comparison](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/frameworks/comparison.md)
- [Workflows vs. Autonomous Agents](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/workflows-vs-agents.md)
- [Multi-Agent Systems](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/multi-agent-systems.md)
- [Wiki Master Index](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/index.md)

*Last Updated: 2026-11-23*
