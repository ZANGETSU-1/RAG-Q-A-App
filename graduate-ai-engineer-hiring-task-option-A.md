
# **Trustie Graduate AI Engineer**


## **Builder Challenge: Option A**

**Build a Monkey Registry App**

**Time limit:** Max 4 hours actual work time

**Goal:** Turn a lightweight spec into a working feature fast, using AI/codegen tools effectively. 

We care about your approach, prompts, and delivery  not hand-crafted perfection.  

We are looking for builders with AI superpowers rather than coding genius. 

We are not looking for proficiency with a specific language or database, rather we are looking for people who can intelligently use AI tools to get things done. 


## **What we are looking for   (15 pts total)**


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
   <td>End-to-end delivery
   </td>
   <td>4
   </td>
   <td>CRUD works; persistence works; no hard crashes
   </td>
  </tr>
  <tr>
   <td>Problem decomposition
   </td>
   <td>3
   </td>
   <td>Clear spec before coding; sensible breakdown
   </td>
  </tr>
  <tr>
   <td>AI tooling proficiency
   </td>
   <td>3
   </td>
   <td>Effective, iterative prompts; smart use of codegen
   </td>
  </tr>
  <tr>
   <td>Trade-off reasoning
   </td>
   <td>2
   </td>
   <td>Justified choices; pragmatic scope management
   </td>
  </tr>
  <tr>
   <td>Communication
   </td>
   <td>3
   </td>
   <td>Clean README; clear process report or Loom
   </td>
  </tr>
</table>



## **The Task**

Build a super basic  CRUD app that manages **Monkeys**. 

Write a plain-English spec for a **Monkey Registry MVP** covering user journey, key functions, data model, and basic validation. 

Then provide **three AI prompts** youd use:



1. project/bootstrap prompt, 

2. implementing a concrete function (e.g., Update monkey with validation), 

3. testing/debugging (e.g., Generate Jest/pytest for CRUD + species rule).


### **Core requirements**



1. **Frontend**  your choice: 

    * CLI (fastest), Streamlit, or React/Next.js.

    * Must support: 

        * **Create**: Add a monkey 

        * **Read**: List/search monkeys 

        * **Update**: Edit a monkey 

        * **Delete**: Remove a monkey 

2. **Data model (minimum fields)**

    * monkey_id (UUID/string) 

    * name (string, required, 240 chars) 

    * species (enum from a fixed list you define: e.g., capuchin, macaque, marmoset, howler) 

    * age_years (integer 045) 

    * favourite_fruit (string) 

    * last_checkup_at (ISO datetime; optional) 

3. **Validation / domain rules**

    * Name required; no duplicates within the same species. 

      * Age must be within 045. 

    * If species = marmoset, age_years d 22 (species cap). 

    * Simple search: by name or species. 

4. **Backend / storage**

    * **Preferred:** AWS DynamoDB (credentials in your email). 

        * Suggested keys: PK = MONKEY#{monkey_id}, SK = MONKEY#{monkey_id} (or monkey_id as partition key). 

        * Add a **GSI** for species to support search (optional but nice). 

    * **Fallback:** SQLite or JSON **with a DB abstraction layer** so swapping to DynamoDB is straightforward.  
    * If you dont know dynamoDB or cant figure it out quickly, dont sweat it, we are not trying to tell if you understand any specific database and dont want you wasting your time getting hung up on infrastructure things. 

5. **Automation / testing**
    * At least **one automated test** (unit or integration). AI-generated is fine. 

6. **AI use is REQUIRED**
    * Use an AI coding assistant (Claude, Copilot, Cursor, ChatGPT, etc.) for part of the build. 

    * Start from a short spec feed it to the AI, then iterate. Include your prompts. 


**Stretch (optional, only if time permits)**

**Tip:** Keep it lean. Ship the core first, stretch only if you truly have time.



* Import/export monkeys as CSV or JSON. 

* Tiny insight: e.g., count by species, average age by species. 

* Image URL per monkey. Source the Image, Store the Image on S3. Storey the image URL in dynamoDB. 



## **What to submit**



1. **Working code**

    * GitHub repo 

    * **README** with clear setup/run steps (local and, if used, AWS/DynamoDB). 

2. **Process report** ** (max 2 pages or 510 min Loom) 

    * Your initial feature spec (the one you gave to the AI). 

    * Which AI tools you used and for what. 

    * **At least 3 key prompts** (paste exact text). 

    * Design/trade-off decisions (e.g., why Streamlit over React, why SQLite fallback). 

    * Blockers and how you unblocked. 

3. **Evidence of AI use**

    * Prompt logs, screenshots, or tool transcripts. 


