# OpenAI Agents SDK

## Summary
The **OpenAI Agents SDK** is OpenAI's official open-source library (available for Python and TypeScript) designed to build, run, and evaluate multi-agent workflows. Emphasizing clean, unbloated code abstractions, the SDK organizes agent applications around three core primitives: **Agents**, **Hand-offs**, and **Guardrails**, backed by integrated tracing hooks.

## Key Concepts
- **Agent Encapsulation:** Defining an agent as a clean object combining instructions, an LLM model, and a registered set of tools [[S05, Core concepts: Agents](#)].
- **Hand-offs:** Transferring conversational context and execution authority dynamically between specialized agents [[S05, Core concepts: Hand-offs](#)].
- **Guardrails:** Pre-execution and post-execution security checks that validate inputs and outputs against organizational policies and injection attacks [[S05, Core concepts: Guardrails](#)].
- **Tracing:** Native telemetry that captures agent loops, function calls, and hand-off sequences without manual logging hooks [[S05, Build with the SDK: Tracing](#)].

---

## Architectural Breakdown

### 1. Agent Definition
In the OpenAI Agents SDK, agents are modular and lightweight:
```python
from agents import Agent, Runner

def get_exchange_rate(currency: str) -> str:
    """Returns the current exchange rate for a given currency."""
    return f"1 USD = 0.92 {currency}"

forex_agent = Agent(
    name="ForexAgent",
    instructions="You are an expert currency conversion assistant.",
    tools=[get_exchange_rate],
    model="gpt-4o"
)
```

### 2. Multi-Agent Hand-offs
Rather than complex supervisor state reducers, the SDK models multi-agent delegation via **Hand-offs**. An agent can have other agents registered as potential destinations:
```python
from agents import Agent, handoff

triage_agent = Agent(
    name="TriageAgent",
    instructions="Determine user needs and delegate to the appropriate specialist.",
    handoffs=[forex_agent, billing_agent]
)

result = Runner.run_sync(triage_agent, "How many Euros can I get for 100 dollars?")
```
When `triage_agent` determines that the user is asking about currency exchange, it executes an automated handoff. The runner switches context to `forex_agent`, which invokes `get_exchange_rate` and completes the response.

### 3. Guardrails & Safety
Guardrails execute deterministically at turn boundaries:
- **Input Guardrails:** Scan the incoming prompt for jailbreaks, prompt injection, or disallowed terms before the LLM inference occurs.
- **Output Guardrails:** Inspect generated text and tool arguments before execution, verifying schema validity or compliance filters [[S05, Core concepts: Guardrails](#)].

---

## When to Use the OpenAI Agents SDK
- **Optimal Scenarios:** Conversational applications, customer support triage networks, and teams already committed to the OpenAI API ecosystem desiring clean, transparent Python or TypeScript code.
- **Suboptimal Scenarios:** Complex cyclic workflows requiring custom state persistence backends, long-running human approval queues with time-travel inspection, or multi-vendor open-source model runtimes (where LangGraph or Microsoft Agent Framework offer broader versatility).

---

## Citations & Evidence
- **[S05, Core concepts: Agents]:** Specifies the agent primitive combining instructions, models, and tools.
- **[S05, Core concepts: Hand-offs]:** Documents the hand-off delegation architecture.
- **[S05, Core concepts: Guardrails]:** Explains input and output guardrail enforcement.
- **[S05, Build with the SDK]:** Outlines the runner execution lifecycle and tracing support.

---

## Related Wiki Pages
- [Comprehensive Framework Comparison](comparison.md)
- [Multi-Agent Systems](../concepts/multi-agent-systems.md)
- [Safety, Guardrails, and Limitations](../safety/safety-and-limitations.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
