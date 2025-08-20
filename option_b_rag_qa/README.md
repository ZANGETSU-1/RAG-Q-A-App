# Option B: RAG Q&A App

## Task Overview

Build a basic RAG Q&A app using a document corpus. We care about your ability to select tools, chunk/index data, retrieve relevant context, and generate grounded answers with citations.

**Time limit**: Max 4 hours actual work time

**Goal**: Turn a lightweight spec into a working feature fast, using AI/codegen tools effectively. We care about your approach, prompts, and delivery - not hand-crafted perfection.

## What We Are Looking For (15 pts total)

| Area                       | Pts | What we look for                                                                  |
| -------------------------- | --- | --------------------------------------------------------------------------------- |
| **Working RAG pipeline**   | 4   | Ingest → chunk → index → retrieve → answer with citations; handles "I don't know" |
| **Problem decomposition**  | 3   | Clear breakdown; rationale for chunking/indexing/generation                       |
| **AI tooling proficiency** | 3   | Concrete, iterative prompts; smart use of assistants for code/scaffolding/debug   |
| **Quality of grounding**   | 2   | Answers align with retrieved chunks; citations sensible                           |
| **Communication**          | 3   | Clean README; clear report/Loom; reproducible eval harness                        |

## Core Requirements

### 1. Corpus Ingestion

- Source and ingest the provided books:
  - [The Art of Money Getting by P.T. Barnum (1880)](https://www.globalgreyebooks.com/art-of-money-getting-ebook.html)
  - [The Science of Getting Rich by Wallace Wattles (1910)](https://www.globalgreyebooks.com/science-of-getting-rich-ebook.html)
  - [Self-Help by Samuel Smiles (1859)](https://www.globalgreyebooks.com/self-help-samuel-smiles-ebook.html)
  - [Acres of Diamonds by Russell Conwell (1890s)](https://mc2method.org/books/AcresOfDiamonds.pdf)
- Implement a **chunking strategy** (state your choices: size, overlap, rules)

### 2. Indexing & Retrieval

- Build a vector index (e.g., FAISS, Chroma, Elastic/Opensearch, Weaviate - your choice)
- Implement a retriever that returns the **top-k supporting chunks**

### 3. Answer Generation

- Generate an answer **grounded** in retrieved chunks
- Show **citations**: file name + chunk ID (and page number if available)
- Must handle **"I don't know"** when confidence is low or retrieval is empty (explain your thresholding logic)

### 4. Evaluation Harness (mini)

- Include a small `questions.json` (5-8 Qs) + your **expected short references** (1-2 key chunks each)
- Provide a quick script/notebook cell to run all Qs and print:
  - retrieved chunk IDs
  - answer
  - whether at least one cited chunk matches your references

### 5. AI/Tool Use is Required

- Use at least one AI tool (Claude/ChatGPT/Copilot/Cursor, etc.) to assist build/debug
- Keep **3+ key prompts** you used (copy/paste exact text) with brief notes on what changed after each

## Stretch (extra credit)

- **Graph RAG**: Build a tiny **entity graph** (Neo4j). Use it to:
  - enrich retrieval (e.g., query expansion via linked entities) **or**
  - re-rank results using graph proximity
- **Hierarchical chunking**: Parent-child structure (doc → section → paragraph). Route queries or re-rank using hierarchy
- **Semantic chunking**: Non-uniform splits based on semantics rather than fixed token windows
- **Reranking**: Add a cross-encoder or simple LLM re-ranker step and justify trade-offs
- **Caching**: Basic cache for embeddings or answers

## What to Submit

1. **Working code** (GitHub or ZIP)

   - README.md with setup and run steps (create venv, install deps, how to pass a corpus folder, how to run eval)
   - If generation uses an API key, document environment variables (don't commit keys)

2. **Process report** (max 2 pages or 5-10 min Loom)

   - Tooling choices and **why** (vector DB, embed model, generator, chunking)
   - **3+ key prompts** you used with notes on iteration
   - Your evaluation approach & limits
   - Known failure modes + how you'd improve with more time

3. **Evidence of AI use** (screenshots/logs of prompts or assistant traces)

## Getting Started

1. **Write your spec first** - what will your RAG app do?
2. **Choose your tech stack** - what's fastest for you?
3. **Start with AI** - feed your spec to an AI assistant
4. **Iterate and build** - keep it simple, get it working
5. **Document everything** - your process, prompts, decisions

**Tip**: Keep it lean. Ship the core first, stretch only if you truly have time.

Good luck! 📚🤖
