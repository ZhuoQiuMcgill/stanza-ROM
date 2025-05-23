# ROM Evaluation Report

**Date:** 2025-05-23 15:26:46
**Total Sentences:** 12
**Processed Sentences:** 12
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 12 |
| Total Expected Relations | 89 |
| Total Generated Relations | 89 |
| Total Correct Relations | 41 |
| Total Missing Relations | 48 |
| Total Over-specified Relations | 48 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **46.1%** |
| **Missing Rate** | **53.9%** |
| **Over-specification Rate** | **53.9%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 46.1% | Percentage of generated relations that are correct |
| Recall | 46.1% | Percentage of expected relations that were found |
| F1-Score | 46.1% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
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

### Sentence 2
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

### Sentence 3
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

### Sentence 4
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

### Sentence 5
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

### Sentence 6
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

### Sentence 7
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

### Sentence 8
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

### Sentence 9
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

### Sentence 10
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

### Sentence 11
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

### Sentence 12
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
