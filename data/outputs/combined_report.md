# Combined POS-based UD vs ROM Relations Analysis Report

**Date:** 2025-05-23 12:05:11
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

### Global Overlap Rates (Mathematical Formula)
| Pattern | Overlap Rate | Description |
|---------|--------------|-------------|
| Forward Matching (Pattern 1) | 0.581 | ROM pairs match UD pairs in same direction |
| Reverse Matching (Pattern 2) | 0.500 | ROM pairs match UD pairs in reverse direction |
| **Maximum Overall Overlap** | **0.581** | **Best matching pattern globally** |

## 🔍 Detailed POS Pair Analysis (Combined) - Bidirectional

This section shows bidirectional POS pair analysis with overlap rates calculated using mathematical formula:
**overlap_rate_k = (∑_{i ∈ M_k} 1(R_i = U_{j(i)})) / |M_k|**
- Pattern 1 (Forward): M₁ = {i : ∃j, (A_i, B_i) = (A_j', B_j')}
- Pattern 2 (Reverse): M₂ = {i : ∃j, (A_i, B_i) = (B_j', A_j')}
- **Max Overlap Rate = max{overlap_rate_1, overlap_rate_2}**
Blocks are sorted by maximum overlap rate (highest first).

### DET ↔ NOUN (Max Overlap Rate: 1.000)

#### DET → NOUN
**ROM Relations:**
- Constraint (64 occurrences)
- Constraint (Determiner - Noun) (1 occurrences)

#### NOUN → DET
**UD Relations:**
- det (65 occurrences)

**Examples:**
*DET→NOUN ROM Examples:*
  - **Constraint**: The → boy, The → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint (Determiner - Noun)**: a → treehouse in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)

*NOUN→DET UD Examples:*
  - **det**: boy → The in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- DET→NOUN: 0 UD, 65 ROM
- NOUN→DET: 65 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- DET→NOUN Pattern 1 (Forward): 0.000
- DET→NOUN Pattern 2 (Reverse): 0.000
- DET→NOUN Max Overlap: 0.000
- NOUN→DET Pattern 1 (Forward): 0.000
- NOUN→DET Pattern 2 (Reverse): 1.000
- NOUN→DET Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (DET→NOUN UD)/(NOUN→DET ROM): 0.00
- Reverse cross ratio (NOUN→DET UD)/(DET→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### NOUN ↔ NOUN (Max Overlap Rate: 1.000)

#### NOUN → NOUN
**UD Relations:**
- nmod (7 occurrences)
- compound (7 occurrences)
- conj (5 occurrences)
- nsubj (4 occurrences)
- acl:relcl (1 occurrences)
- acl (1 occurrences)

**ROM Relations:**
- Constraint (6 occurrences)

#### NOUN → NOUN
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
*NOUN→NOUN UD Examples:*
  - **nsubj**: friend → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **acl:relcl**: boy → doctor in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)
  - **conj**: stories → emotions in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

*NOUN→NOUN ROM Examples:*
  - **Constraint**: sincerity → details in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

*NOUN→NOUN UD Examples:*
  - **nsubj**: friend → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **acl:relcl**: boy → doctor in "The boy whose father is a doctor is my classmate." (adjective_clauses_sentences_input.txt)
  - **conj**: stories → emotions in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

*NOUN→NOUN ROM Examples:*
  - **Constraint**: sincerity → details in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→NOUN: 25 UD, 6 ROM
- NOUN→NOUN: 25 UD, 6 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→NOUN Pattern 1 (Forward): 0.240
- NOUN→NOUN Pattern 2 (Reverse): 1.000
- NOUN→NOUN Max Overlap: 1.000
- NOUN→NOUN Pattern 1 (Forward): 0.240
- NOUN→NOUN Pattern 2 (Reverse): 1.000
- NOUN→NOUN Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.24
- Reverse ROM/UD ratio: 0.24
- Cross ratio (NOUN→NOUN UD)/(NOUN→NOUN ROM): 4.17
- Reverse cross ratio (NOUN→NOUN UD)/(NOUN→NOUN ROM): 4.17
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### PRON ↔ VERB (Max Overlap Rate: 1.000)

#### PRON → VERB
**UD Relations:**
- acl:relcl (1 occurrences)

**ROM Relations:**
- Predicate (Subject - Verb) (68 occurrences)
- Constraint (1 occurrences)
- Predicate (Subject - Verb) (Second Clause) (1 occurrences)

#### VERB → PRON
**UD Relations:**
- nsubj (67 occurrences)
- obj (9 occurrences)
- obl (3 occurrences)
- iobj (2 occurrences)
- nsubj:pass (1 occurrences)

**ROM Relations:**
- Predicate (Verb/Proposition - Object) (8 occurrences)
- Predicate (Verb/Preposition - Object) (2 occurrences)
- Predicate (Verb - Object) (2 occurrences)

**Examples:**
*PRON→VERB UD Examples:*
  - **acl:relcl**: What → said in "What she said surprised everyone." (noun_clauses_sentences_input.txt)

*PRON→VERB ROM Examples:*
  - **Predicate (Subject - Verb)**: Who → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: her → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (Subject - Verb) (Second Clause)**: She → enjoys in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)

*VERB→PRON UD Examples:*
  - **nsubj**: sings → who in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **obj**: painted → this in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **obl**: stayed → her in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)

*VERB→PRON ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Painted → this in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: surprised → her in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (Verb - Object)**: found → themselves in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PRON→VERB: 1 UD, 70 ROM
- VERB→PRON: 82 UD, 12 ROM

**Overlap Rates (Mathematical Formula):**
- PRON→VERB Pattern 1 (Forward): 1.000
- PRON→VERB Pattern 2 (Reverse): 0.083
- PRON→VERB Max Overlap: 1.000
- VERB→PRON Pattern 1 (Forward): 0.146
- VERB→PRON Pattern 2 (Reverse): 1.000
- VERB→PRON Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 70.00
- Reverse ROM/UD ratio: 0.15
- Cross ratio (PRON→VERB UD)/(VERB→PRON ROM): 0.08
- Reverse cross ratio (VERB→PRON UD)/(PRON→VERB ROM): 1.17
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### NOUN ↔ VERB (Max Overlap Rate: 1.000)

#### NOUN → VERB
**UD Relations:**
- acl:relcl (14 occurrences)
- acl (3 occurrences)
- advcl (1 occurrences)
- amod (1 occurrences)
- csubj (1 occurrences)

**ROM Relations:**
- Predicate (Subject - Verb) (25 occurrences)
- Constraint (3 occurrences)

#### VERB → NOUN
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
- Predicate (Verb/Preposition - Object) (19 occurrences)
- Predicate (Verb/Proposition - Object) (18 occurrences)
- Predicate (Verb - Object) (6 occurrences)
- Constraint (4 occurrences)
- Predicate (Preposition - Object) (1 occurrences)
- Predicate (Verb/Preposition - Object) (Second Clause) (1 occurrences)
- Predicate (Verb/Preposition - Object) (Implied) (1 occurrences)

**Examples:**
*NOUN→VERB UD Examples:*
  - **acl:relcl**: boy → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **advcl**: year → moved in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **amod**: memories → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

*NOUN→VERB ROM Examples:*
  - **Predicate (Subject - Verb)**: boy → sings in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: week → received in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)

*VERB→NOUN UD Examples:*
  - **nsubj**: broke → car in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **obj**: remember → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **obl:agent**: Inspired → memories in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

*VERB→NOUN ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Remember → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **Constraint**: met → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **Predicate (Verb - Object)**: cherished → memories in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→VERB: 20 UD, 28 ROM
- VERB→NOUN: 76 UD, 50 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→VERB Pattern 1 (Forward): 1.000
- NOUN→VERB Pattern 2 (Reverse): 0.400
- NOUN→VERB Max Overlap: 1.000
- VERB→NOUN Pattern 1 (Forward): 0.658
- VERB→NOUN Pattern 2 (Reverse): 1.000
- VERB→NOUN Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 1.40
- Reverse ROM/UD ratio: 0.66
- Cross ratio (NOUN→VERB UD)/(VERB→NOUN ROM): 0.40
- Reverse cross ratio (VERB→NOUN UD)/(NOUN→VERB ROM): 2.71
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### AUX ↔ NOUN (Max Overlap Rate: 1.000)

#### AUX → NOUN
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (7 occurrences)
- Predicate (Verb - Object) (1 occurrences)
- Predicate (Verb/Preposition - Object) (1 occurrences)

#### NOUN → AUX
**UD Relations:**
- cop (9 occurrences)

**ROM Relations:**
- Predicate (Subject - Verb) (16 occurrences)
- Constraint (1 occurrences)

**Examples:**
*AUX→NOUN ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Is → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (Verb - Object)**: was → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: Are → engineers in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*NOUN→AUX UD Examples:*
  - **cop**: friend → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)

*NOUN→AUX ROM Examples:*
  - **Predicate (Subject - Verb)**: Boy → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: yesterday → was in "She was very sad yesterday." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→NOUN: 0 UD, 9 ROM
- NOUN→AUX: 9 UD, 17 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→NOUN Pattern 1 (Forward): 0.000
- AUX→NOUN Pattern 2 (Reverse): 0.000
- AUX→NOUN Max Overlap: 0.000
- NOUN→AUX Pattern 1 (Forward): 1.000
- NOUN→AUX Pattern 2 (Reverse): 1.000
- NOUN→AUX Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.89
- Cross ratio (AUX→NOUN UD)/(NOUN→AUX ROM): 0.00
- Reverse cross ratio (NOUN→AUX UD)/(AUX→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ NOUN (Max Overlap Rate: 1.000)

#### ADJ → NOUN
**UD Relations:**
- nsubj (6 occurrences)
- obl:unmarked (1 occurrences)
- obl (1 occurrences)

**ROM Relations:**
- Constraint (11 occurrences)

#### NOUN → ADJ
**UD Relations:**
- amod (12 occurrences)

**Examples:**
*ADJ→NOUN UD Examples:*
  - **nsubj**: famous → artist in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **obl:unmarked**: sad → yesterday in "She was very sad yesterday." (basic_sentences_input.txt)
  - **obl**: tall → brother in "She’s as tall as her brother." (compound_sentences_input.txt)

*ADJ→NOUN ROM Examples:*
  - **Constraint**: heartfelt → tone in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

*NOUN→ADJ UD Examples:*
  - **amod**: tone → heartfelt in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→NOUN: 8 UD, 11 ROM
- NOUN→ADJ: 12 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→NOUN Pattern 1 (Forward): 1.000
- ADJ→NOUN Pattern 2 (Reverse): 0.000
- ADJ→NOUN Max Overlap: 1.000
- NOUN→ADJ Pattern 1 (Forward): 0.000
- NOUN→ADJ Pattern 2 (Reverse): 1.000
- NOUN→ADJ Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 1.38
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→NOUN UD)/(NOUN→ADJ ROM): 0.00
- Reverse cross ratio (NOUN→ADJ UD)/(ADJ→NOUN ROM): 1.09
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ AUX (Max Overlap Rate: 1.000)

#### ADJ → AUX
**UD Relations:**
- cop (16 occurrences)

#### AUX → ADJ
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (7 occurrences)
- Predicate (Verb/Preposition - Object) (7 occurrences)
- Predicate (Verb - Object) (1 occurrences)

**Examples:**
*ADJ→AUX UD Examples:*
  - **cop**: famous → is in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)

