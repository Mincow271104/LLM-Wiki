# Educational Python Agent Example

## Summary
This page presents a self-contained, fully runnable educational Python implementation of an **Agent Loop** adhering to the **ReAct** pattern (`Thought → Action → Observation`). To ensure accessibility for beginners without requiring paid API keys or external cloud credentials, this example utilizes a deterministic educational reasoning simulator while adhering to the exact architecture used by production LLM-powered agents.

## Key Concepts
- **Sense-Plan-Act-Observe Cycle:** The foundational execution loop implemented in pure standard-library Python [[S01, Section 2](#)].
- **Tool Registration & Execution:** Decoupling tool definitions from the core execution loop [[S04, Agent tools](#)].
- **Simulated vs. Production Agent Distinction:** Explaining what makes an agent "educational/simulated" versus "production LLM-powered" [[S03, Building block: The augmented LLM](#)].
- **Bounded Iteration Safety:** Enforcing strict loop limits to prevent infinite execution cycles [[S08, Important: Bounded looping](#)].

---

## Simulated vs. Production Agent: Critical Distinction

Before examining the code, beginners must understand the difference between this educational implementation and a production deployment:

| Architectural Component | Educational Simulated Agent (This Example) | Production LLM-Powered Agent |
| :--- | :--- | :--- |
| **Reasoning Engine** | Deterministic rule-based heuristic function mimicking LLM thinking. | Foundation model API (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro). |
| **Tool Calling Mechanism** | Simple dictionary dispatch on tool name and keyword arguments. | Native JSON Schema function calling (e.g., OpenAI Tool Calling, MCP). |
| **API Key Requirement** | **None.** Runs 100% offline using standard Python. | Requires valid cloud provider API keys and internet access. |
| **Control Flow & State** | **Identical:** Scratchpad message history, action parsing, and observation loop. | **Identical:** Scratchpad message history, action parsing, and observation loop. |

---

## Complete Runnable Python Code

You can copy and run this script directly in any Python 3 environment without installing external dependencies:

```python
"""
Educational AI Agent Implementation
Pattern: ReAct (Reasoning and Acting)
Dependencies: Python 3 Standard Library only (No API keys required)
"""

import json
import re

# ==============================================================================
# 1. TOOL DEFINITIONS (The Agent's Actuators)
# ==============================================================================

def tool_calculator(expression: str) -> str:
    """Safely evaluates basic arithmetic expressions."""
    # Allow only basic math characters for safety
    if not re.match(r"^[\d\s\+\-\*\/\(\)\.]+$", expression):
        return "Error: Invalid characters in arithmetic expression."
    try:
        # Evaluate sanitized expression
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Calculation Error: {e}"

def tool_database_search(query: str) -> str:
    """Simulates an external database or search API lookup."""
    knowledge_base = {
        "apollo 11": "Apollo 11 launched on July 16, 1969, carrying Neil Armstrong, Buzz Aldrin, and Michael Collins.",
        "mars rover perseverance": "Perseverance landed on Mars on February 18, 2021, searching for signs of ancient life.",
        "voyager 1": "Voyager 1 was launched on September 5, 1977, and entered interstellar space in August 2012."
    }
    query_lower = query.lower().strip()
    for key, fact in knowledge_base.items():
        if key in query_lower or query_lower in key:
            return fact
    return "No matching records found in external database."

# Tool Registry
TOOL_REGISTRY = {
    "calculator": tool_calculator,
    "search": tool_database_search
}

# ==============================================================================
# 2. EDUCATIONAL REASONING SIMULATOR (Mock LLM)
# ==============================================================================

def simulated_llm_brain(messages: list) -> dict:
    """
    Simulates an LLM producing ReAct output:
    In production, this function is replaced by an actual API call:
    response = client.chat.completions.create(model='gpt-4o', messages=messages, tools=tools)
    """
    # Inspect the history to determine progress
    history_text = " ".join([m["content"] for m in messages])

    # Check if we already have Apollo 11 launch year
    if "Apollo 11 launched on July 16, 1969" in history_text:
        # Check if we computed the years since launch
        if "Observation: 57" in history_text or "Observation: 57.0" in history_text:
            return {
                "thought": "I have the launch year (1969) and calculated the elapsed years until 2026 (57 years). I am ready to conclude.",
                "action": None,
                "final_answer": "Apollo 11 launched in 1969. As of 2026, it has been 57 years since the historic launch."
            }
        else:
            return {
                "thought": "The database revealed that Apollo 11 launched in 1969. Now I need to calculate how many years have passed between 1969 and 2026.",
                "action": {"tool": "calculator", "argument": "2026 - 1969"},
                "final_answer": None
            }
    else:
        return {
            "thought": "I need to find the launch date of Apollo 11 before I can calculate the time elapsed.",
            "action": {"tool": "search", "argument": "Apollo 11"},
            "final_answer": None
        }

# ==============================================================================
# 3. THE RE推ACT EXECUTION LOOP (The Agent Orchestrator)
# ==============================================================================

def run_agent(user_goal: str, max_iterations: int = 5):
    print("=" * 70)
    print(f"USER GOAL: {user_goal}")
    print("=" * 70)

    messages = [
        {"role": "user", "content": user_goal}
    ]

    for step in range(1, max_iterations + 1):
        print(f"\n--- [AGENT LOOP ITERATION {step}] ---")

        # Phase 1: Think (Invoke Reasoning Engine)
        decision = simulated_llm_brain(messages)
        print(f"THOUGHT: {decision['thought']}")

        # Check for Termination
        if decision["final_answer"] is not None:
            print(f"\nFINAL ANSWER:\n{decision['final_answer']}")
            print("=" * 70)
            return decision["final_answer"]

        # Phase 2: Act (Tool Dispatch)
        tool_call = decision["action"]
        tool_name = tool_call["tool"]
        tool_arg = tool_call["argument"]
        print(f"ACTION: Invoke tool '{tool_name}' with argument '{tool_arg}'")

        if tool_name in TOOL_REGISTRY:
            observation = TOOL_REGISTRY[tool_name](tool_arg)
        else:
            observation = f"Error: Tool '{tool_name}' not recognized."

        print(f"OBSERVATION: {observation}")

        # Phase 3: Update Context Scratchpad
        messages.append({"role": "assistant", "content": f"Thought: {decision['thought']}\nAction: {tool_name}[{tool_arg}]"})
        messages.append({"role": "tool", "content": f"Observation: {observation}"})

    print("\nTERMINATION WARNING: Maximum iterations reached without final answer.")
    return None

# ==============================================================================
# 4. EXECUTION
# ==============================================================================

if __name__ == "__main__":
    run_agent("How many years have passed between the launch of Apollo 11 and 2026?")
```

---

## Code Walkthrough & Key Takeaways

1. **Decoupled Tool Interfaces:** The tools (`tool_calculator`, `tool_database_search`) are pure, standard Python functions. The agent interacts with them through a unified dictionary registry.
2. **Interleaved State Scratchpad:** Notice how the `messages` list accumulates `thought`, `action`, and `observation` tokens on every turn. This matches the exact ReAct formulation demonstrated in Yao et al. [[S01, Section 2](#)].
3. **Termination Guard:** The `max_iterations` parameter guarantees that if an unexpected error occurs, execution terminates safely rather than consuming infinite CPU cycles [[S08, Important: Bounded looping](#)].

---

## Citations & Evidence
- **[S01, Section 2]:** Demonstrates the alternating sequence of thought, action, and observation tokens.
- **[S03, Building block: The augmented LLM]:** Documents how tools and memory augment foundational reasoning.
- **[S04, Agent tools]:** Emphasizes decoupled tool architectures.
- **[S08, Important: Bounded looping]:** Requires hard iteration boundaries on agent loops.

---

## Related Wiki Pages
- [The Agent Loop](../architecture/agent-loop.md)
- [The ReAct Pattern](../concepts/react-pattern.md)
- [Tools & Function Calling](../architecture/tools-and-function-calling.md)
- [Wiki Master Index](../index.md)

*Last Updated: 2026-11-23*
