# Combined POS-based UD vs ROM Relations Analysis Report

**Date:** 2025-05-23 00:11:03
**Total Files Processed:** 5
**Total Sentences Processed:** 74
**Total Sentences Skipped:** 0

## 📁 File Processing Summary

| Input File | Benchmark File | Processed | Skipped | Total | POS-UD | POS-ROM |
|------------|----------------|-----------|---------|-------|--------|---------|
| adjective_clauses_sentences_input.txt | Adjective clauses.md | 10 | 0 | 10 | 80 | 70 |
| adverb_clauses_sentence_input.txt | Adverb clauses.md | 2 | 0 | 2 | 16 | 13 |
| basic_sentences_input.txt | Basic Sentences.md | 21 | 0 | 21 | 228 | 196 |
| compound_sentences_input.txt | Compound Sentences.md | 23 | 0 | 23 | 218 | 165 |
| noun_clauses_sentences_input.txt | Noun clauses.md | 18 | 0 | 18 | 145 | 126 |

## 📊 Overall Combined Statistics

| Metric | Count |
|--------|-------|
| Total POS-UD Relations | 687 |
| Total POS-ROM Relations | 570 |

## 📈 Overall Match Rate Analysis

| Metric | Value |
|--------|-------|
| Unique POS Pairs in UD | 51 |
| Unique POS Pairs in ROM | 58 |
| Common POS Pairs | 18 |
| POS Pair Overlap Rate | 19.8% |

## 🔍 Detailed POS Pair Analysis (Combined)

This section shows for each POS pair what UD relations and ROM relations appeared across all files.

### ADJ → ADJ

**UD Relations:**
- conj (2 occurrences)

**Examples:**
*UD Examples:*
  - **conj**: smart → creative in "She is both smart and creative." (compound_sentences_input.txt)
  - **conj**: long → boring in "The movie was not only long but also boring." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 2
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → ADV