*AUX→ADJ ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Is → famous in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
  - **Predicate (Verb - Object)**: was → sad in "She was very sad yesterday." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: Was → clear in "The sky was clear; we decided to go stargazing." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→AUX: 16 UD, 0 ROM
- AUX→ADJ: 0 UD, 15 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→AUX Pattern 1 (Forward): 0.000
- ADJ→AUX Pattern 2 (Reverse): 1.000
- ADJ→AUX Max Overlap: 1.000
- AUX→ADJ Pattern 1 (Forward): 0.000
- AUX→ADJ Pattern 2 (Reverse): 0.000
- AUX→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→AUX UD)/(AUX→ADJ ROM): 1.07
- Reverse cross ratio (AUX→ADJ UD)/(ADJ→AUX ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### NOUN ↔ NUM (Max Overlap Rate: 1.000)

#### NOUN → NUM
**UD Relations:**
- nummod (3 occurrences)
- nsubj (1 occurrences)

#### NUM → NOUN
**UD Relations:**
- nmod (1 occurrences)

**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*NOUN→NUM UD Examples:*
  - **nsubj**: year → 2018 in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **nummod**: location → one in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

*NUM→NOUN UD Examples:*
  - **nmod**: one → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

*NUM→NOUN ROM Examples:*
  - **Constraint**: One → location in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→NUM: 4 UD, 0 ROM
- NUM→NOUN: 1 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→NUM Pattern 1 (Forward): 0.000
- NOUN→NUM Pattern 2 (Reverse): 1.000
- NOUN→NUM Max Overlap: 1.000
- NUM→NOUN Pattern 1 (Forward): 1.000
- NUM→NOUN Pattern 2 (Reverse): 0.000
- NUM→NOUN Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (NOUN→NUM UD)/(NUM→NOUN ROM): 4.00
- Reverse cross ratio (NUM→NOUN UD)/(NOUN→NUM ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADV ↔ VERB (Max Overlap Rate: 1.000)

#### ADV → VERB
**ROM Relations:**
- Constraint (19 occurrences)
- Predicate (Verb/Proposition - Object) (5 occurrences)
- Predicate (Verb/Preposition - Object) (4 occurrences)

#### VERB → ADV
**UD Relations:**
- advmod (32 occurrences)
- cc (1 occurrences)
- mark (1 occurrences)

**ROM Relations:**
- Predicate (Verb/Proposition - Object) (2 occurrences)
- Constraint (1 occurrences)

**Examples:**
*ADV→VERB ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: When → moved in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **Constraint**: together → built in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: However → kept in "I was tired; however, I kept working." (compound_sentences_input.txt)

*VERB→ADV UD Examples:*
  - **advmod**: moved → when in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **cc**: drive → rather in "He chose to walk rather than drive." (compound_sentences_input.txt)
  - **mark**: complain → Rather in "Rather than complain, she took action." (compound_sentences_input.txt)

*VERB→ADV ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Stayed → home in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Constraint**: Stay → home in "You can either stay home or come with us." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→VERB: 0 UD, 28 ROM
- VERB→ADV: 34 UD, 3 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→VERB Pattern 1 (Forward): 0.000
- ADV→VERB Pattern 2 (Reverse): 0.000
- ADV→VERB Max Overlap: 0.000
- VERB→ADV Pattern 1 (Forward): 0.088
- VERB→ADV Pattern 2 (Reverse): 1.000
- VERB→ADV Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.09
- Cross ratio (ADV→VERB UD)/(VERB→ADV ROM): 0.00
- Reverse cross ratio (VERB→ADV UD)/(ADV→VERB ROM): 1.21
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADP ↔ PROPN (Max Overlap Rate: 1.000)

#### ADP → PROPN
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (1 occurrences)

#### PROPN → ADP
**UD Relations:**
- case (1 occurrences)

**Examples:**
*ADP→PROPN ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: To → Canada in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

*PROPN→ADP UD Examples:*
  - **case**: Canada → to in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→PROPN: 0 UD, 1 ROM
- PROPN→ADP: 1 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→PROPN Pattern 1 (Forward): 0.000
- ADP→PROPN Pattern 2 (Reverse): 0.000
- ADP→PROPN Max Overlap: 0.000
- PROPN→ADP Pattern 1 (Forward): 0.000
- PROPN→ADP Pattern 2 (Reverse): 1.000
- PROPN→ADP Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→PROPN UD)/(PROPN→ADP ROM): 0.00
- Reverse cross ratio (PROPN→ADP UD)/(ADP→PROPN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADV ↔ NOUN (Max Overlap Rate: 1.000)

#### ADV → NOUN
**ROM Relations:**
- Constraint (5 occurrences)

#### NOUN → ADV
**UD Relations:**
- advmod (5 occurrences)

**Examples:**
*ADV→NOUN ROM Examples:*
  - **Constraint**: When → year in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

*NOUN→ADV UD Examples:*
  - **advmod**: stories → only, emotions → also in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→NOUN: 0 UD, 5 ROM
- NOUN→ADV: 5 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→NOUN Pattern 1 (Forward): 0.000
- ADV→NOUN Pattern 2 (Reverse): 0.000
- ADV→NOUN Max Overlap: 0.000
- NOUN→ADV Pattern 1 (Forward): 0.000
- NOUN→ADV Pattern 2 (Reverse): 1.000
- NOUN→ADV Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→NOUN UD)/(NOUN→ADV ROM): 0.00
- Reverse cross ratio (NOUN→ADV UD)/(ADV→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### VERB ↔ VERB (Max Overlap Rate: 1.000)

#### VERB → VERB
**UD Relations:**
- advcl (17 occurrences)
- xcomp (14 occurrences)
- conj (7 occurrences)
- ccomp (3 occurrences)

**ROM Relations:**
- Predicate (Verb/Preposition - Object) (6 occurrences)
- Predicate (Verb/Proposition - Object) (2 occurrences)
- Constraint (2 occurrences)
- Predicate (Verb - Object) (1 occurrences)
- Predicate (Subject - Verb) (1 occurrences)

#### VERB → VERB
**UD Relations:**
- advcl (17 occurrences)
- xcomp (14 occurrences)
- conj (7 occurrences)
- ccomp (3 occurrences)

**ROM Relations:**
- Predicate (Verb/Preposition - Object) (6 occurrences)
- Predicate (Verb/Proposition - Object) (2 occurrences)
- Constraint (2 occurrences)
- Predicate (Verb - Object) (1 occurrences)
- Predicate (Subject - Verb) (1 occurrences)

**Examples:**
*VERB→VERB UD Examples:*
  - **advcl**: remember → met in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **xcomp**: decided → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **ccomp**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

*VERB→VERB ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: gave → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: consider → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Predicate (Verb - Object)**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

*VERB→VERB UD Examples:*
  - **advcl**: remember → met in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
  - **xcomp**: decided → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **ccomp**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

*VERB→VERB ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: gave → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: consider → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Predicate (Verb - Object)**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- VERB→VERB: 41 UD, 12 ROM
- VERB→VERB: 41 UD, 12 ROM

**Overlap Rates (Mathematical Formula):**
- VERB→VERB Pattern 1 (Forward): 0.293
- VERB→VERB Pattern 2 (Reverse): 1.000
- VERB→VERB Max Overlap: 1.000
- VERB→VERB Pattern 1 (Forward): 0.293
- VERB→VERB Pattern 2 (Reverse): 1.000
- VERB→VERB Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.29
- Reverse ROM/UD ratio: 0.29
- Cross ratio (VERB→VERB UD)/(VERB→VERB ROM): 3.42
- Reverse cross ratio (VERB→VERB UD)/(VERB→VERB ROM): 3.42
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### AUX ↔ VERB (Max Overlap Rate: 1.000)

#### AUX → VERB
**ROM Relations:**
- Constraint (13 occurrences)
- Predicate (Verb/Proposition - Object) (5 occurrences)
- Constraint (Auxiliary - Main Verb) (1 occurrences)

#### VERB → AUX
**UD Relations:**
- aux (24 occurrences)
- cop (4 occurrences)
- aux:pass (3 occurrences)

**ROM Relations:**
- Predicate (Subject - Verb) (1 occurrences)
- Predicate (Verb/Proposition - Object) (1 occurrences)

**Examples:**
*AUX→VERB ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Was → raining in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Constraint (Auxiliary - Main Verb)**: would → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)
  - **Constraint**: Can → fly in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

*VERB→AUX UD Examples:*
  - **aux**: know → do in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **aux:pass**: filled → was in "The letter was filled with stories about their childhood adventures." (basic_sentences_input.txt)
  - **cop**: left → is in "The truth is that she never left." (noun_clauses_sentences_input.txt)

*VERB→AUX ROM Examples:*
  - **Predicate (Subject - Verb)**: lied → was in "That he lied was obvious." (noun_clauses_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: Know → is in "I know that she is right." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→VERB: 0 UD, 19 ROM
- VERB→AUX: 31 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→VERB Pattern 1 (Forward): 0.000
- AUX→VERB Pattern 2 (Reverse): 0.000
- AUX→VERB Max Overlap: 0.000
- VERB→AUX Pattern 1 (Forward): 0.065
- VERB→AUX Pattern 2 (Reverse): 1.000
- VERB→AUX Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.06
- Cross ratio (AUX→VERB UD)/(VERB→AUX ROM): 0.00
- Reverse cross ratio (VERB→AUX UD)/(AUX→VERB ROM): 1.63
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ SCONJ (Max Overlap Rate: 1.000)

#### ADJ → SCONJ
**UD Relations:**
- mark (3 occurrences)

#### SCONJ → ADJ
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (2 occurrences)

**Examples:**
*ADJ→SCONJ UD Examples:*
  - **mark**: tired → Although in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)

*SCONJ→ADJ ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: As → easy in "This task is not as easy as it looks." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→SCONJ: 3 UD, 0 ROM
- SCONJ→ADJ: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→SCONJ Pattern 1 (Forward): 0.000
- ADJ→SCONJ Pattern 2 (Reverse): 1.000
- ADJ→SCONJ Max Overlap: 1.000
- SCONJ→ADJ Pattern 1 (Forward): 0.000
- SCONJ→ADJ Pattern 2 (Reverse): 0.000
- SCONJ→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→SCONJ UD)/(SCONJ→ADJ ROM): 1.50
- Reverse cross ratio (SCONJ→ADJ UD)/(ADJ→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### CCONJ ↔ NOUN (Max Overlap Rate: 1.000)

#### CCONJ → NOUN
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (3 occurrences)

#### NOUN → CCONJ
**UD Relations:**
- cc (5 occurrences)
- cc:preconj (1 occurrences)

**ROM Relations:**
- Connection (4 occurrences)

**Examples:**
*CCONJ→NOUN ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: Both → brother, And → sister in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*NOUN→CCONJ UD Examples:*
  - **cc**: emotions → but in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)
  - **cc:preconj**: brother → Both in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*NOUN→CCONJ ROM Examples:*
  - **Connection**: nostalgia → and, comfort → and in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- CCONJ→NOUN: 0 UD, 3 ROM
- NOUN→CCONJ: 6 UD, 4 ROM

