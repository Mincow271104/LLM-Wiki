# LLM Foundations for Agents

## Summary
Large Language Models (LLMs) serve as the computational cognitive core of AI agents. Understanding the capabilities and constraints of modern LLMs—including autoregressive token generation, context windows, in-context learning, instruction tuning, and structured JSON output—is essential for designing reliable agentic workflows.

## Key Concepts
- **Autoregressive Generation:** Generating text token-by-token conditioned on prior context, meaning reasoning emerges through generated tokens (e.g., scratchpads, thoughts) [[S01, Section 2](#)].
- **Context Window Dynamics:** The finite token budget accommodating system prompts, tool schemas, retrieved knowledge, and conversation history [[S04, Agent memory](#)].
- **In-Context Learning (ICL):** The model's ability to adapt to task specifications and few-shot tool examples without updating underlying neural weights [[S02, Section 2](#)].
- **Structured Output & Schema Conformance:** Generating machine-readable outputs (such as JSON) strictly conforming to predefined schemas for reliable tool execution [[S05, Build with the SDK](#)].

---

## The Role of the LLM in an Agent System

In an agent architecture, the LLM is not merely a generator of conversational prose; it functions as an **instruction-following reasoning engine** and **semantic router** [[S03, Building block: The augmented LLM](#)]. The LLM performs four foundational functions:

```
                  ┌─────────────────────────────────────────┐
                  │          Foundation Model Core          │
                  └──────┬────────────┬────────────┬────────┘
                         │            │            │
          ┌──────────────▼───┐  ┌─────▼─────┐  ┌───▼──────────────┐
          │  Reasoning &     │  │ Tool Call │  │ State Evaluation │
          │  Decomposition   │  │ Decision  │  │ & Self-Critique  │
          └──────────────────┘  └───────────┘  └──────────────────┘
```

1. **Task Decomposition:** Translating ambiguous human goals into structured subtasks.
2. **Tool Selection & Parameter Extraction:** Evaluating available tool schemas, choosing the appropriate tool, and populating exact arguments from context [[S02, Section 3](#)], [[S05, Build with the SDK](#)].
3. **Observation Synthesis:** Interpreting the textual or numerical output returned by a tool and deciding how it impacts the broader objective [[S01, Section 2](#)].
4. **Self-Critique & Termination:** Assessing whether the intermediate results satisfy the user's criteria or require further iterations [[S03, Workflow: Evaluator-optimizer](#)].

---

## Critical LLM Capabilities Required for Agents

### 1. Chain-of-Thought & Working Scratchpads
Because transformer models perform a fixed amount of computation per generated token, complex multi-step reasoning cannot happen in a single step. Forcing the model to output intermediate "thinking" tokens (a scratchpad) provides computational working space, allowing the model to decompose logic and correct course before executing actions [[S01, Section 2](#)].

### 2. Instruction Adherence & System Prompts
An agent depends heavily on its system prompt (persona, instructions, and rules). Frontier models are fine-tuned with Reinforcement Learning from Human Feedback (RLHF) and Reinforcement Learning from AI Feedback (RLAIF) to prioritize developer instructions, resist prompt injection, and respect operational boundaries [[S04, Agent security and governance](#)], [[S05, Core concepts: Guardrails](#)].

### 3. Structured Function Calling
Early agent systems (e.g., early LangChain implementations) relied on regex parsing of unstructured text output to extract tool commands (such as `Action: search[term]`). This was fragile and prone to parsing errors. Modern LLMs support native **Function Calling**, where models are fine-tuned to emit valid JSON objects conforming to JSON Schema specifications, drastically improving reliability in production pipelines [[S04, Agent tools: Custom function tool](#)], [[S05, Build with the SDK](#)].

---

## Inherent LLM Limitations Impacting Agents

While LLMs are remarkably versatile, their architectural properties introduce key challenges:
- **Context Window Exhaustion:** Multi-turn agent loops accumulate long histories of tool outputs, risking context saturation, high token costs, and attention dilution ("lost in the middle") [[S04, Agent memory](#)].
- **Stochasticity & Nondeterminism:** Unless temperature is set to zero (and even then on distributed inference hardware), identical prompts can yield varying execution trajectories, necessitating defensive parsing and retry logic.
- **Parametric Hallucination:** LLMs can fabricate plausible-sounding facts when lacking grounded data, which is why external grounding via ReAct or retrieval tools is required [[S01, Section 1](#)].

---

## Citations & Evidence
- **[S01, Section 2]:** Yao et al. formalize how generating thought tokens in the generation stream enables multi-step planning and error recovery.
- **[S02, Section 2]:** Schick et al. demonstrate that self-supervised in-context learning enables models to identify API call opportunities.
- **[S03, Building block: The augmented LLM]:** Anthropic outlines the augmented LLM as the fundamental foundation of agentic architecture.
- **[S04, Agent memory]:** Google Cloud emphasizes context window constraints as the primary driver for tiered memory architectures.

---

## Related Wiki Pages
- [What is an AI Agent?](what-is-an-agent.md)
- [Tools & Function Calling](../architecture/tools-and-function-calling.md)
- [The ReAct Pattern](../concepts/react-pattern.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
