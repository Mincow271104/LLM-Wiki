# Source Card: S01

## Metadata
- **Source ID:** S01
- **Title:** ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan
- **Affiliations:** Princeton University, Google Research, Brain team
- **Publisher / Venue:** arXiv preprint (arXiv:2210.03629) / ICLR 2023
- **Publication Date:** 2022-10-06 (v1), revised 2023-03-10 (v2)
- **URL:** [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Peer-reviewed academic paper

## Summary
ReAct explores the synergy between reasoning (e.g., chain-of-thought prompting) and acting (action generation in an environment) in Large Language Models (LLMs). While previous approaches evaluated reasoning and acting in isolation, ReAct prompts the LLM to generate both reasoning traces ("thoughts") and task-specific actions in an interleaved sequence: `Thought -> Action -> Observation -> Thought -> Action -> ...`. 

The paper demonstrates that:
1. Reasoning traces help the model induce, track, and update action plans, handle exceptions, and synthesize facts.
2. External actions (such as searching a Wikipedia API or interacting with an environment) allow the model to retrieve real-world factual information, drastically reducing the hallucination rates common in pure chain-of-thought reasoning.
3. On multi-hop question answering (HotpotQA, Fever) and interactive decision-making benchmarks (ALFWorld, WebShop), ReAct consistently outperforms both reason-only baselines (which hallucinate) and act-only baselines (which fail to maintain long-term plans).

## Verified Section Structure
- **Section 1: Introduction** — Theoretical motivation for combining reasoning and acting; contrast with human intelligence.
- **Section 2: ReAct: Synergizing Reasoning + Acting** — Formal definition of the ReAct formulation: observation space, action space, thought space, and token-level interleaving.
- **Section 3: Knowledge-Intensive Reasoning** — Experiments on HotpotQA and Fever; comparison with standard prompting, CoT, and Act-only.
- **Section 4: Decision Making Tasks** — Interactive decision environments (ALFWorld text game and WebShop online shopping benchmark).
- **Section 5: Related Work** — Prior work in language-based decision making, chain-of-thought reasoning, and tool use.
- **Section 6: Conclusion** — Summary of findings, computational cost trade-offs, and directions for human-in-the-loop and fine-tuning.

## Key Claims & Evidence Locators
- **[S01, Section 1]:** Pure reasoning (Chain-of-Thought) suffers from factual hallucinations and cannot incorporate fresh environmental feedback.
- **[S01, Section 2]:** ReAct alternates `Thought`, `Action`, and `Observation` tokens, enabling dynamic plan revision and external tool retrieval.
- **[S01, Section 3]:** On HotpotQA, ReAct achieves higher factual accuracy than pure CoT by grounding intermediate reasoning steps in external Wikipedia search results.
- **[S01, Section 4]:** In interactive environments (ALFWorld, WebShop), reasoning traces allow the agent to recover from erroneous actions and dead ends.
