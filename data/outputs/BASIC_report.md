# ROM Evaluation Report

**Date:** 2025-05-23 14:13:38
**Total Sentences:** 21
**Processed Sentences:** 21
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 21 |
| Total Expected Relations | 202 |
| Total Generated Relations | 197 |
| Total Correct Relations | 92 |
| Total Missing Relations | 110 |
| Total Over-specified Relations | 105 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **45.5%** |
| **Missing Rate** | **54.5%** |
| **Over-specification Rate** | **53.3%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 46.7% | Percentage of generated relations that are correct |
| Recall | 45.5% | Percentage of expected relations that were found |
| F1-Score | 46.1% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
**Input:** Inspired by those cherished memories, Sarah decided to start a journal to preserve them.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 13 | - |
| Correct Relations | 5 | 38.5% |
| Missing Relations | 8 | 61.5% |
| Over-specified Relations | 8 | 61.5% |

**✅ Correct Relations:**
- a → journal: constraint
- those → memories: constraint
- to → decided: constraint
- to → preserve: predicate (preposition - object)
- to → start: predicate (preposition - object)

**❌ Missing Relations:**
- cherished → memories: predicate (verb - object)
- inspired → sarah: constraint
- journal → preserve: predicate (subject - verb)
- memories → inspired: predicate (subject - verb)
- sarah → cherished: predicate (subject - verb)
- sarah → decided: predicate (subject - verb)
- start → journal: predicate (preposition - object)
- them → memories: connection

**➕ Over-specified Relations:**
- by → memories: predicate (preposition - object)
- decided → start: predicate (verb/proposition - object)
- inspired → decided: constraint
- inspired → memories: predicate (verb/preposition - object)
- preserve → start: constraint
- preserve → them: predicate (verb/proposition - object)
- start → journal: predicate (verb/proposition - object)
- to → start: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → journal: constraint
- cherished → memories: predicate (verb - object)
- inspired → sarah: constraint
- journal → preserve: predicate (subject - verb)
- memories → inspired: predicate (subject - verb)
- sarah → cherished: predicate (subject - verb)
- sarah → decided: predicate (subject - verb)
- start → journal: predicate (preposition - object)
- them → memories: connection
- those → memories: constraint
- to → decided: constraint
- to → preserve: predicate (preposition - object)
- to → start: predicate (preposition - object)

**Generated Relations:**
- Inspired → decided: Constraint (UD: advcl)
- Inspired → memories: Predicate (Verb/Preposition - Object) (UD: obl:agent)
- a → journal: Constraint (UD: det)
- by → memories: Predicate (Preposition - Object) (UD: case)
- decided → start: Predicate (Verb/Proposition - Object) (UD: xcomp)
- preserve → start: Constraint (UD: advcl)
- preserve → them: Predicate (Verb/Proposition - Object) (UD: obj)
- start → journal: Predicate (Verb/Proposition - Object) (UD: obj)
- those → memories: Constraint (UD: det)
- to → decided: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → preserve: Predicate (Preposition - Object) (UD: mark)
- to → preserve: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- to → start: Predicate (Preposition - Object) (UD: mark)
- to → start: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- to → start: Constraint (UD: mark(to)→main_verb_of(advcl))

</details>

---

### Sentence 2
**Input:** She described not only the stories her grandmother shared, but also the emotions they stirred.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 14 | - |
| Generated Relations | 13 | - |
| Correct Relations | 6 | 42.9% |
| Missing Relations | 8 | 57.1% |
| Over-specified Relations | 7 | 53.8% |

**✅ Correct Relations:**
- grandmother → shared: predicate (subject - verb)
- her → grandmother: constraint
- she → described: predicate (subject - verb)
- the → emotions: constraint
- the → stories: constraint
- they → stirred: predicate (subject - verb)

**❌ Missing Relations:**
- but also → described: constraint
- but also → emotions: predicate (verb/preposition - object)
- described → emotions: predicate (verb/preposition - object)
- described → stories: predicate (verb/preposition - object)
- not only → described: constraint
- not only → stories: predicate (verb/preposition - object)
- shared → stories: predicate (verb/preposition - object)
- stirred → emotions: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- also → emotions: constraint
- but → emotions: constraint
- described → stories: predicate (verb/proposition - object)
- emotions → stories: connection
- only → stories: constraint
- shared → stories: predicate (verb/proposition - object)
- stirred → emotions: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- but also → described: constraint
- but also → emotions: predicate (verb/preposition - object)
- described → emotions: predicate (verb/preposition - object)
- described → stories: predicate (verb/preposition - object)
- grandmother → shared: predicate (subject - verb)
- her → grandmother: constraint
- not only → described: constraint
- not only → stories: predicate (verb/preposition - object)
- shared → stories: predicate (verb/preposition - object)
- she → described: predicate (subject - verb)
- stirred → emotions: predicate (verb/preposition - object)
- the → emotions: constraint
- the → stories: constraint
- they → stirred: predicate (subject - verb)