**UD Relations:**
- advmod (9 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: sad → very in "She was very sad yesterday." (basic_sentences_input.txt)
  - **advmod**: smart → both in "She is both smart and creative." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 9
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → AUX

**UD Relations:**
- cop (16 occurrences)

**Examples:**
*UD Examples:*
  - **cop**: famous → is in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **cop**: nice → is in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 16
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → CCONJ

**UD Relations:**
- cc (2 occurrences)

**Examples:**
*UD Examples:*
  - **cc**: creative → and in "She is both smart and creative." (compound_sentences_input.txt)
  - **cc**: boring → but in "The movie was not only long but also boring." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 2
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → NOUN

**UD Relations:**
- nsubj (6 occurrences)
- obl:unmarked (1 occurrences)
- obl (1 occurrences)

**ROM Relations:**
- Constraint (10 occurrences)
- constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: famous → artist in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **nsubj**: nice → girl in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **obl:unmarked**: sad → yesterday in "She was very sad yesterday." (basic_sentences_input.txt)
  - **obl**: tall → brother in "She’s as tall as her brother." (compound_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: heartfelt → tone in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Constraint**: vivid → details in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **constraint**: Many → others in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 8
- Total ROM instances: 11
- ROM/UD ratio: 1.38
- **Status: Both UD and ROM relations exist for this POS pair**

---

### ADJ → PART

**UD Relations:**
- advmod (3 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: long → not in "The movie was not only long but also boring." (compound_sentences_input.txt)
  - **advmod**: easy → not in "This task is not as easy as it looks." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 3
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → PRON

**UD Relations:**
- nsubj (8 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: tired → she in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **nsubj**: sad → She in "She was very sad yesterday." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 8
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → PUNCT

**UD Relations:**
- punct (15 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: famous → . in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **punct**: nice → . in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 15
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → SCONJ

**UD Relations:**
- mark (3 occurrences)

**Examples:**
*UD Examples:*
  - **mark**: tired → Although in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **mark**: obvious → That in "That he lied was obvious." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 3
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADJ → VERB

**UD Relations:**
- advcl (3 occurrences)
- parataxis (2 occurrences)
- xcomp (1 occurrences)
- csubj (1 occurrences)
- ccomp (1 occurrences)

**Examples:**
*UD Examples:*
  - **parataxis**: clear → decided in "The sky was clear; we decided to go stargazing." (compound_sentences_input.txt)
  - **parataxis**: tired → kept in "I was tired; however, I kept working." (compound_sentences_input.txt)
  - **xcomp**: unsure → accept in "She’s unsure whether to accept the job or continue studying." (compound_sentences_input.txt)
  - **advcl**: easy → looks in "This task is not as easy as it looks." (compound_sentences_input.txt)
  - **advcl**: much → enjoys in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)
  - **csubj**: obvious → lied in "That he lied was obvious." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 8
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADP → ADJ

**ROM Relations:**
- Predicate (verb/preposition - object) (2 occurrences)
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: To → upscale in "Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: As → tall in "She’s as tall as her brother." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: As → much in "He doesn’t eat as much chocolate as his brother." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → ADP

**ROM Relations:**
- Connection (1 occurrences)
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Connection**: From → to in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **Constraint**: Out → of in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → ADV

**ROM Relations:**
- Predicate (verb/preposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/preposition - object)**: As → quickly in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → NOUN

**ROM Relations:**
- Predicate (verb/preposition - object) (8 occurrences)
- Predicate (preposition - object) (7 occurrences)
- Predicate (verb/proposition - object) (4 occurrences)
- Constraint (3 occurrences)
- constraint (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/preposition - object)**: of → nostalgia, of → comfort in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: of → nostalgia, of → comfort in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (preposition - object)**: into → book in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Predicate (preposition - object)**: from → friend in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)
  - **Constraint**: from → letter in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)
  - **Constraint**: of → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 24
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → NUM

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: of → one in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → PRON

**ROM Relations:**
- Predicate (verb/proposition - object) (1 occurrences)
- Predicate (prep - object) (1 occurrences)
- Predicate (verb/preposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: with → her in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)
  - **Predicate (prep - object)**: within → her in "The pain, like before, settled deep within her." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: With → us in "You can either stay home or come with us." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → PROPN

**ROM Relations:**
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: To → Canada in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### ADP → VERB

**ROM Relations:**
- Constraint (8 occurrences)
- constraint (6 occurrences)
- Predicate (verb/preposition - object) (3 occurrences)

**Examples:**
*ROM Examples:*
  - **constraint**: into → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **constraint**: with → filled in "The letter was filled with stories about their childhood adventures." (basic_sentences_input.txt)
  - **Constraint**: from → received in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)
  - **Constraint**: from → Fly, To → fly in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Than → watch in "I’d rather read a book than watch TV." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Than → drive in "He chose to walk rather than drive." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 17
- **Status: Only ROM relations exist (no UD match)**

---

### ADV → ADJ

**ROM Relations:**
- Constraint (1 occurrences)
- Predicate (verb/preposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: very → sad in "She was very sad yesterday." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Both → smart in "She is both smart and creative." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### ADV → ADP

**UD Relations:**
- fixed (2 occurrences)

**ROM Relations:**
- Connection (2 occurrences)

**Examples:**
*UD Examples:*
  - **fixed**: rather → than in "He chose to walk rather than drive." (compound_sentences_input.txt)
  - **fixed**: Rather → than in "Rather than complain, she took action." (compound_sentences_input.txt)

*ROM Examples:*
  - **Connection**: Rather → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)
  - **Connection**: Rather → than in "He chose to walk rather than drive." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 2
- Total ROM instances: 2
- ROM/UD ratio: 1.00
- **Status: Both UD and ROM relations exist for this POS pair**

---

### ADV → ADV

**UD Relations:**
- advmod (2 occurrences)
- conj (1 occurrences)

**ROM Relations:**
- Constraint (2 occurrences)

**Examples:**
*UD Examples:*
  - **conj**: effectively → efficiently in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **advmod**: quickly → as in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)
  - **advmod**: sooner → No in "No sooner had she sat down than the phone rang." (compound_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: Just → so in "Just as honesty builds trust, so does kindness." (compound_sentences_input.txt)
  - **Constraint**: Just → so in "Just as we need water to survive, so do plants need sunlight." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 3
- Total ROM instances: 2
- ROM/UD ratio: 0.67
- **Status: Both UD and ROM relations exist for this POS pair**

---

### ADV → AUX

**ROM Relations:**
- Constraint (4 occurrences)
- Predicate (subject - verb) (2 occurrences)
- Connection (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: However → was in "I was tired; however, I kept working." (compound_sentences_input.txt)
  - **Constraint**: both → is in "She is both smart and creative." (compound_sentences_input.txt)
  - **Predicate (subject - verb)**: How → is in "How she managed to escape is still a mystery." (noun_clauses_sentences_input.txt)
  - **Predicate (subject - verb)**: When → is in "When the meeting starts is still unknown." (noun_clauses_sentences_input.txt)
  - **Connection**: How → is in "The problem is how we can get there." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 7
- **Status: Only ROM relations exist (no UD match)**

---

### ADV → CCONJ

**UD Relations:**
- cc (1 occurrences)

**Examples:**
*UD Examples:*
  - **cc**: efficiently → and in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADV → INTJ

**UD Relations:**
- discourse (1 occurrences)

**Examples:**
*UD Examples:*
  - **discourse**: before → like in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADV → NOUN

**ROM Relations:**
- Constraint (5 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: When → year in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **Constraint**: When → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 5
- **Status: Only ROM relations exist (no UD match)**

---

### ADV → PUNCT

**UD Relations:**
- punct (2 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: before → , in "The pain, like before, settled deep within her." (basic_sentences_input.txt)
  - **punct**: however → , in "I was tired; however, I kept working." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 2
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### ADV → SCONJ

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: Just → as in "Just as the moon affects the tides, so does the sun influence them." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### ADV → VERB

**ROM Relations:**
- Constraint (16 occurrences)
- Predicate (verb/proposition - object) (5 occurrences)
- Predicate (verb/preposition - object) (4 occurrences)
- constraint (3 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: When → moved in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: When → met in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **constraint**: together → built in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)
  - **constraint**: Never → happened in "But it never happened." (basic_sentences_input.txt)
  - **Constraint**: again → broke in "That truth broke her heart again." (basic_sentences_input.txt)
  - **Constraint**: deep → settled in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 28
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → ADJ

**ROM Relations:**
- Predicate (verb/proposition - object) (7 occurrences)
- Predicate (verb/preposition - object) (7 occurrences)
- Predicate (verb - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Is → famous in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Is → nice in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb - object)**: was → sad in "She was very sad yesterday." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Was → clear in "The sky was clear; we decided to go stargazing." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Was → tired in "I was tired; however, I kept working." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 15
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → ADP

**ROM Relations:**
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Were → out in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → ADV

**ROM Relations:**
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Is → how in "The problem is how we can get there." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → NOUN

**ROM Relations:**
- Predicate (verb/proposition - object) (7 occurrences)
- Predicate (verb - object) (1 occurrences)
- Predicate (verb/preposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Is → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Is → doctor, Is → classmate in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb - object)**: was → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Are → engineers in "Both my brother and sister are engineers." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 9
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → SCONJ

**ROM Relations:**
- Predicate (verb/proposition - object) (3 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Is → that in "The truth is that she never left." (noun_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Is → that in "My suggestion is that we take a break." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### AUX → VERB

**ROM Relations:**
- Constraint (13 occurrences)
- Predicate (verb/proposition - object) (5 occurrences)
- Constraint (auxiliary - main verb) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Was → raining in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Predicate (verb/proposition - object)**: Is → left in "The truth is that she never left." (noun_clauses_sentences_input.txt)
  - **Constraint (auxiliary - main verb)**: would → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)
  - **Constraint**: Can → fly in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **Constraint**: Can → stay, Can → come in "You can either stay home or come with us." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 19
- **Status: Only ROM relations exist (no UD match)**

---

### CCONJ → ADJ

**ROM Relations:**
- connection (1 occurrences)
- Predicate (verb/preposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **connection**: and → vivid in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: And → creative in "She is both smart and creative." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### CCONJ → AUX

**ROM Relations:**
- Constraint (3 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: and → is in "She is both smart and creative." (compound_sentences_input.txt)
  - **Constraint**: both → are, and → are in "Both my brother and sister are engineers." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### CCONJ → CCONJ

**ROM Relations:**
- connection (2 occurrences)
- Connection (1 occurrences)

**Examples:**
*ROM Examples:*
  - **connection**: both → and in "Both my brother and sister are engineers." (compound_sentences_input.txt)
  - **connection**: Either → or in "You can either stay home or come with us." (compound_sentences_input.txt)
  - **Connection**: Neither → Nor in "Neither did he apologize, nor did he show any regret." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### CCONJ → NOUN

**ROM Relations:**
- Predicate (verb/preposition - object) (3 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/preposition - object)**: Both → brother, And → sister in "Both my brother and sister are engineers." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Both → brother, And → sister in "Both my brother and sister are engineers." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 3
- **Status: Only ROM relations exist (no UD match)**

---

### CCONJ → VERB

**ROM Relations:**
- Predicate (verb/preposition - object) (6 occurrences)
- Constraint (3 occurrences)
- connect (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: But → happened in "But it never happened." (basic_sentences_input.txt)
  - **Constraint**: But → wanted in "She wanted to go for a walk, but it started raining." (compound_sentences_input.txt)
  - **connect**: and → stop, and → slow in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **connect**: and → stop, and → slow in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: But → started in "She wanted to go for a walk, but it started raining." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Either → stay, Or → come in "You can either stay home or come with us." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 11
- **Status: Only ROM relations exist (no UD match)**

---

### DET → ADP

**UD Relations:**
- case (1 occurrences)

**Examples:**
*UD Examples:*
  - **case**: another → to in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### DET → NOUN

**ROM Relations:**
- Constraint (60 occurrences)
- constraint (4 occurrences)
- Constraint (determiner - noun) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: The → boy, The → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: The → boy, The → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **constraint**: The → time in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)
  - **constraint**: That → truth in "That truth broke her heart again." (basic_sentences_input.txt)
  - **Constraint (determiner - noun)**: a → treehouse in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 65
- **Status: Only ROM relations exist (no UD match)**

---

### INTJ → ADV

**ROM Relations:**
- Predicate (prep - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (prep - object)**: Like → before in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### INTJ → NOUN

**ROM Relations:**
- constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **constraint**: Like → pain in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### NOUN → ADJ

**UD Relations:**
- amod (12 occurrences)

**Examples:**
*UD Examples:*
  - **amod**: tone → heartfelt in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **amod**: details → vivid in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 12
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → ADP

**UD Relations:**
- case (22 occurrences)

**Examples:**
*UD Examples:*
  - **case**: memories → by in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **case**: nostalgia → of in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 22
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → ADV

**UD Relations:**
- advmod (5 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: stories → only, emotions → also in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)
  - **advmod**: stories → only, emotions → also in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 5
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → AUX

**UD Relations:**
- cop (9 occurrences)

**ROM Relations:**
- Predicate (subject - verb) (16 occurrences)
- Constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **cop**: friend → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **cop**: doctor → is, classmate → is in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)

*ROM Examples:*
  - **Predicate (subject - verb)**: Boy → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (subject - verb)**: Artist → is in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Constraint**: yesterday → was in "She was very sad yesterday." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 9
- Total ROM instances: 17
- ROM/UD ratio: 1.89
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NOUN → CCONJ

**UD Relations:**
- cc (5 occurrences)
- cc:preconj (1 occurrences)

**ROM Relations:**
- Connection (4 occurrences)

**Examples:**
*UD Examples:*
  - **cc**: emotions → but in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)
  - **cc**: love → and in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **cc:preconj**: brother → Both in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*ROM Examples:*
  - **Connection**: nostalgia → and, comfort → and in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Connection**: nostalgia → and, comfort → and in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 6
- Total ROM instances: 4
- ROM/UD ratio: 0.67
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NOUN → DET

**UD Relations:**
- det (65 occurrences)

**Examples:**
*UD Examples:*
  - **det**: boy → The in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **det**: artist → The in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 65
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → NOUN

**UD Relations:**
- nmod (7 occurrences)
- compound (7 occurrences)
- conj (5 occurrences)
- nsubj (4 occurrences)
- acl:relcl (1 occurrences)
- acl (1 occurrences)

**ROM Relations:**
- Constraint (6 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: friend → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **nsubj**: classmate → boy, doctor → father in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)
  - **acl:relcl**: boy → doctor in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)
  - **conj**: stories → emotions in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)
  - **conj**: nostalgia → comfort, nostalgia → love in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **nmod**: emotions → nostalgia in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: sincerity → details in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **Constraint**: childhood → adventures in "The letter was filled with stories about their childhood adventures." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 25
- Total ROM instances: 6
- ROM/UD ratio: 0.24
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NOUN → NUM

**UD Relations:**
- nummod (3 occurrences)
- nsubj (1 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: year → 2018 in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **nummod**: location → one in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **nummod**: MW → 5, MW → 10 in "Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 4
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → PART

**UD Relations:**
- advmod (1 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: stories → not in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → PRON

**UD Relations:**
- nmod:poss (17 occurrences)
- nsubj (3 occurrences)
- appos (2 occurrences)

**ROM Relations:**
- Connection (2 occurrences)
- connection (1 occurrences)
- constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **nmod:poss**: friend → my in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **nmod:poss**: car → whose in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **appos**: girl → whom in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **appos**: movie → that in "The movie (that) we watched was amazing." (adjective_clauses_sentences_input.txt)
  - **nsubj**: place → This in "This is the place where we stayed." (adjective_clauses_sentences_input.txt)
  - **nsubj**: lie → It in "It is a lie that you love her." (basic_sentences_input.txt)

*ROM Examples:*
  - **Connection**: tone → that in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Connection**: House → that in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **connection**: friends → who in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **constraint**: story → her in "Nobody told her the full story." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 22
- Total ROM instances: 4
- ROM/UD ratio: 0.18
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NOUN → PROPN

**UD Relations:**
- compound (1 occurrences)

**Examples:**
*UD Examples:*
  - **compound**: journal → JIDPS in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → PUNCT

**UD Relations:**
- punct (15 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: friend → . in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **punct**: man → . in "The man whose car broke down." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 15
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → SCONJ

**UD Relations:**
- mark (1 occurrences)

**Examples:**
*UD Examples:*
  - **mark**: time → that in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NOUN → VERB

**UD Relations:**
- acl:relcl (14 occurrences)
- acl (3 occurrences)
- advcl (1 occurrences)
- amod (1 occurrences)
- csubj (1 occurrences)

**ROM Relations:**
- Predicate (subject - verb) (25 occurrences)
- Constraint (2 occurrences)
- constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **acl:relcl**: boy → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **acl:relcl**: artist → painted in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **advcl**: year → moved in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **amod**: memories → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **csubj**: mystery → managed in "How she managed to escape is still a mystery." (noun_clauses_sentences_input.txt)
  - **acl**: news → married in "I heard the news that she got married." (noun_clauses_sentences_input.txt)

*ROM Examples:*
  - **Predicate (subject - verb)**: boy → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (subject - verb)**: artist → painted in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Constraint**: week → received in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)
  - **Constraint**: Water → survive in "Just as we need water to survive, so do plants need sunlight." (compound_sentences_input.txt)
  - **constraint**: time → built in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 20
- Total ROM instances: 28
- ROM/UD ratio: 1.40
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NUM → AUX

**UD Relations:**
- cop (1 occurrences)

**ROM Relations:**
- Predicate (subject - verb) (1 occurrences)

**Examples:**
*UD Examples:*
  - **cop**: one → was in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

*ROM Examples:*
  - **Predicate (subject - verb)**: 2018 → was in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 1
- ROM/UD ratio: 1.00
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NUM → NOUN

**UD Relations:**
- nmod (1 occurrences)

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **nmod**: one → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: One → location in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 1
- ROM/UD ratio: 1.00
- **Status: Both UD and ROM relations exist for this POS pair**

---

### NUM → PRON

**UD Relations:**
- nsubj (1 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: one → It in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### NUM → PUNCT

**UD Relations:**
- punct (1 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: one → . in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### PART → ADJ

**ROM Relations:**
- Constraint (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: Not → easy in "This task is not as easy as it looks." (compound_sentences_input.txt)
  - **Constraint**: Not → sure in "He’s not sure if he locked the door." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### PART → VERB

**ROM Relations:**
- Constraint (10 occurrences)
- Predicate (verb/preposition - object) (6 occurrences)
- Predicate (verb/proposition - object) (4 occurrences)
- Predicate (preposition - object) (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: to → decided, to → decided in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Constraint**: to → decided, to → decided in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (preposition - object)**: to → preserve, to → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (preposition - object)**: to → preserve, to → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: To → manage in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: to → stop, To → slow in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 22
- **Status: Only ROM relations exist (no UD match)**

---

### PRON → ADP

**UD Relations:**
- case (3 occurrences)

**Examples:**
*UD Examples:*
  - **case**: her → with in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)
  - **case**: her → within in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 3
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### PRON → AUX

**ROM Relations:**
- Predicate (subject - verb) (11 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (subject - verb)**: This → is in "This is the place where we stayed." (adjective_clauses_sentences_input.txt)
  - **Predicate (subject - verb)**: It → was in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 11
- **Status: Only ROM relations exist (no UD match)**

---

### PRON → NOUN

**ROM Relations:**
- Constraint (16 occurrences)
- Connection (7 occurrences)
- connection (2 occurrences)
- Predicate (subject - verb) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Connection**: Who → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Connection**: Who → artist in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Constraint**: My → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: Whose → car in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **connection**: its → journal in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **connection**: that → lie in "It is a lie that you love her." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 26
- **Status: Only ROM relations exist (no UD match)**

---

### PRON → PRON

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: me → what in "She didn’t tell me what had happened." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### PRON → PUNCT

**UD Relations:**
- punct (4 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: whom → (, whom → ) in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **punct**: whom → (, whom → ) in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 4
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### PRON → VERB

**UD Relations:**
- acl:relcl (1 occurrences)

**ROM Relations:**
- Predicate (subject - verb) (68 occurrences)
- constraint (1 occurrences)
- Predicate (subject - verb) (second clause) (1 occurrences)

**Examples:**
*UD Examples:*
  - **acl:relcl**: What → said in "What she said surprised everyone." (noun_clauses_sentences_input.txt)

*ROM Examples:*
  - **Predicate (subject - verb)**: Who → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (subject - verb)**: Who → painted in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **constraint**: her → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (subject - verb) (second clause)**: She → enjoys in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 70
- ROM/UD ratio: 70.00
- **Status: Both UD and ROM relations exist for this POS pair**

---

### PROPN → ADP

**UD Relations:**
- case (1 occurrences)

**Examples:**
*UD Examples:*
  - **case**: Canada → to in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### PROPN → NOUN

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: JIDPS → journal in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 1
- **Status: Only ROM relations exist (no UD match)**

---

### PROPN → VERB

**ROM Relations:**
- Predicate (subject - verb) (5 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (subject - verb)**: Sarah → decided, Sarah → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (subject - verb)**: Sarah → decided, Sarah → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 5
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → ADJ

**ROM Relations:**
- Predicate (verb/preposition - object) (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/preposition - object)**: As → easy in "This task is not as easy as it looks." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: As → much in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → ADV

**ROM Relations:**
- Connection (3 occurrences)
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Connection**: As → so in "Just as the moon affects the tides, so does the sun influence them." (compound_sentences_input.txt)
  - **Connection**: As → so in "Just as honesty builds trust, so does kindness." (compound_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: About → how in "We’re thinking about how we can solve the problem." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 4
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → AUX

**ROM Relations:**
- Predicate (verb/proposition - object) (4 occurrences)
- Constraint (1 occurrences)
- Predicate (subject - verb) (1 occurrences)
- Connection (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Because → was in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Predicate (verb/proposition - object)**: Although → was in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **Constraint**: As → is in "This task is not as easy as it looks." (compound_sentences_input.txt)
  - **Predicate (subject - verb)**: That → was in "That he lied was obvious." (noun_clauses_sentences_input.txt)
  - **Connection**: That → is in "I know that she is right." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 7
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → CCONJ

**ROM Relations:**
- Connection (2 occurrences)

**Examples:**
*ROM Examples:*
  - **Connection**: Whether → Or in "I don't know whether he’ll call or text." (compound_sentences_input.txt)
  - **Connection**: Whether → Or in "She’s unsure whether to accept the job or continue studying." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 2
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → NOUN

**ROM Relations:**
- Constraint (4 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: that → News in "I heard the news that she got married." (noun_clauses_sentences_input.txt)
  - **Constraint**: That → idea in "The idea that hard work brings success is widely accepted." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 4
- **Status: Only ROM relations exist (no UD match)**

---

### SCONJ → VERB

**ROM Relations:**
- Constraint (9 occurrences)
- Predicate (verb/proposition - object) (5 occurrences)
- Predicate (verb/preposition - object) (2 occurrences)
- Connection (2 occurrences)
- Predicate (verb - object) (1 occurrences)
- connection (1 occurrences)
- Predicate (subject - verb) (1 occurrences)

**Examples:**
*ROM Examples:*
  - **Constraint**: Because → stayed in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Constraint**: Although → finished in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **Predicate (verb - object)**: as → read in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Whether → call in "I don't know whether he’ll call or text." (compound_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Whether → accept in "She’s unsure whether to accept the job or continue studying." (compound_sentences_input.txt)
  - **connection**: That → lied in "That he lied was obvious." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 0
- Total ROM instances: 21
- **Status: Only ROM relations exist (no UD match)**

---

### VERB → ADJ

**UD Relations:**
- advcl (1 occurrences)
- advmod (1 occurrences)
- ccomp (1 occurrences)

**Examples:**
*UD Examples:*
  - **advcl**: finished → tired in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **advmod**: enjoys → much in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)
  - **ccomp**: know → right in "I know that she is right." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 3
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → ADP

**UD Relations:**
- compound:prt (3 occurrences)
- mark (1 occurrences)

**ROM Relations:**
- Constraint (3 occurrences)

**Examples:**
*UD Examples:*
  - **compound:prt**: broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **compound:prt**: slow → down in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **mark**: watch → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: Broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **Constraint**: Moved → to in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 4
- Total ROM instances: 3
- ROM/UD ratio: 0.75
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → ADV

**UD Relations:**
- advmod (32 occurrences)
- cc (1 occurrences)
- mark (1 occurrences)

**ROM Relations:**
- Predicate (verb/proposition - object) (2 occurrences)
- Constraint (1 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: moved → when in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **advmod**: met → when in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **cc**: drive → rather in "He chose to walk rather than drive." (compound_sentences_input.txt)
  - **mark**: complain → Rather in "Rather than complain, she took action." (compound_sentences_input.txt)

*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Stayed → home in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Predicate (verb/proposition - object)**: Get → there in "The problem is how we can get there." (noun_clauses_sentences_input.txt)
  - **Constraint**: Stay → home in "You can either stay home or come with us." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 34
- Total ROM instances: 3
- ROM/UD ratio: 0.09
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → AUX

**UD Relations:**
- aux (24 occurrences)
- cop (4 occurrences)
- aux:pass (3 occurrences)

**ROM Relations:**
- Predicate (subject - verb) (1 occurrences)
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*UD Examples:*
  - **aux**: know → do in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **aux**: raining → was in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **aux:pass**: filled → was in "The letter was filled with stories about their childhood adventures." (basic_sentences_input.txt)
  - **aux:pass**: married → got in "I heard the news that she got married." (noun_clauses_sentences_input.txt)
  - **cop**: left → is in "The truth is that she never left." (noun_clauses_sentences_input.txt)
  - **cop**: take → is in "My suggestion is that we take a break." (noun_clauses_sentences_input.txt)

*ROM Examples:*
  - **Predicate (subject - verb)**: lied → was in "That he lied was obvious." (noun_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Know → is in "I know that she is right." (noun_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 31
- Total ROM instances: 2
- ROM/UD ratio: 0.06
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → CCONJ

**UD Relations:**
- cc (7 occurrences)
- cc:preconj (2 occurrences)

**Examples:**
*UD Examples:*
  - **cc**: happened → But in "But it never happened." (basic_sentences_input.txt)
  - **cc**: slow → and in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **cc:preconj**: stay → either in "You can either stay home or come with us." (compound_sentences_input.txt)
  - **cc:preconj**: apologize → Neither in "Neither did he apologize, nor did he show any regret." (compound_sentences_input.txt)

**Analysis:**
- Total UD instances: 9
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → DET

**UD Relations:**
- obl (1 occurrences)

**Examples:**
*UD Examples:*
  - **obl**: fly → another in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 1
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → NOUN

**UD Relations:**
- obj (39 occurrences)
- nsubj (17 occurrences)
- obl (9 occurrences)
- nsubj:outer (4 occurrences)
- obl:agent (2 occurrences)
- obl:unmarked (2 occurrences)
- nsubj:pass (2 occurrences)
- conj (1 occurrences)

**ROM Relations:**
- Predicate (verb/preposition - object) (19 occurrences)
- Predicate (verb/proposition - object) (18 occurrences)
- Predicate (verb - object) (6 occurrences)
- Constraint (4 occurrences)
- Predicate (preposition - object) (1 occurrences)
- Predicate (verb/preposition - object) (second clause) (1 occurrences)
- Predicate (verb/preposition - object) (implied) (1 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: broke → car in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **nsubj**: shared → grandmother in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)
  - **obj**: remember → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **obj**: know → reason in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **obl:agent**: Inspired → memories in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **obl:agent**: moved → sincerity in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Remember → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Know → reason in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **Constraint**: met → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **Constraint**: stayed → place in "This is the place where we stayed." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb - object)**: cherished → memories in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (verb - object)**: moved → friends, read → journal in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 76
- Total ROM instances: 50
- ROM/UD ratio: 0.66
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → PART

**UD Relations:**
- mark (11 occurrences)
- advmod (6 occurrences)

**Examples:**
*UD Examples:*
  - **advmod**: know → n’t in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **advmod**: win → Not in "Not only did he win, but he also broke the record." (compound_sentences_input.txt)
  - **mark**: start → to, preserve → to in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **mark**: start → to, preserve → to in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 17
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → PRON

**UD Relations:**
- nsubj (67 occurrences)
- obj (9 occurrences)
- obl (3 occurrences)
- iobj (2 occurrences)
- nsubj:pass (1 occurrences)

**ROM Relations:**
- Predicate (verb/proposition - object) (8 occurrences)
- Predicate (verb/preposition - object) (2 occurrences)
- Predicate (verb - object) (2 occurrences)

**Examples:**
*UD Examples:*
  - **nsubj**: sings → who in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **nsubj**: painted → who in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **obj**: painted → this in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **obj**: preserve → them in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **obl**: stayed → her in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)
  - **obl**: settled → her in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

*ROM Examples:*
  - **Predicate (verb/proposition - object)**: Painted → this in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Met → whom in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: surprised → her in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Influence → them in "Just as the moon affects the tides, so does the sun influence them." (compound_sentences_input.txt)
  - **Predicate (verb - object)**: found → themselves in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **Predicate (verb - object)**: told → her in "Nobody told her the full story." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 82
- Total ROM instances: 12
- ROM/UD ratio: 0.15
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → PROPN

**UD Relations:**
- nsubj (2 occurrences)
- obl (1 occurrences)
- obj (1 occurrences)

**ROM Relations:**
- Constraint (1 occurrences)
- Predicate (verb/proposition - object) (1 occurrences)

**Examples:**
*UD Examples:*
  - **obl**: moved → Canada in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **nsubj**: decided → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **nsubj**: received → Emily in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)
  - **obj**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)

*ROM Examples:*
  - **Constraint**: Inspired → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 4
- Total ROM instances: 2
- ROM/UD ratio: 0.50
- **Status: Both UD and ROM relations exist for this POS pair**

---

### VERB → PUNCT

**UD Relations:**
- punct (61 occurrences)

**Examples:**
*UD Examples:*
  - **punct**: remember → . in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **punct**: know → . in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)

**Analysis:**
- Total UD instances: 61
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → SCONJ

**UD Relations:**
- mark (19 occurrences)

**Examples:**
*UD Examples:*
  - **mark**: raining → because in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **mark**: read → as in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 19
- Total ROM instances: 0
- **Status: Only UD relations exist (no ROM coverage)**

---

### VERB → VERB

**UD Relations:**
- advcl (17 occurrences)
- xcomp (14 occurrences)
- conj (7 occurrences)
- ccomp (3 occurrences)

**ROM Relations:**
- Predicate (verb/preposition - object) (6 occurrences)
- Predicate (verb/proposition - object) (2 occurrences)
- Predicate (verb - object) (1 occurrences)
- constraint (1 occurrences)
- Constraint (1 occurrences)
- Predicate (subject - verb) (1 occurrences)

**Examples:**
*UD Examples:*
  - **advcl**: remember → met in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **advcl**: stayed → raining in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **xcomp**: decided → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **xcomp**: gave → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **ccomp**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)
  - **ccomp**: know → call in "I don't know whether he’ll call or text." (compound_sentences_input.txt)

*ROM Examples:*
  - **Predicate (verb/preposition - object)**: gave → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (verb/preposition - object)**: Started → raining in "She wanted to go for a walk, but it started raining." (compound_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: consider → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Predicate (verb/proposition - object)**: Know → arrive in "I don’t know when the package will arrive." (noun_clauses_sentences_input.txt)
  - **Predicate (verb - object)**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)
  - **constraint**: hoping → waited in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

**Analysis:**
- Total UD instances: 41
- Total ROM instances: 12
- ROM/UD ratio: 0.29
- **Status: Both UD and ROM relations exist for this POS pair**

---

## 📋 Combined Summary Tables

### UD Relations Summary (All Files)
| UD Relation | Count | Percentage |
|-------------|-------|------------|
| nsubj | 109 | 15.9% |
| punct | 98 | 14.3% |
| det | 65 | 9.5% |
| advmod | 59 | 8.6% |
| obj | 49 | 7.1% |
| mark | 36 | 5.2% |
| cop | 30 | 4.4% |
| case | 27 | 3.9% |
| aux | 24 | 3.5% |
| advcl | 22 | 3.2% |
| nmod:poss | 17 | 2.5% |
| acl:relcl | 16 | 2.3% |
| cc | 16 | 2.3% |
| conj | 16 | 2.3% |
| obl | 15 | 2.2% |
| xcomp | 15 | 2.2% |
| amod | 13 | 1.9% |
| nmod | 8 | 1.2% |
| compound | 8 | 1.2% |
| ccomp | 5 | 0.7% |
| nsubj:outer | 4 | 0.6% |
| acl | 4 | 0.6% |
| compound:prt | 3 | 0.4% |
| obl:unmarked | 3 | 0.4% |
| nsubj:pass | 3 | 0.4% |
| aux:pass | 3 | 0.4% |
| nummod | 3 | 0.4% |
| cc:preconj | 3 | 0.4% |
| appos | 2 | 0.3% |
| obl:agent | 2 | 0.3% |
| iobj | 2 | 0.3% |
| parataxis | 2 | 0.3% |
| fixed | 2 | 0.3% |
| csubj | 2 | 0.3% |
| discourse | 1 | 0.1% |

### ROM Relations Summary (All Files)
| ROM Relation | Count | Percentage |
|--------------|-------|------------|
| Constraint | 196 | 34.4% |
| Predicate (subject - verb) | 133 | 23.3% |
| Predicate (verb/proposition - object) | 81 | 14.2% |
| Predicate (verb/preposition - object) | 75 | 13.2% |
| Connection | 26 | 4.6% |
| constraint | 21 | 3.7% |
| Predicate (verb - object) | 12 | 2.1% |
| Predicate (preposition - object) | 10 | 1.8% |
| connection | 7 | 1.2% |
| Predicate (prep - object) | 2 | 0.4% |
| connect | 2 | 0.4% |
| Constraint (determiner - noun) | 1 | 0.2% |
| Constraint (auxiliary - main verb) | 1 | 0.2% |
| Predicate (subject - verb) (second clause) | 1 | 0.2% |
| Predicate (verb/preposition - object) (second clause) | 1 | 0.2% |
| Predicate (verb/preposition - object) (implied) | 1 | 0.2% |

### POS Pairs Distribution (All Files)
| POS Pair | UD Count | ROM Count | Status |
|----------|----------|-----------|--------|
| VERB → NOUN | 76 | 50 | Both |
| VERB → PRON | 82 | 12 | Both |
| PRON → VERB | 1 | 70 | Both |
| NOUN → DET | 65 | 0 | UD Only |
| DET → NOUN | 0 | 65 | ROM Only |
| VERB → PUNCT | 61 | 0 | UD Only |
| VERB → VERB | 41 | 12 | Both |
| NOUN → VERB | 20 | 28 | Both |
| VERB → ADV | 34 | 3 | Both |
| VERB → AUX | 31 | 2 | Both |
| NOUN → NOUN | 25 | 6 | Both |
| ADV → VERB | 0 | 28 | ROM Only |
| PRON → NOUN | 0 | 26 | ROM Only |
| NOUN → PRON | 22 | 4 | Both |
| NOUN → AUX | 9 | 17 | Both |
| ADP → NOUN | 0 | 24 | ROM Only |
| NOUN → ADP | 22 | 0 | UD Only |
| PART → VERB | 0 | 22 | ROM Only |
| SCONJ → VERB | 0 | 21 | ROM Only |
| ADJ → NOUN | 8 | 11 | Both |
| VERB → SCONJ | 19 | 0 | UD Only |
| AUX → VERB | 0 | 19 | ROM Only |
| VERB → PART | 17 | 0 | UD Only |
| ADP → VERB | 0 | 17 | ROM Only |
| ADJ → AUX | 16 | 0 | UD Only |
| NOUN → PUNCT | 15 | 0 | UD Only |
| AUX → ADJ | 0 | 15 | ROM Only |
| ADJ → PUNCT | 15 | 0 | UD Only |
| NOUN → ADJ | 12 | 0 | UD Only |
| CCONJ → VERB | 0 | 11 | ROM Only |
| PRON → AUX | 0 | 11 | ROM Only |
| NOUN → CCONJ | 6 | 4 | Both |
| AUX → NOUN | 0 | 9 | ROM Only |
| VERB → CCONJ | 9 | 0 | UD Only |
| ADJ → ADV | 9 | 0 | UD Only |
| ADJ → VERB | 8 | 0 | UD Only |
| ADJ → PRON | 8 | 0 | UD Only |
| VERB → ADP | 4 | 3 | Both |
| SCONJ → AUX | 0 | 7 | ROM Only |
| ADV → AUX | 0 | 7 | ROM Only |
| VERB → PROPN | 4 | 2 | Both |
| PROPN → VERB | 0 | 5 | ROM Only |
| ADV → NOUN | 0 | 5 | ROM Only |
| ADV → ADV | 3 | 2 | Both |
| NOUN → ADV | 5 | 0 | UD Only |
| PRON → PUNCT | 4 | 0 | UD Only |
| SCONJ → NOUN | 0 | 4 | ROM Only |
| ADV → ADP | 2 | 2 | Both |
| SCONJ → ADV | 0 | 4 | ROM Only |
| NOUN → NUM | 4 | 0 | UD Only |
| PRON → ADP | 3 | 0 | UD Only |
| CCONJ → NOUN | 0 | 3 | ROM Only |
| ADP → ADJ | 0 | 3 | ROM Only |
| ADJ → SCONJ | 3 | 0 | UD Only |
| ADJ → PART | 3 | 0 | UD Only |
| ADP → PRON | 0 | 3 | ROM Only |
| CCONJ → AUX | 0 | 3 | ROM Only |
| AUX → SCONJ | 0 | 3 | ROM Only |
| VERB → ADJ | 3 | 0 | UD Only |
| CCONJ → CCONJ | 0 | 3 | ROM Only |
| SCONJ → CCONJ | 0 | 2 | ROM Only |
| ADP → ADP | 0 | 2 | ROM Only |
| NUM → NOUN | 1 | 1 | Both |
| ADJ → ADJ | 2 | 0 | UD Only |
| ADJ → CCONJ | 2 | 0 | UD Only |
| CCONJ → ADJ | 0 | 2 | ROM Only |
| SCONJ → ADJ | 0 | 2 | ROM Only |
| PART → ADJ | 0 | 2 | ROM Only |
| ADV → ADJ | 0 | 2 | ROM Only |
| NUM → AUX | 1 | 1 | Both |
| ADV → PUNCT | 2 | 0 | UD Only |
| NOUN → PART | 1 | 0 | UD Only |
| INTJ → NOUN | 0 | 1 | ROM Only |
| AUX → ADP | 0 | 1 | ROM Only |
| VERB → DET | 1 | 0 | UD Only |
| ADP → PROPN | 0 | 1 | ROM Only |
| NOUN → PROPN | 1 | 0 | UD Only |
| ADP → ADV | 0 | 1 | ROM Only |
| ADV → SCONJ | 0 | 1 | ROM Only |
| AUX → ADV | 0 | 1 | ROM Only |
| NOUN → SCONJ | 1 | 0 | UD Only |
| NUM → PRON | 1 | 0 | UD Only |
| PROPN → NOUN | 0 | 1 | ROM Only |
| ADV → INTJ | 1 | 0 | UD Only |
| ADV → CCONJ | 1 | 0 | UD Only |
| INTJ → ADV | 0 | 1 | ROM Only |
| PRON → PRON | 0 | 1 | ROM Only |
| DET → ADP | 1 | 0 | UD Only |
| ADP → NUM | 0 | 1 | ROM Only |
| PROPN → ADP | 1 | 0 | UD Only |
| NUM → PUNCT | 1 | 0 | UD Only |

## 📂 File-Specific Analysis

### adjective_clauses_sentences_input.txt ↔ Adjective clauses.md

| Metric | Count |
|--------|-------|
| Processed Sentences | 10 |
| Skipped Sentences | 0 |
| POS-UD Relations | 80 |
| POS-ROM Relations | 70 |

**Top UD Relations:**
- nsubj: 19
- punct: 14
- det: 11
- acl:relcl: 8
- cop: 8

**Top ROM Relations:**
- Constraint: 25
- Predicate (subject - verb): 21
- Predicate (verb/proposition - object): 18
- Connection: 6

---

### adverb_clauses_sentence_input.txt ↔ Adverb clauses.md

| Metric | Count |
|--------|-------|
| Processed Sentences | 2 |
| Skipped Sentences | 0 |
| POS-UD Relations | 16 |
| POS-ROM Relations | 13 |

**Top UD Relations:**
- nsubj: 4
- punct: 3
- mark: 2
- advcl: 2
- advmod: 1

**Top ROM Relations:**
- Predicate (verb/proposition - object): 6
- Predicate (subject - verb): 4
- Constraint: 3

---

### basic_sentences_input.txt ↔ Basic Sentences.md

| Metric | Count |
|--------|-------|
| Processed Sentences | 21 |
| Skipped Sentences | 0 |
| POS-UD Relations | 228 |
| POS-ROM Relations | 196 |

**Top UD Relations:**
- punct: 30
- nsubj: 26
- det: 25
- obj: 20
- case: 18

**Top ROM Relations:**
- Constraint: 69
- Predicate (subject - verb): 36
- constraint: 20
- Predicate (verb/preposition - object): 16
- Predicate (verb/proposition - object): 16

---

### compound_sentences_input.txt ↔ Compound Sentences.md

| Metric | Count |
|--------|-------|
| Processed Sentences | 23 |
| Skipped Sentences | 0 |
| POS-UD Relations | 218 |
| POS-ROM Relations | 165 |

**Top UD Relations:**
- nsubj: 34
- punct: 33
- advmod: 28
- mark: 15
- obj: 15

**Top ROM Relations:**
- Predicate (verb/preposition - object): 59
- Constraint: 57
- Predicate (subject - verb): 35
- Connection: 8
- connection: 2

---

### noun_clauses_sentences_input.txt ↔ Noun clauses.md

| Metric | Count |
|--------|-------|
| Processed Sentences | 18 |
| Skipped Sentences | 0 |
| POS-UD Relations | 145 |
| POS-ROM Relations | 126 |

**Top UD Relations:**
- nsubj: 26
- punct: 18
- det: 15
- mark: 13
- advmod: 13

**Top ROM Relations:**
- Constraint: 42
- Predicate (verb/proposition - object): 41
- Predicate (subject - verb): 37
- Connection: 4
- connection: 1

---

## 📝 Detailed Sentence Analysis

<details>
<summary>Click to expand individual sentence analysis</summary>

### Sentence 1 (adjective_clauses_sentences_input.txt)
**Input:** The boy who sings is my friend.

**POS-UD Relations:**
- NOUN → DET: det
- NOUN → NOUN: nsubj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- NOUN → AUX: cop
- NOUN → PRON: nmod:poss
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → VERB: Predicate (subject - verb)
- NOUN → VERB: Predicate (subject - verb)
- NOUN → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- PRON → NOUN: Constraint
- DET → NOUN: Constraint

### Sentence 2 (adjective_clauses_sentences_input.txt)
**Input:** The artist who painted this is famous.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- VERB → PRON: obj
- ADJ → AUX: cop
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → VERB: Predicate (subject - verb)
- NOUN → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)
- NOUN → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)

### Sentence 3 (adjective_clauses_sentences_input.txt)
**Input:** The girl (whom) I met is nice.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- PRON → PUNCT: punct
- NOUN → PRON: appos
- PRON → PUNCT: punct
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- ADJ → AUX: cop
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)
- NOUN → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)

### Sentence 4 (adjective_clauses_sentences_input.txt)
**Input:** The movie (that) we watched was amazing.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- PRON → PUNCT: punct
- NOUN → PRON: appos
- PRON → PUNCT: punct
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- ADJ → AUX: cop
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)
- NOUN → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)

### Sentence 5 (adjective_clauses_sentences_input.txt)
**Input:** The man whose car broke down.

**POS-UD Relations:**
- NOUN → DET: det
- NOUN → PRON: nmod:poss
- VERB → NOUN: nsubj
- NOUN → VERB: acl:relcl
- VERB → ADP: compound:prt
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → ADP: Constraint

### Sentence 6 (adjective_clauses_sentences_input.txt)
**Input:** The boy whose father is a doctor is my classmate.

**POS-UD Relations:**
- NOUN → DET: det
- NOUN → NOUN: nsubj
- NOUN → PRON: nmod:poss
- NOUN → NOUN: nsubj
- NOUN → AUX: cop
- NOUN → DET: det
- NOUN → NOUN: acl:relcl
- NOUN → AUX: cop
- NOUN → PRON: nmod:poss
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- PRON → NOUN: Constraint

### Sentence 7 (adjective_clauses_sentences_input.txt)
**Input:** 2018 was the year when I moved to Canada.

**POS-UD Relations:**
- NOUN → NUM: nsubj
- NOUN → AUX: cop
- NOUN → DET: det
- VERB → ADV: advmod
- VERB → PRON: nsubj
- NOUN → VERB: advcl
- PROPN → ADP: case
- VERB → PROPN: obl
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- NUM → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- ADV → VERB: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → ADP: Constraint
- ADP → PROPN: Predicate (verb/proposition - object)

### Sentence 8 (adjective_clauses_sentences_input.txt)
**Input:** I remember the day when we met.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → ADV: advmod
- VERB → PRON: nsubj
- VERB → VERB: advcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- ADV → VERB: Predicate (verb/proposition - object)
- VERB → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)

### Sentence 9 (adjective_clauses_sentences_input.txt)
**Input:** This is the place where we stayed.

**POS-UD Relations:**
- NOUN → PRON: nsubj
- NOUN → AUX: cop
- NOUN → DET: det
- VERB → ADV: advmod
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: Predicate (verb/proposition - object)
- VERB → NOUN: Constraint

### Sentence 10 (adjective_clauses_sentences_input.txt)
**Input:** I don’t know the reason why he left.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → PART: advmod
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → ADV: advmod
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: Predicate (verb/proposition - object)
- VERB → NOUN: Constraint

---

### Sentence 11 (adverb_clauses_sentence_input.txt)
**Input:** I stayed home because it was raining.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → ADV: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: advcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → ADV: Predicate (verb/proposition - object)
- SCONJ → VERB: Constraint
- SCONJ → AUX: Predicate (verb/proposition - object)
- PRON → AUX: Predicate (subject - verb)
- AUX → VERB: Predicate (verb/proposition - object)

### Sentence 12 (adverb_clauses_sentence_input.txt)
**Input:** Although she was tired, she finished the report.

**POS-UD Relations:**
- ADJ → SCONJ: mark
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- VERB → ADJ: advcl
- ADJ → PUNCT: punct
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- SCONJ → AUX: Predicate (verb/proposition - object)
- SCONJ → VERB: Constraint
- PRON → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 13 (basic_sentences_input.txt)
**Input:** Inspired by those cherished memories, Sarah decided to start a journal to preserve them.

**POS-UD Relations:**
- VERB → VERB: advcl
- NOUN → ADP: case
- NOUN → DET: det
- NOUN → VERB: amod
- VERB → NOUN: obl:agent
- VERB → PUNCT: punct
- VERB → PROPN: nsubj
- VERB → PART: mark
- VERB → VERB: xcomp
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PART: mark
- VERB → VERB: advcl
- VERB → PRON: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- VERB → PROPN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- DET → NOUN: Constraint
- VERB → NOUN: Predicate (verb - object)
- PROPN → VERB: Predicate (subject - verb)
- PROPN → VERB: Predicate (subject - verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (preposition - object)
- VERB → NOUN: Predicate (preposition - object)
- DET → NOUN: Constraint
- PART → VERB: Constraint
- PART → VERB: Predicate (preposition - object)
- NOUN → VERB: Predicate (subject - verb)
- PRON → NOUN: Connection

### Sentence 14 (basic_sentences_input.txt)
**Input:** She described not only the stories her grandmother shared, but also the emotions they stirred.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → PART: advmod
- NOUN → ADV: advmod
- NOUN → DET: det
- VERB → NOUN: obj
- NOUN → PRON: nmod:poss
- VERB → NOUN: nsubj
- NOUN → VERB: acl:relcl
- NOUN → PUNCT: punct
- NOUN → CCONJ: cc
- NOUN → ADV: advmod
- NOUN → DET: det
- NOUN → NOUN: conj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- PRON → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- VERB → NOUN: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)

### Sentence 15 (basic_sentences_input.txt)
**Input:** The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj
- NOUN → ADP: case
- NOUN → NOUN: nmod
- NOUN → PUNCT: punct
- NOUN → NOUN: conj
- NOUN → PUNCT: punct
- NOUN → CCONJ: cc
- NOUN → NOUN: conj
- VERB → PRON: obj
- VERB → VERB: xcomp
- NOUN → DET: det
- NOUN → ADJ: amod
- VERB → NOUN: obj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- VERB → PRON: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- NOUN → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/preposition - object)
- PRON → VERB: constraint
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- VERB → NOUN: Constraint
- ADJ → NOUN: Constraint
- NOUN → PRON: Connection
- NOUN → VERB: Predicate (subject - verb)
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/preposition - object)
- ADP → NOUN: Predicate (verb/preposition - object)
- ADP → NOUN: Predicate (verb/preposition - object)
- ADP → NOUN: Predicate (verb/preposition - object)
- NOUN → CCONJ: Connection
- NOUN → CCONJ: Connection
- NOUN → CCONJ: Connection

### Sentence 16 (basic_sentences_input.txt)
**Input:** Her friends who read the journal found themselves moved by its sincerity and vivid details.

**POS-UD Relations:**
- NOUN → PRON: nmod:poss
- VERB → NOUN: nsubj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PRON: obj
- VERB → VERB: xcomp
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- VERB → NOUN: obl:agent
- NOUN → CCONJ: cc
- NOUN → ADJ: amod
- NOUN → NOUN: conj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb - object)
- VERB → NOUN: Predicate (verb - object)
- NOUN → VERB: Predicate (subject - verb)
- PRON → NOUN: Constraint
- NOUN → CCONJ: Connection
- NOUN → NOUN: Constraint
- CCONJ → ADJ: connection
- ADJ → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)
- NOUN → VERB: Predicate (subject - verb)
- NOUN → PRON: connection
- VERB → NOUN: Predicate (verb - object)
- DET → NOUN: Constraint
- PRON → NOUN: connection

### Sentence 17 (basic_sentences_input.txt)
**Input:** Their encouragement pushed Sarah to consider turning the journal into a book.

**POS-UD Relations:**
- NOUN → PRON: nmod:poss
- VERB → NOUN: nsubj
- VERB → PROPN: obj
- VERB → PART: mark
- VERB → VERB: advcl
- VERB → VERB: xcomp
- NOUN → DET: det
- VERB → NOUN: obj
- NOUN → ADP: case
- NOUN → DET: det
- VERB → NOUN: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → PROPN: Predicate (verb/proposition - object)
- PROPN → VERB: Predicate (subject - verb)
- PROPN → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/proposition - object)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADP → VERB: constraint
- ADP → NOUN: Predicate (preposition - object)
- DET → NOUN: Constraint

