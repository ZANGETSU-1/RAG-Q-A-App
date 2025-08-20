# Option A: Monkey Registry App

## Task Overview

Build a super basic CRUD app that manages **Monkeys** using AI/codegen tools effectively.

**Time limit**: Max 4 hours actual work time

**Goal**: Turn a lightweight spec into a working feature fast, using AI/codegen tools effectively. We care about your approach, prompts, and delivery - not hand-crafted perfection.

## What We Are Looking For (15 pts total)

| Area                       | Pts | What we look for                                   |
| -------------------------- | --- | -------------------------------------------------- |
| **End-to-end delivery**    | 4   | CRUD works; persistence works; no hard crashes     |
| **Problem decomposition**  | 3   | Clear spec before coding; sensible breakdown       |
| **AI tooling proficiency** | 3   | Effective, iterative prompts; smart use of codegen |
| **Trade-off reasoning**    | 2   | Justified choices; pragmatic scope management      |
| **Communication**          | 3   | Clean README; clear process report or Loom         |

## Core Requirements

### 1. Frontend

- **Your choice**: CLI (fastest), Streamlit, or React/Next.js
- **Must support**:
  - **Create**: Add a monkey
  - **Read**: List/search monkeys
  - **Update**: Edit a monkey
  - **Delete**: Remove a monkey

### 2. Data Model (minimum fields)

- `monkey_id` (UUID/string)
- `name` (string, required, 2-40 chars)
- `species` (enum from fixed list: capuchin, macaque, marmoset, howler)
- `age_years` (integer 0-45)
- `favourite_fruit` (string)
- `last_checkup_at` (ISO datetime; optional)

### 3. Validation / Domain Rules

- Name required; no duplicates within the same species
- Age must be within 0-45
- If species = marmoset, age_years ≤ 22 (species cap)
- Simple search: by name or species

### 4. Backend / Storage

- **Preferred**: AWS DynamoDB (credentials provided)
  - Suggested keys: PK = `MONKEY#{monkey_id}`, SK = `MONKEY#{monkey_id}`
  - Add a **GSI** for species to support search (optional but nice)
- **Fallback**: SQLite or JSON **with a DB abstraction layer** so swapping to DynamoDB is straightforward
- If you don't know DynamoDB or can't figure it out quickly, don't sweat it

### 5. Automation / Testing

- At least **one automated test** (unit or integration). AI-generated is fine.

### 6. AI Use is REQUIRED

- Use an AI coding assistant (Claude, Copilot, Cursor, ChatGPT, etc.) for part of the build
- Start from a short spec, feed it to the AI, then iterate
- Include your prompts

## Stretch (optional, only if time permits)

- Import/export monkeys as CSV or JSON
- Tiny "insight": e.g., count by species, average age by species
- Image URL per monkey. Source the image, store on S3, store URL in DynamoDB

## What to Submit

1. **Working code**

   - GitHub repo
   - **README** with clear setup/run steps (local and, if used, AWS/DynamoDB)

2. **Process report** (max 2 pages or 5-10 min Loom)

   - Your initial feature spec (the one you gave to the AI)
   - Which AI tools you used and for what
   - **At least 3 key prompts** (paste exact text)
   - Design/trade-off decisions
   - Blockers and how you unblocked

3. **Evidence of AI use**
   - Prompt logs, screenshots, or tool transcripts

## Getting Started

1. **Write your spec first** - what will your app do?
2. **Choose your tech stack** - what's fastest for you?
3. **Start with AI** - feed your spec to an AI assistant
4. **Iterate and build** - keep it simple, get it working
5. **Document everything** - your process, prompts, decisions

**Tip**: Keep it lean. Ship the core first, stretch only if you truly have time.

Good luck! 🐒