**Generated Relations:**
- She → described: Predicate (Subject - Verb) (UD: nsubj)
- also → emotions: Constraint (UD: advmod)
- but → emotions: Constraint (UD: cc)
- described → stories: Predicate (Verb/Proposition - Object) (UD: obj)
- emotions → stories: Connection (UD: conj)
- grandmother → shared: Predicate (Subject - Verb) (UD: nsubj)
- her → grandmother: Constraint (UD: nmod:poss)
- only → stories: Constraint (UD: advmod)
- shared → stories: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- stirred → emotions: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- the → emotions: Constraint (UD: det)
- the → stories: Constraint (UD: det)
- they → stirred: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 3
**Input:** The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 18 | - |
| Generated Relations | 16 | - |
| Correct Relations | 5 | 27.8% |
| Missing Relations | 13 | 72.2% |
| Over-specified Relations | 11 | 68.8% |

**✅ Correct Relations:**
- a → tone: constraint
- emotions → gave: predicate (subject - verb)
- heartfelt → tone: constraint
- that → surprised: predicate (subject - verb)
- tone → surprised: predicate (subject - verb)

**❌ Missing Relations:**
- comfort → and: connection
- gave → tone: predicate (verb/preposition - object)
- gave → writing: predicate (verb/preposition - object)
- her → writing: constraint
- love → and: connection
- nostalgia → and: connection
- of → comfort: predicate (verb/preposition - object)
- of → emotion: constraint
- of → love: predicate (verb/preposition - object)
- of → nostalgia: predicate (verb/preposition - object)
- surprised → her: predicate (verb/preposition - object)
- tone → that: connection
- writing → tone: constraint

**➕ Over-specified Relations:**
- and → love: connection
- comfort → nostalgia: connection
- gave → her: predicate (verb/proposition - object)
- gave → writing: predicate (verb/proposition - object)
- love → nostalgia: connection
- nostalgia → emotions: constraint
- of → nostalgia: predicate (preposition - object)
- surprised → her: predicate (verb/proposition - object)
- that → tone: connection
- the → emotions: constraint
- writing → tone: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → tone: constraint
- comfort → and: connection
- emotions → gave: predicate (subject - verb)
- gave → tone: predicate (verb/preposition - object)
- gave → writing: predicate (verb/preposition - object)
- heartfelt → tone: constraint
- her → writing: constraint
- love → and: connection
- nostalgia → and: connection
- of → comfort: predicate (verb/preposition - object)
- of → emotion: constraint
- of → love: predicate (verb/preposition - object)
- of → nostalgia: predicate (verb/preposition - object)
- surprised → her: predicate (verb/preposition - object)
- that → surprised: predicate (subject - verb)
- tone → surprised: predicate (subject - verb)
- tone → that: connection
- writing → tone: constraint

**Generated Relations:**
- The → emotions: Constraint (UD: det)
- a → tone: Constraint (UD: det)
- and → love: Connection (UD: cc)
- comfort → nostalgia: Connection (UD: conj)
- emotions → gave: Predicate (Subject - Verb) (UD: nsubj)
- gave → her: Predicate (Verb/Proposition - Object) (UD: obj)
- gave → writing: Predicate (Verb/Proposition - Object) (UD: xcomp)
- heartfelt → tone: Constraint (UD: amod)
- love → nostalgia: Connection (UD: conj)
- nostalgia → emotions: Constraint (UD: nmod)
- of → nostalgia: Predicate (Preposition - Object) (UD: case)
- surprised → her: Predicate (Verb/Proposition - Object) (UD: obj)
- that → surprised: Predicate (Subject - Verb) (UD: nsubj)
- that → tone: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- tone → surprised: Predicate (Subject - Verb) (UD: antecedent→relcl_verb(acl:relcl))
- writing → tone: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---

### Sentence 4
**Input:** Her friends who read the journal found themselves moved by its sincerity and vivid details.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 16 | - |
| Generated Relations | 15 | - |
| Correct Relations | 6 | 37.5% |
| Missing Relations | 10 | 62.5% |
| Over-specified Relations | 9 | 60.0% |

**✅ Correct Relations:**
- friends → found: predicate (subject - verb)
- friends → read: predicate (subject - verb)
- her → friends: constraint
- the → journal: constraint
- vivid → details: constraint
- who → read: predicate (subject - verb)