### Sentence 18 (basic_sentences_input.txt)
**Input:** Emily received a letter from her best friend last week.

**POS-UD Relations:**
- VERB → PROPN: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- NOUN → ADJ: amod
- NOUN → NOUN: nmod
- NOUN → ADJ: amod
- VERB → NOUN: obl:unmarked
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PROPN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb - object)
- ADP → NOUN: Predicate (preposition - object)
- ADP → VERB: Constraint
- ADP → NOUN: Constraint
- NOUN → VERB: Constraint
- ADJ → NOUN: Constraint

### Sentence 19 (basic_sentences_input.txt)
**Input:** The letter was filled with stories about their childhood adventures.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj:pass
- VERB → AUX: aux:pass
- NOUN → ADP: case
- VERB → NOUN: obl
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- NOUN → NOUN: compound
- NOUN → NOUN: nmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- DET → NOUN: Constraint
- ADP → VERB: constraint
- ADP → NOUN: Predicate (verb/preposition - object)
- ADP → NOUN: constraint
- ADP → NOUN: Predicate (verb/preposition - object)
- PRON → NOUN: Constraint
- NOUN → NOUN: Constraint

### Sentence 20 (basic_sentences_input.txt)
**Input:** She smiled as she read about the time they built a treehouse together.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → VERB: advcl
- NOUN → ADP: case
- NOUN → DET: det
- VERB → NOUN: obl
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- PRON → VERB: Predicate (subject - verb)
- ADP → VERB: constraint
- ADP → NOUN: Predicate (preposition - object)
- DET → NOUN: constraint
- NOUN → VERB: constraint
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb - object)
- ADV → VERB: constraint
- DET → NOUN: Constraint (determiner - noun)
- SCONJ → VERB: Predicate (verb - object)
- SCONJ → VERB: Constraint

