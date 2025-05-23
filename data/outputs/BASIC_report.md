# ROM Evaluation Report

**Date:** 2025-05-22 22:44:05
**Total Sentences:** 21
**Processed Sentences:** 21
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 21 |
| Total Expected Relations | 202 |
| Total Generated Relations | 208 |
| Total Correct Relations | 92 |
| Total Missing Relations | 110 |
| Total Over-specified Relations | 116 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **45.5%** |
| **Missing Rate** | **54.5%** |
| **Over-specification Rate** | **55.8%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 44.2% | Percentage of generated relations that are correct |
| Recall | 45.5% | Percentage of expected relations that were found |
| F1-Score | 44.9% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
**Input:** Inspired by those cherished memories, Sarah decided to start a journal to preserve them.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 16 | - |
| Correct Relations | 6 | 46.2% |
| Missing Relations | 7 | 53.8% |
| Over-specified Relations | 10 | 62.5% |

**✅ Correct Relations:**
- a → journal: constraint
- sarah → decided: predicate (subject - verb)
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
- start → journal: predicate (preposition - object)
- them → memories: connection

**➕ Over-specified Relations:**
- by → memories: predicate (preposition - object)
- cherished → memories: constraint
- decided → start: predicate (verb/proposition - object)
- inspired → decided: constraint
- inspired → memories: predicate (verb - oblique)
- preserve → start: constraint
- preserve → them: predicate (verb/proposition - object)
- start → journal: predicate (verb/proposition - object)
- to → preserve: predicate (conjunction - clause_verb)
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
- Inspired → memories: Predicate (verb - oblique) (UD: obl:agent)
- Sarah → decided: Predicate (subject - verb) (UD: nsubj)
- a → journal: Constraint (UD: det)
- by → memories: Predicate (preposition - object) (UD: case)
- cherished → memories: Constraint (UD: amod)
- decided → start: Predicate (verb/proposition - object) (UD: xcomp)
- preserve → start: Constraint (UD: advcl)
- preserve → them: Predicate (verb/proposition - object) (UD: obj)
- start → journal: Predicate (verb/proposition - object) (UD: obj)
- those → memories: Constraint (UD: det)
- to → decided: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → preserve: Predicate (preposition - object) (UD: mark)
- to → preserve: Predicate (conjunction - clause_verb) (UD: mark→verb_of_advcl (mark))
- to → preserve: Predicate (preposition - object) (UD: mark(to)→inf_verb)
- to → start: Predicate (preposition - object) (UD: mark)
- to → start: Constraint (UD: mark→main_verb (mark))
- to → start: Predicate (preposition - object) (UD: mark(to)→inf_verb)
- to → start: Constraint (UD: mark(to)→main_verb_of(advcl))

</details>

---

### Sentence 2
**Input:** She described not only the stories her grandmother shared, but also the emotions they stirred.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 14 | - |
| Generated Relations | 14 | - |
| Correct Relations | 6 | 42.9% |
| Missing Relations | 8 | 57.1% |
| Over-specified Relations | 8 | 57.1% |

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
- but → emotions: connection
- described → stories: predicate (verb/proposition - object)
- emotions → stirred: connection
- emotions → stories: connection
- not → stories: constraint
- only → stories: constraint
- stories → shared: connection

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
- She → described: Predicate (subject - verb) (UD: nsubj)
- also → emotions: Constraint (UD: advmod)
- but → emotions: Connection (UD: cc)
- described → stories: Predicate (verb/proposition - object) (UD: obj)
- emotions → stirred: Connection (UD: acl:relcl)
- emotions → stories: Connection (UD: conj)
- grandmother → shared: Predicate (subject - verb) (UD: nsubj)
- her → grandmother: Constraint (UD: nmod:poss)
- not → stories: Constraint (UD: advmod)
- only → stories: Constraint (UD: advmod)
- stories → shared: Connection (UD: acl:relcl)
- the → emotions: Constraint (UD: det)
- the → stories: Constraint (UD: det)
- they → stirred: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 3
**Input:** The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 18 | - |
| Generated Relations | 16 | - |
| Correct Relations | 4 | 22.2% |
| Missing Relations | 14 | 77.8% |
| Over-specified Relations | 12 | 75.0% |

**✅ Correct Relations:**
- a → tone: constraint
- emotions → gave: predicate (subject - verb)
- heartfelt → tone: constraint
- that → surprised: predicate (subject - verb)

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
- tone → surprised: predicate (subject - verb)
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
- tone → surprised: connection
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
- emotions → gave: Predicate (subject - verb) (UD: nsubj)
- gave → her: Predicate (verb/proposition - object) (UD: obj)
- gave → writing: Predicate (verb/proposition - object) (UD: xcomp)
- heartfelt → tone: Constraint (UD: amod)
- love → nostalgia: Connection (UD: conj)
- nostalgia → emotions: Constraint (UD: nmod)
- of → nostalgia: Predicate (preposition - object) (UD: case)
- surprised → her: Predicate (verb/proposition - object) (UD: obj)
- that → surprised: Predicate (subject - verb) (UD: nsubj)
- that → tone: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- tone → surprised: Connection (UD: acl:relcl)
- writing → tone: Predicate (verb/proposition - object) (UD: obj)