**❌ Missing Relations:**
- and → vivid: connection
- details → moved: predicate (subject - verb)
- found → themselves: predicate (verb - object)
- friends → who: connection
- its → details: constraint
- its → journal: connection
- moved → friends: predicate (verb - object)
- read → journal: predicate (verb - object)
- sincerity → and: connection
- sincerity → details: constraint

**➕ Over-specified Relations:**
- and → details: connection
- by → sincerity: predicate (preposition - object)
- details → sincerity: connection
- found → moved: predicate (verb/proposition - object)
- found → themselves: predicate (verb/proposition - object)
- its → sincerity: constraint
- moved → sincerity: predicate (verb/preposition - object)
- read → journal: predicate (verb/proposition - object)
- who → friends: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- and → vivid: connection
- details → moved: predicate (subject - verb)
- found → themselves: predicate (verb - object)
- friends → found: predicate (subject - verb)
- friends → read: predicate (subject - verb)
- friends → who: connection
- her → friends: constraint
- its → details: constraint
- its → journal: connection
- moved → friends: predicate (verb - object)
- read → journal: predicate (verb - object)
- sincerity → and: connection
- sincerity → details: constraint
- the → journal: constraint
- vivid → details: constraint
- who → read: predicate (subject - verb)

**Generated Relations:**
- Her → friends: Constraint (UD: nmod:poss)
- and → details: Connection (UD: cc)
- by → sincerity: Predicate (Preposition - Object) (UD: case)
- details → sincerity: Connection (UD: conj)
- found → moved: Predicate (Verb/Proposition - Object) (UD: xcomp)
- found → themselves: Predicate (Verb/Proposition - Object) (UD: obj)
- friends → found: Predicate (Subject - Verb) (UD: nsubj)
- friends → read: Predicate (Subject - Verb) (UD: antecedent→relcl_verb(acl:relcl))
- its → sincerity: Constraint (UD: nmod:poss)
- moved → sincerity: Predicate (Verb/Preposition - Object) (UD: obl:agent)
- read → journal: Predicate (Verb/Proposition - Object) (UD: obj)
- the → journal: Constraint (UD: det)
- vivid → details: Constraint (UD: amod)
- who → friends: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → read: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 5
**Input:** Their encouragement pushed Sarah to consider turning the journal into a book.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 11 | - |
| Correct Relations | 7 | 63.6% |
| Missing Relations | 4 | 36.4% |
| Over-specified Relations | 4 | 36.4% |

**✅ Correct Relations:**
- a → book: constraint
- consider → turning: predicate (verb/proposition - object)
- encouragement → pushed: predicate (subject - verb)
- into → book: predicate (preposition - object)
- the → journal: constraint
- their → encouragement: constraint
- turning → journal: predicate (verb/proposition - object)

**❌ Missing Relations:**
- into → turning: constraint
- pushed → sarah: predicate (verb/proposition - object)
- sarah → consider: predicate (subject - verb)
- sarah → turning: predicate (subject - verb)