---

### Sentence 21 (basic_sentences_input.txt)
**Input:** It was one of the happiest moments of her life.

**POS-UD Relations:**
- NUM → PRON: nsubj
- NUM → AUX: cop
- NOUN → ADP: case
- NOUN → DET: det
- NOUN → ADJ: amod
- NUM → NOUN: nmod
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- NOUN → NOUN: nmod
- NUM → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb - object)
- ADP → NUM: Constraint
- ADP → NOUN: Predicate (preposition - object)
- DET → NOUN: Constraint
- ADJ → NOUN: Constraint
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (preposition - object)
- PRON → NOUN: Constraint

### Sentence 22 (basic_sentences_input.txt)
**Input:** That memory, like many others, stayed with her even today.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj
- NOUN → PUNCT: punct
- NOUN → ADP: case
- NOUN → ADJ: amod
- NOUN → NOUN: nmod
- NOUN → PUNCT: punct
- PRON → ADP: case
- VERB → PRON: obl
- NOUN → ADV: advmod
- VERB → NOUN: obl:unmarked
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- ADP → VERB: constraint
- ADP → PRON: Predicate (verb/proposition - object)
- ADV → NOUN: Constraint
- ADP → NOUN: constraint
- ADP → NOUN: Predicate (verb/proposition - object)
- ADJ → NOUN: constraint