**Overlap Rates (Mathematical Formula):**
- CCONJ→NOUN Pattern 1 (Forward): 0.000
- CCONJ→NOUN Pattern 2 (Reverse): 0.000
- CCONJ→NOUN Max Overlap: 0.000
- NOUN→CCONJ Pattern 1 (Forward): 0.667
- NOUN→CCONJ Pattern 2 (Reverse): 1.000
- NOUN→CCONJ Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.67
- Cross ratio (CCONJ→NOUN UD)/(NOUN→CCONJ ROM): 0.00
- Reverse cross ratio (NOUN→CCONJ UD)/(CCONJ→NOUN ROM): 2.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ CCONJ (Max Overlap Rate: 1.000)

#### ADJ → CCONJ
**UD Relations:**
- cc (2 occurrences)

#### CCONJ → ADJ
**ROM Relations:**
- Connection (1 occurrences)
- Predicate (Verb/Preposition - Object) (1 occurrences)

**Examples:**
*ADJ→CCONJ UD Examples:*
  - **cc**: creative → and in "She is both smart and creative." (compound_sentences_input.txt)

*CCONJ→ADJ ROM Examples:*
  - **Connection**: and → vivid in "Her friends who read the journal found themselves moved by its sincerity and vivid details." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: And → creative in "She is both smart and creative." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→CCONJ: 2 UD, 0 ROM
- CCONJ→ADJ: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→CCONJ Pattern 1 (Forward): 0.000
- ADJ→CCONJ Pattern 2 (Reverse): 1.000
- ADJ→CCONJ Max Overlap: 1.000
- CCONJ→ADJ Pattern 1 (Forward): 0.000
- CCONJ→ADJ Pattern 2 (Reverse): 0.000
- CCONJ→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→CCONJ UD)/(CCONJ→ADJ ROM): 1.00
- Reverse cross ratio (CCONJ→ADJ UD)/(ADJ→CCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADP ↔ PRON (Max Overlap Rate: 1.000)

#### ADP → PRON
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (1 occurrences)
- Predicate (Prep - Object) (1 occurrences)
- Predicate (Verb/Preposition - Object) (1 occurrences)

#### PRON → ADP
**UD Relations:**
- case (3 occurrences)

**Examples:**
*ADP→PRON ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: with → her in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)
  - **Predicate (Prep - Object)**: within → her in "The pain, like before, settled deep within her." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: With → us in "You can either stay home or come with us." (compound_sentences_input.txt)

*PRON→ADP UD Examples:*
  - **case**: her → with in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→PRON: 0 UD, 3 ROM
- PRON→ADP: 3 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→PRON Pattern 1 (Forward): 0.000
- ADP→PRON Pattern 2 (Reverse): 0.000
- ADP→PRON Max Overlap: 0.000
- PRON→ADP Pattern 1 (Forward): 0.000
- PRON→ADP Pattern 2 (Reverse): 1.000
- PRON→ADP Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→PRON UD)/(PRON→ADP ROM): 0.00
- Reverse cross ratio (PRON→ADP UD)/(ADP→PRON ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ ADV (Max Overlap Rate: 1.000)

#### ADJ → ADV
**UD Relations:**
- advmod (9 occurrences)

#### ADV → ADJ
**ROM Relations:**
- Constraint (1 occurrences)
- Predicate (Verb/Preposition - Object) (1 occurrences)

**Examples:**
*ADJ→ADV UD Examples:*
  - **advmod**: sad → very in "She was very sad yesterday." (basic_sentences_input.txt)

*ADV→ADJ ROM Examples:*
  - **Constraint**: very → sad in "She was very sad yesterday." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: Both → smart in "She is both smart and creative." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→ADV: 9 UD, 0 ROM
- ADV→ADJ: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→ADV Pattern 1 (Forward): 0.000
- ADJ→ADV Pattern 2 (Reverse): 1.000
- ADJ→ADV Max Overlap: 1.000
- ADV→ADJ Pattern 1 (Forward): 0.000
- ADV→ADJ Pattern 2 (Reverse): 0.000
- ADV→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→ADV UD)/(ADV→ADJ ROM): 4.50
- Reverse cross ratio (ADV→ADJ UD)/(ADJ→ADV ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADV ↔ INTJ (Max Overlap Rate: 1.000)

#### ADV → INTJ
**UD Relations:**
- discourse (1 occurrences)

#### INTJ → ADV
**ROM Relations:**
- Predicate (Prep - Object) (1 occurrences)

**Examples:**
*ADV→INTJ UD Examples:*
  - **discourse**: before → like in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

*INTJ→ADV ROM Examples:*
  - **Predicate (Prep - Object)**: Like → before in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→INTJ: 1 UD, 0 ROM
- INTJ→ADV: 0 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→INTJ Pattern 1 (Forward): 0.000
- ADV→INTJ Pattern 2 (Reverse): 1.000
- ADV→INTJ Max Overlap: 1.000
- INTJ→ADV Pattern 1 (Forward): 0.000
- INTJ→ADV Pattern 2 (Reverse): 0.000
- INTJ→ADV Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→INTJ UD)/(INTJ→ADV ROM): 1.00
- Reverse cross ratio (INTJ→ADV UD)/(ADV→INTJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### NOUN ↔ PROPN (Max Overlap Rate: 1.000)

#### NOUN → PROPN
**UD Relations:**
- compound (1 occurrences)

#### PROPN → NOUN
**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*NOUN→PROPN UD Examples:*
  - **compound**: journal → JIDPS in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)

*PROPN→NOUN ROM Examples:*
  - **Constraint**: JIDPS → journal in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→PROPN: 1 UD, 0 ROM
- PROPN→NOUN: 0 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→PROPN Pattern 1 (Forward): 0.000
- NOUN→PROPN Pattern 2 (Reverse): 1.000
- NOUN→PROPN Max Overlap: 1.000
- PROPN→NOUN Pattern 1 (Forward): 0.000
- PROPN→NOUN Pattern 2 (Reverse): 0.000
- PROPN→NOUN Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PROPN UD)/(PROPN→NOUN ROM): 1.00
- Reverse cross ratio (PROPN→NOUN UD)/(NOUN→PROPN ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADV ↔ ADV (Max Overlap Rate: 1.000)

#### ADV → ADV
**UD Relations:**
- advmod (2 occurrences)
- conj (1 occurrences)

**ROM Relations:**
- Constraint (2 occurrences)

#### ADV → ADV
**UD Relations:**
- advmod (2 occurrences)
- conj (1 occurrences)

**ROM Relations:**
- Constraint (2 occurrences)

**Examples:**
*ADV→ADV UD Examples:*
  - **conj**: effectively → efficiently in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **advmod**: quickly → as in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)

*ADV→ADV ROM Examples:*
  - **Constraint**: Just → so in "Just as honesty builds trust, so does kindness." (compound_sentences_input.txt)

*ADV→ADV UD Examples:*
  - **conj**: effectively → efficiently in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **advmod**: quickly → as in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)

*ADV→ADV ROM Examples:*
  - **Constraint**: Just → so in "Just as honesty builds trust, so does kindness." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→ADV: 3 UD, 2 ROM
- ADV→ADV: 3 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→ADV Pattern 1 (Forward): 0.667
- ADV→ADV Pattern 2 (Reverse): 1.000
- ADV→ADV Max Overlap: 1.000
- ADV→ADV Pattern 1 (Forward): 0.667
- ADV→ADV Pattern 2 (Reverse): 1.000
- ADV→ADV Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.67
- Reverse ROM/UD ratio: 0.67
- Cross ratio (ADV→ADV UD)/(ADV→ADV ROM): 1.50
- Reverse cross ratio (ADV→ADV UD)/(ADV→ADV ROM): 1.50
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADJ ↔ PART (Max Overlap Rate: 1.000)

#### ADJ → PART
**UD Relations:**
- advmod (3 occurrences)

#### PART → ADJ
**ROM Relations:**
- Constraint (2 occurrences)

**Examples:**
*ADJ→PART UD Examples:*
  - **advmod**: long → not in "The movie was not only long but also boring." (compound_sentences_input.txt)

*PART→ADJ ROM Examples:*
  - **Constraint**: Not → easy in "This task is not as easy as it looks." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→PART: 3 UD, 0 ROM
- PART→ADJ: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→PART Pattern 1 (Forward): 0.000
- ADJ→PART Pattern 2 (Reverse): 1.000
- ADJ→PART Max Overlap: 1.000
- PART→ADJ Pattern 1 (Forward): 0.000
- PART→ADJ Pattern 2 (Reverse): 0.000
- PART→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→PART UD)/(PART→ADJ ROM): 1.50
- Reverse cross ratio (PART→ADJ UD)/(ADJ→PART ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADP ↔ ADV (Max Overlap Rate: 1.000)

#### ADP → ADV
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (1 occurrences)

#### ADV → ADP
**UD Relations:**
- fixed (2 occurrences)

**ROM Relations:**
- Connection (2 occurrences)

**Examples:**
*ADP→ADV ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: As → quickly in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)

*ADV→ADP UD Examples:*
  - **fixed**: rather → than in "He chose to walk rather than drive." (compound_sentences_input.txt)

*ADV→ADP ROM Examples:*
  - **Connection**: Rather → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→ADV: 0 UD, 1 ROM
- ADV→ADP: 2 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→ADV Pattern 1 (Forward): 0.000
- ADP→ADV Pattern 2 (Reverse): 0.000
- ADP→ADV Max Overlap: 0.000
- ADV→ADP Pattern 1 (Forward): 1.000
- ADV→ADP Pattern 2 (Reverse): 1.000
- ADV→ADP Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 1.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (ADP→ADV UD)/(ADV→ADP ROM): 0.00
- Reverse cross ratio (ADV→ADP UD)/(ADP→ADV ROM): 2.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### ADP ↔ NOUN (Max Overlap Rate: 0.917)

#### ADP → NOUN
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (8 occurrences)
- Predicate (Preposition - Object) (7 occurrences)
- Constraint (5 occurrences)
- Predicate (Verb/Proposition - Object) (4 occurrences)

#### NOUN → ADP
**UD Relations:**
- case (22 occurrences)

**Examples:**
*ADP→NOUN ROM Examples:*
  - **Predicate (Verb/Preposition - Object)**: of → nostalgia, of → comfort in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Predicate (Preposition - Object)**: into → book in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Constraint**: from → letter in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)

*NOUN→ADP UD Examples:*
  - **case**: memories → by in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→NOUN: 0 UD, 24 ROM
- NOUN→ADP: 22 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→NOUN Pattern 1 (Forward): 0.000
- ADP→NOUN Pattern 2 (Reverse): 0.000
- ADP→NOUN Max Overlap: 0.000
- NOUN→ADP Pattern 1 (Forward): 0.000
- NOUN→ADP Pattern 2 (Reverse): 0.917
- NOUN→ADP Max Overlap: 0.917
- **Overall Maximum Overlap Rate: 0.917**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→NOUN UD)/(NOUN→ADP ROM): 0.00
- Reverse cross ratio (NOUN→ADP UD)/(ADP→NOUN ROM): 0.92
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### SCONJ ↔ VERB (Max Overlap Rate: 0.905)

#### SCONJ → VERB
**ROM Relations:**
- Constraint (9 occurrences)
- Predicate (Verb/Proposition - Object) (5 occurrences)
- Connection (3 occurrences)
- Predicate (Verb/Preposition - Object) (2 occurrences)
- Predicate (Verb - Object) (1 occurrences)
- Predicate (Subject - Verb) (1 occurrences)

#### VERB → SCONJ
**UD Relations:**
- mark (19 occurrences)