</details>

---

### Sentence 4
**Input:** Her friends who read the journal found themselves moved by its sincerity and vivid details.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 16 | - |
| Generated Relations | 15 | - |
| Correct Relations | 5 | 31.2% |
| Missing Relations | 11 | 68.8% |
| Over-specified Relations | 10 | 66.7% |

**✅ Correct Relations:**
- friends → found: predicate (subject - verb)
- her → friends: constraint
- the → journal: constraint
- vivid → details: constraint
- who → read: predicate (subject - verb)

**❌ Missing Relations:**
- and → vivid: connection
- details → moved: predicate (subject - verb)
- found → themselves: predicate (verb - object)
- friends → read: predicate (subject - verb)
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
- friends → read: connection
- its → sincerity: constraint
- moved → sincerity: predicate (verb - oblique)
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
- by → sincerity: Predicate (preposition - object) (UD: case)
- details → sincerity: Connection (UD: conj)
- found → moved: Predicate (verb/proposition - object) (UD: xcomp)
- found → themselves: Predicate (verb/proposition - object) (UD: obj)
- friends → found: Predicate (subject - verb) (UD: nsubj)
- friends → read: Connection (UD: acl:relcl)
- its → sincerity: Constraint (UD: nmod:poss)
- moved → sincerity: Predicate (verb - oblique) (UD: obl:agent)
- read → journal: Predicate (verb/proposition - object) (UD: obj)
- the → journal: Constraint (UD: det)
- vivid → details: Constraint (UD: amod)
- who → friends: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → read: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 5
**Input:** Their encouragement pushed Sarah to consider turning the journal into a book.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 13 | - |
| Correct Relations | 8 | 72.7% |
| Missing Relations | 3 | 27.3% |
| Over-specified Relations | 5 | 38.5% |

**✅ Correct Relations:**
- a → book: constraint
- consider → turning: predicate (verb/proposition - object)
- encouragement → pushed: predicate (subject - verb)
- into → book: predicate (preposition - object)
- pushed → sarah: predicate (verb/proposition - object)
- the → journal: constraint
- their → encouragement: constraint
- turning → journal: predicate (verb/proposition - object)

**❌ Missing Relations:**
- into → turning: constraint
- sarah → consider: predicate (subject - verb)
- sarah → turning: predicate (subject - verb)

**➕ Over-specified Relations:**
- consider → pushed: constraint
- to → consider: predicate (conjunction - clause_verb)
- to → consider: predicate (preposition - object)
- to → pushed: constraint
- turning → book: predicate (verb - oblique)

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
- consider → turning: Predicate (verb/proposition - object) (UD: xcomp)
- encouragement → pushed: Predicate (subject - verb) (UD: nsubj)
- into → book: Predicate (preposition - object) (UD: case)
- pushed → Sarah: Predicate (verb/proposition - object) (UD: obj)
- the → journal: Constraint (UD: det)
- to → consider: Predicate (preposition - object) (UD: mark)
- to → consider: Predicate (conjunction - clause_verb) (UD: mark→verb_of_advcl (mark))
- to → consider: Predicate (preposition - object) (UD: mark(to)→inf_verb)
- to → pushed: Constraint (UD: mark→main_verb (mark))
- to → pushed: Constraint (UD: mark(to)→main_verb_of(advcl))
- turning → book: Predicate (verb - oblique) (UD: obl)
- turning → journal: Predicate (verb/proposition - object) (UD: obj)

</details>

---

### Sentence 6
**Input:** Emily received a letter from her best friend last week.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 8 | - |
| Correct Relations | 3 | 42.9% |
| Missing Relations | 4 | 57.1% |
| Over-specified Relations | 5 | 62.5% |

**✅ Correct Relations:**
- emily → received: predicate (subject - verb)
- from → friend: predicate (preposition - object)
- last → week: constraint

