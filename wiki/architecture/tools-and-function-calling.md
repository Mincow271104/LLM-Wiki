# Tools and Function Calling

## Summary
Tools are the actuators of AI agents. They bridge the gap between static text prediction and real-world computation, enabling language models to query databases, compute mathematical operations, interact with software APIs, search the web, and execute terminal commands. From early academic experiments in self-taught tool use (Toolformer) to modern JSON Schema function calling and the Model Context Protocol (MCP), tool integration has matured into a foundational pillar of agentic engineering.

## Key Concepts
- **Actuators & Tools:** Software functions, web APIs, or database interfaces that an LLM can invoke with arguments to inspect or alter environment state [[S03, Building block: The augmented LLM](#)], [[S04, Agent tools](#)].
- **Structured Function Calling:** An inference mechanism where the LLM produces machine-readable structured arguments (typically JSON) strictly matching a registered schema [[S05, Build with the SDK](#)].
- **Model Context Protocol (MCP):** An open standard protocol created to unify how applications provide context and tools to LLMs safely and modularly [[S04, Agent tools: MCP](#)], [[S08, In this article: Description](#)].
- **Tool Bloat:** A common architectural anti-pattern where an agent is overloaded with excessive tools, degrading selection accuracy, bloating token consumption, and increasing attack surfaces [[S04, Tool bloat](#)].

---

## Evolution of Tool Use: From Inline Tokens to MCP

### 1. Self-Taught Inline Tool Invocation (Toolformer, 2023)
In the seminal Toolformer paper [[S02, Approach](#)], Timo Schick et al. demonstrated that language models can autonomously teach themselves when and how to call external tools. Toolformer formulated tool calls as inline text tokens inserted into autoregressive generation:
$$\dots \text{The capital of France is } [\text{Search}(\text{"capital of France"}) \to \text{"Paris"}] \text{ Paris} \dots$$

Candidate API calls were generated using in-context few-shot prompts, executed, and filtered based on whether the API output reduced the model's token-level perplexity. While groundbreaking, this inline approach required fine-tuning the model weights and made dynamic tool registration difficult [[S02, Limitations](#)].

### 2. Structured JSON Function Calling (2023–Present)
Modern foundation models (OpenAI, Anthropic, Google Gemini) shifted tool calling to the API orchestration layer:
1. The developer passes a list of tool definitions (names, descriptions, and JSON Schemas specifying required parameters) in the API request.
2. The model reasons over the user request and decides whether to output regular conversational text or a structured `tool_calls` payload.
3. The host application parses the JSON arguments, executes the local Python or REST function, and returns the result in a `tool` role message [[S05, Build with the SDK](#)].

### 3. Model Context Protocol (MCP) (2024–Present)
As enterprise ecosystems scaled, maintaining bespoke tool integration code for every API became unmaintainable. The **Model Context Protocol (MCP)** emerged as an open standard enabling agents to connect to local or remote tool servers using standardized RPC endpoints. Major enterprise frameworks—including Google Cloud [[S04, Agent tools: MCP](#)] and Microsoft Agent Framework [[S08, In this article: Description](#)]—now natively support MCP client integration.

---

## Anatomy of a Production Tool Definition

A robust tool definition requires three essential elements [[S03, Appendix 2: Prompt engineering your tools](#)]:
1. **Name:** A descriptive, snake_case identifier (e.g., `get_weather_forecast`).
2. **Detailed Description:** Clear instructions specifying *when* the tool should be used, *what* it does, and *what limitations* it has.
3. **Strict Parameter Schema:** A JSON Schema declaring data types, allowed values, default values, and parameter descriptions.

```json
{
  "name": "calculate_compound_interest",
  "description": "Calculates the future value of an investment based on principal, annual interest rate, compounding frequency, and years.",
  "parameters": {
    "type": "object",
    "properties": {
      "principal": { "type": "number", "description": "Initial investment amount in USD." },
      "annual_rate": { "type": "number", "description": "Annual interest rate expressed as a decimal (e.g., 0.05 for 5%)." },
      "compounding_frequency": { "type": "integer", "description": "Number of times interest is compounded per year (e.g., 12 for monthly)." },
      "years": { "type": "number", "description": "Investment duration in years." }
    },
    "required": ["principal", "annual_rate", "compounding_frequency", "years"]
  }
}
```

---

## The Danger of Tool Bloat

Google Cloud's architecture guide [[S04, Tool bloat](#)] identifies **Tool Bloat** as one of the most pervasive failure modes in agent design:
- **Degraded Selection Accuracy:** When presented with 50+ tools with overlapping descriptions, LLMs frequently pick suboptimal or incorrect tools.
- **Latency & Token Overhead:** Injecting dozens of extensive JSON Schemas into the system prompt consumes thousands of tokens on every forward pass, driving up costs and response times.
- **Security Attack Surface:** Every tool exposed to an agent is a potential vector for privilege escalation or unintended destructive actions.

### Mitigation Strategies:
1. **Tool Routing:** Use a lightweight classification model to select a small subset of relevant tools (3–5 tools) before invoking the primary reasoning model [[S03, Workflow: Routing](#)].
2. **Hierarchical Multi-Agent Delegation:** Distribute tools across specialized domain agents (e.g., a Database Agent, a Web Search Agent) and route requests via hand-offs [[S05, Core concepts: Hand-offs](#)], [[S07, Why CrewAI?](#)].
3. **Dynamic MCP Tool Discovery:** Query an MCP catalog dynamically based on user intent rather than loading all schemas into every prompt.

---

## Citations & Evidence
- **[S02, Approach & Limitations]:** Toolformer establishes self-supervised API calling but notes limitations in chaining and dynamic execution.
- **[S03, Appendix 2: Prompt engineering your tools]:** Anthropic emphasizes that tool schemas require rigorous prompt engineering to prevent model misinterpretation.
- **[S04, Agent tools & Tool bloat]:** Google Cloud documents the enterprise tool taxonomy (built-in, MCP, custom) and cautions against tool bloat.
- **[S05, Build with the SDK]:** OpenAI outlines structured function calling within the Agents SDK.
- **[S08, In this article: Description]:** Microsoft Agent Framework natively integrates MCP clients for secure tool execution.

---

## Related Wiki Pages
- [Agent Architecture Stack](agent-architecture.md)
- [The Agent Loop](agent-loop.md)
- [Safety, Guardrails, and Limitations](../safety/safety-and-limitations.md)
- [Educational Python Agent Example](../implementation/python-agent-example.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