**Examples:**
*SCONJ→VERB ROM Examples:*
  - **Constraint**: Because → stayed in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Predicate (Verb - Object)**: as → read in "She smiled as she read about the time they built a treehouse together." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: Whether → call in "I don't know whether he’ll call or text." (compound_sentences_input.txt)

*VERB→SCONJ UD Examples:*
  - **mark**: raining → because in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)

**Mathematical Overlap Analysis:**
- SCONJ→VERB: 0 UD, 21 ROM
- VERB→SCONJ: 19 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- SCONJ→VERB Pattern 1 (Forward): 0.000
- SCONJ→VERB Pattern 2 (Reverse): 0.000
- SCONJ→VERB Max Overlap: 0.000
- VERB→SCONJ Pattern 1 (Forward): 0.000
- VERB→SCONJ Pattern 2 (Reverse): 0.905
- VERB→SCONJ Max Overlap: 0.905
- **Overall Maximum Overlap Rate: 0.905**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (SCONJ→VERB UD)/(VERB→SCONJ ROM): 0.00
- Reverse cross ratio (VERB→SCONJ UD)/(SCONJ→VERB ROM): 0.90
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### NOUN ↔ PRON (Max Overlap Rate: 0.846)

#### NOUN → PRON
**UD Relations:**
- nmod:poss (17 occurrences)
- nsubj (3 occurrences)
- appos (2 occurrences)

**ROM Relations:**
- Connection (3 occurrences)
- Constraint (1 occurrences)

#### PRON → NOUN
**ROM Relations:**
- Constraint (16 occurrences)
- Connection (9 occurrences)
- Predicate (Subject - Verb) (1 occurrences)

**Examples:**
*NOUN→PRON UD Examples:*
  - **nmod:poss**: friend → my in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **appos**: girl → whom in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)
  - **nsubj**: place → This in "This is the place where we stayed." (adjective_clauses_sentences_input.txt)

*NOUN→PRON ROM Examples:*
  - **Connection**: tone → that in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
  - **Constraint**: story → her in "Nobody told her the full story." (basic_sentences_input.txt)

*PRON→NOUN ROM Examples:*
  - **Connection**: Who → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Constraint**: My → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
  - **Predicate (Subject - Verb)**: He → text in "I don't know whether he’ll call or text." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→PRON: 22 UD, 4 ROM
- PRON→NOUN: 0 UD, 26 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→PRON Pattern 1 (Forward): 0.182
- NOUN→PRON Pattern 2 (Reverse): 0.846
- NOUN→PRON Max Overlap: 0.846
- PRON→NOUN Pattern 1 (Forward): 0.000
- PRON→NOUN Pattern 2 (Reverse): 0.000
- PRON→NOUN Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.846**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.18
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PRON UD)/(PRON→NOUN ROM): 0.85
- Reverse cross ratio (PRON→NOUN UD)/(NOUN→PRON ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### CCONJ ↔ VERB (Max Overlap Rate: 0.818)

#### CCONJ → VERB
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (6 occurrences)
- Constraint (3 occurrences)
- Connect (2 occurrences)

#### VERB → CCONJ
**UD Relations:**
- cc (7 occurrences)
- cc:preconj (2 occurrences)

**Examples:**
*CCONJ→VERB ROM Examples:*
  - **Constraint**: But → happened in "But it never happened." (basic_sentences_input.txt)
  - **Connect**: and → stop, and → slow in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: But → started in "She wanted to go for a walk, but it started raining." (compound_sentences_input.txt)

*VERB→CCONJ UD Examples:*
  - **cc**: happened → But in "But it never happened." (basic_sentences_input.txt)
  - **cc:preconj**: stay → either in "You can either stay home or come with us." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- CCONJ→VERB: 0 UD, 11 ROM
- VERB→CCONJ: 9 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- CCONJ→VERB Pattern 1 (Forward): 0.000
- CCONJ→VERB Pattern 2 (Reverse): 0.000
- CCONJ→VERB Max Overlap: 0.000
- VERB→CCONJ Pattern 1 (Forward): 0.000
- VERB→CCONJ Pattern 2 (Reverse): 0.818
- VERB→CCONJ Max Overlap: 0.818
- **Overall Maximum Overlap Rate: 0.818**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (CCONJ→VERB UD)/(VERB→CCONJ ROM): 0.00
- Reverse cross ratio (VERB→CCONJ UD)/(CCONJ→VERB ROM): 0.82
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### PROPN ↔ VERB (Max Overlap Rate: 0.800)

#### PROPN → VERB
**ROM Relations:**
- Predicate (Subject - Verb) (5 occurrences)

#### VERB → PROPN
**UD Relations:**
- nsubj (2 occurrences)
- obl (1 occurrences)
- obj (1 occurrences)

**ROM Relations:**
- Constraint (1 occurrences)
- Predicate (Verb/Proposition - Object) (1 occurrences)

**Examples:**
*PROPN→VERB ROM Examples:*
  - **Predicate (Subject - Verb)**: Sarah → decided, Sarah → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

*VERB→PROPN UD Examples:*
  - **obl**: moved → Canada in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
  - **nsubj**: decided → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **obj**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)

*VERB→PROPN ROM Examples:*
  - **Constraint**: Inspired → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PROPN→VERB: 0 UD, 5 ROM
- VERB→PROPN: 4 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- PROPN→VERB Pattern 1 (Forward): 0.000
- PROPN→VERB Pattern 2 (Reverse): 0.000
- PROPN→VERB Max Overlap: 0.000
- VERB→PROPN Pattern 1 (Forward): 0.500
- VERB→PROPN Pattern 2 (Reverse): 0.800
- VERB→PROPN Max Overlap: 0.800
- **Overall Maximum Overlap Rate: 0.800**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.50
- Cross ratio (PROPN→VERB UD)/(VERB→PROPN ROM): 0.00
- Reverse cross ratio (VERB→PROPN UD)/(PROPN→VERB ROM): 0.80
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟢 Excellent overlap**

---

### PART ↔ VERB (Max Overlap Rate: 0.773)

#### PART → VERB
**ROM Relations:**
- Constraint (10 occurrences)
- Predicate (Verb/Preposition - Object) (6 occurrences)
- Predicate (Verb/Proposition - Object) (4 occurrences)
- Predicate (Preposition - Object) (2 occurrences)

#### VERB → PART
**UD Relations:**
- mark (11 occurrences)
- advmod (6 occurrences)

**Examples:**
*PART→VERB ROM Examples:*
  - **Constraint**: to → decided, to → decided in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (Preposition - Object)**: to → preserve, to → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: To → manage in "Design a web system to manage the editorial workflow of the JIDPS journal." (basic_sentences_input.txt)

*VERB→PART UD Examples:*
  - **advmod**: know → n’t in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
  - **mark**: start → to, preserve → to in "Inspired by those cherished memories, Sarah decided to start a journal to preserve them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PART→VERB: 0 UD, 22 ROM
- VERB→PART: 17 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- PART→VERB Pattern 1 (Forward): 0.000
- PART→VERB Pattern 2 (Reverse): 0.000
- PART→VERB Max Overlap: 0.000
- VERB→PART Pattern 1 (Forward): 0.000
- VERB→PART Pattern 2 (Reverse): 0.773
- VERB→PART Max Overlap: 0.773
- **Overall Maximum Overlap Rate: 0.773**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (PART→VERB UD)/(VERB→PART ROM): 0.00
- Reverse cross ratio (VERB→PART UD)/(PART→VERB ROM): 0.77
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🟡 Good overlap**

---

### NOUN ↔ SCONJ (Max Overlap Rate: 0.250)

#### NOUN → SCONJ
**UD Relations:**
- mark (1 occurrences)

#### SCONJ → NOUN
**ROM Relations:**
- Constraint (4 occurrences)

**Examples:**
*NOUN→SCONJ UD Examples:*
  - **mark**: time → that in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

*SCONJ→NOUN ROM Examples:*
  - **Constraint**: that → News in "I heard the news that she got married." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→SCONJ: 1 UD, 0 ROM
