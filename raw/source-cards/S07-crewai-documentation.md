# Source Card: S07

## Metadata
- **Source ID:** S07
- **Title:** CrewAI Documentation & Repository
- **Authors:** João Moura, CrewAI Inc.
- **Publisher / Organization:** CrewAI Inc. (GitHub Repository)
- **Publication Date:** 2023-11-20 (Updated 2025/2026)
- **URL:** [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Technical specification & open-source repository

## Summary
CrewAI is a widely adopted Python framework designed specifically for orchestrating collaborative teams of autonomous, role-playing AI agents. It models multi-agent collaboration by drawing analogies to human organizational structures, where individual contributors possess specialized personas, goals, and skill sets.

Key primitives and concepts:
1. **Agent:** An autonomous actor defined by:
   - `role`: The agent's functional domain or job title (e.g., "Senior Financial Analyst").
   - `goal`: The specific objective the agent strives to achieve.
   - `backstory`: Contextual narrative that shapes the agent's tone, reasoning style, and decision boundaries.
   - `tools`: Set of functions or external integrations the agent can invoke.
   - `allow_delegation`: Flag enabling an agent to assign subtasks to other crew members.
2. **Task:** A discrete unit of work assigned to an agent, specifying `description`, `expected_output`, and optional dependencies on previous tasks.
3. **Crew:** The organizational container that bundles Agents and Tasks together and manages execution according to a defined Process.
4. **Processes:**
   - *Sequential Process:* Tasks are executed in strict linear order, with outputs from earlier tasks automatically passed into downstream tasks.
   - *Hierarchical Process:* A manager agent (configured via a manager LLM) dynamically plans task assignments, delegates to specialized agents, reviews outputs, and synthesizes the final response.
5. **Memory System:** Multi-tiered memory architecture incorporating:
   - *Short-term memory:* Stores context of the active execution session using local embeddings.
   - *Long-term memory:* Retains historical task executions to improve future task coordination.
   - *Entity memory:* Extracts and preserves key entities encountered across interactions.

## Verified Section Structure
- **Fast and Flexible Multi-Agent Automation Framework** — Core mission and value proposition.
- **Crew Control Plane Key Features** — Observability, orchestration, and enterprise features.
- **Why CrewAI?** — Design philosophy: role-based collaboration, multi-agent cooperation, and ease of use.
- **Getting Started** — Quickstart installation (`pip install crewai`), defining agents, tasks, and crews.
- **Core Concepts** — In-depth definitions of Agents (role, goal, backstory), Tasks, Crews, and Tools.
- **Processes** — Comparison of Sequential vs. Hierarchical task orchestration.
- **Connecting Your Crew to a Model** — Configuring model providers (OpenAI, Anthropic, Ollama, Azure, etc.).

## Key Claims & Evidence Locators
- **[S07, Core Concepts: Agents]:** Agents in CrewAI are parameterized by Role, Goal, and Backstory, providing strong persona conditioning that guides tool usage and collaboration.
- **[S07, Processes: Sequential Process]:** In sequential processes, tasks execute linearly with outputs cascading deterministically to subsequent agents.
- **[S07, Processes: Hierarchical Process]:** Hierarchical processes employ a manager LLM that dynamically delegates tasks to worker agents and validates their deliverables.
- **[S07, Key Features: Memory]:** CrewAI provides a built-in multi-layered memory system (short-term, long-term, and entity memory) to enhance collaborative agent performance across executions.
