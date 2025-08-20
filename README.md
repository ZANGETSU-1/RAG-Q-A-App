# Graduate AI Engineer Assessment

Welcome to your coding assessment! This repository contains two AI-focused tasks designed to evaluate your ability to build working applications using AI tools effectively.

## Prerequisites

- **Node.js** (v16 or higher) and **npm** for JavaScript/TypeScript tasks
- **Python** (3.8 or higher) and **pip** for Python tasks
- **Git** for version control
- **AWS Account** and **AWS CLI** for Option A (DynamoDB)

## Assessment Tasks

You can choose to complete **one or both** of the following tasks:

### Option A: Monkey Registry App (CRUD + AI Tools)

**File**: `option_a_monkey_registry/`

**Goal**: Build a basic CRUD app that manages Monkeys using AI/codegen tools effectively.

**Requirements**:

- Frontend: CLI, Streamlit, or React/Next.js
- Data model: monkey_id, name, species, age_years, favourite_fruit, last_checkup_at
- Validation rules and domain logic
- Backend: AWS DynamoDB (preferred) or SQLite/JSON with abstraction layer
- At least one automated test
- **AI use is REQUIRED** - include your prompts and process

**Estimated time**: 4 hours maximum

### Option B: RAG Q&A App (Retrieval-Augmented Generation)

**File**: `option_b_rag_qa/`

**Goal**: Build a working RAG Q&A tool using a document corpus.

**Requirements**:

- Corpus ingestion and chunking strategy
- Vector indexing and retrieval (FAISS, Chroma, etc.)
- Answer generation with citations
- Handle "I don't know" responses
- Mini evaluation harness
- **AI use is REQUIRED** - include your prompts and process

**Estimated time**: 4 hours maximum

## Getting Started

1. **Choose your task(s)**: Option A, Option B, or both
2. **Install dependencies** for your chosen language:

   ```bash
   # For JavaScript/TypeScript
   npm install

   # For Python
   pip install -r requirements.txt
   ```

3. **Set up AWS credentials** (if choosing Option A - see `AWS_CREDENTIALS_TEMPLATE.md`)
4. **Complete your chosen task(s)** using AI tools effectively
5. **Document your process** and include your AI prompts

## Submission Guidelines

- Complete **at least one** of the two options
- Include a process report (max 2 pages or 5-10 min Loom)
- Document your AI tool usage and key prompts
- Ensure all code is well-documented and follows best practices
- Test your solutions thoroughly
- Commit and push your changes to this repository

## What We're Looking For

- **End-to-end delivery**: Working application with no hard crashes
- **Problem decomposition**: Clear specification and sensible breakdown
- **AI tooling proficiency**: Effective, iterative prompts and smart use of codegen
- **Trade-off reasoning**: Justified choices and pragmatic scope management
- **Communication**: Clean README and clear process documentation

## Total Estimated Time: 4 hours per option

## 🆘 Getting Help

If you encounter any issues:

1. **Technical Problems**: Create an issue in this repository
2. **Clarifications**: Contact the hiring team via email
3. **Repository Access**: Ensure you've accepted the collaboration invitation

## 📞 Contact

If you have any questions about the assessment, please don't hesitate to reach out:

- Create an issue in this repository for technical questions
- Email the hiring team for other inquiries

---

**Good luck with your assessment! We look forward to reviewing your solution.** 🚀

> **Note**: This repository is private and only accessible to you and the assessment team. Your solution will be kept confidential.