### Sentence 23 (basic_sentences_input.txt)
**Input:** She was very sad yesterday.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- ADJ → ADV: advmod
- ADJ → NOUN: obl:unmarked
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb - object)
- ADV → ADJ: Constraint
- NOUN → AUX: Constraint

### Sentence 24 (basic_sentences_input.txt)
**Input:** It is a lie that you love her.

**POS-UD Relations:**
- NOUN → PRON: nsubj
- NOUN → AUX: cop
- NOUN → DET: det
- VERB → PRON: obj
- VERB → PRON: nsubj
- NOUN → VERB: acl:relcl
- VERB → PRON: obj
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- PRON → NOUN: connection
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)

### Sentence 25 (basic_sentences_input.txt)
**Input:** That truth broke her heart again.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj
- NOUN → PRON: nmod:poss
- VERB → NOUN: obj
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- PRON → NOUN: Constraint
- ADV → VERB: Constraint

### Sentence 26 (basic_sentences_input.txt)
**Input:** Nobody told her the full story.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → PRON: iobj
- NOUN → DET: det
- NOUN → ADJ: amod
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb - object)
- VERB → NOUN: Predicate (verb - object)
- NOUN → PRON: constraint
- DET → NOUN: Constraint
- ADJ → NOUN: Constraint

