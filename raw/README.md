# Raw Sources Layer (Layer A)

This directory forms **Layer A (Raw Sources)** of the Karpathy-inspired LLM Wiki architecture.

## Principles of Raw Sources
1. **Immutability:** Original source records and extracted text fragments are immutable. The agent reads from this directory but never alters original historical source files.
2. **Traceability:** Every source has a permanent, stable ID (`S01` through `S08`).
3. **Verified Retrieval:** No source is ingested without direct network verification and recording of access date, HTTP status, and metadata.
4. **Copyright Compliance:** In accordance with fair-use guidelines and project requirements, full copyrighted books or proprietary papers are never republished in full; instead, metadata, verified section hierarchies, and claim-level evidence cards are curated.

## Ingestion Directory Layout
```
raw/
├── README.md               # This layer description and ingestion guidelines
├── sources.json            # Master machine-readable source registry (validates against source.schema.json)
├── claims.json             # Master machine-readable claim evidence registry (validates against claim.schema.json)
└── source-cards/           # Individual Markdown and JSON source cards
    ├── S01-react.md
    ├── S01-react.json
    ├── S02-toolformer.md
    ├── S02-toolformer.json
    ├── S03-building-effective-agents.md
    ├── S03-building-effective-agents.json
    ├── S04-cloud-architecture-components.md
    ├── S04-cloud-architecture-components.json
    ├── S05-openai-agents-sdk.md
    ├── S05-openai-agents-sdk.json
    ├── S06-langgraph-overview.md
    ├── S06-langgraph-overview.json
    ├── S07-crewai-documentation.md
    ├── S07-crewai-documentation.json
    ├── S08-microsoft-agent-framework.md
    └── S08-microsoft-agent-framework.json
```

## Source Status Overview
| Source ID | Title | Publisher / Authors | Access Date | Status |
| :--- | :--- | :--- | :--- | :--- |
| **S01** | ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. (Princeton / Google Brain) | 2026-11-23 | Verified (HTTP 200) |
| **S02** | Toolformer: Language Models Can Teach Themselves to Use Tools | Schick et al. (Meta AI) | 2026-11-23 | Verified (HTTP 200) |
| **S03** | Building Effective Agents | Anthropic (Schluntz & Zhang) | 2026-11-23 | Verified (HTTP 200) |
| **S04** | Choose your agentic AI architecture components | Google Cloud Architecture Center | 2026-11-23 | Verified (HTTP 200) |
| **S05** | Agents SDK | OpenAI Developer Platform | 2026-11-23 | Verified (HTTP 200) |
| **S06** | LangGraph Overview | LangChain | 2026-11-23 | Verified (HTTP 200) |
| **S07** | CrewAI Documentation | CrewAI Inc. (João Moura) | 2026-11-23 | Verified (HTTP 200) |
| **S08** | Microsoft Agent Framework Overview | Microsoft Learn | 2026-11-23 | Verified (HTTP 200) |
