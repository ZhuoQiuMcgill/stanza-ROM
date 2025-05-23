## 🔍 Detailed POS Pair Analysis (Combined) - Bidirectional

This section shows bidirectional POS pair analysis with coverage rates calculated using overall balance formula:
**Note: UD-only pairs are excluded from this detailed analysis.**
**Overall Balance Formula: min(total_UD, total_ROM) / max(total_UD, total_ROM)**

- Individual Coverage: Coverage within each direction separately
- Overall Balanced Coverage: Balance across both directions combined
- **Coverage rates range from 0 (no balance) to 1 (perfect balance)**
  Blocks are sorted by overall balanced coverage (highest first).

### DET ↔ NOUN (Max Coverage Rate: 1.000)

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
- **Constraint (Determiner - Noun)**: a → treehouse in "She smiled as she read about the time they built a treehouse
  together." (basic_sentences_input.txt)

*NOUN→DET UD Examples:*

- **det**: boy → The in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**

- DET→NOUN: 0 UD, 65 ROM
- NOUN→DET: 65 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- DET→NOUN Individual Coverage: 0.000
- NOUN→DET Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (DET→NOUN UD)/(NOUN→DET ROM): 0.00
- Reverse cross ratio (NOUN→DET UD)/(DET→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADP ↔ PROPN (Max Coverage Rate: 1.000)

#### ADP → PROPN

**ROM Relations:**

- Predicate (Verb/Proposition - Object) (1 occurrences)

#### PROPN → ADP

**UD Relations:**

- case (1 occurrences)

**Examples:**
*ADP→PROPN ROM Examples:*

- **Predicate (Verb/Proposition - Object)**: To → Canada in "2018 was the year when I moved to Canada." (
  adjective_clauses_sentences_input.txt)

*PROPN→ADP UD Examples:*

- **case**: Canada → to in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADP→PROPN: 0 UD, 1 ROM
- PROPN→ADP: 1 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- ADP→PROPN Individual Coverage: 0.000
- PROPN→ADP Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→PROPN UD)/(PROPN→ADP ROM): 0.00
- Reverse cross ratio (PROPN→ADP UD)/(ADP→PROPN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### AUX ↔ NUM (Max Coverage Rate: 1.000)

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

- **Predicate (Subject - Verb)**: 2018 → was in "2018 was the year when I moved to Canada." (
  adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**

- AUX→NUM: 0 UD, 0 ROM
- NUM→AUX: 1 UD, 1 ROM

**Coverage Rates (Overall Balance Formula):**

- AUX→NUM Individual Coverage: 0.000
- NUM→AUX Individual Coverage: 1.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (AUX→NUM UD)/(NUM→AUX ROM): 0.00
- Reverse cross ratio (NUM→AUX UD)/(AUX→NUM ROM): 0.00
- **Status: Unidirectional coverage only**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADV ↔ NOUN (Max Coverage Rate: 1.000)

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

- **advmod**: stories → only, emotions → also in "She described not only the stories her grandmother shared, but also
  the emotions they stirred." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADV→NOUN: 0 UD, 5 ROM
- NOUN→ADV: 5 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- ADV→NOUN Individual Coverage: 0.000
- NOUN→ADV Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→NOUN UD)/(NOUN→ADV ROM): 0.00
- Reverse cross ratio (NOUN→ADV UD)/(ADV→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADJ ↔ CCONJ (Max Coverage Rate: 1.000)

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

- **Connection**: and → vivid in "Her friends who read the journal found themselves moved by its sincerity and vivid
  details." (basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: And → creative in "She is both smart and creative." (
  compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADJ→CCONJ: 2 UD, 0 ROM
- CCONJ→ADJ: 0 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- ADJ→CCONJ Individual Coverage: 0.000
- CCONJ→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→CCONJ UD)/(CCONJ→ADJ ROM): 1.00
- Reverse cross ratio (CCONJ→ADJ UD)/(ADJ→CCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADP ↔ PRON (Max Coverage Rate: 1.000)

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

- **Predicate (Verb/Proposition - Object)**: with → her in "That memory, like many others, stayed with her even
  today." (basic_sentences_input.txt)
- **Predicate (Prep - Object)**: within → her in "The pain, like before, settled deep within her." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: With → us in "You can either stay home or come with us." (
  compound_sentences_input.txt)

*PRON→ADP UD Examples:*

- **case**: her → with in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADP→PRON: 0 UD, 3 ROM
- PRON→ADP: 3 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- ADP→PRON Individual Coverage: 0.000
- PRON→ADP Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→PRON UD)/(PRON→ADP ROM): 0.00
- Reverse cross ratio (PRON→ADP UD)/(ADP→PRON ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADV ↔ INTJ (Max Coverage Rate: 1.000)

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

- **Predicate (Prep - Object)**: Like → before in "The pain, like before, settled deep within her." (
  basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADV→INTJ: 1 UD, 0 ROM
- INTJ→ADV: 0 UD, 1 ROM

**Coverage Rates (Overall Balance Formula):**

- ADV→INTJ Individual Coverage: 0.000
- INTJ→ADV Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADV→INTJ UD)/(INTJ→ADV ROM): 1.00
- Reverse cross ratio (INTJ→ADV UD)/(ADV→INTJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### NOUN ↔ PROPN (Max Coverage Rate: 1.000)

#### NOUN → PROPN

**UD Relations:**

- compound (1 occurrences)

#### PROPN → NOUN

**ROM Relations:**

- Constraint (1 occurrences)

**Examples:**
*NOUN→PROPN UD Examples:*

- **compound**: journal → JIDPS in "Design a web system to manage the editorial workflow of the JIDPS journal." (
  basic_sentences_input.txt)

*PROPN→NOUN ROM Examples:*

- **Constraint**: JIDPS → journal in "Design a web system to manage the editorial workflow of the JIDPS journal." (
  basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- NOUN→PROPN: 1 UD, 0 ROM
- PROPN→NOUN: 0 UD, 1 ROM

**Coverage Rates (Overall Balance Formula):**

- NOUN→PROPN Individual Coverage: 0.000
- PROPN→NOUN Individual Coverage: 0.000
- **Overall Balanced Coverage: 1.000**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PROPN UD)/(PROPN→NOUN ROM): 1.00
- Reverse cross ratio (PROPN→NOUN UD)/(NOUN→PROPN ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### PRON ↔ VERB (Max Coverage Rate: 0.988)

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

- **Predicate (Subject - Verb)**: Who → sings in "The boy who sings is my friend." (
  adjective_clauses_sentences_input.txt)
- **Constraint**: her → writing in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that
  surprised her." (basic_sentences_input.txt)
- **Predicate (Subject - Verb) (Second Clause)**: She → enjoys in "She enjoys painting as much as she enjoys dancing." (
  compound_sentences_input.txt)

*VERB→PRON UD Examples:*

- **nsubj**: sings → who in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
- **obj**: painted → this in "The artist who painted this is famous." (adjective_clauses_sentences_input.txt)
- **obl**: stayed → her in "That memory, like many others, stayed with her even today." (basic_sentences_input.txt)

*VERB→PRON ROM Examples:*

- **Predicate (Verb/Proposition - Object)**: Painted → this in "The artist who painted this is famous." (
  adjective_clauses_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: surprised → her in "The emotions of nostalgia, comfort, and love gave her
  writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
- **Predicate (Verb - Object)**: found → themselves in "Her friends who read the journal found themselves moved by its
  sincerity and vivid details." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- PRON→VERB: 1 UD, 70 ROM
- VERB→PRON: 82 UD, 12 ROM

**Coverage Rates (Overall Balance Formula):**

- PRON→VERB Individual Coverage: 0.014
- VERB→PRON Individual Coverage: 0.146
- **Overall Balanced Coverage: 0.988**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 70.00
- Reverse ROM/UD ratio: 0.15
- Cross ratio (PRON→VERB UD)/(VERB→PRON ROM): 0.08
- Reverse cross ratio (VERB→PRON UD)/(PRON→VERB ROM): 1.17
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADJ ↔ AUX (Max Coverage Rate: 0.938)

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

- **Predicate (Verb/Proposition - Object)**: Is → famous in "The artist who painted this is famous." (
  adjective_clauses_sentences_input.txt)
- **Predicate (Verb - Object)**: was → sad in "She was very sad yesterday." (basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: Was → clear in "The sky was clear; we decided to go stargazing." (
  compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADJ→AUX: 16 UD, 0 ROM
- AUX→ADJ: 0 UD, 15 ROM

**Coverage Rates (Overall Balance Formula):**

- ADJ→AUX Individual Coverage: 0.000
- AUX→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.938**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→AUX UD)/(AUX→ADJ ROM): 1.07
- Reverse cross ratio (AUX→ADJ UD)/(ADJ→AUX ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADP ↔ NOUN (Max Coverage Rate: 0.917)

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

- **Predicate (Verb/Preposition - Object)**: of → nostalgia, of → comfort in "The emotions of nostalgia, comfort, and
  love gave her writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
- **Predicate (Preposition - Object)**: into → book in "Their encouragement pushed Sarah to consider turning the journal
  into a book." (basic_sentences_input.txt)
- **Constraint**: from → letter in "Emily received a letter from her best friend last week." (basic_sentences_input.txt)

*NOUN→ADP UD Examples:*

- **case**: memories → by in "Inspired by those cherished memories, Sarah decided to start a journal to preserve
  them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADP→NOUN: 0 UD, 24 ROM
- NOUN→ADP: 22 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- ADP→NOUN Individual Coverage: 0.000
- NOUN→ADP Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.917**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADP→NOUN UD)/(NOUN→ADP ROM): 0.00
- Reverse cross ratio (NOUN→ADP UD)/(ADP→NOUN ROM): 0.92
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### ADV ↔ VERB (Max Coverage Rate: 0.912)

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

- **Predicate (Verb/Proposition - Object)**: When → moved in "2018 was the year when I moved to Canada." (
  adjective_clauses_sentences_input.txt)
- **Constraint**: together → built in "She smiled as she read about the time they built a treehouse together." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: However → kept in "I was tired; however, I kept working." (
  compound_sentences_input.txt)

*VERB→ADV UD Examples:*

- **advmod**: moved → when in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
- **cc**: drive → rather in "He chose to walk rather than drive." (compound_sentences_input.txt)
- **mark**: complain → Rather in "Rather than complain, she took action." (compound_sentences_input.txt)

*VERB→ADV ROM Examples:*

- **Predicate (Verb/Proposition - Object)**: Stayed → home in "I stayed home because it was raining." (
  adverb_clauses_sentence_input.txt)
- **Constraint**: Stay → home in "You can either stay home or come with us." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADV→VERB: 0 UD, 28 ROM
- VERB→ADV: 34 UD, 3 ROM

**Coverage Rates (Overall Balance Formula):**

- ADV→VERB Individual Coverage: 0.000
- VERB→ADV Individual Coverage: 0.088
- **Overall Balanced Coverage: 0.912**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.09
- Cross ratio (ADV→VERB UD)/(VERB→ADV ROM): 0.00
- Reverse cross ratio (VERB→ADV UD)/(ADV→VERB ROM): 1.21
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### SCONJ ↔ VERB (Max Coverage Rate: 0.905)

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
- **Predicate (Verb - Object)**: as → read in "She smiled as she read about the time they built a treehouse together." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: Whether → call in "I don't know whether he’ll call or text." (
  compound_sentences_input.txt)

*VERB→SCONJ UD Examples:*

- **mark**: raining → because in "I stayed home because it was raining." (adverb_clauses_sentence_input.txt)

**Mathematical Overlap Analysis:**

- SCONJ→VERB: 0 UD, 21 ROM
- VERB→SCONJ: 19 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- SCONJ→VERB Individual Coverage: 0.000
- VERB→SCONJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.905**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (SCONJ→VERB UD)/(VERB→SCONJ ROM): 0.00
- Reverse cross ratio (VERB→SCONJ UD)/(SCONJ→VERB ROM): 0.90
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### CCONJ ↔ NOUN (Max Coverage Rate: 0.857)

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

- **Predicate (Verb/Preposition - Object)**: Both → brother, And → sister in "Both my brother and sister are
  engineers." (compound_sentences_input.txt)

*NOUN→CCONJ UD Examples:*

- **cc**: emotions → but in "She described not only the stories her grandmother shared, but also the emotions they
  stirred." (basic_sentences_input.txt)
- **cc:preconj**: brother → Both in "Both my brother and sister are engineers." (compound_sentences_input.txt)

*NOUN→CCONJ ROM Examples:*

- **Connection**: nostalgia → and, comfort → and in "The emotions of nostalgia, comfort, and love gave her writing a
  heartfelt tone that surprised her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- CCONJ→NOUN: 0 UD, 3 ROM
- NOUN→CCONJ: 6 UD, 4 ROM

**Coverage Rates (Overall Balance Formula):**

- CCONJ→NOUN Individual Coverage: 0.000
- NOUN→CCONJ Individual Coverage: 0.667
- **Overall Balanced Coverage: 0.857**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.67
- Cross ratio (CCONJ→NOUN UD)/(NOUN→CCONJ ROM): 0.00
- Reverse cross ratio (NOUN→CCONJ UD)/(CCONJ→NOUN ROM): 2.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### CCONJ ↔ VERB (Max Coverage Rate: 0.818)

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
- **Connect**: and → stop, and → slow in "Driver needs to stop and slow down a vehicle effectively and efficiently." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: But → started in "She wanted to go for a walk, but it started raining." (
  compound_sentences_input.txt)

*VERB→CCONJ UD Examples:*

- **cc**: happened → But in "But it never happened." (basic_sentences_input.txt)
- **cc:preconj**: stay → either in "You can either stay home or come with us." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- CCONJ→VERB: 0 UD, 11 ROM
- VERB→CCONJ: 9 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- CCONJ→VERB Individual Coverage: 0.000
- VERB→CCONJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.818**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (CCONJ→VERB UD)/(VERB→CCONJ ROM): 0.00
- Reverse cross ratio (VERB→CCONJ UD)/(CCONJ→VERB ROM): 0.82
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### NOUN ↔ VERB (Max Coverage Rate: 0.812)

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
- **amod**: memories → cherished in "Inspired by those cherished memories, Sarah decided to start a journal to preserve
  them." (basic_sentences_input.txt)

*NOUN→VERB ROM Examples:*

- **Predicate (Subject - Verb)**: boy → sings in "The boy who sings is my friend." (
  adjective_clauses_sentences_input.txt)
- **Constraint**: week → received in "Emily received a letter from her best friend last week." (
  basic_sentences_input.txt)

*VERB→NOUN UD Examples:*

- **nsubj**: broke → car in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
- **obj**: remember → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
- **obl:agent**: Inspired → memories in "Inspired by those cherished memories, Sarah decided to start a journal to
  preserve them." (basic_sentences_input.txt)

*VERB→NOUN ROM Examples:*

- **Predicate (Verb/Proposition - Object)**: Remember → day in "I remember the day when we met." (
  adjective_clauses_sentences_input.txt)
- **Constraint**: met → day in "I remember the day when we met." (adjective_clauses_sentences_input.txt)
- **Predicate (Verb - Object)**: cherished → memories in "Inspired by those cherished memories, Sarah decided to start a
  journal to preserve them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- NOUN→VERB: 20 UD, 28 ROM
- VERB→NOUN: 76 UD, 50 ROM

**Coverage Rates (Overall Balance Formula):**

- NOUN→VERB Individual Coverage: 0.714
- VERB→NOUN Individual Coverage: 0.658
- **Overall Balanced Coverage: 0.812**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 1.40
- Reverse ROM/UD ratio: 0.66
- Cross ratio (NOUN→VERB UD)/(VERB→NOUN ROM): 0.40
- Reverse cross ratio (VERB→NOUN UD)/(NOUN→VERB ROM): 2.71
- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**
- **Coverage Assessment: 🟢 Excellent coverage**

---

### PART ↔ VERB (Max Coverage Rate: 0.773)

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

- **Constraint**: to → decided, to → decided in "Inspired by those cherished memories, Sarah decided to start a journal
  to preserve them." (basic_sentences_input.txt)
- **Predicate (Preposition - Object)**: to → preserve, to → start in "Inspired by those cherished memories, Sarah
  decided to start a journal to preserve them." (basic_sentences_input.txt)
- **Predicate (Verb/Proposition - Object)**: To → manage in "Design a web system to manage the editorial workflow of the
  JIDPS journal." (basic_sentences_input.txt)

*VERB→PART UD Examples:*

- **advmod**: know → n’t in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
- **mark**: start → to, preserve → to in "Inspired by those cherished memories, Sarah decided to start a journal to
  preserve them." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- PART→VERB: 0 UD, 22 ROM
- VERB→PART: 17 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- PART→VERB Individual Coverage: 0.000
- VERB→PART Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.773**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (PART→VERB UD)/(VERB→PART ROM): 0.00
- Reverse cross ratio (VERB→PART UD)/(PART→VERB ROM): 0.77
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### NOUN ↔ PRON (Max Coverage Rate: 0.733)

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

- **Connection**: tone → that in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that
  surprised her." (basic_sentences_input.txt)
- **Constraint**: story → her in "Nobody told her the full story." (basic_sentences_input.txt)

*PRON→NOUN ROM Examples:*

- **Connection**: Who → boy in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
- **Constraint**: My → friend in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
- **Predicate (Subject - Verb)**: He → text in "I don't know whether he’ll call or text." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- NOUN→PRON: 22 UD, 4 ROM
- PRON→NOUN: 0 UD, 26 ROM

**Coverage Rates (Overall Balance Formula):**

- NOUN→PRON Individual Coverage: 0.182
- PRON→NOUN Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.733**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.18
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→PRON UD)/(PRON→NOUN ROM): 0.85
- Reverse cross ratio (PRON→NOUN UD)/(NOUN→PRON ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### AUX ↔ VERB (Max Coverage Rate: 0.677)

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

- **Predicate (Verb/Proposition - Object)**: Was → raining in "I stayed home because it was raining." (
  adverb_clauses_sentence_input.txt)
- **Constraint (Auxiliary - Main Verb)**: would → return in "She waited by the window, hoping you would return." (
  basic_sentences_input.txt)
- **Constraint**: Can → fly in "Design a vacation house that can fly easily from one location to another." (
  basic_sentences_input.txt)

*VERB→AUX UD Examples:*

- **aux**: know → do in "I don’t know the reason why he left." (adjective_clauses_sentences_input.txt)
- **aux:pass**: filled → was in "The letter was filled with stories about their childhood adventures." (
  basic_sentences_input.txt)
- **cop**: left → is in "The truth is that she never left." (noun_clauses_sentences_input.txt)

*VERB→AUX ROM Examples:*

- **Predicate (Subject - Verb)**: lied → was in "That he lied was obvious." (noun_clauses_sentences_input.txt)
- **Predicate (Verb/Proposition - Object)**: Know → is in "I know that she is right." (noun_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**

- AUX→VERB: 0 UD, 19 ROM
- VERB→AUX: 31 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- AUX→VERB Individual Coverage: 0.000
- VERB→AUX Individual Coverage: 0.065
- **Overall Balanced Coverage: 0.677**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.06
- Cross ratio (AUX→VERB UD)/(VERB→AUX ROM): 0.00
- Reverse cross ratio (VERB→AUX UD)/(AUX→VERB ROM): 1.63
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### ADJ ↔ SCONJ (Max Coverage Rate: 0.667)

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

- **Predicate (Verb/Preposition - Object)**: As → easy in "This task is not as easy as it looks." (
  compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADJ→SCONJ: 3 UD, 0 ROM
- SCONJ→ADJ: 0 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- ADJ→SCONJ Individual Coverage: 0.000
- SCONJ→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.667**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→SCONJ UD)/(SCONJ→ADJ ROM): 1.50
- Reverse cross ratio (SCONJ→ADJ UD)/(ADJ→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### ADV → ADV (Max Coverage Rate: 0.667)

#### ADV → ADV

**UD Relations:**

- advmod (2 occurrences)
- conj (1 occurrences)

**ROM Relations:**

- Constraint (2 occurrences)

**Examples:**
*ADV→ADV UD Examples:*

- **conj**: effectively → efficiently in "Driver needs to stop and slow down a vehicle effectively and efficiently." (
  basic_sentences_input.txt)
- **advmod**: quickly → as in "He ran as quickly as a professional athlete." (compound_sentences_input.txt)

*ADV→ADV ROM Examples:*

- **Constraint**: Just → so in "Just as honesty builds trust, so does kindness." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADV→ADV: 3 UD, 2 ROM

**Overlap Rates (Balanced Coverage Formula):**

- ADV→ADV Direct Coverage: 0.667
- **ADV→ADV Max Coverage: 0.667**

**Traditional Ratios (for reference):**

- ROM/UD ratio: 0.67
- Cross ratio (UD/ROM): 1.50
- **Status: Self-referential POS pair with both UD and ROM relations**
- **Coverage Assessment: 🟡 Good coverage**

---

### ADJ ↔ PART (Max Coverage Rate: 0.667)

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

**Coverage Rates (Overall Balance Formula):**

- ADJ→PART Individual Coverage: 0.000
- PART→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.667**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→PART UD)/(PART→ADJ ROM): 1.50
- Reverse cross ratio (PART→ADJ UD)/(ADJ→PART ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### ADP ↔ ADV (Max Coverage Rate: 0.667)

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

- **Predicate (Verb/Preposition - Object)**: As → quickly in "He ran as quickly as a professional athlete." (
  compound_sentences_input.txt)

*ADV→ADP UD Examples:*

- **fixed**: rather → than in "He chose to walk rather than drive." (compound_sentences_input.txt)

*ADV→ADP ROM Examples:*

- **Connection**: Rather → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADP→ADV: 0 UD, 1 ROM
- ADV→ADP: 2 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- ADP→ADV Individual Coverage: 0.000
- ADV→ADP Individual Coverage: 1.000
- **Overall Balanced Coverage: 0.667**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (ADP→ADV UD)/(ADV→ADP ROM): 0.00
- Reverse cross ratio (ADV→ADP UD)/(ADP→ADV ROM): 2.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟡 Good coverage**

---

### PROPN ↔ VERB (Max Coverage Rate: 0.571)

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

- **Predicate (Subject - Verb)**: Sarah → decided, Sarah → cherished in "Inspired by those cherished memories, Sarah
  decided to start a journal to preserve them." (basic_sentences_input.txt)

*VERB→PROPN UD Examples:*

- **obl**: moved → Canada in "2018 was the year when I moved to Canada." (adjective_clauses_sentences_input.txt)
- **nsubj**: decided → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to preserve
  them." (basic_sentences_input.txt)
- **obj**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the journal into a book." (
  basic_sentences_input.txt)

*VERB→PROPN ROM Examples:*

- **Constraint**: Inspired → Sarah in "Inspired by those cherished memories, Sarah decided to start a journal to
  preserve them." (basic_sentences_input.txt)
- **Predicate (Verb/Proposition - Object)**: pushed → Sarah in "Their encouragement pushed Sarah to consider turning the
  journal into a book." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- PROPN→VERB: 0 UD, 5 ROM
- VERB→PROPN: 4 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- PROPN→VERB Individual Coverage: 0.000
- VERB→PROPN Individual Coverage: 0.500
- **Overall Balanced Coverage: 0.571**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.50
- Cross ratio (PROPN→VERB UD)/(VERB→PROPN ROM): 0.00
- Reverse cross ratio (VERB→PROPN UD)/(PROPN→VERB ROM): 0.80
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟠 Moderate coverage**

---

### ADJ ↔ NOUN (Max Coverage Rate: 0.550)

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

- **Constraint**: heartfelt → tone in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone
  that surprised her." (basic_sentences_input.txt)

*NOUN→ADJ UD Examples:*

- **amod**: tone → heartfelt in "The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that
  surprised her." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADJ→NOUN: 8 UD, 11 ROM
- NOUN→ADJ: 12 UD, 0 ROM

**Coverage Rates (Overall Balance Formula):**

- ADJ→NOUN Individual Coverage: 0.727
- NOUN→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.550**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 1.38
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→NOUN UD)/(NOUN→ADJ ROM): 0.00
- Reverse cross ratio (NOUN→ADJ UD)/(ADJ→NOUN ROM): 1.09
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🟠 Moderate coverage**

---

### AUX ↔ NOUN (Max Coverage Rate: 0.346)

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

- **Predicate (Verb/Proposition - Object)**: Is → friend in "The boy who sings is my friend." (
  adjective_clauses_sentences_input.txt)
- **Predicate (Verb - Object)**: was → moments in "It was one of the happiest moments of her life." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: Are → engineers in "Both my brother and sister are engineers." (
  compound_sentences_input.txt)

*NOUN→AUX UD Examples:*

- **cop**: friend → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)

*NOUN→AUX ROM Examples:*

- **Predicate (Subject - Verb)**: Boy → is in "The boy who sings is my friend." (adjective_clauses_sentences_input.txt)
- **Constraint**: yesterday → was in "She was very sad yesterday." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- AUX→NOUN: 0 UD, 9 ROM
- NOUN→AUX: 9 UD, 17 ROM

**Coverage Rates (Overall Balance Formula):**

- AUX→NOUN Individual Coverage: 0.000
- NOUN→AUX Individual Coverage: 0.529
- **Overall Balanced Coverage: 0.346**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.89
- Cross ratio (AUX→NOUN UD)/(NOUN→AUX ROM): 0.00
- Reverse cross ratio (NOUN→AUX UD)/(AUX→NOUN ROM): 1.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🔴 Low coverage**

---

### VERB → VERB (Max Coverage Rate: 0.293)

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
- **xcomp**: decided → start in "Inspired by those cherished memories, Sarah decided to start a journal to preserve
  them." (basic_sentences_input.txt)
- **ccomp**: hoping → return in "She waited by the window, hoping you would return." (basic_sentences_input.txt)

*VERB→VERB ROM Examples:*

- **Predicate (Verb/Preposition - Object)**: gave → writing in "The emotions of nostalgia, comfort, and love gave her
  writing a heartfelt tone that surprised her." (basic_sentences_input.txt)
- **Predicate (Verb/Proposition - Object)**: consider → turning in "Their encouragement pushed Sarah to consider turning
  the journal into a book." (basic_sentences_input.txt)
- **Predicate (Verb - Object)**: hoping → return in "She waited by the window, hoping you would return." (
  basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- VERB→VERB: 41 UD, 12 ROM

**Overlap Rates (Balanced Coverage Formula):**

- VERB→VERB Direct Coverage: 0.293
- **VERB→VERB Max Coverage: 0.293**

**Traditional Ratios (for reference):**

- ROM/UD ratio: 0.29
- Cross ratio (UD/ROM): 3.42
- **Status: Self-referential POS pair with both UD and ROM relations**
- **Coverage Assessment: 🔴 Low coverage**

---

### NOUN ↔ SCONJ (Max Coverage Rate: 0.250)

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

**Coverage Rates (Overall Balance Formula):**

- NOUN→SCONJ Individual Coverage: 0.000
- SCONJ→NOUN Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.250**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (NOUN→SCONJ UD)/(SCONJ→NOUN ROM): 0.25
- Reverse cross ratio (SCONJ→NOUN UD)/(NOUN→SCONJ ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🔴 Low coverage**

---

### NOUN → NOUN (Max Coverage Rate: 0.240)

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
- **acl:relcl**: boy → doctor in "The boy whose father is a doctor is my classmate." (
  adjective_clauses_sentences_input.txt)
- **conj**: stories → emotions in "She described not only the stories her grandmother shared, but also the emotions they
  stirred." (basic_sentences_input.txt)

*NOUN→NOUN ROM Examples:*

- **Constraint**: sincerity → details in "Her friends who read the journal found themselves moved by its sincerity and
  vivid details." (basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- NOUN→NOUN: 25 UD, 6 ROM

**Overlap Rates (Balanced Coverage Formula):**

- NOUN→NOUN Direct Coverage: 0.240
- **NOUN→NOUN Max Coverage: 0.240**

**Traditional Ratios (for reference):**

- ROM/UD ratio: 0.24
- Cross ratio (UD/ROM): 4.17
- **Status: Self-referential POS pair with both UD and ROM relations**
- **Coverage Assessment: 🔴 Low coverage**

---

### ADJ ↔ ADV (Max Coverage Rate: 0.222)

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
- **Predicate (Verb/Preposition - Object)**: Both → smart in "She is both smart and creative." (
  compound_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADJ→ADV: 9 UD, 0 ROM
- ADV→ADJ: 0 UD, 2 ROM

**Coverage Rates (Overall Balance Formula):**

- ADJ→ADV Individual Coverage: 0.000
- ADV→ADJ Individual Coverage: 0.000
- **Overall Balanced Coverage: 0.222**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.00
- Cross ratio (ADJ→ADV UD)/(ADV→ADJ ROM): 4.50
- Reverse cross ratio (ADV→ADJ UD)/(ADJ→ADV ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🔴 Low coverage**

---

### ADP ↔ VERB (Max Coverage Rate: 0.200)

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

- **Constraint**: into → turning in "Their encouragement pushed Sarah to consider turning the journal into a book." (
  basic_sentences_input.txt)
- **Predicate (Verb/Preposition - Object)**: Than → watch in "I’d rather read a book than watch TV." (
  compound_sentences_input.txt)

*VERB→ADP UD Examples:*

- **compound:prt**: broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)
- **mark**: watch → than in "I’d rather read a book than watch TV." (compound_sentences_input.txt)

*VERB→ADP ROM Examples:*

- **Constraint**: Broke → down in "The man whose car broke down." (adjective_clauses_sentences_input.txt)

**Mathematical Overlap Analysis:**

- ADP→VERB: 0 UD, 17 ROM
- VERB→ADP: 4 UD, 3 ROM

**Coverage Rates (Overall Balance Formula):**

- ADP→VERB Individual Coverage: 0.000
- VERB→ADP Individual Coverage: 0.750
- **Overall Balanced Coverage: 0.200**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 0.75
- Cross ratio (ADP→VERB UD)/(VERB→ADP ROM): 0.00
- Reverse cross ratio (VERB→ADP UD)/(ADP→VERB ROM): 0.24
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🔴 Low coverage**

---

### NOUN ↔ NUM (Max Coverage Rate: 0.200)

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
- **nummod**: location → one in "Design a vacation house that can fly easily from one location to another." (
  basic_sentences_input.txt)

*NUM→NOUN UD Examples:*

- **nmod**: one → moments in "It was one of the happiest moments of her life." (basic_sentences_input.txt)

*NUM→NOUN ROM Examples:*

- **Constraint**: One → location in "Design a vacation house that can fly easily from one location to another." (
  basic_sentences_input.txt)

**Mathematical Overlap Analysis:**

- NOUN→NUM: 4 UD, 0 ROM
- NUM→NOUN: 1 UD, 1 ROM

**Coverage Rates (Overall Balance Formula):**

- NOUN→NUM Individual Coverage: 0.000
- NUM→NOUN Individual Coverage: 1.000
- **Overall Balanced Coverage: 0.200**

**Traditional Ratios (for reference):**

- Forward ROM/UD ratio: 0.00
- Reverse ROM/UD ratio: 1.00
- Cross ratio (NOUN→NUM UD)/(NUM→NOUN ROM): 4.00
- Reverse cross ratio (NUM→NOUN UD)/(NOUN→NUM ROM): 0.00
- **Status: Partial bidirectional coverage**
- **Coverage Assessment: 🔴 Low coverage**

---