**➕ Over-specified Relations:**
- consider → pushed: constraint
- to → consider: predicate (preposition - object)
- to → pushed: constraint
- turning → book: predicate (verb/preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → book: constraint
- consider → turning: predicate (verb/proposition - object)
- encouragement → pushed: predicate (subject - verb)
- into → book: predicate (preposition - object)
- into → turning: constraint
- pushed → sarah: predicate (verb/proposition - object)
- sarah → consider: predicate (subject - verb)
- sarah → turning: predicate (subject - verb)
- the → journal: constraint
- their → encouragement: constraint
- turning → journal: predicate (verb/proposition - object)

**Generated Relations:**
- Their → encouragement: Constraint (UD: nmod:poss)
- a → book: Constraint (UD: det)
- consider → pushed: Constraint (UD: advcl)
- consider → turning: Predicate (Verb/Proposition - Object) (UD: xcomp)
- encouragement → pushed: Predicate (Subject - Verb) (UD: nsubj)
- into → book: Predicate (Preposition - Object) (UD: case)
- the → journal: Constraint (UD: det)
- to → consider: Predicate (Preposition - Object) (UD: mark)
- to → consider: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- to → pushed: Constraint (UD: mark(to)→main_verb_of(advcl))
- turning → book: Predicate (Verb/Preposition - Object) (UD: obl)
- turning → journal: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---

### Sentence 6
**Input:** Emily received a letter from her best friend last week.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 8 | - |
| Correct Relations | 2 | 28.6% |
| Missing Relations | 5 | 71.4% |
| Over-specified Relations | 6 | 75.0% |

**✅ Correct Relations:**
- from → friend: predicate (preposition - object)
- last → week: constraint

**❌ Missing Relations:**
- emily → received: predicate (subject - verb)
- from → letter: constraint
- from → received: constraint
- received → letter: predicate (verb - object)
- week → received: constraint

**➕ Over-specified Relations:**
- a → letter: constraint
- best → friend: constraint
- friend → letter: constraint
- her → friend: constraint
- received → letter: predicate (verb/proposition - object)
- received → week: predicate (verb/preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- emily → received: predicate (subject - verb)
- from → friend: predicate (preposition - object)
- from → letter: constraint
- from → received: constraint
- last → week: constraint
- received → letter: predicate (verb - object)
- week → received: constraint

**Generated Relations:**
- a → letter: Constraint (UD: det)
- best → friend: Constraint (UD: amod)
- friend → letter: Constraint (UD: nmod)
- from → friend: Predicate (Preposition - Object) (UD: case)
- her → friend: Constraint (UD: nmod:poss)
- last → week: Constraint (UD: amod)
- received → letter: Predicate (Verb/Proposition - Object) (UD: obj)
- received → week: Predicate (Verb/Preposition - Object) (UD: obl:unmarked)

</details>

---

### Sentence 7
**Input:** The letter was filled with stories about their childhood adventures.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 9 | - |
| Correct Relations | 1 | 12.5% |
| Missing Relations | 7 | 87.5% |
| Over-specified Relations | 8 | 88.9% |

**✅ Correct Relations:**
- the → letter: constraint

**❌ Missing Relations:**
- about → adventures: predicate (verb/preposition - object)
- about → stories: constraint
- childhood → adventures: constraint
- stories → filled: predicate (subject - verb)
- their → childhood: constraint
- with → filled: constraint
- with → letter: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- about → adventures: predicate (preposition - object)
- adventures → childhood: constraint
- adventures → stories: constraint
- filled → stories: predicate (verb/preposition - object)
- letter → filled: predicate (subject - verb)
- their → adventures: constraint
- was → filled: constraint
- with → stories: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- about → adventures: predicate (verb/preposition - object)
- about → stories: constraint
- childhood → adventures: constraint
- stories → filled: predicate (subject - verb)
- the → letter: constraint
- their → childhood: constraint
- with → filled: constraint
- with → letter: predicate (verb/preposition - object)

**Generated Relations:**
- The → letter: Constraint (UD: det)
- about → adventures: Predicate (Preposition - Object) (UD: case)
- adventures → childhood: Constraint (UD: compound)
- adventures → stories: Constraint (UD: nmod)
- filled → stories: Predicate (Verb/Preposition - Object) (UD: obl)
- letter → filled: Predicate (Subject - Verb) (UD: nsubj:pass)
- their → adventures: Constraint (UD: nmod:poss)
- was → filled: Constraint (UD: aux:pass)
- with → stories: Predicate (Preposition - Object) (UD: case)

</details>

---

### Sentence 8
**Input:** She smiled as she read about the time they built a treehouse together.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 12 | - |
| Correct Relations | 7 | 58.3% |
| Missing Relations | 5 | 41.7% |
| Over-specified Relations | 5 | 41.7% |

**✅ Correct Relations:**
- about → time: predicate (preposition - object)
- as → smiled: constraint
- she → read: predicate (subject - verb)
- she → smiled: predicate (subject - verb)
- the → time: constraint
- they → built: predicate (subject - verb)
- together → built: constraint

**❌ Missing Relations:**
- a → treehouse: constraint (determiner - noun)
- about → read: constraint
- as → read: predicate (verb - object)
- built → treehouse: predicate (verb - object)
- time → built: constraint

**➕ Over-specified Relations:**
- a → treehouse: constraint
- as → read: predicate (conjunction - clause_verb)
- built → treehouse: predicate (verb/proposition - object)
- read → smiled: constraint
- read → time: predicate (verb/preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → treehouse: constraint (determiner - noun)
- about → read: constraint
- about → time: predicate (preposition - object)
- as → read: predicate (verb - object)
- as → smiled: constraint
- built → treehouse: predicate (verb - object)
- she → read: predicate (subject - verb)
- she → smiled: predicate (subject - verb)
- the → time: constraint
- they → built: predicate (subject - verb)
- time → built: constraint
- together → built: constraint

**Generated Relations:**
- She → smiled: Predicate (Subject - Verb) (UD: nsubj)
- a → treehouse: Constraint (UD: det)
- about → time: Predicate (Preposition - Object) (UD: case)
- as → read: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- as → smiled: Constraint (UD: mark→main_verb (mark))
- built → treehouse: Predicate (Verb/Proposition - Object) (UD: obj)
- read → smiled: Constraint (UD: advcl)
- read → time: Predicate (Verb/Preposition - Object) (UD: obl)
- she → read: Predicate (Subject - Verb) (UD: nsubj)
- the → time: Constraint (UD: det)
- they → built: Predicate (Subject - Verb) (UD: nsubj)
- together → built: Constraint (UD: advmod)

</details>

---

### Sentence 9
**Input:** It was one of the happiest moments of her life.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 6 | 66.7% |
| Missing Relations | 3 | 33.3% |
| Over-specified Relations | 2 | 25.0% |

**✅ Correct Relations:**
- happiest → moments: constraint
- her → life: constraint
- it → was: predicate (subject - verb)
- of → life: predicate (preposition - object)
- of → moments: predicate (preposition - object)
- the → moments: constraint

**❌ Missing Relations:**
- of → moments: constraint
- of → one: constraint
- was → moments: predicate (verb - object)

**➕ Over-specified Relations:**
- life → moments: constraint
- was → one: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- happiest → moments: constraint
- her → life: constraint
- it → was: predicate (subject - verb)
- of → life: predicate (preposition - object)
- of → moments: constraint
- of → moments: predicate (preposition - object)
- of → one: constraint
- the → moments: constraint
- was → moments: predicate (verb - object)

**Generated Relations:**
- It → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- happiest → moments: Constraint (UD: amod)
- her → life: Constraint (UD: nmod:poss)
- life → moments: Constraint (UD: nmod)
- of → life: Predicate (Preposition - Object) (UD: case)
- of → moments: Predicate (Preposition - Object) (UD: case)
- the → moments: Constraint (UD: det)
- was → one: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 10
**Input:** That memory, like many others, stayed with her even today.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 9 | - |
| Correct Relations | 4 | 50.0% |
| Missing Relations | 4 | 50.0% |
| Over-specified Relations | 5 | 55.6% |

**✅ Correct Relations:**
- even → today: constraint
- many → others: constraint
- memory → stayed: predicate (subject - verb)
- that → memory: constraint

**❌ Missing Relations:**
- like → memory: constraint
- like → others: predicate (verb/proposition - object)
- with → her: predicate (verb/proposition - object)
- with → stayed: constraint

**➕ Over-specified Relations:**
- like → others: predicate (preposition - object)
- others → memory: constraint
- stayed → her: predicate (verb/preposition - object)
- stayed → today: predicate (verb/preposition - object)
- with → her: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- even → today: constraint
- like → memory: constraint
- like → others: predicate (verb/proposition - object)
- many → others: constraint
- memory → stayed: predicate (subject - verb)
- that → memory: constraint
- with → her: predicate (verb/proposition - object)
- with → stayed: constraint

**Generated Relations:**
- That → memory: Constraint (UD: det)
- even → today: Constraint (UD: advmod)
- like → others: Predicate (Preposition - Object) (UD: case)
- many → others: Constraint (UD: amod)
- memory → stayed: Predicate (Subject - Verb) (UD: nsubj)
- others → memory: Constraint (UD: nmod)
- stayed → her: Predicate (Verb/Preposition - Object) (UD: obl)
- stayed → today: Predicate (Verb/Preposition - Object) (UD: obl:unmarked)
- with → her: Predicate (Preposition - Object) (UD: case)

</details>

---

### Sentence 11
**Input:** She was very sad yesterday.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 4 | - |
| Generated Relations | 3 | - |
| Correct Relations | 2 | 50.0% |
| Missing Relations | 2 | 50.0% |
| Over-specified Relations | 1 | 33.3% |

**✅ Correct Relations:**
- she → was: predicate (subject - verb)
- very → sad: constraint

**❌ Missing Relations:**
- was → sad: predicate (verb - object)
- yesterday → was: constraint

**➕ Over-specified Relations:**
- was → sad: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- she → was: predicate (subject - verb)
- very → sad: constraint
- was → sad: predicate (verb - object)
- yesterday → was: constraint

**Generated Relations:**
- She → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- very → sad: Constraint (UD: advmod)
- was → sad: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 12
**Input:** It is a lie that you love her.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 7 | - |
| Correct Relations | 6 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 1 | 14.3% |

**✅ Correct Relations:**
- a → lie: constraint
- is → lie: predicate (verb/proposition - object)
- it → is: predicate (subject - verb)
- love → her: predicate (verb/proposition - object)
- that → lie: connection
- you → love: predicate (subject - verb)

**➕ Over-specified Relations:**
- love → that: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → lie: constraint
- is → lie: predicate (verb/proposition - object)
- it → is: predicate (subject - verb)
- love → her: predicate (verb/proposition - object)
- that → lie: connection
- you → love: predicate (subject - verb)

**Generated Relations:**
- It → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- a → lie: Constraint (UD: det)
- is → lie: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- love → her: Predicate (Verb/Proposition - Object) (UD: obj)
- love → that: Predicate (Verb/Proposition - Object) (UD: obj)
- love → that: Predicate (Verb/Proposition - Object) (UD: relcl_verb→obj_pronoun(acl:relcl))
- that → lie: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- you → love: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 13
**Input:** That truth broke her heart again.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 5 | - |
| Generated Relations | 5 | - |
| Correct Relations | 5 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 0 | 0.0% |

**✅ Correct Relations:**
- again → broke: constraint
- broke → heart: predicate (verb/proposition - object)
- her → heart: constraint
- that → truth: constraint
- truth → broke: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- again → broke: constraint
- broke → heart: predicate (verb/proposition - object)
- her → heart: constraint
- that → truth: constraint
- truth → broke: predicate (subject - verb)

**Generated Relations:**
- That → truth: Constraint (UD: det)
- again → broke: Constraint (UD: advmod)
- broke → heart: Predicate (Verb/Proposition - Object) (UD: obj)
- her → heart: Constraint (UD: nmod:poss)
- truth → broke: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 14
**Input:** Nobody told her the full story.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 5 | - |
| Correct Relations | 3 | 50.0% |
| Missing Relations | 3 | 50.0% |
| Over-specified Relations | 2 | 40.0% |

**✅ Correct Relations:**
- full → story: constraint
- nobody → told: predicate (subject - verb)
- the → story: constraint

**❌ Missing Relations:**
- story → her: constraint
- told → her: predicate (verb - object)
- told → story: predicate (verb - object)

**➕ Over-specified Relations:**
- told → her: predicate (verb/proposition - object)
- told → story: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- full → story: constraint
- nobody → told: predicate (subject - verb)
- story → her: constraint
- the → story: constraint
- told → her: predicate (verb - object)
- told → story: predicate (verb - object)

**Generated Relations:**
- Nobody → told: Predicate (Subject - Verb) (UD: nsubj)
- full → story: Constraint (UD: amod)
- the → story: Constraint (UD: det)
- told → her: Predicate (Verb/Proposition - Object) (UD: iobj)
- told → story: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---

### Sentence 15
**Input:** She waited by the window, hoping you would return.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 5 | 55.6% |
| Missing Relations | 4 | 44.4% |
| Over-specified Relations | 3 | 37.5% |

**✅ Correct Relations:**
- by → window: predicate (preposition - object)
- hoping → waited: constraint
- she → waited: predicate (subject - verb)
- the → window: constraint
- you → return: predicate (subject - verb)

**❌ Missing Relations:**
- by → waited: constraint
- hoping → return: predicate (verb - object)
- she → hoping: predicate (subject - verb)
- would → return: constraint (auxiliary - main verb)

**➕ Over-specified Relations:**
- hoping → return: predicate (verb/proposition - object)
- waited → window: predicate (verb/preposition - object)
- would → return: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- by → waited: constraint
- by → window: predicate (preposition - object)
- hoping → return: predicate (verb - object)
- hoping → waited: constraint
- she → hoping: predicate (subject - verb)
- she → waited: predicate (subject - verb)
- the → window: constraint
- would → return: constraint (auxiliary - main verb)
- you → return: predicate (subject - verb)

**Generated Relations:**
- She → waited: Predicate (Subject - Verb) (UD: nsubj)
- by → window: Predicate (Preposition - Object) (UD: case)
- hoping → return: Predicate (Verb/Proposition - Object) (UD: ccomp)
- hoping → waited: Constraint (UD: advcl)
- the → window: Constraint (UD: det)
- waited → window: Predicate (Verb/Preposition - Object) (UD: obl)
- would → return: Constraint (UD: aux)
- you → return: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 16
**Input:** But it never happened.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 3 | - |
| Generated Relations | 3 | - |
| Correct Relations | 3 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 0 | 0.0% |

**✅ Correct Relations:**
- but → happened: constraint
- it → happened: predicate (subject - verb)
- never → happened: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- but → happened: constraint
- it → happened: predicate (subject - verb)
- never → happened: constraint

**Generated Relations:**
- But → happened: Constraint (UD: cc)
- it → happened: Predicate (Subject - Verb) (UD: nsubj)
- never → happened: Constraint (UD: advmod)

</details>

---

### Sentence 17
**Input:** The pain, like before, settled deep within her.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 7 | - |
| Correct Relations | 3 | 42.9% |
| Missing Relations | 4 | 57.1% |
| Over-specified Relations | 4 | 57.1% |

**✅ Correct Relations:**
- deep → settled: constraint
- pain → settled: predicate (subject - verb)
- the → pain: constraint

**❌ Missing Relations:**
- like → before: predicate (prep - object)
- like → pain: constraint
- within → her: predicate (prep - object)
- within → settled: constraint

**➕ Over-specified Relations:**
- before → settled: constraint
- like → before: connection
- settled → her: predicate (verb/preposition - object)
- within → her: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- deep → settled: constraint
- like → before: predicate (prep - object)
- like → pain: constraint
- pain → settled: predicate (subject - verb)
- the → pain: constraint
- within → her: predicate (prep - object)
- within → settled: constraint

**Generated Relations:**
- The → pain: Constraint (UD: det)
- before → settled: Constraint (UD: advmod)
- deep → settled: Constraint (UD: advmod)
- like → before: Connection (UD: discourse)
- pain → settled: Predicate (Subject - Verb) (UD: nsubj)
- settled → her: Predicate (Verb/Preposition - Object) (UD: obl)
- within → her: Predicate (Preposition - Object) (UD: case)

</details>

---

### Sentence 18
**Input:** Design a vacation house that can fly easily from one location to another.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 11 | - |
| Correct Relations | 4 | 30.8% |
| Missing Relations | 9 | 69.2% |
| Over-specified Relations | 7 | 63.6% |

**✅ Correct Relations:**
- a → house: constraint
- can → fly: constraint
- one → location: constraint
- that → fly: predicate (subject - verb)

**❌ Missing Relations:**
- another → location: constraint
- design → house: predicate (verb/preposition - object)
- from → fly: constraint
- from → location: predicate (verb/preposition - object)
- from → to: connection
- house → that: connection
- to → fly: constraint
- to → location: predicate (verb/preposition - object)
- vacation → house: constraint

**➕ Over-specified Relations:**
- design → house: predicate (verb/proposition - object)
- easily → fly: constraint
- fly → location: predicate (verb/preposition - object)
- from → location: predicate (preposition - object)
- house → fly: predicate (subject - verb)
- house → vacation: constraint
- that → house: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → house: constraint
- another → location: constraint
- can → fly: constraint
- design → house: predicate (verb/preposition - object)
- from → fly: constraint
- from → location: predicate (verb/preposition - object)
- from → to: connection
- house → that: connection
- one → location: constraint
- that → fly: predicate (subject - verb)
- to → fly: constraint
- to → location: predicate (verb/preposition - object)
- vacation → house: constraint

**Generated Relations:**
- Design → house: Predicate (Verb/Proposition - Object) (UD: obj)
- a → house: Constraint (UD: det)
- can → fly: Constraint (UD: aux)
- easily → fly: Constraint (UD: advmod)
- fly → location: Predicate (Verb/Preposition - Object) (UD: obl)
- from → location: Predicate (Preposition - Object) (UD: case)
- house → fly: Predicate (Subject - Verb) (UD: antecedent→relcl_verb(acl:relcl))
- house → vacation: Constraint (UD: compound)
- one → location: Constraint (UD: nummod)
- that → fly: Predicate (Subject - Verb) (UD: nsubj)
- that → house: Connection (UD: rel_pronoun→antecedent(acl:relcl))

</details>

---

### Sentence 19
**Input:** Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 9 | - |
| Correct Relations | 0 | 0.0% |
| Missing Relations | 7 | 100.0% |
| Over-specified Relations | 9 | 100.0% |

**❌ Missing Relations:**
- 10 mw → turbine_2: constraint
- 5 mw → turbine_1: constraint
- to → turbine_2: predicate (verb/preposition - object)
- to → upscale: constraint
- upscale → turbine: predicate (verb/preposition - object)
- wind → turbine_1: constraint
- wind → turbine_2: constraint

**➕ Over-specified Relations:**
- 10 → mw: constraint
- 5 → mw: constraint
- to → turbine_2: predicate (preposition - object)
- turbine_1 → mw: constraint
- turbine_1 → wind: constraint
- turbine_2 → mw: constraint
- turbine_2 → turbine_1: constraint
- turbine_2 → wind: constraint
- upscale → turbine_1: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- 10 mw → turbine_2: constraint
- 5 mw → turbine_1: constraint
- to → turbine_2: predicate (verb/preposition - object)
- to → upscale: constraint
- upscale → turbine: predicate (verb/preposition - object)
- wind → turbine_1: constraint
- wind → turbine_2: constraint

**Generated Relations:**
- 10 → MW: Constraint (UD: nummod)
- 5 → MW: Constraint (UD: nummod)
- Upscale → turbine_1: Constraint (UD: amod)
- to → turbine_2: Predicate (Preposition - Object) (UD: case)
- turbine_1 → MW: Constraint (UD: compound)
- turbine_1 → wind: Constraint (UD: compound)
- turbine_2 → MW: Constraint (UD: compound)
- turbine_2 → turbine_1: Constraint (UD: nmod)
- turbine_2 → wind: Constraint (UD: compound)

</details>

---

### Sentence 20
**Input:** Design a web system to manage the editorial workflow of the JIDPS journal.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 13 | - |
| Correct Relations | 7 | 58.3% |
| Missing Relations | 5 | 41.7% |
| Over-specified Relations | 6 | 46.2% |

**✅ Correct Relations:**
- a → system: constraint
- design → system: predicate (verb/proposition - object)
- editorial → workflow: constraint
- manage → workflow: predicate (verb/proposition - object)
- the → journal: constraint
- the → workflow: constraint
- to → design: constraint

**❌ Missing Relations:**
- jidps → journal: constraint
- of → journal: predicate (verb/proposition - object)
- of → workflow: constraint
- to → manage: predicate (verb/proposition - object)
- web → system: constraint

**➕ Over-specified Relations:**
- journal → jidps: constraint
- journal → workflow: constraint
- manage → design: constraint
- of → journal: predicate (preposition - object)
- system → web: constraint
- to → manage: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → system: constraint
- design → system: predicate (verb/proposition - object)
- editorial → workflow: constraint
- jidps → journal: constraint
- manage → workflow: predicate (verb/proposition - object)
- of → journal: predicate (verb/proposition - object)
- of → workflow: constraint
- the → journal: constraint
- the → workflow: constraint
- to → design: constraint
- to → manage: predicate (verb/proposition - object)
- web → system: constraint

**Generated Relations:**
- Design → system: Predicate (Verb/Proposition - Object) (UD: obj)
- a → system: Constraint (UD: det)
- editorial → workflow: Constraint (UD: amod)
- journal → JIDPS: Constraint (UD: compound)
- journal → workflow: Constraint (UD: nmod)
- manage → Design: Constraint (UD: advcl)
- manage → workflow: Predicate (Verb/Proposition - Object) (UD: obj)
- of → journal: Predicate (Preposition - Object) (UD: case)
- system → web: Constraint (UD: compound)
- the → journal: Constraint (UD: det)
- the → workflow: Constraint (UD: det)
- to → Design: Constraint (UD: mark(to)→main_verb_of(advcl))
- to → manage: Predicate (Preposition - Object) (UD: mark)
- to → manage: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)

</details>

---

### Sentence 21
**Input:** Driver needs to stop and slow down a vehicle effectively and efficiently.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 14 | - |
| Generated Relations | 12 | - |
| Correct Relations | 5 | 35.7% |
| Missing Relations | 9 | 64.3% |
| Over-specified Relations | 7 | 58.3% |

**✅ Correct Relations:**
- a → vehicle: constraint
- driver → needs: predicate (subject - verb)
- effectively → slow: constraint
- slow → vehicle: predicate (verb/proposition - object)
- to → needs: constraint

**❌ Missing Relations:**
- and → slow: connect
- and → stop: connect
- down → slow: constraint
- effectively → stop: constraint
- efficiently → slow: constraint
- efficiently → stop: constraint
- stop → vehicle: predicate (verb/proposition - object)
- to → slow: predicate (verb/proposition - object)
- to → stop: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- and → efficiently: connection
- and → slow: connection
- efficiently → effectively: connection
- needs → stop: predicate (verb/proposition - object)
- slow → down: constraint
- slow → stop: connection
- to → stop: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → vehicle: constraint
- and → slow: connect
- and → stop: connect
- down → slow: constraint
- driver → needs: predicate (subject - verb)
- effectively → slow: constraint
- effectively → stop: constraint
- efficiently → slow: constraint
- efficiently → stop: constraint
- slow → vehicle: predicate (verb/proposition - object)
- stop → vehicle: predicate (verb/proposition - object)
- to → needs: constraint
- to → slow: predicate (verb/proposition - object)
- to → stop: predicate (verb/proposition - object)

**Generated Relations:**
- Driver → needs: Predicate (Subject - Verb) (UD: nsubj)
- a → vehicle: Constraint (UD: det)
- and → efficiently: Connection (UD: cc)
- and → slow: Connection (UD: cc)
- effectively → slow: Constraint (UD: advmod)
- efficiently → effectively: Connection (UD: conj)
- needs → stop: Predicate (Verb/Proposition - Object) (UD: xcomp)
- slow → down: Constraint (UD: compound:prt)
- slow → stop: Connection (UD: conj)
- slow → vehicle: Predicate (Verb/Proposition - Object) (UD: obj)
- to → needs: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → stop: Predicate (Preposition - Object) (UD: mark)
- to → stop: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)

</details>

---
