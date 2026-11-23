# Planning and Reasoning in AI Agents

## Summary
Planning and reasoning constitute the cognitive engine of an AI agent. While simple tasks can be solved by immediate pattern matching, complex real-world objectives require agents to decompose goals into subtasks, anticipate dependencies, evaluate intermediate outcomes, self-correct errors, and formulate alternative paths.

## Key Concepts
- **Task Decomposition:** Breaking an overarching objective into a sequence of smaller, manageable subgoals [[S03, Workflow: Orchestrator-workers](#)].
- **Chain-of-Thought (CoT):** Prompting language models to articulate intermediate reasoning steps before arriving at a final answer [[S01, Section 1](#)].
- **Plan-and-Solve:** A two-phase paradigm where an agent first generates an explicit multi-step plan, then systematically executes each step [[S04, Agent design patterns](#)].
- **Reflection & Self-Critique:** An agent inspecting its own intermediate outputs or tool errors to evaluate correctness and revise its trajectory [[S03, Workflow: Evaluator-optimizer](#)], [[S04, Agent design patterns](#)].

---

## Planning Paradigms in Agent Systems

Agent planning strategies balance the trade-off between upfront deliberation and dynamic flexibility:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Planning Strategies                             │
├───────────────────────────────────┬────────────────────────────────────┤
│ Upfront Deliberative Planning     │ Reactive Dynamic Planning          │
│ (Plan-and-Solve)                  │ (ReAct, Dynamic Loops)             │
├───────────────────────────────────┼────────────────────────────────────┤
│ 1. Formulate complete plan (1..N) │ 1. Take immediate single step      │
│ 2. Execute steps sequentially     │ 2. Observe environment feedback    │
│ 3. Evaluate final outcome         │ 3. Formulate next step dynamically │
│ - Efficient for predictable tasks │ - Resilient to unexpected errors   │
│ - Fragile if intermediate step fails│ - Higher token and API call costs  │
└───────────────────────────────────┴────────────────────────────────────┘
```

### 1. Chain-of-Thought & Scratchpad Reasoning
Pioneered by Wei et al. and formalized in ReAct [[S01, Section 1](#)], Chain-of-Thought prompting directs the LLM to generate internal monologue ("thoughts") prior to taking actions. These thoughts serve three computational functions:
- Tracking progress toward the goal.
- Synthesizing facts gathered from multiple prior tool outputs.
- Diagnosing exceptions and updating action strategies.

### 2. Upfront Planning (Plan-and-Solve)
In the Plan-and-Solve paradigm [[S04, Agent design patterns](#)], the agent begins by generating an explicit task breakdown:
1. *Step 1: Fetch quarterly earnings report from SEC EDGAR API.*
2. *Step 2: Parse operating revenue and net profit figures.*
3. *Step 3: Calculate year-over-year percentage change using calculator.*
4. *Step 4: Draft comparative summary.*

While intuitive, pure upfront planning suffers from rigidity: if Step 1 fails because the API endpoint is down, the entire plan collapses unless an adaptive replanning mechanism is active.

### 3. Reactive Planning (ReAct)
Rather than committing to an unalterable multi-step plan, reactive planning couples each individual reasoning step directly to an environment action and observation [[S01, Section 2](#)]. If a search query yields no results, the agent immediately reflects: *"The query returned zero records. I will rephrase my search keywords using synonyms."*

### 4. Reflection and Evaluator-Optimizer
In the Evaluator-Optimizer pattern [[S03, Workflow: Evaluator-optimizer](#)], reasoning is distributed between two roles:
- **Generator / Worker:** Produces a solution, code snippet, or analysis.
- **Evaluator / Critic:** Tests the candidate solution against formal rubrics, unit tests, or criteria. If defects are found, actionable feedback is fed back to the generator for revision.

---

## Common Planning Failure Modes

1. **Hallucinated Planning:** The model creates a plan that relies on tools, endpoints, or data that do not exist.
2. **Infinite Deadlocks / Action Loops:** The agent repeatedly issues identical failing tool calls without recognizing that the action is not progressing the goal.
3. **Plan Drift:** Over long trajectories (15+ steps), the agent loses track of the original user objective due to context dilution [[S04, Agent memory](#)].

---

## Citations & Evidence
- **[S01, Section 1 & 2]:** Yao et al. demonstrate that reasoning traces allow models to induce, track, and update action plans dynamically.
- **[S03, Workflow: Evaluator-optimizer & Orchestrator-workers]:** Anthropic documents architectural patterns for task decomposition and iterative reflection.
- **[S04, Agent design patterns]:** Google Cloud surveys planning, ReAct, and reflection patterns in enterprise architectures.
- **[S08, In this article: Harness Agent]:** Microsoft emphasizes explicit todo tracking and planning within the Harness Agent.

---

## Related Wiki Pages
- [What is an AI Agent?](../fundamentals/what-is-an-agent.md)
- [The ReAct Pattern](react-pattern.md)
- [The Agent Loop](../architecture/agent-loop.md)
- [Workflows vs. Autonomous Agents](workflows-vs-agents.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