### Sentence 27 (basic_sentences_input.txt)
**Input:** She waited by the window, hoping you would return.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → ADP: case
- NOUN → DET: det
- VERB → NOUN: obl
- VERB → PUNCT: punct
- VERB → VERB: advcl
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: ccomp
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- ADP → VERB: constraint
- ADP → NOUN: Predicate (preposition - object)
- DET → NOUN: constraint
- PRON → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb - object)
- VERB → VERB: constraint
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint (auxiliary - main verb)

### Sentence 28 (basic_sentences_input.txt)
**Input:** But it never happened.

**POS-UD Relations:**
- VERB → CCONJ: cc
- VERB → PRON: nsubj
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- CCONJ → VERB: Constraint
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: constraint

### Sentence 29 (basic_sentences_input.txt)
**Input:** The pain, like before, settled deep within her.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj
- NOUN → PUNCT: punct
- ADV → INTJ: discourse
- VERB → ADV: advmod
- ADV → PUNCT: punct
- VERB → ADV: advmod
- PRON → ADP: case
- VERB → PRON: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: constraint
- NOUN → VERB: Predicate (subject - verb)
- INTJ → NOUN: constraint
- INTJ → ADV: Predicate (prep - object)
- ADV → VERB: Constraint
- ADP → VERB: constraint
- ADP → PRON: Predicate (prep - object)

### Sentence 30 (basic_sentences_input.txt)
**Input:** Design a vacation house that can fly easily from one location to another.

**POS-UD Relations:**
- NOUN → DET: det
- NOUN → NOUN: compound
- VERB → NOUN: obj
- VERB → PRON: nsubj
- VERB → AUX: aux
- NOUN → VERB: acl:relcl
- VERB → ADV: advmod
- NOUN → ADP: case
- NOUN → NUM: nummod
- VERB → NOUN: obl
- DET → ADP: case
- VERB → DET: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- NOUN → NOUN: Constraint
- NOUN → PRON: Connection
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (verb/preposition - object)
- NUM → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- ADP → ADP: Connection

---

### Sentence 31 (basic_sentences_input.txt)
**Input:** Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2.

**POS-UD Relations:**
- NOUN → ADJ: amod
- NOUN → NUM: nummod
- NOUN → NOUN: compound
- NOUN → NOUN: compound
- NOUN → ADP: case
- NOUN → NUM: nummod
- NOUN → NOUN: compound
- NOUN → NOUN: compound
- NOUN → NOUN: nmod
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- NOUN → NOUN: Constraint
- NOUN → NOUN: Constraint
- ADP → ADJ: Constraint
- ADP → NOUN: Predicate (verb/preposition - object)

### Sentence 32 (basic_sentences_input.txt)
**Input:** Design a web system to manage the editorial workflow of the JIDPS journal.

