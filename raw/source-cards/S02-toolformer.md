# Source Card: S02

## Metadata
- **Source ID:** S02
- **Title:** Toolformer: Language Models Can Teach Themselves to Use Tools
- **Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Affiliations:** Meta AI Research, Universitat Pompeu Fabra
- **Publisher / Venue:** arXiv preprint (arXiv:2302.04761) / NeurIPS 2023
- **Publication Date:** 2023-02-09
- **URL:** [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)
- **Access Date:** 2026-11-23
- **Retrieval Status:** Accessible (HTTP 200)
- **Document Type:** Peer-reviewed academic paper

## Summary
Toolformer demonstrates that language models can teach themselves how to use external tools via APIs in a self-supervised manner, without requiring large-scale human annotations. The authors address a fundamental paradox of LLMs: while they excel at few-shot learning and generalized language understanding, they struggle with precise calculations, up-to-date factual retrieval, and temporal reasoning.

The paper introduces a self-supervised training pipeline:
1. **API Call Generation:** Using in-context few-shot prompting, the model annotates plain text with potential API calls (e.g., `[Calculator(4 * 12)]`).
2. **Execution:** The candidate API calls are executed using external tools (Calculator, QA retrieval, Wikipedia search, Machine Translation, Calendar).
3. **Filtering:** The model evaluates whether inserting the API call and its result reduces the language modeling loss (perplexity) on future tokens. Only calls that genuinely improve prediction are retained.
4. **Fine-Tuning:** The model is fine-tuned on the filtered dataset using standard autoregressive language modeling objectives.

Toolformer (based on GPT-J 6.7B) achieves performance comparable to or exceeding much larger models (such as GPT-3 175B) on zero-shot mathematical reasoning, question answering, and factual queries, while retaining its core language modeling competence.

## Verified Section Structure
- **Section 1: Introduction** — The paradox of LLM scale vs. arithmetic/factual lookup limitations.
- **Section 2: Approach** — The four-stage self-supervised pipeline: sampling API calls, executing calls, filtering by loss reduction, and fine-tuning.
- **Section 3: Tools** — Tool specifications for Calculator, Wikipedia Search, Machine Translation, QA System, and Calendar.
- **Section 4: Experiments** — Downstream evaluation on LAMA, TempLAMA, ASDiv, SVAMP, and MAWPS.
- **Section 5: Related Work** — Comparison with tool-augmented models, prompting-based tool use, and retrieval-augmented generation.
- **Section 6: Limitations** — Tool chaining limitations, interactive multi-turn exploration limits, and tool execution overhead.
- **Section 7: Conclusion** — Summary and future directions for self-taught tool-using models.

## Key Claims & Evidence Locators
- **[S02, Section 1]:** Language models struggle with basic tasks like exact arithmetic or current factual lookup despite having billions of parameters.
- **[S02, Section 2]:** API calls can be represented as inline special token sequences, allowing external tools to be invoked within the autoregressive generation stream.
- **[S02, Section 2.2]:** Filtering candidate tool calls based on whether they decrease perplexity on subsequent tokens ensures the model only invokes tools when helpful.
- **[S02, Section 6]:** Toolformer cannot natively chain multiple tools or make exploratory tool calls across a dynamic environment without external orchestration.
