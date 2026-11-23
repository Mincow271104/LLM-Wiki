# The Agent Loop: Control Flow and Execution

## Summary
The **Agent Loop** is the iterative control flow mechanism that drives autonomous agent behavior. Unlike traditional linear computer programs with deterministic branching, the agent loop couples an LLM reasoning engine with dynamic environment feedback. It repeatedly executes an evaluation, planning, tool execution, and observation cycle until a termination condition is satisfied or a safety constraint is triggered.

## Key Concepts
- **Perception-Reasoning-Action-Observation Cycle:** The foundational four-phase loop that defines agent execution [[S01, Section 2](#)].
- **Termination Conditions:** Explicit criteria determining when an agent must halt (e.g., goal achieved, maximum iterations reached, human interruption, or unrecoverable error) [[S06, Capabilities: Human-in-the-loop](#)], [[S08, Important: Bounded looping](#)].
- **Context Accumulation:** How the state of intermediate thoughts, actions, and observations is maintained across loop turns [[S04, Short-term memory](#)].
- **Bounded Looping & Guardrails:** Hard algorithmic limits ensuring the agent never enters an infinite, costly, or runaway execution loop [[S05, Core concepts: Guardrails](#)], [[S08, Important: Bounded looping](#)].

---

## Anatomy of the Agent Execution Loop

The classic agent loop can be visualized as an iterative state machine:

```
                     ┌───────────────────────────┐
                     │    User Goal / Request    │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │   1. SENSE (Perceive) │ <─────────────────────┐
                       │ Current state & inputs│                       │
                       └───────────┬───────────┘                       │
                                   │                                   │
                                   ▼                                   │
                       ┌───────────────────────┐                       │
                       │   2. THINK (Reason)   │                       │
                       │ Evaluate, plan, choose│                       │
                       └───────────┬───────────┘                       │
                                   │                                   │
                      Does model request action?                       │
                                   │                                   │
                    YES ───────────┴─────────── NO (Goal Done)         │
                     │                                │                │
                     ▼                                ▼                │
          ┌─────────────────────┐          ┌───────────────────────┐   │
          │   3. ACT (Execute)  │          │   Deliver Final Answer│   │
          │  Call tool / API    │          └───────────────────────┘   │
          └──────────┬──────────┘                                      │
                     │                                                 │
                     ▼                                                 │
          ┌─────────────────────┐                                      │
          │ 4. OBSERVE (Feedback)                                      │
          │  Parse tool output  │                                      │
          └──────────┬──────────┘                                      │
                     │                                                 │
                     └─────────────────────────────────────────────────┘
                              Next Loop Iteration (t = t + 1)
```

### Detailed Loop Phases:
1. **Sense (Perceive):** The runtime constructs the current prompt by aggregating the system prompt, tool schemas, conversation history, and the accumulated scratchpad of prior iterations.
2. **Think (Reason & Plan):** The LLM performs inference. It evaluates whether the goal has been achieved or whether intermediate steps are required. If additional information or action is needed, it generates a structured tool call [[S01, Section 2](#)], [[S03, Agents](#)].
3. **Act (Execute):** The host environment intercepts the tool call, verifies permissions, and executes the designated software tool (e.g., querying a database, calculating a formula, or calling a web search API).
4. **Observe (Feedback):** The output returned by the tool is captured and formatted as an `observation` or `tool` message. It is appended to the scratchpad, closing the loop.

---

## Termination Logic and Safety Controls

A naive agent loop (`while True: ...`) is dangerous. In production architectures, four distinct termination boundaries must be enforced:

1. **Explicit Goal Satisfaction:** The LLM evaluates that the user's objective is fully accomplished and outputs a final user-facing text answer without tool calls.
2. **Maximum Iteration Limit (Bounded Looping):** A hard cap (e.g., `max_iterations = 10`) stops execution if the model enters a cyclic deadlock or repetitive action loop [[S08, Important: Bounded looping](#)].
3. **Token & Budget Caps:** Halting if cumulative token usage or monetary cost exceeds configured safety thresholds.
4. **Human-in-the-Loop Interruption:** Stateful runtimes (such as LangGraph) allow execution to pause deterministically before critical actions, waiting for human approval or parameter editing [[S06, Capabilities: Human-in-the-loop](#)].

---

## Minimal Agent Loop Implementation Pattern (Python Pseudocode)

```python
def run_agent_loop(system_prompt, user_goal, tools, max_steps=10):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_goal}
    ]
    
    for step in range(max_steps):
        # 1. Sense & Think: Invoke model with available tools
        response = call_llm(messages=messages, tools=tools)
        
        # 2. Check Termination: If model provided final answer without tool calls
        if not response.tool_calls:
            return response.content
        
        # 3. Act & Observe: Execute requested tools
        messages.append(response.to_message()) # Record thought/action
        for tool_call in response.tool_calls:
            result = execute_tool(tool_call.name, tool_call.arguments)
            # Append environmental observation
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
            
    raise TimeoutError("Agent exceeded maximum configured loop iterations.")
```

---

## Citations & Evidence
- **[S01, Section 2]:** Yao et al. define the formal mathematical interleaving of action spaces, observation spaces, and thought spaces.
- **[S03, Agents]:** Anthropic outlines the autonomous agent loop where the model maintains dynamic control over process flow.
- **[S06, Capabilities: Human-in-the-loop]:** LangGraph details stateful interrupts within agent loops.
- **[S08, Important: Bounded looping]:** Microsoft Agent Framework requires bounded looping and harness controls to prevent runaway costs.

---

## Related Wiki Pages
- [What is an AI Agent?](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/fundamentals/what-is-an-agent.md)
- [The ReAct Pattern](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/concepts/react-pattern.md)
- [Tools & Function Calling](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/architecture/tools-and-function-calling.md)
- [Educational Python Agent Example](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/implementation/python-agent-example.md)
- [Wiki Master Index](file:///e:/HƯ/ai-agents-wiki-assignment/wiki/index.md)

*Last Updated: 2026-11-23*