**POS-UD Relations:**
- NOUN → DET: det
- NOUN → NOUN: compound
- VERB → NOUN: obj
- VERB → PART: mark
- VERB → VERB: advcl
- NOUN → DET: det
- NOUN → ADJ: amod
- VERB → NOUN: obj
- NOUN → ADP: case
- NOUN → DET: det
- NOUN → PROPN: compound
- NOUN → NOUN: nmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- NOUN → NOUN: Constraint
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/proposition - object)
- VERB → NOUN: Predicate (verb/proposition - object)
- ADJ → NOUN: Constraint
- DET → NOUN: Constraint
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (verb/proposition - object)
- PROPN → NOUN: Constraint
- DET → NOUN: Constraint

### Sentence 33 (basic_sentences_input.txt)
**Input:** Driver needs to stop and slow down a vehicle effectively and efficiently.

**POS-UD Relations:**
- VERB → NOUN: nsubj
- VERB → PART: mark
- VERB → VERB: xcomp
- VERB → CCONJ: cc
- VERB → VERB: conj
- VERB → ADP: compound:prt
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → ADV: advmod
- ADV → CCONJ: cc
- ADV → ADV: conj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- NOUN → VERB: Predicate (subject - verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- ADV → VERB: Constraint
- CCONJ → VERB: connect
- CCONJ → VERB: connect
- PART → VERB: Predicate (verb/proposition - object)
- ADP → VERB: Constraint
- ADV → VERB: Constraint
- ADV → VERB: Constraint
- VERB → NOUN: Predicate (verb/proposition - object)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 34 (compound_sentences_input.txt)
**Input:** She wanted to go for a walk, but it started raining.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → PART: mark
- VERB → VERB: xcomp
- NOUN → ADP: case
- NOUN → DET: det
- VERB → NOUN: obl
- VERB → PUNCT: punct
- VERB → CCONJ: cc
- VERB → PRON: nsubj
- VERB → VERB: conj
- VERB → VERB: xcomp
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/preposition - object)
- PART → VERB: Constraint
- VERB → NOUN: Predicate (verb/preposition - object)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (preposition - object)
- DET → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/preposition - object)
- CCONJ → VERB: Constraint
- CCONJ → VERB: Predicate (verb/preposition - object)

### Sentence 35 (compound_sentences_input.txt)
**Input:** The sky was clear; we decided to go stargazing.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- ADJ → AUX: cop
- VERB → PUNCT: punct
- VERB → PRON: nsubj
- ADJ → VERB: parataxis
- VERB → PART: mark
- VERB → VERB: xcomp
- VERB → VERB: xcomp
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- NOUN → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- PRON → VERB: Predicate (subject - verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/preposition - object)
- VERB → VERB: Predicate (verb/preposition - object)

### Sentence 36 (compound_sentences_input.txt)
**Input:** I was tired; however, I kept working.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- VERB → PUNCT: punct
- VERB → ADV: advmod
- ADV → PUNCT: punct
- VERB → PRON: nsubj
- ADJ → VERB: parataxis
- VERB → VERB: xcomp
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/preposition - object)
- ADV → AUX: Constraint
- ADV → VERB: Predicate (verb/preposition - object)

### Sentence 37 (compound_sentences_input.txt)
**Input:** She is both smart and creative.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- ADJ → ADV: advmod
- ADJ → CCONJ: cc
- ADJ → ADJ: conj
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/preposition - object)
- AUX → ADJ: Predicate (verb/preposition - object)
- ADV → ADJ: Predicate (verb/preposition - object)
- CCONJ → ADJ: Predicate (verb/preposition - object)
- ADV → AUX: Constraint
- CCONJ → AUX: Constraint

### Sentence 38 (compound_sentences_input.txt)
**Input:** Both my brother and sister are engineers.

**POS-UD Relations:**
- NOUN → CCONJ: cc:preconj
- NOUN → PRON: nmod:poss
- NOUN → NOUN: nsubj
- NOUN → CCONJ: cc
- NOUN → NOUN: conj
- NOUN → AUX: cop
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- PRON → NOUN: Constraint
- CCONJ → NOUN: Predicate (verb/preposition - object)
- CCONJ → NOUN: Predicate (verb/preposition - object)
- NOUN → AUX: Predicate (subject - verb)
- NOUN → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/preposition - object)
- CCONJ → CCONJ: connection
- CCONJ → AUX: Constraint
- CCONJ → AUX: Constraint

### Sentence 39 (compound_sentences_input.txt)
**Input:** Not only did he win, but he also broke the record.

**POS-UD Relations:**
- VERB → PART: advmod
- VERB → ADV: advmod
- VERB → AUX: aux
- VERB → PRON: nsubj
- VERB → PUNCT: punct
- VERB → CCONJ: cc
- VERB → PRON: nsubj
- VERB → ADV: advmod
- VERB → VERB: conj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint

### Sentence 40 (compound_sentences_input.txt)
**Input:** The movie was not only long but also boring.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- ADJ → AUX: cop
- ADJ → PART: advmod
- ADJ → ADV: advmod
- ADJ → CCONJ: cc
- ADJ → ADV: advmod
- ADJ → ADJ: conj
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- NOUN → AUX: Predicate (subject - verb)
- DET → NOUN: Constraint
- AUX → ADJ: Predicate (verb/preposition - object)
- AUX → ADJ: Predicate (verb/preposition - object)

---

### Sentence 41 (compound_sentences_input.txt)
**Input:** You can either stay home or come with us.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → CCONJ: cc:preconj
- VERB → ADV: advmod
- VERB → CCONJ: cc
- VERB → VERB: conj
- PRON → ADP: case
- VERB → PRON: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- AUX → VERB: Constraint
- VERB → ADV: Constraint
- VERB → ADP: Constraint
- ADP → PRON: Predicate (verb/preposition - object)
- CCONJ → VERB: Predicate (verb/preposition - object)
- CCONJ → VERB: Predicate (verb/preposition - object)
- CCONJ → CCONJ: connection

### Sentence 42 (compound_sentences_input.txt)
**Input:** Neither did he apologize, nor did he show any regret.

**POS-UD Relations:**
- VERB → CCONJ: cc:preconj
- VERB → AUX: aux
- VERB → PRON: nsubj
- VERB → PUNCT: punct
- VERB → CCONJ: cc
- VERB → AUX: aux
- VERB → PRON: nsubj
- VERB → VERB: conj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- CCONJ → VERB: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- CCONJ → VERB: Predicate (verb/preposition - object)
- CCONJ → CCONJ: Connection

### Sentence 43 (compound_sentences_input.txt)
**Input:** I don't know whether he’ll call or text.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → PART: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: ccomp
- NOUN → CCONJ: cc
- VERB → NOUN: conj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- SCONJ → VERB: Predicate (verb/preposition - object)
- CCONJ → NOUN: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)
- PRON → NOUN: Predicate (subject - verb)
- SCONJ → CCONJ: Connection
- SCONJ → VERB: Constraint
- CCONJ → VERB: Constraint

### Sentence 44 (compound_sentences_input.txt)
**Input:** She’s unsure whether to accept the job or continue studying.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- VERB → SCONJ: mark
- VERB → PART: mark
- ADJ → VERB: xcomp
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → CCONJ: cc
- VERB → VERB: conj
- VERB → VERB: xcomp
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- SCONJ → VERB: Predicate (verb/preposition - object)
- CCONJ → VERB: Predicate (verb/preposition - object)
- PART → VERB: Predicate (verb/preposition - object)
- PART → VERB: Predicate (verb/preposition - object)
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- VERB → VERB: Predicate (verb/preposition - object)
- SCONJ → CCONJ: Connection

### Sentence 45 (compound_sentences_input.txt)
**Input:** She’s as tall as her brother.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- ADJ → ADV: advmod
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- ADJ → NOUN: obl
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- ADP → ADJ: Predicate (verb/preposition - object)
- PRON → NOUN: Constraint

### Sentence 46 (compound_sentences_input.txt)
**Input:** He ran as quickly as a professional athlete.

**POS-UD Relations:**
- VERB → PRON: nsubj
- ADV → ADV: advmod
- VERB → ADV: advmod
- NOUN → ADP: case
- NOUN → DET: det
- NOUN → ADJ: amod
- VERB → NOUN: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: Constraint
- ADP → VERB: Constraint
- ADP → ADV: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- ADJ → NOUN: Constraint

### Sentence 47 (compound_sentences_input.txt)
**Input:** This task is not as easy as it looks.

**POS-UD Relations:**
- NOUN → DET: det
- ADJ → NOUN: nsubj
- ADJ → AUX: cop
- ADJ → PART: advmod
- ADJ → ADV: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- ADJ → VERB: advcl
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- NOUN → AUX: Predicate (subject - verb)
- DET → NOUN: Constraint
- AUX → ADJ: Predicate (verb/preposition - object)
- PART → ADJ: Constraint
- SCONJ → AUX: Constraint
- SCONJ → ADJ: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)

### Sentence 48 (compound_sentences_input.txt)
**Input:** He doesn’t eat as much chocolate as his brother.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → PART: advmod
- ADJ → ADV: advmod
- NOUN → ADJ: amod
- VERB → NOUN: obj
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- VERB → NOUN: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- ADJ → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → ADJ: Predicate (verb/preposition - object)
- PRON → NOUN: Constraint

### Sentence 49 (compound_sentences_input.txt)
**Input:** She enjoys painting as much as she enjoys dancing.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → NOUN: obj
- ADJ → ADV: advmod
- VERB → ADJ: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- ADJ → VERB: advcl
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb) (second clause)
- VERB → NOUN: Predicate (verb/preposition - object) (second clause)
- ADJ → NOUN: Constraint
- SCONJ → VERB: Constraint
- SCONJ → ADJ: Predicate (verb/preposition - object)

### Sentence 50 (compound_sentences_input.txt)
**Input:** Just as the moon affects the tides, so does the sun influence them.

**POS-UD Relations:**
- VERB → ADV: advmod
- VERB → SCONJ: mark
- NOUN → DET: det
- VERB → NOUN: nsubj
- VERB → VERB: advcl
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct
- VERB → ADV: advmod
- VERB → AUX: aux
- NOUN → DET: det
- VERB → NOUN: nsubj
- VERB → PRON: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- DET → NOUN: Constraint
- ADV → SCONJ: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- ADV → VERB: Predicate (verb/preposition - object)
- AUX → VERB: Constraint
- SCONJ → ADV: Connection

