# What is an AI Agent?

## Summary
An **AI Agent** is an autonomous or semi-autonomous computation system powered by a foundation model (such as a Large Language Model) that observes its environment, reasons about objectives, formulates multi-step plans, executes actions via external tools, and dynamically adjusts its behavior based on observed outcomes until it satisfies a specified goal.

## Key Concepts
- **Agency:** The capacity of an entity to act autonomously upon an environment to achieve an intended objective.
- **Augmented Intelligence:** Coupling neural language models with deterministic tools, external databases, and stateful memory [[S03, Building block: The augmented LLM](#)].
- **Perception-Action Loop:** The continuous cycle of taking input from the environment, processing it through an internal reasoning engine, and producing an action that alters environment state [[S01, Section 2](#)].
- **The Simplicity Principle:** An engineering guideline asserting that deterministic programmatic functions should be preferred over stochastic agents whenever a task has well-defined, predictable execution steps [[S03, When (and when not) to use agents](#)], [[S08, When to use agents vs workflows](#)].

---

## Detailed Explanation

### 1. Defining the Modern AI Agent
Historically, artificial intelligence defined an "agent" as any entity that perceives its environment through sensors and acts upon that environment through actuators (Russell & Norvig). In modern Generative AI, this concept has evolved: the **core reasoning engine** is now a Large Language Model (LLM) or Multimodal Foundation Model.

An AI Agent is characterized by four foundational capabilities:
1. **Goal Formulation & Context Understanding:** The agent receives high-level user instructions and decomposes them into executable intents [[S05, Core concepts: Agents](#)].
2. **Environment Grounding:** Through external tools and APIs, the agent interacts with live data sources, filesystems, search engines, and enterprise services [[S04, Agent tools](#)].
3. **Autonomous Reasoning & Planning:** Rather than following a rigid script, the agent dynamically decides what actions to take, assesses intermediate progress, and updates its strategy [[S01, Section 2](#)].
4. **State & Memory Management:** The agent maintains context across multiple steps and sessions, learning from prior errors and adapting to changing conditions [[S04, Agent memory](#)].

### 2. The Autonomy Spectrum
Autonomy in AI systems is not binary; it exists along a spectrum:
- **Level 0 (Static Prompts):** A single prompt produces a single completion with no external actions.
- **Level 1 (Prompt Workflows):** Deterministic code chains multiple LLM calls together (e.g., Prompt Chaining or Routing) where branching logic is hardcoded [[S03, Building blocks, workflows, and agents](#)].
- **Level 2 (Tool-Augmented Model):** An LLM makes one-off tool calls to retrieve information or calculate values before generating an answer.
- **Level 3 (Autonomous Agent):** An LLM operates within an iterative loop, deciding dynamically which tools to invoke, inspecting results, adjusting intermediate hypotheses, and deciding when the goal has been met [[S03, What are agents?](#)].
- **Level 4 (Multi-Agent Systems):** Multiple autonomous agents with specialized roles coordinate, negotiate, and delegate subtasks to complete complex missions [[S07, Why CrewAI?](#)], [[S08, Agent Framework brings together four primary areas](#)].

```
  Static Prompt ──> Deterministic Workflow ──> Tool-Augmented LLM ──> Autonomous Agent ──> Multi-Agent System
   (Zero loops)       (Hardcoded DAG)          (Single tool call)       (Dynamic loop)      (Collaborative team)
```

### 3. When to Use (and When Not to Use) AI Agents
A critical insight shared by leading AI research and engineering groups (Anthropic, Google Cloud, Microsoft) is that **agents should not be used indiscriminately**:
- **Use an agent when:** The problem domain is open-ended, the sequence of necessary steps cannot be predetermined, the environment is dynamic, or unexpected exceptions must be handled autonomously [[S03, When (and when not) to use agents](#)], [[S08, When to use agents vs workflows](#)].
- **Avoid agents when:** The process has well-defined, predictable steps that can be implemented with standard code or deterministic workflow pipelines. As Microsoft Learn explicitly instructs: *"If you can write a function to handle the task, do that instead of using an AI agent"* [[S08, When to use agents vs workflows](#)].

---

## Citations & Evidence
- **[S01, Section 2]:** ReAct demonstrates that interleaving reasoning and action allows models to autonomously formulate and adjust plans in dynamic environments.
- **[S03, What are agents?]:** Anthropic defines agents as systems where LLMs dynamically direct their own processes and tool usage.
- **[S05, Core concepts: Agents]:** OpenAI defines an agent as an entity combining a model, instructions, and tools.
- **[S08, When to use agents vs workflows]:** Microsoft highlights the clear operational boundary between deterministic workflows and autonomous agents.

---

## Related Wiki Pages
- [AI Agents vs. Traditional Chatbots](agents-vs-chatbots.md)
- [Agent Architecture Stack](../architecture/agent-architecture.md)
- [The Agent Loop](../architecture/agent-loop.md)
- [Workflows vs. Autonomous Agents](../concepts/workflows-vs-agents.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