**❌ Missing Relations:**
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
- Emily → received: Predicate (subject - verb) (UD: nsubj)
- a → letter: Constraint (UD: det)
- best → friend: Constraint (UD: amod)
- friend → letter: Constraint (UD: nmod)
- from → friend: Predicate (preposition - object) (UD: case)
- her → friend: Constraint (UD: nmod:poss)
- last → week: Constraint (UD: amod)
- received → letter: Predicate (verb/proposition - object) (UD: obj)

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
- filled → stories: predicate (verb - oblique)
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
- about → adventures: Predicate (preposition - object) (UD: case)
- adventures → childhood: Constraint (UD: compound)
- adventures → stories: Constraint (UD: nmod)
- filled → stories: Predicate (verb - oblique) (UD: obl)
- letter → filled: Predicate (subject - verb) (UD: nsubj:pass)
- their → adventures: Constraint (UD: nmod:poss)
- was → filled: Constraint (UD: aux:pass)
- with → stories: Predicate (preposition - object) (UD: case)

</details>

---

### Sentence 8
**Input:** She smiled as she read about the time they built a treehouse together.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 13 | - |
| Correct Relations | 7 | 58.3% |
| Missing Relations | 5 | 41.7% |
| Over-specified Relations | 6 | 46.2% |

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
- read → time: predicate (verb - oblique)
- time → built: connection

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
- She → smiled: Predicate (subject - verb) (UD: nsubj)
- a → treehouse: Constraint (UD: det)
- about → time: Predicate (preposition - object) (UD: case)
- as → read: Predicate (conjunction - clause_verb) (UD: mark→verb_of_advcl (mark))
- as → smiled: Constraint (UD: mark→main_verb (mark))
- built → treehouse: Predicate (verb/proposition - object) (UD: obj)
- read → smiled: Constraint (UD: advcl)
- read → time: Predicate (verb - oblique) (UD: obl)
- she → read: Predicate (subject - verb) (UD: nsubj)
- the → time: Constraint (UD: det)
- they → built: Predicate (subject - verb) (UD: nsubj)
- time → built: Connection (UD: acl:relcl)
- together → built: Constraint (UD: advmod)

</details>

---

### Sentence 9
**Input:** It was one of the happiest moments of her life.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 9 | - |
| Correct Relations | 6 | 66.7% |
| Missing Relations | 3 | 33.3% |
| Over-specified Relations | 3 | 33.3% |

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
- moments → one: constraint
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
- It → was: Predicate (subject - verb) (UD: nsubj→cop)
- happiest → moments: Constraint (UD: amod)
- her → life: Constraint (UD: nmod:poss)
- life → moments: Constraint (UD: nmod)
- moments → one: Constraint (UD: nmod)
- of → life: Predicate (preposition - object) (UD: case)
- of → moments: Predicate (preposition - object) (UD: case)
- the → moments: Constraint (UD: det)
- was → one: Predicate (verb/proposition - object) (UD: cop→pred_complement)

</details>

---

### Sentence 10
**Input:** That memory, like many others, stayed with her even today.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 8 | - |
| Correct Relations | 4 | 50.0% |
| Missing Relations | 4 | 50.0% |
| Over-specified Relations | 4 | 50.0% |

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
- stayed → her: predicate (verb - oblique)
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
- like → others: Predicate (preposition - object) (UD: case)
- many → others: Constraint (UD: amod)
- memory → stayed: Predicate (subject - verb) (UD: nsubj)
- others → memory: Constraint (UD: nmod)
- stayed → her: Predicate (verb - oblique) (UD: obl)
- with → her: Predicate (preposition - object) (UD: case)

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
- She → was: Predicate (subject - verb) (UD: nsubj→cop)
- very → sad: Constraint (UD: advmod)
- was → sad: Predicate (verb/proposition - object) (UD: cop→pred_complement)

</details>

---

### Sentence 12
**Input:** It is a lie that you love her.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 8 | - |
| Correct Relations | 6 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 2 | 25.0% |

**✅ Correct Relations:**
- a → lie: constraint
- is → lie: predicate (verb/proposition - object)
- it → is: predicate (subject - verb)
- love → her: predicate (verb/proposition - object)
- that → lie: connection
- you → love: predicate (subject - verb)

**➕ Over-specified Relations:**
- lie → love: connection
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
- It → is: Predicate (subject - verb) (UD: nsubj→cop)
- a → lie: Constraint (UD: det)
- is → lie: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- lie → love: Connection (UD: acl:relcl)
- love → her: Predicate (verb/proposition - object) (UD: obj)
- love → that: Predicate (verb/proposition - object) (UD: obj)
- love → that: Predicate (verb/proposition - object) (UD: relcl_verb→obj_pronoun(acl:relcl))
- that → lie: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- you → love: Predicate (subject - verb) (UD: nsubj)

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
- broke → heart: Predicate (verb/proposition - object) (UD: obj)
- her → heart: Constraint (UD: nmod:poss)
- truth → broke: Predicate (subject - verb) (UD: nsubj)

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
- Nobody → told: Predicate (subject - verb) (UD: nsubj)
- full → story: Constraint (UD: amod)
- the → story: Constraint (UD: det)
- told → her: Predicate (verb/proposition - object) (UD: iobj)
- told → story: Predicate (verb/proposition - object) (UD: obj)

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
- waited → window: predicate (verb - oblique)
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
- She → waited: Predicate (subject - verb) (UD: nsubj)
- by → window: Predicate (preposition - object) (UD: case)
- hoping → return: Predicate (verb/proposition - object) (UD: ccomp)
- hoping → waited: Constraint (UD: advcl)
- the → window: Constraint (UD: det)
- waited → window: Predicate (verb - oblique) (UD: obl)
- would → return: Constraint (UD: aux)
- you → return: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 16
**Input:** But it never happened.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 3 | - |
| Generated Relations | 3 | - |
| Correct Relations | 2 | 66.7% |
| Missing Relations | 1 | 33.3% |
| Over-specified Relations | 1 | 33.3% |

