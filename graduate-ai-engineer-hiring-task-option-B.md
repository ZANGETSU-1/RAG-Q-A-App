

# **Graduate AI Engineer**

## **Builder Task Option B**

**Build a basic RAG Q&A  App**

**Time limit:** Max 4 hours actual work time

**Goal:** 

Turn a lightweight spec into a working feature fast, using AI/codegen tools effectively. 

We care about your approach, prompts, and delivery  not hand-crafted perfection.  

We are looking for builders with AI superpowers rather than coding genius. 

We are not looking for proficiency with a specific language or database, rather we are looking for people who can intelligently use AI tools to get things done. 


## **What we are looking for (15 pts total)**


<table>
  <tr>
   <td><strong>Area</strong>
   </td>
   <td><strong>Pts</strong>
   </td>
   <td><strong>What we look for</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Working RAG pipeline</strong>
   </td>
   <td>4
   </td>
   <td>Ingest ’ chunk ’ index ’ retrieve ’ answer with citations; handles I dont know
   </td>
  </tr>
  <tr>
   <td><strong>Problem decomposition</strong>
   </td>
   <td>3
   </td>
   <td>Clear breakdown; rationale for chunking/indexing/generation
   </td>
  </tr>
  <tr>
   <td><strong>AI tooling proficiency</strong>
   </td>
   <td>3
   </td>
   <td>Concrete, iterative prompts; smart use of assistants for code/scaffolding/debug
   </td>
  </tr>
  <tr>
   <td><strong>Quality of grounding</strong>
   </td>
   <td>2
   </td>
   <td>Answers align with retrieved chunks; citations sensible
   </td>
  </tr>
  <tr>
   <td><strong>Communication</strong>
   </td>
   <td>3
   </td>
   <td>Clean README; clear report/Loom; reproducible eval harness
   </td>
  </tr>
</table>


**Bonus signals (not scored, but note them):**



* Graph RAG used well (entity extraction, graph-assisted retrieval/re-rank). 

* Hierarchical or semantic chunking meaningfully improves retrieval. 

* Simple re-ranker or cache implemented with reasoning and measurement.


## 


## **The Task**

Turn a small document corpus into a working **RAG Q&A tool**. We care about your ability to select tools, chunk/index data, retrieve relevant context, and generate grounded answers with citations.

Extra credit for **Graph RAG**, **hierarchical chunking**, and **semantic  chunking**.

Here are some classic books on personal finance: 



* [The Art of Money Getting by P.T. Barnum (1880)](https://www.globalgreyebooks.com/art-of-money-getting-ebook.html)
* [The Science of Getting Rich by Wallace Wattles (1910](https://www.globalgreyebooks.com/science-of-getting-rich-ebook.html))
* [Self-Help by Samuel Smiles (1859)](https://www.globalgreyebooks.com/self-help-samuel-smiles-ebook.html)
* [Acres of Diamonds by Russell Conwell (1890s)](https://mc2method.org/books/AcresOfDiamonds.pdf) (gotcha! :-))

Write a plain-English spec for a **Money Chat MVP** covering user journey, key functions, data model, and basic validation. 

Then provide **three AI prompts** youd use:



1. project/bootstrap prompt, 

2. implementing a concrete function (e.g., "generate an embedding), 

3. testing/debugging (e.g., Generate Jest/pytest for RAG retrieval).


### **Core requirements**



1. **Corpus ingestion**
    * Source and ingest the books. 
    * Implement a **chunking strategy** (state your choices: size, overlap, rules). 

2. **Indexing & retrieval**
    * Build a vector index (e.g., FAISS, Chroma, Elastic/Opensearch, Weaviateyour choice). 

    * Implement a retriever that returns the **top-k supporting chunks**.

3. **Answer generation**
    * Generate an answer **grounded** in retrieved chunks. 

    * Show **citations**: file name + chunk ID (and page number if available). 

    * Must handle **I dont know** when confidence is low or retrieval is empty (explain your thresholding logic).  This is key.   

4. **Evaluation harness (mini)**
    * Include a small questions.json (58 Qs) + your **expected short references** (12 key chunks each). 

    * Provide a quick script/notebook cell to run all Qs and print: 

        * retrieved chunk IDs, 

        * answer, 

        * whether at least one cited chunk matches your references. 

5. **AI/tool use is required**
    * Use at least one AI tool (Claude/ChatGPT/Copilot/Cursor, etc.) to assist build/debug. 

    * Keep **3+ key prompts** you used (copy/paste exact text) with brief notes on what changed after each. 



### **Stretch (extra credit)**


* **Graph RAG:** Build a tiny **entity graph** ( Neo4j). Use it to: 

    * enrich retrieval (e.g., query expansion via linked entities) **or**
    * re-rank results using graph proximity. 

* **Hierarchical chunking:** Parentchild structure (doc ’ section ’ paragraph). Route queries or re-rank using hierarchy. 

* **Semantic chunking:** Non-uniform splits based on semantics (e.g., sentence boundaries, topic shifts) rather than fixed token windows. Explain your method. 

* **Reranking:** Add a cross-encoder or simple LLM re-ranker step and justify trade-offs. 

* **Caching:** Basic cache for embeddings or answers. 





## **What to submit**



1. **Working code** (GitHub or ZIP) 

    * README.md with setup and run steps (create venv, install deps, how to pass a corpus folder, how to run eval). 

    * If generation uses an API key, document environment variables (dont commit keys). 

2. **Process report** *(max 2 pages or 510 min Loom) 
*
    * Tooling choices and **why** (vector DB, embed model, generator, chunking). 

    * **3+ key prompts** you used with notes on iteration. 

    * Your evaluation approach & limits. 

    * Known failure modes + how youd improve with more time. 

3. **Evidence of AI use** (screenshots/logs of prompts or assistant traces). 