- SCONJ→NOUN: 0 UD, 4 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→SCONJ Pattern 1 (Forward): 0.000
- NOUN→SCONJ Pattern 2 (Reverse): 0.250
- NOUN→SCONJ Max Overlap: 0.250
- SCONJ→NOUN Pattern 1 (Forward): 0.000
- SCONJ→NOUN Pattern 2 (Reverse): 0.000
- SCONJ→NOUN Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.250**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→SCONJ UD)/(SCONJ→NOUN ROM): 0.25
- Reverse cross ratio (SCONJ→NOUN UD)/(NOUN→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🔴 Low overlap**

---

### ADP ↔ VERB (Max Overlap Rate: 0.235)

#### ADP → VERB
**ROM Relations:**
- Constraint (14 occurrences)
- Predicate (Verb/Preposition - Object) (3 occurrences)

#### VERB → ADP
**UD Relations:**
- compound:prt (3 occurrences)
- mark (1 occurrences)

**ROM Relations:**
- Constraint (3 occurrences)

**Examples:**
*ADP→VERB ROM Examples:*
  - **Constraint**: into → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: Than → watch in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

*VERB→ADP UD Examples:*
  - **compound:prt**: broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
  - **mark**: watch → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

*VERB→ADP ROM Examples:*
  - **Constraint**: Broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→VERB: 0 UD, 17 ROM
- VERB→ADP: 4 UD, 3 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→VERB Pattern 1 (Forward): 0.000
- ADP→VERB Pattern 2 (Reverse): 0.000
- ADP→VERB Max Overlap: 0.000
- VERB→ADP Pattern 1 (Forward): 0.750
- VERB→ADP Pattern 2 (Reverse): 0.235
- VERB→ADP Max Overlap: 0.750
- **Overall Maximum Overlap Rate: 0.235**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.75
- Cross ratio (ADP→VERB UD)/(VERB→ADP ROM): 0.00
- Reverse cross ratio (VERB→ADP UD)/(ADP→VERB ROM): 0.24
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: 🔴 Low overlap**

---

### NOUN ↔ PUNCT (Max Overlap Rate: 0.000)

#### NOUN → PUNCT
**UD Relations:**
- punct (15 occurrences)

#### PUNCT → NOUN
**Examples:**
*NOUN→PUNCT UD Examples:*
  - **punct**: friend → . in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→PUNCT: 15 UD, 0 ROM
- PUNCT→NOUN: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→PUNCT Pattern 1 (Forward): 0.000
- NOUN→PUNCT Pattern 2 (Reverse): 0.000
- NOUN→PUNCT Max Overlap: 0.000
- PUNCT→NOUN Pattern 1 (Forward): 0.000
- PUNCT→NOUN Pattern 2 (Reverse): 0.000
- PUNCT→NOUN Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PUNCT UD)/(PUNCT→NOUN ROM): 0.00
- Reverse cross ratio (PUNCT→NOUN UD)/(NOUN→PUNCT ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADJ ↔ PUNCT (Max Overlap Rate: 0.000)

#### ADJ → PUNCT
**UD Relations:**
- punct (15 occurrences)

#### PUNCT → ADJ
**Examples:**
*ADJ→PUNCT UD Examples:*
  - **punct**: famous → . in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→PUNCT: 15 UD, 0 ROM
- PUNCT→ADJ: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→PUNCT Pattern 1 (Forward): 0.000
- ADJ→PUNCT Pattern 2 (Reverse): 0.000
- ADJ→PUNCT Max Overlap: 0.000
- PUNCT→ADJ Pattern 1 (Forward): 0.000
- PUNCT→ADJ Pattern 2 (Reverse): 0.000
- PUNCT→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→PUNCT UD)/(PUNCT→ADJ ROM): 0.00
- Reverse cross ratio (PUNCT→ADJ UD)/(ADJ→PUNCT ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### PRON ↔ PUNCT (Max Overlap Rate: 0.000)

#### PRON → PUNCT
**UD Relations:**
- punct (4 occurrences)

#### PUNCT → PRON
**Examples:**
*PRON→PUNCT UD Examples:*
  - **punct**: whom → (, whom → ) in "The girl (whom) I met is nice." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PRON→PUNCT: 4 UD, 0 ROM
- PUNCT→PRON: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- PRON→PUNCT Pattern 1 (Forward): 0.000
- PRON→PUNCT Pattern 2 (Reverse): 0.000
- PRON→PUNCT Max Overlap: 0.000
- PUNCT→PRON Pattern 1 (Forward): 0.000
- PUNCT→PRON Pattern 2 (Reverse): 0.000
- PUNCT→PRON Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (PRON→PUNCT UD)/(PUNCT→PRON ROM): 0.00
- Reverse cross ratio (PUNCT→PRON UD)/(PRON→PUNCT ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### AUX ↔ NUM (Max Overlap Rate: 0.000)

#### AUX → NUM
#### NUM → AUX
**UD Relations:**
- cop (1 occurrences)

**ROM Relations:**
- Predicate (Subject - Verb) (1 occurrences)

**Examples:**
*NUM→AUX UD Examples:*
  - **cop**: one → was in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

*NUM→AUX ROM Examples:*
  - **Predicate (Subject - Verb)**: 2018 → was in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→NUM: 0 UD, 0 ROM
- NUM→AUX: 1 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→NUM Pattern 1 (Forward): 0.000
- AUX→NUM Pattern 2 (Reverse): 0.000
- AUX→NUM Max Overlap: 0.000
- NUM→AUX Pattern 1 (Forward): 1.000
- NUM→AUX Pattern 2 (Reverse): 0.000
- NUM→AUX Max Overlap: 1.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (AUX→NUM UD)/(NUM→AUX ROM): 0.00
- Reverse cross ratio (NUM→AUX UD)/(AUX→NUM ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### PUNCT ↔ VERB (Max Overlap Rate: 0.000)

#### PUNCT → VERB
#### VERB → PUNCT
**UD Relations:**
- punct (61 occurrences)

**Examples:**
*VERB→PUNCT UD Examples:*
  - **punct**: remember → . in "I remember the day when we met." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PUNCT→VERB: 0 UD, 0 ROM
- VERB→PUNCT: 61 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- PUNCT→VERB Pattern 1 (Forward): 0.000
- PUNCT→VERB Pattern 2 (Reverse): 0.000
- PUNCT→VERB Max Overlap: 0.000
- VERB→PUNCT Pattern 1 (Forward): 0.000
- VERB→PUNCT Pattern 2 (Reverse): 0.000
- VERB→PUNCT Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (PUNCT→VERB UD)/(VERB→PUNCT ROM): 0.00
- Reverse cross ratio (VERB→PUNCT UD)/(PUNCT→VERB ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### AUX ↔ PRON (Max Overlap Rate: 0.000)

#### AUX → PRON
#### PRON → AUX
**ROM Relations:**
- Predicate (Subject - Verb) (11 occurrences)

**Examples:**
*PRON→AUX ROM Examples:*
  - **Predicate (Subject - Verb)**: This → is in "This is the place where we stayed." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→PRON: 0 UD, 0 ROM
- PRON→AUX: 0 UD, 11 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→PRON Pattern 1 (Forward): 0.000
- AUX→PRON Pattern 2 (Reverse): 0.000
- AUX→PRON Max Overlap: 0.000
- PRON→AUX Pattern 1 (Forward): 0.000
- PRON→AUX Pattern 2 (Reverse): 0.000
- PRON→AUX Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (AUX→PRON UD)/(PRON→AUX ROM): 0.00
- Reverse cross ratio (PRON→AUX UD)/(AUX→PRON ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### AUX ↔ SCONJ (Max Overlap Rate: 0.000)

#### AUX → SCONJ
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (3 occurrences)

#### SCONJ → AUX
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (4 occurrences)
- Constraint (1 occurrences)
- Predicate (Subject - Verb) (1 occurrences)
- Connection (1 occurrences)

**Examples:**
*AUX→SCONJ ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Is → that in "The truth is that she never left." (noun_clauses_sentences_input.txt)

*SCONJ→AUX ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Because → was in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)
  - **Constraint**: As → is in "This task is not as easy as it looks." (compound_sentences_input.txt)
  - **Predicate (Subject - Verb)**: That → was in "That he lied was obvious." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→SCONJ: 0 UD, 3 ROM
- SCONJ→AUX: 0 UD, 7 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→SCONJ Pattern 1 (Forward): 0.000
- AUX→SCONJ Pattern 2 (Reverse): 0.000
- AUX→SCONJ Max Overlap: 0.000
- SCONJ→AUX Pattern 1 (Forward): 0.000
- SCONJ→AUX Pattern 2 (Reverse): 0.000
- SCONJ→AUX Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (AUX→SCONJ UD)/(SCONJ→AUX ROM): 0.00
- Reverse cross ratio (SCONJ→AUX UD)/(AUX→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### ADJ ↔ PRON (Max Overlap Rate: 0.000)

#### ADJ → PRON
**UD Relations:**
- nsubj (8 occurrences)

#### PRON → ADJ
**Examples:**
*ADJ→PRON UD Examples:*
  - **nsubj**: tired → she in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→PRON: 8 UD, 0 ROM
- PRON→ADJ: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→PRON Pattern 1 (Forward): 0.000
- ADJ→PRON Pattern 2 (Reverse): 0.000
- ADJ→PRON Max Overlap: 0.000
- PRON→ADJ Pattern 1 (Forward): 0.000
- PRON→ADJ Pattern 2 (Reverse): 0.000
- PRON→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→PRON UD)/(PRON→ADJ ROM): 0.00
- Reverse cross ratio (PRON→ADJ UD)/(ADJ→PRON ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADJ ↔ VERB (Max Overlap Rate: 0.000)

#### ADJ → VERB
**UD Relations:**
- advcl (3 occurrences)
- parataxis (2 occurrences)
- xcomp (1 occurrences)
- csubj (1 occurrences)
- ccomp (1 occurrences)

#### VERB → ADJ
**UD Relations:**
- advcl (1 occurrences)
- advmod (1 occurrences)
- ccomp (1 occurrences)

**Examples:**
*ADJ→VERB UD Examples:*
  - **parataxis**: clear → decided in "The sky was clear; we decided to go stargazing." (compound_sentences_input.txt)
  - **xcomp**: unsure → accept in "She’s unsure whether to accept the job or continue studying." (compound_sentences_input.txt)
  - **advcl**: easy → looks in "This task is not as easy as it looks." (compound_sentences_input.txt)

*VERB→ADJ UD Examples:*
  - **advcl**: finished → tired in "Although she was tired, she finished the report." (adverb_clauses_sentence_input.txt)
  - **advmod**: enjoys → much in "She enjoys painting as much as she enjoys dancing." (compound_sentences_input.txt)
  - **ccomp**: know → right in "I know that she is right." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→VERB: 8 UD, 0 ROM
- VERB→ADJ: 3 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→VERB Pattern 1 (Forward): 0.000
- ADJ→VERB Pattern 2 (Reverse): 0.000
- ADJ→VERB Max Overlap: 0.000
- VERB→ADJ Pattern 1 (Forward): 0.000
- VERB→ADJ Pattern 2 (Reverse): 0.000
- VERB→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→VERB UD)/(VERB→ADJ ROM): 0.00
- Reverse cross ratio (VERB→ADJ UD)/(ADJ→VERB ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### NOUN ↔ PART (Max Overlap Rate: 0.000)

#### NOUN → PART
**UD Relations:**
- advmod (1 occurrences)

#### PART → NOUN
**Examples:**
*NOUN→PART UD Examples:*
  - **advmod**: stories → not in "She described not only the stories her grandmother shared, but also the emotions they stirred." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NOUN→PART: 1 UD, 0 ROM
- PART→NOUN: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- NOUN→PART Pattern 1 (Forward): 0.000
- NOUN→PART Pattern 2 (Reverse): 0.000
- NOUN→PART Max Overlap: 0.000
- PART→NOUN Pattern 1 (Forward): 0.000
- PART→NOUN Pattern 2 (Reverse): 0.000
- PART→NOUN Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PART UD)/(PART→NOUN ROM): 0.00
- Reverse cross ratio (PART→NOUN UD)/(NOUN→PART ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### NUM ↔ PRON (Max Overlap Rate: 0.000)

#### NUM → PRON
**UD Relations:**
- nsubj (1 occurrences)

#### PRON → NUM
**Examples:**
*NUM→PRON UD Examples:*
  - **nsubj**: one → It in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NUM→PRON: 1 UD, 0 ROM
- PRON→NUM: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- NUM→PRON Pattern 1 (Forward): 0.000
- NUM→PRON Pattern 2 (Reverse): 0.000
- NUM→PRON Max Overlap: 0.000
- PRON→NUM Pattern 1 (Forward): 0.000
- PRON→NUM Pattern 2 (Reverse): 0.000
- PRON→NUM Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NUM→PRON UD)/(PRON→NUM ROM): 0.00
- Reverse cross ratio (PRON→NUM UD)/(NUM→PRON ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### NUM ↔ PUNCT (Max Overlap Rate: 0.000)

#### NUM → PUNCT
**UD Relations:**
- punct (1 occurrences)

#### PUNCT → NUM
**Examples:**
*NUM→PUNCT UD Examples:*
  - **punct**: one → . in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- NUM→PUNCT: 1 UD, 0 ROM
- PUNCT→NUM: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- NUM→PUNCT Pattern 1 (Forward): 0.000
- NUM→PUNCT Pattern 2 (Reverse): 0.000
- NUM→PUNCT Max Overlap: 0.000
- PUNCT→NUM Pattern 1 (Forward): 0.000
- PUNCT→NUM Pattern 2 (Reverse): 0.000
- PUNCT→NUM Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NUM→PUNCT UD)/(PUNCT→NUM ROM): 0.00
- Reverse cross ratio (PUNCT→NUM UD)/(NUM→PUNCT ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADP ↔ NUM (Max Overlap Rate: 0.000)

#### ADP → NUM
**ROM Relations:**
- Constraint (1 occurrences)

#### NUM → ADP
**Examples:**
*ADP→NUM ROM Examples:*
  - **Constraint**: of → one in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→NUM: 0 UD, 1 ROM
- NUM→ADP: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→NUM Pattern 1 (Forward): 0.000
- ADP→NUM Pattern 2 (Reverse): 0.000
- ADP→NUM Max Overlap: 0.000
- NUM→ADP Pattern 1 (Forward): 0.000
- NUM→ADP Pattern 2 (Reverse): 0.000
- NUM→ADP Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→NUM UD)/(NUM→ADP ROM): 0.00
- Reverse cross ratio (NUM→ADP UD)/(ADP→NUM ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADV ↔ PUNCT (Max Overlap Rate: 0.000)

#### ADV → PUNCT
**UD Relations:**
- punct (2 occurrences)

#### PUNCT → ADV
**Examples:**
*ADV→PUNCT UD Examples:*
  - **punct**: before → , in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→PUNCT: 2 UD, 0 ROM
- PUNCT→ADV: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→PUNCT Pattern 1 (Forward): 0.000
- ADV→PUNCT Pattern 2 (Reverse): 0.000
- ADV→PUNCT Max Overlap: 0.000
- PUNCT→ADV Pattern 1 (Forward): 0.000
- PUNCT→ADV Pattern 2 (Reverse): 0.000
- PUNCT→ADV Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→PUNCT UD)/(PUNCT→ADV ROM): 0.00
- Reverse cross ratio (PUNCT→ADV UD)/(ADV→PUNCT ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### INTJ ↔ NOUN (Max Overlap Rate: 0.000)

#### INTJ → NOUN
**ROM Relations:**
- Constraint (1 occurrences)

#### NOUN → INTJ
**Examples:**
*INTJ→NOUN ROM Examples:*
  - **Constraint**: Like → pain in "The pain, like before, settled deep within her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- INTJ→NOUN: 0 UD, 1 ROM
- NOUN→INTJ: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- INTJ→NOUN Pattern 1 (Forward): 0.000
- INTJ→NOUN Pattern 2 (Reverse): 0.000
- INTJ→NOUN Max Overlap: 0.000
- NOUN→INTJ Pattern 1 (Forward): 0.000
- NOUN→INTJ Pattern 2 (Reverse): 0.000
- NOUN→INTJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (INTJ→NOUN UD)/(NOUN→INTJ ROM): 0.00
- Reverse cross ratio (NOUN→INTJ UD)/(INTJ→NOUN ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADP ↔ DET (Max Overlap Rate: 0.000)

#### ADP → DET
#### DET → ADP
**UD Relations:**
- case (1 occurrences)

**Examples:**
*DET→ADP UD Examples:*
  - **case**: another → to in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→DET: 0 UD, 0 ROM
- DET→ADP: 1 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→DET Pattern 1 (Forward): 0.000
- ADP→DET Pattern 2 (Reverse): 0.000
- ADP→DET Max Overlap: 0.000
- DET→ADP Pattern 1 (Forward): 0.000
- DET→ADP Pattern 2 (Reverse): 0.000
- DET→ADP Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→DET UD)/(DET→ADP ROM): 0.00
- Reverse cross ratio (DET→ADP UD)/(ADP→DET ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### DET ↔ VERB (Max Overlap Rate: 0.000)

#### DET → VERB
#### VERB → DET
**UD Relations:**
- obl (1 occurrences)

**Examples:**
*VERB→DET UD Examples:*
  - **obl**: fly → another in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- DET→VERB: 0 UD, 0 ROM
- VERB→DET: 1 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- DET→VERB Pattern 1 (Forward): 0.000
- DET→VERB Pattern 2 (Reverse): 0.000
- DET→VERB Max Overlap: 0.000
- VERB→DET Pattern 1 (Forward): 0.000
- VERB→DET Pattern 2 (Reverse): 0.000
- VERB→DET Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (DET→VERB UD)/(VERB→DET ROM): 0.00
- Reverse cross ratio (VERB→DET UD)/(DET→VERB ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADP ↔ ADP (Max Overlap Rate: 0.000)

#### ADP → ADP
**ROM Relations:**
- Connection (1 occurrences)
- Constraint (1 occurrences)

#### ADP → ADP
**ROM Relations:**
- Connection (1 occurrences)
- Constraint (1 occurrences)

**Examples:**
*ADP→ADP ROM Examples:*
  - **Connection**: From → to in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **Constraint**: Out → of in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

*ADP→ADP ROM Examples:*
  - **Connection**: From → to in "Design a vacation house that can fly easily from one location to another." (basic_sentences_input.txt)
  - **Constraint**: Out → of in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→ADP: 0 UD, 2 ROM
- ADP→ADP: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→ADP Pattern 1 (Forward): 0.000
- ADP→ADP Pattern 2 (Reverse): 0.000
- ADP→ADP Max Overlap: 0.000
- ADP→ADP Pattern 1 (Forward): 0.000
- ADP→ADP Pattern 2 (Reverse): 0.000
- ADP→ADP Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→ADP UD)/(ADP→ADP ROM): 0.00
- Reverse cross ratio (ADP→ADP UD)/(ADP→ADP ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### ADJ ↔ ADP (Max Overlap Rate: 0.000)

#### ADJ → ADP
#### ADP → ADJ
**ROM Relations:**
- Predicate (Verb/Preposition - Object) (2 occurrences)
- Constraint (1 occurrences)

**Examples:**
*ADP→ADJ ROM Examples:*
  - **Constraint**: To → upscale in "Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2." (basic_sentences_input.txt)
  - **Predicate (Verb/Preposition - Object)**: As → tall in "She’s as tall as her brother." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→ADP: 0 UD, 0 ROM
- ADP→ADJ: 0 UD, 3 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→ADP Pattern 1 (Forward): 0.000
- ADJ→ADP Pattern 2 (Reverse): 0.000
- ADJ→ADP Max Overlap: 0.000
- ADP→ADJ Pattern 1 (Forward): 0.000
- ADP→ADJ Pattern 2 (Reverse): 0.000
- ADP→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→ADP UD)/(ADP→ADJ ROM): 0.00
- Reverse cross ratio (ADP→ADJ UD)/(ADJ→ADP ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADV ↔ CCONJ (Max Overlap Rate: 0.000)

#### ADV → CCONJ
**UD Relations:**
- cc (1 occurrences)

#### CCONJ → ADV
**Examples:**
*ADV→CCONJ UD Examples:*
  - **cc**: efficiently → and in "Driver needs to stop and slow down a vehicle effectively and efficiently." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→CCONJ: 1 UD, 0 ROM
- CCONJ→ADV: 0 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→CCONJ Pattern 1 (Forward): 0.000
- ADV→CCONJ Pattern 2 (Reverse): 0.000
- ADV→CCONJ Max Overlap: 0.000
- CCONJ→ADV Pattern 1 (Forward): 0.000
- CCONJ→ADV Pattern 2 (Reverse): 0.000
- CCONJ→ADV Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→CCONJ UD)/(CCONJ→ADV ROM): 0.00
- Reverse cross ratio (CCONJ→ADV UD)/(ADV→CCONJ ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADV ↔ AUX (Max Overlap Rate: 0.000)

#### ADV → AUX
**ROM Relations:**
- Constraint (4 occurrences)
- Predicate (Subject - Verb) (2 occurrences)
- Connection (1 occurrences)

#### AUX → ADV
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (1 occurrences)

**Examples:**
*ADV→AUX ROM Examples:*
  - **Constraint**: However → was in "I was tired; however, I kept working." (compound_sentences_input.txt)
  - **Predicate (Subject - Verb)**: How → is in "How she managed to escape is still a mystery." (noun_clauses_sentences_input.txt)
  - **Connection**: How → is in "The problem is how we can get there." (noun_clauses_sentences_input.txt)

*AUX→ADV ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Is → how in "The problem is how we can get there." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→AUX: 0 UD, 7 ROM
- AUX→ADV: 0 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→AUX Pattern 1 (Forward): 0.000
- ADV→AUX Pattern 2 (Reverse): 0.000
- ADV→AUX Max Overlap: 0.000
- AUX→ADV Pattern 1 (Forward): 0.000
- AUX→ADV Pattern 2 (Reverse): 0.000
- AUX→ADV Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→AUX UD)/(AUX→ADV ROM): 0.00
- Reverse cross ratio (AUX→ADV UD)/(ADV→AUX ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### ADJ ↔ ADJ (Max Overlap Rate: 0.000)

#### ADJ → ADJ
**UD Relations:**
- conj (2 occurrences)

#### ADJ → ADJ
**UD Relations:**
- conj (2 occurrences)

**Examples:**
*ADJ→ADJ UD Examples:*
  - **conj**: smart → creative in "She is both smart and creative." (compound_sentences_input.txt)

*ADJ→ADJ UD Examples:*
  - **conj**: smart → creative in "She is both smart and creative." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADJ→ADJ: 2 UD, 0 ROM
- ADJ→ADJ: 2 UD, 0 ROM

**Overlap Rates (Mathematical Formula):**
- ADJ→ADJ Pattern 1 (Forward): 0.000
- ADJ→ADJ Pattern 2 (Reverse): 0.000
- ADJ→ADJ Max Overlap: 0.000
- ADJ→ADJ Pattern 1 (Forward): 0.000
- ADJ→ADJ Pattern 2 (Reverse): 0.000
- ADJ→ADJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→ADJ UD)/(ADJ→ADJ ROM): 0.00
- Reverse cross ratio (ADJ→ADJ UD)/(ADJ→ADJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### AUX ↔ CCONJ (Max Overlap Rate: 0.000)

#### AUX → CCONJ
#### CCONJ → AUX
**ROM Relations:**
- Constraint (3 occurrences)

**Examples:**
*CCONJ→AUX ROM Examples:*
  - **Constraint**: and → is in "She is both smart and creative." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- AUX→CCONJ: 0 UD, 0 ROM
- CCONJ→AUX: 0 UD, 3 ROM

**Overlap Rates (Mathematical Formula):**
- AUX→CCONJ Pattern 1 (Forward): 0.000
- AUX→CCONJ Pattern 2 (Reverse): 0.000
- AUX→CCONJ Max Overlap: 0.000
- CCONJ→AUX Pattern 1 (Forward): 0.000
- CCONJ→AUX Pattern 2 (Reverse): 0.000
- CCONJ→AUX Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (AUX→CCONJ UD)/(CCONJ→AUX ROM): 0.00
- Reverse cross ratio (CCONJ→AUX UD)/(AUX→CCONJ ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### CCONJ ↔ CCONJ (Max Overlap Rate: 0.000)

#### CCONJ → CCONJ
**ROM Relations:**
- Connection (3 occurrences)

#### CCONJ → CCONJ
**ROM Relations:**
- Connection (3 occurrences)

**Examples:**
*CCONJ→CCONJ ROM Examples:*
  - **Connection**: both → and in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*CCONJ→CCONJ ROM Examples:*
  - **Connection**: both → and in "Both my brother and sister are engineers." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- CCONJ→CCONJ: 0 UD, 3 ROM
- CCONJ→CCONJ: 0 UD, 3 ROM

**Overlap Rates (Mathematical Formula):**
- CCONJ→CCONJ Pattern 1 (Forward): 0.000
- CCONJ→CCONJ Pattern 2 (Reverse): 0.000
- CCONJ→CCONJ Max Overlap: 0.000
- CCONJ→CCONJ Pattern 1 (Forward): 0.000
- CCONJ→CCONJ Pattern 2 (Reverse): 0.000
- CCONJ→CCONJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (CCONJ→CCONJ UD)/(CCONJ→CCONJ ROM): 0.00
- Reverse cross ratio (CCONJ→CCONJ UD)/(CCONJ→CCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### CCONJ ↔ SCONJ (Max Overlap Rate: 0.000)

#### CCONJ → SCONJ
#### SCONJ → CCONJ
**ROM Relations:**
- Connection (2 occurrences)

**Examples:**
*SCONJ→CCONJ ROM Examples:*
  - **Connection**: Whether → Or in "I don't know whether he’ll call or text." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**
- CCONJ→SCONJ: 0 UD, 0 ROM
- SCONJ→CCONJ: 0 UD, 2 ROM

**Overlap Rates (Mathematical Formula):**
- CCONJ→SCONJ Pattern 1 (Forward): 0.000
- CCONJ→SCONJ Pattern 2 (Reverse): 0.000
- CCONJ→SCONJ Max Overlap: 0.000
- SCONJ→CCONJ Pattern 1 (Forward): 0.000
- SCONJ→CCONJ Pattern 2 (Reverse): 0.000
- SCONJ→CCONJ Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (CCONJ→SCONJ UD)/(SCONJ→CCONJ ROM): 0.00
- Reverse cross ratio (SCONJ→CCONJ UD)/(CCONJ→SCONJ ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

---

### ADV ↔ SCONJ (Max Overlap Rate: 0.000)

#### ADV → SCONJ
**ROM Relations:**
- Constraint (1 occurrences)

#### SCONJ → ADV
**ROM Relations:**
- Connection (3 occurrences)
- Predicate (Verb/Proposition - Object) (1 occurrences)

**Examples:**
*ADV→SCONJ ROM Examples:*
  - **Constraint**: Just → as in "Just as the moon affects the tides, so does the sun influence them." (compound_sentences_input.txt)

*SCONJ→ADV ROM Examples:*
  - **Connection**: As → so in "Just as the moon affects the tides, so does the sun influence them." (compound_sentences_input.txt)
  - **Predicate (Verb/Proposition - Object)**: About → how in "We’re thinking about how we can solve the problem." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADV→SCONJ: 0 UD, 1 ROM
- SCONJ→ADV: 0 UD, 4 ROM

**Overlap Rates (Mathematical Formula):**
- ADV→SCONJ Pattern 1 (Forward): 0.000
- ADV→SCONJ Pattern 2 (Reverse): 0.000
- ADV→SCONJ Max Overlap: 0.000
- SCONJ→ADV Pattern 1 (Forward): 0.000
- SCONJ→ADV Pattern 2 (Reverse): 0.000
- SCONJ→ADV Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→SCONJ UD)/(SCONJ→ADV ROM): 0.00
- Reverse cross ratio (SCONJ→ADV UD)/(ADV→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### PRON ↔ PRON (Max Overlap Rate: 0.000)

#### PRON → PRON
**ROM Relations:**
- Constraint (1 occurrences)

#### PRON → PRON
**ROM Relations:**
- Constraint (1 occurrences)

**Examples:**
*PRON→PRON ROM Examples:*
  - **Constraint**: me → what in "She didn’t tell me what had happened." (noun_clauses_sentences_input.txt)

*PRON→PRON ROM Examples:*
  - **Constraint**: me → what in "She didn’t tell me what had happened." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- PRON→PRON: 0 UD, 1 ROM
- PRON→PRON: 0 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- PRON→PRON Pattern 1 (Forward): 0.000
- PRON→PRON Pattern 2 (Reverse): 0.000
- PRON→PRON Max Overlap: 0.000
- PRON→PRON Pattern 1 (Forward): 0.000
- PRON→PRON Pattern 2 (Reverse): 0.000
- PRON→PRON Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (PRON→PRON UD)/(PRON→PRON ROM): 0.00
- Reverse cross ratio (PRON→PRON UD)/(PRON→PRON ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Overlap Assessment: ⚫ No overlap**

---

### ADP ↔ AUX (Max Overlap Rate: 0.000)

#### ADP → AUX
#### AUX → ADP
**ROM Relations:**
- Predicate (Verb/Proposition - Object) (1 occurrences)

**Examples:**
*AUX→ADP ROM Examples:*
  - **Predicate (Verb/Proposition - Object)**: Were → out in "We faced the fact that we were out of time." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**
- ADP→AUX: 0 UD, 0 ROM
- AUX→ADP: 0 UD, 1 ROM

**Overlap Rates (Mathematical Formula):**
- ADP→AUX Pattern 1 (Forward): 0.000
- ADP→AUX Pattern 2 (Reverse): 0.000
- ADP→AUX Max Overlap: 0.000
- AUX→ADP Pattern 1 (Forward): 0.000
- AUX→ADP Pattern 2 (Reverse): 0.000
- AUX→ADP Max Overlap: 0.000
- **Overall Maximum Overlap Rate: 0.000**

**Traditional Ratios (for reference):**
- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→AUX UD)/(AUX→ADP ROM): 0.00
- Reverse cross ratio (AUX→ADP UD)/(ADP→AUX ROM): 0.00
- **Status: Unidirectional coverage only**
- **Overlap Assessment: ⚫ No overlap**

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
| Constraint | 217 | 38.1% |
| Predicate (Subject - Verb) | 133 | 23.3% |
| Predicate (Verb/Proposition - Object) | 81 | 14.2% |
| Predicate (Verb/Preposition - Object) | 75 | 13.2% |
| Connection | 33 | 5.8% |
| Predicate (Verb - Object) | 12 | 2.1% |
| Predicate (Preposition - Object) | 10 | 1.8% |
| Predicate (Prep - Object) | 2 | 0.4% |
| Connect | 2 | 0.4% |
| Constraint (Determiner - Noun) | 1 | 0.2% |
| Constraint (Auxiliary - Main Verb) | 1 | 0.2% |
| Predicate (Subject - Verb) (Second Clause) | 1 | 0.2% |
| Predicate (Verb/Preposition - Object) (Second Clause) | 1 | 0.2% |
| Predicate (Verb/Preposition - Object) (Implied) | 1 | 0.2% |

### POS Pairs Distribution (All Files)
| POS Pair | UD Count | ROM Count | Status |
|----------|----------|-----------|--------|
| VERB → NOUN | 76 | 50 | Both |
| VERB → PRON | 82 | 12 | Both |
| PRON → VERB | 1 | 70 | Both |
| DET → NOUN | 0 | 65 | ROM Only |
| NOUN → DET | 65 | 0 | UD Only |
| VERB → PUNCT | 61 | 0 | UD Only |
| VERB → VERB | 41 | 12 | Both |
| NOUN → VERB | 20 | 28 | Both |
| VERB → ADV | 34 | 3 | Both |
| VERB → AUX | 31 | 2 | Both |
| NOUN → NOUN | 25 | 6 | Both |
| ADV → VERB | 0 | 28 | ROM Only |
| NOUN → AUX | 9 | 17 | Both |
| NOUN → PRON | 22 | 4 | Both |
| PRON → NOUN | 0 | 26 | ROM Only |
| ADP → NOUN | 0 | 24 | ROM Only |
| NOUN → ADP | 22 | 0 | UD Only |
| PART → VERB | 0 | 22 | ROM Only |
| SCONJ → VERB | 0 | 21 | ROM Only |
| VERB → SCONJ | 19 | 0 | UD Only |
| ADJ → NOUN | 8 | 11 | Both |
| AUX → VERB | 0 | 19 | ROM Only |
| ADP → VERB | 0 | 17 | ROM Only |
| VERB → PART | 17 | 0 | UD Only |
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
| ADV → AUX | 0 | 7 | ROM Only |
| VERB → ADP | 4 | 3 | Both |
| SCONJ → AUX | 0 | 7 | ROM Only |
| VERB → PROPN | 4 | 2 | Both |
| ADV → NOUN | 0 | 5 | ROM Only |
| ADV → ADV | 3 | 2 | Both |
| NOUN → ADV | 5 | 0 | UD Only |
| PROPN → VERB | 0 | 5 | ROM Only |
| ADV → ADP | 2 | 2 | Both |
| PRON → PUNCT | 4 | 0 | UD Only |
| NOUN → NUM | 4 | 0 | UD Only |
| SCONJ → ADV | 0 | 4 | ROM Only |
| SCONJ → NOUN | 0 | 4 | ROM Only |
| ADP → PRON | 0 | 3 | ROM Only |
| ADJ → PART | 3 | 0 | UD Only |
| AUX → SCONJ | 0 | 3 | ROM Only |
| CCONJ → AUX | 0 | 3 | ROM Only |
| ADJ → SCONJ | 3 | 0 | UD Only |
| CCONJ → CCONJ | 0 | 3 | ROM Only |
| PRON → ADP | 3 | 0 | UD Only |
| CCONJ → NOUN | 0 | 3 | ROM Only |
| ADP → ADJ | 0 | 3 | ROM Only |
| VERB → ADJ | 3 | 0 | UD Only |
| NUM → AUX | 1 | 1 | Both |
| ADV → ADJ | 0 | 2 | ROM Only |
| SCONJ → CCONJ | 0 | 2 | ROM Only |
| ADV → PUNCT | 2 | 0 | UD Only |
| ADJ → ADJ | 2 | 0 | UD Only |
| PART → ADJ | 0 | 2 | ROM Only |
| NUM → NOUN | 1 | 1 | Both |
| ADJ → CCONJ | 2 | 0 | UD Only |
| CCONJ → ADJ | 0 | 2 | ROM Only |
| SCONJ → ADJ | 0 | 2 | ROM Only |
| ADP → ADP | 0 | 2 | ROM Only |
| AUX → ADV | 0 | 1 | ROM Only |
| PRON → PRON | 0 | 1 | ROM Only |
| PROPN → ADP | 1 | 0 | UD Only |
| NOUN → PART | 1 | 0 | UD Only |
| DET → ADP | 1 | 0 | UD Only |
| INTJ → ADV | 0 | 1 | ROM Only |
| NUM → PRON | 1 | 0 | UD Only |
| PROPN → NOUN | 0 | 1 | ROM Only |
| ADV → SCONJ | 0 | 1 | ROM Only |
| ADP → ADV | 0 | 1 | ROM Only |
| ADV → CCONJ | 1 | 0 | UD Only |
| NOUN → SCONJ | 1 | 0 | UD Only |
| AUX → ADP | 0 | 1 | ROM Only |
| INTJ → NOUN | 0 | 1 | ROM Only |
| NUM → PUNCT | 1 | 0 | UD Only |
| ADP → PROPN | 0 | 1 | ROM Only |
| VERB → DET | 1 | 0 | UD Only |
| ADV → INTJ | 1 | 0 | UD Only |
| ADP → NUM | 0 | 1 | ROM Only |
| NOUN → PROPN | 1 | 0 | UD Only |

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
- Predicate (Subject - Verb): 21
- Predicate (Verb/Proposition - Object): 18
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
- Predicate (Verb/Proposition - Object): 6
- Predicate (Subject - Verb): 4
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
- Constraint: 89
- Predicate (Subject - Verb): 36
- Predicate (Verb/Preposition - Object): 16
- Predicate (Verb/Proposition - Object): 16
- Predicate (Verb - Object): 12

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
- Predicate (Verb/Preposition - Object): 59
- Constraint: 57
- Predicate (Subject - Verb): 35
- Connection: 10
- Predicate (Preposition - Object): 1

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
- Constraint: 43
- Predicate (Verb/Proposition - Object): 41
- Predicate (Subject - Verb): 37
- Connection: 5

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
- PRON → VERB: Predicate (Subject - Verb)
- NOUN → VERB: Predicate (Subject - Verb)
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)

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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)

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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)

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
- NOUN → VERB: Predicate (Subject - Verb)
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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
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
- NUM → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- ADV → VERB: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → ADP: Constraint
- ADP → PROPN: Predicate (Verb/Proposition - Object)

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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- ADV → VERB: Predicate (Verb/Proposition - Object)
- VERB → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)

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
- PRON → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- ADV → VERB: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- ADV → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- ADV → VERB: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → ADV: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Constraint
- SCONJ → AUX: Predicate (Verb/Proposition - Object)
- PRON → AUX: Predicate (Subject - Verb)
- AUX → VERB: Predicate (Verb/Proposition - Object)

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
- SCONJ → AUX: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Constraint
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- DET → NOUN: Constraint
- VERB → NOUN: Predicate (Verb - Object)
- PROPN → VERB: Predicate (Subject - Verb)
- PROPN → VERB: Predicate (Subject - Verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (Preposition - Object)
- VERB → NOUN: Predicate (Preposition - Object)
- DET → NOUN: Constraint
- PART → VERB: Constraint
- PART → VERB: Predicate (Preposition - Object)
- NOUN → VERB: Predicate (Subject - Verb)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- PRON → NOUN: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)

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
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Preposition - Object)
- PRON → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- VERB → NOUN: Constraint
- ADJ → NOUN: Constraint
- NOUN → PRON: Connection
- NOUN → VERB: Predicate (Subject - Verb)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Preposition - Object)
- ADP → NOUN: Predicate (Verb/Preposition - Object)
- ADP → NOUN: Predicate (Verb/Preposition - Object)
- ADP → NOUN: Predicate (Verb/Preposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb - Object)
- VERB → NOUN: Predicate (Verb - Object)
- NOUN → VERB: Predicate (Subject - Verb)
- PRON → NOUN: Constraint
- NOUN → CCONJ: Connection
- NOUN → NOUN: Constraint
- CCONJ → ADJ: Connection
- ADJ → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- NOUN → VERB: Predicate (Subject - Verb)
- NOUN → PRON: Connection
- VERB → NOUN: Predicate (Verb - Object)
- DET → NOUN: Constraint
- PRON → NOUN: Connection

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
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → PROPN: Predicate (Verb/Proposition - Object)
- PROPN → VERB: Predicate (Subject - Verb)
- PROPN → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Proposition - Object)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
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
- PROPN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb - Object)
- ADP → NOUN: Predicate (Preposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- DET → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Verb/Preposition - Object)
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- PRON → VERB: Predicate (Subject - Verb)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
- DET → NOUN: Constraint
- NOUN → VERB: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb - Object)
- ADV → VERB: Constraint
- DET → NOUN: Constraint (Determiner - Noun)
- SCONJ → VERB: Predicate (Verb - Object)
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
- PRON → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb - Object)
- ADP → NUM: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
- DET → NOUN: Constraint
- ADJ → NOUN: Constraint
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- ADP → VERB: Constraint
- ADP → PRON: Predicate (Verb/Proposition - Object)
- ADV → NOUN: Constraint
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (Verb/Proposition - Object)
- ADJ → NOUN: Constraint