**✅ Correct Relations:**
- it → happened: predicate (subject - verb)
- never → happened: constraint

**❌ Missing Relations:**
- but → happened: constraint

**➕ Over-specified Relations:**
- but → happened: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- but → happened: constraint
- it → happened: predicate (subject - verb)
- never → happened: constraint

**Generated Relations:**
- But → happened: Connection (UD: cc)
- it → happened: Predicate (subject - verb) (UD: nsubj)
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
- settled → her: predicate (verb - oblique)
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
- pain → settled: Predicate (subject - verb) (UD: nsubj)
- settled → her: Predicate (verb - oblique) (UD: obl)
- within → her: Predicate (preposition - object) (UD: case)

</details>

---

### Sentence 18
**Input:** Design a vacation house that can fly easily from one location to another.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 13 | - |
| Correct Relations | 4 | 30.8% |
| Missing Relations | 9 | 69.2% |
| Over-specified Relations | 9 | 69.2% |

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
- fly → another: predicate (verb - oblique)
- fly → location: predicate (verb - oblique)
- from → location: predicate (preposition - object)
- house → fly: connection
- house → vacation: constraint
- that → house: connection
- to → another: predicate (preposition - object)

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
- Design → house: Predicate (verb/proposition - object) (UD: obj)
- a → house: Constraint (UD: det)
- can → fly: Constraint (UD: aux)
- easily → fly: Constraint (UD: advmod)
- fly → another: Predicate (verb - oblique) (UD: obl)
- fly → location: Predicate (verb - oblique) (UD: obl)
- from → location: Predicate (preposition - object) (UD: case)
- house → fly: Connection (UD: acl:relcl)
- house → vacation: Constraint (UD: compound)
- one → location: Constraint (UD: nummod)
- that → fly: Predicate (subject - verb) (UD: nsubj)
- that → house: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- to → another: Predicate (preposition - object) (UD: case)

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
- to → turbine_2: Predicate (preposition - object) (UD: case)
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
| Generated Relations | 14 | - |
| Correct Relations | 7 | 58.3% |
| Missing Relations | 5 | 41.7% |
| Over-specified Relations | 7 | 50.0% |

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
- to → manage: predicate (conjunction - clause_verb)
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
- Design → system: Predicate (verb/proposition - object) (UD: obj)
- a → system: Constraint (UD: det)
- editorial → workflow: Constraint (UD: amod)
- journal → JIDPS: Constraint (UD: compound)
- journal → workflow: Constraint (UD: nmod)
- manage → Design: Constraint (UD: advcl)
- manage → workflow: Predicate (verb/proposition - object) (UD: obj)
- of → journal: Predicate (preposition - object) (UD: case)
- system → web: Constraint (UD: compound)
- the → journal: Constraint (UD: det)
- the → workflow: Constraint (UD: det)
- to → Design: Constraint (UD: mark→main_verb (mark))
- to → Design: Constraint (UD: mark(to)→main_verb_of(advcl))
- to → manage: Predicate (preposition - object) (UD: mark)
- to → manage: Predicate (conjunction - clause_verb) (UD: mark→verb_of_advcl (mark))
- to → manage: Predicate (preposition - object) (UD: mark(to)→inf_verb)

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
- Driver → needs: Predicate (subject - verb) (UD: nsubj)
- a → vehicle: Constraint (UD: det)
- and → efficiently: Connection (UD: cc)
- and → slow: Connection (UD: cc)
- effectively → slow: Constraint (UD: advmod)
- efficiently → effectively: Connection (UD: conj)
- needs → stop: Predicate (verb/proposition - object) (UD: xcomp)
- slow → down: Constraint (UD: compound:prt)
- slow → stop: Connection (UD: conj)
- slow → vehicle: Predicate (verb/proposition - object) (UD: obj)
- to → needs: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → stop: Predicate (preposition - object) (UD: mark)
- to → stop: Predicate (preposition - object) (UD: mark(to)→inf_verb)

</details>

---