---

### Sentence 51 (compound_sentences_input.txt)
**Input:** Just as honesty builds trust, so does kindness.

**POS-UD Relations:**
- VERB → ADV: advmod
- VERB → SCONJ: mark
- VERB → NOUN: nsubj
- VERB → VERB: advcl
- VERB → NOUN: obj
- VERB → PUNCT: punct
- VERB → ADV: advmod
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- ADV → ADV: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object) (implied)
- ADV → VERB: Predicate (verb/preposition - object)
- VERB → VERB: Constraint
- SCONJ → ADV: Connection

### Sentence 52 (compound_sentences_input.txt)
**Input:** Just as we need water to survive, so do plants need sunlight.

**POS-UD Relations:**
- VERB → ADV: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → VERB: advcl
- VERB → NOUN: obj
- VERB → PART: mark
- VERB → VERB: xcomp
- VERB → PUNCT: punct
- VERB → ADV: advmod
- VERB → AUX: aux
- VERB → NOUN: nsubj
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- NOUN → VERB: Constraint
- PART → VERB: Constraint
- ADV → ADV: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- ADV → VERB: Predicate (verb/preposition - object)
- AUX → VERB: Constraint
- SCONJ → ADV: Connection

### Sentence 53 (compound_sentences_input.txt)
**Input:** No sooner had she sat down than the phone rang.

**POS-UD Relations:**
- ADV → ADV: advmod
- VERB → ADV: advmod
- VERB → AUX: aux
- VERB → PRON: nsubj
- VERB → ADP: compound:prt
- VERB → SCONJ: mark
- NOUN → DET: det
- VERB → NOUN: nsubj
- VERB → VERB: advcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- No ROM relations found

### Sentence 54 (compound_sentences_input.txt)
**Input:** I’d rather read a book than watch TV.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → ADV: advmod
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → ADP: mark
- VERB → VERB: advcl
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: Constraint
- VERB → NOUN: Predicate (verb/preposition - object)
- DET → NOUN: Constraint
- ADP → VERB: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- ADV → ADP: Connection

### Sentence 55 (compound_sentences_input.txt)
**Input:** He chose to walk rather than drive.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → PART: mark
- VERB → VERB: xcomp
- VERB → ADV: cc
- ADV → ADP: fixed
- VERB → VERB: conj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/preposition - object)
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/preposition - object)
- PART → VERB: Predicate (verb/preposition - object)
- ADV → VERB: Constraint
- ADP → VERB: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)
- ADV → ADP: Connection

### Sentence 56 (compound_sentences_input.txt)
**Input:** Rather than complain, she took action.

**POS-UD Relations:**
- VERB → ADV: mark
- ADV → ADP: fixed
- VERB → VERB: advcl
- VERB → PUNCT: punct
- VERB → PRON: nsubj
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/preposition - object)
- ADV → VERB: Constraint
- ADP → VERB: Predicate (verb/preposition - object)
- PRON → VERB: Predicate (subject - verb)

### Sentence 57 (noun_clauses_sentences_input.txt)
**Input:** What she said surprised everyone.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → PRON: nsubj
- PRON → VERB: acl:relcl
- VERB → PRON: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)

### Sentence 58 (noun_clauses_sentences_input.txt)
**Input:** That he lied was obvious.

**POS-UD Relations:**
- ADJ → SCONJ: mark
- VERB → PRON: nsubj
- ADJ → VERB: csubj
- ADJ → AUX: cop
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- SCONJ → VERB: connection
- SCONJ → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)
- VERB → AUX: Predicate (subject - verb)

### Sentence 59 (noun_clauses_sentences_input.txt)
**Input:** Whether we will win depends on our effort.

**POS-UD Relations:**
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: advcl
- NOUN → ADP: case
- NOUN → PRON: nmod:poss
- VERB → NOUN: obl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- SCONJ → VERB: Predicate (verb/proposition - object)
- SCONJ → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (subject - verb)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (verb/proposition - object)
- PRON → NOUN: Constraint

### Sentence 60 (noun_clauses_sentences_input.txt)
**Input:** How she managed to escape is still a mystery.

**POS-UD Relations:**
- NOUN → ADV: advmod
- VERB → PRON: nsubj
- NOUN → VERB: csubj
- VERB → PART: mark
- VERB → VERB: xcomp
- NOUN → AUX: cop
- NOUN → ADV: advmod
- NOUN → DET: det
- NOUN → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- ADV → AUX: Predicate (subject - verb)
- AUX → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- ADV → AUX: Constraint

---

### Sentence 61 (noun_clauses_sentences_input.txt)
**Input:** When the meeting starts is still unknown.

**POS-UD Relations:**
- VERB → ADV: advmod
- NOUN → DET: det
- VERB → NOUN: nsubj
- ADJ → VERB: advcl
- ADJ → AUX: cop
- ADJ → ADV: advmod
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- ADV → VERB: constraint
- ADV → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)
- ADV → AUX: Constraint

### Sentence 62 (noun_clauses_sentences_input.txt)
**Input:** I know that she is right.

**POS-UD Relations:**
- VERB → PRON: nsubj
- ADJ → SCONJ: mark
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- VERB → ADJ: ccomp
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → AUX: Predicate (verb/proposition - object)
- PRON → AUX: Predicate (subject - verb)
- AUX → ADJ: Predicate (verb/proposition - object)
- SCONJ → AUX: Connection

### Sentence 63 (noun_clauses_sentences_input.txt)
**Input:** She didn’t tell me what had happened.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → PART: advmod
- VERB → PRON: iobj
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: ccomp
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → PRON: Predicate (verb/proposition - object)
- VERB → PRON: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- PRON → PRON: Constraint

### Sentence 64 (noun_clauses_sentences_input.txt)
**Input:** We’re thinking about how we can solve the problem.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → SCONJ: mark
- VERB → ADV: advmod
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → VERB: advcl
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- SCONJ → VERB: Constraint
- SCONJ → ADV: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 65 (noun_clauses_sentences_input.txt)
**Input:** He’s not sure if he locked the door.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- ADJ → PART: advmod
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- ADJ → VERB: ccomp
- NOUN → DET: det
- VERB → NOUN: obj
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PART → ADJ: Constraint
- SCONJ → VERB: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 66 (noun_clauses_sentences_input.txt)
**Input:** I don’t know when the package will arrive.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → PART: advmod
- VERB → ADV: advmod
- NOUN → DET: det
- VERB → NOUN: nsubj
- VERB → AUX: aux
- VERB → VERB: advcl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → VERB: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- ADV → VERB: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint

### Sentence 67 (noun_clauses_sentences_input.txt)
**Input:** The truth is that she never left.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj:outer
- VERB → AUX: cop
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → VERB: Predicate (verb/proposition - object)
- AUX → SCONJ: Predicate (verb/proposition - object)
- SCONJ → VERB: Connection
- PRON → VERB: Predicate (subject - verb)
- ADV → VERB: Constraint

### Sentence 68 (noun_clauses_sentences_input.txt)
**Input:** My suggestion is that we take a break.

**POS-UD Relations:**
- NOUN → PRON: nmod:poss
- VERB → NOUN: nsubj:outer
- VERB → AUX: cop
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → VERB: Predicate (verb/proposition - object)
- AUX → SCONJ: Predicate (verb/proposition - object)
- SCONJ → VERB: Connection
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 69 (noun_clauses_sentences_input.txt)
**Input:** The problem is how we can get there.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj:outer
- VERB → AUX: cop
- VERB → ADV: advmod
- VERB → PRON: nsubj
- VERB → AUX: aux
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → ADV: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- ADV → AUX: Connection
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- VERB → ADV: Predicate (verb/proposition - object)

### Sentence 70 (noun_clauses_sentences_input.txt)
**Input:** The question is whether he will accept the offer.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj:outer
- VERB → AUX: cop
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- VERB → AUX: aux
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → SCONJ: Predicate (verb/proposition - object)
- SCONJ → VERB: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

---

### Sentence 71 (noun_clauses_sentences_input.txt)
**Input:** I heard the news that she got married.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → SCONJ: mark
- VERB → PRON: nsubj:pass
- VERB → AUX: aux:pass
- NOUN → VERB: acl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → AUX: Predicate (verb/proposition - object)
- PRON → AUX: Predicate (subject - verb)
- AUX → VERB: Predicate (verb/proposition - object)

### Sentence 72 (noun_clauses_sentences_input.txt)
**Input:** The idea that hard work brings success is widely accepted.

**POS-UD Relations:**
- NOUN → DET: det
- VERB → NOUN: nsubj:pass
- VERB → SCONJ: mark
- NOUN → ADJ: amod
- VERB → NOUN: nsubj
- NOUN → VERB: acl
- VERB → NOUN: obj
- VERB → AUX: aux:pass
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (subject - verb)
- AUX → VERB: Predicate (verb/proposition - object)
- ADV → VERB: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → VERB: Predicate (verb/proposition - object)
- ADJ → NOUN: Constraint
- NOUN → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)

### Sentence 73 (noun_clauses_sentences_input.txt)
**Input:** She rejected the suggestion that we cancel the meeting.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → SCONJ: mark
- VERB → PRON: nsubj
- NOUN → VERB: acl
- NOUN → DET: det
- VERB → NOUN: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → VERB: Predicate (verb/proposition - object)
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint

### Sentence 74 (noun_clauses_sentences_input.txt)
**Input:** We faced the fact that we were out of time.

**POS-UD Relations:**
- VERB → PRON: nsubj
- NOUN → DET: det
- VERB → NOUN: obj
- NOUN → SCONJ: mark
- NOUN → PRON: nsubj
- NOUN → AUX: cop
- NOUN → ADP: case
- NOUN → ADP: case
- NOUN → NOUN: acl
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (subject - verb)
- VERB → NOUN: Predicate (verb/proposition - object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → AUX: Predicate (verb/proposition - object)
- PRON → AUX: Predicate (subject - verb)
- AUX → ADP: Predicate (verb/proposition - object)
- ADP → ADP: Constraint
- ADP → NOUN: Predicate (verb/proposition - object)

</details>