### Sentence 23 (basic_sentences_input.txt)
**Input:** She was very sad yesterday.

**POS-UD Relations:**
- ADJ → PRON: nsubj
- ADJ → AUX: cop
- ADJ → ADV: advmod
- ADJ → NOUN: obl:unmarked
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb - Object)
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
- PRON → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- PRON → NOUN: Connection
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)

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
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb - Object)
- VERB → NOUN: Predicate (Verb - Object)
- NOUN → PRON: Constraint
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
- PRON → VERB: Predicate (Subject - Verb)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
- DET → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb - Object)
- VERB → VERB: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint (Auxiliary - Main Verb)

### Sentence 28 (basic_sentences_input.txt)
**Input:** But it never happened.

**POS-UD Relations:**
- VERB → CCONJ: cc
- VERB → PRON: nsubj
- VERB → ADV: advmod
- VERB → PUNCT: punct

**POS-ROM Relations:**
- CCONJ → VERB: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- ADV → VERB: Constraint

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
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- INTJ → NOUN: Constraint
- INTJ → ADV: Predicate (Prep - Object)
- ADV → VERB: Constraint
- ADP → VERB: Constraint
- ADP → PRON: Predicate (Prep - Object)

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
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- NOUN → NOUN: Constraint
- NOUN → PRON: Connection
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Verb/Preposition - Object)
- NUM → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Verb/Preposition - Object)
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
- ADP → NOUN: Predicate (Verb/Preposition - Object)

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
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- NOUN → NOUN: Constraint
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Proposition - Object)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- ADJ → NOUN: Constraint
- DET → NOUN: Constraint
- ADP → NOUN: Constraint
- ADP → NOUN: Predicate (Verb/Proposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- ADV → VERB: Constraint
- CCONJ → VERB: Connect
- CCONJ → VERB: Connect
- PART → VERB: Predicate (Verb/Proposition - Object)
- ADP → VERB: Constraint
- ADV → VERB: Constraint
- ADV → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Preposition - Object)
- PART → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Preposition - Object)
- DET → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Preposition - Object)
- CCONJ → VERB: Constraint
- CCONJ → VERB: Predicate (Verb/Preposition - Object)

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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Preposition - Object)
- VERB → VERB: Predicate (Verb/Preposition - Object)

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
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Preposition - Object)
- ADV → AUX: Constraint
- ADV → VERB: Predicate (Verb/Preposition - Object)

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
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- ADV → ADJ: Predicate (Verb/Preposition - Object)
- CCONJ → ADJ: Predicate (Verb/Preposition - Object)
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
- CCONJ → NOUN: Predicate (Verb/Preposition - Object)
- CCONJ → NOUN: Predicate (Verb/Preposition - Object)
- NOUN → AUX: Predicate (Subject - Verb)
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Preposition - Object)
- CCONJ → CCONJ: Connection
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
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
- NOUN → AUX: Predicate (Subject - Verb)
- DET → NOUN: Constraint
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- AUX → ADJ: Predicate (Verb/Preposition - Object)

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
- PRON → VERB: Predicate (Subject - Verb)
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- AUX → VERB: Constraint
- VERB → ADV: Constraint
- VERB → ADP: Constraint
- ADP → PRON: Predicate (Verb/Preposition - Object)
- CCONJ → VERB: Predicate (Verb/Preposition - Object)
- CCONJ → VERB: Predicate (Verb/Preposition - Object)
- CCONJ → CCONJ: Connection

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
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- CCONJ → VERB: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- CCONJ → VERB: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- SCONJ → VERB: Predicate (Verb/Preposition - Object)
- CCONJ → NOUN: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- PRON → NOUN: Predicate (Subject - Verb)
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
- SCONJ → VERB: Predicate (Verb/Preposition - Object)
- CCONJ → VERB: Predicate (Verb/Preposition - Object)
- PART → VERB: Predicate (Verb/Preposition - Object)
- PART → VERB: Predicate (Verb/Preposition - Object)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- VERB → VERB: Predicate (Verb/Preposition - Object)
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
- ADP → ADJ: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- ADV → VERB: Constraint
- ADP → VERB: Constraint
- ADP → ADV: Predicate (Verb/Preposition - Object)
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
- NOUN → AUX: Predicate (Subject - Verb)
- DET → NOUN: Constraint
- AUX → ADJ: Predicate (Verb/Preposition - Object)
- PART → ADJ: Constraint
- SCONJ → AUX: Constraint
- SCONJ → ADJ: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)

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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- ADJ → NOUN: Constraint
- ADP → VERB: Constraint
- ADP → ADJ: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb) (Second Clause)
- VERB → NOUN: Predicate (Verb/Preposition - Object) (Second Clause)
- ADJ → NOUN: Constraint
- SCONJ → VERB: Constraint
- SCONJ → ADJ: Predicate (Verb/Preposition - Object)

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
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- DET → NOUN: Constraint
- ADV → SCONJ: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- ADV → VERB: Predicate (Verb/Preposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- ADV → ADV: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object) (Implied)
- ADV → VERB: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- NOUN → VERB: Constraint
- PART → VERB: Constraint
- ADV → ADV: Constraint
- SCONJ → VERB: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- ADV → VERB: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- ADV → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- DET → NOUN: Constraint
- ADP → VERB: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Preposition - Object)
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Preposition - Object)
- PART → VERB: Predicate (Verb/Preposition - Object)
- ADV → VERB: Constraint
- ADP → VERB: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Preposition - Object)
- ADV → VERB: Constraint
- ADP → VERB: Predicate (Verb/Preposition - Object)
- PRON → VERB: Predicate (Subject - Verb)

### Sentence 57 (noun_clauses_sentences_input.txt)
**Input:** What she said surprised everyone.

**POS-UD Relations:**
- VERB → PRON: nsubj
- VERB → PRON: nsubj
- PRON → VERB: acl:relcl
- VERB → PRON: obj
- VERB → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)

### Sentence 58 (noun_clauses_sentences_input.txt)
**Input:** That he lied was obvious.

**POS-UD Relations:**
- ADJ → SCONJ: mark
- VERB → PRON: nsubj
- ADJ → VERB: csubj
- ADJ → AUX: cop
- ADJ → PUNCT: punct

**POS-ROM Relations:**
- PRON → VERB: Predicate (Subject - Verb)
- SCONJ → VERB: Connection
- SCONJ → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)
- VERB → AUX: Predicate (Subject - Verb)

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
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- SCONJ → VERB: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Subject - Verb)
- ADP → VERB: Constraint
- ADP → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- PART → VERB: Constraint
- PART → VERB: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- ADV → AUX: Predicate (Subject - Verb)
- AUX → NOUN: Predicate (Verb/Proposition - Object)
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
- NOUN → VERB: Predicate (Subject - Verb)
- ADV → VERB: Constraint
- ADV → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → AUX: Predicate (Verb/Proposition - Object)
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADJ: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- VERB → PRON: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
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
- PRON → VERB: Predicate (Subject - Verb)
- SCONJ → VERB: Constraint
- SCONJ → ADV: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- SCONJ → VERB: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → VERB: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- ADV → VERB: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → VERB: Predicate (Verb/Proposition - Object)
- AUX → SCONJ: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Connection
- PRON → VERB: Predicate (Subject - Verb)
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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → VERB: Predicate (Verb/Proposition - Object)
- AUX → SCONJ: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Connection
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → ADV: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- ADV → AUX: Connection
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- VERB → ADV: Predicate (Verb/Proposition - Object)

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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → SCONJ: Predicate (Verb/Proposition - Object)
- SCONJ → VERB: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- AUX → VERB: Constraint
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → AUX: Predicate (Verb/Proposition - Object)
- PRON → AUX: Predicate (Subject - Verb)
- AUX → VERB: Predicate (Verb/Proposition - Object)

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
- NOUN → AUX: Predicate (Subject - Verb)
- AUX → VERB: Predicate (Verb/Proposition - Object)
- ADV → VERB: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → VERB: Predicate (Verb/Proposition - Object)
- ADJ → NOUN: Constraint
- NOUN → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)

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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → VERB: Predicate (Verb/Proposition - Object)
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
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
- PRON → VERB: Predicate (Subject - Verb)
- VERB → NOUN: Predicate (Verb/Proposition - Object)
- DET → NOUN: Constraint
- SCONJ → NOUN: Constraint
- SCONJ → AUX: Predicate (Verb/Proposition - Object)
- PRON → AUX: Predicate (Subject - Verb)
- AUX → ADP: Predicate (Verb/Proposition - Object)
- ADP → ADP: Constraint
- ADP → NOUN: Predicate (Verb/Proposition - Object)

</details>
