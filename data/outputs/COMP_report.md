# ROM Evaluation Report

**Date:** 2025-05-23 14:13:42
**Total Sentences:** 23
**Processed Sentences:** 23
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 23 |
| Total Expected Relations | 223 |
| Total Generated Relations | 193 |
| Total Correct Relations | 60 |
| Total Missing Relations | 163 |
| Total Over-specified Relations | 133 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **26.9%** |
| **Missing Rate** | **73.1%** |
| **Over-specification Rate** | **68.9%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 31.1% | Percentage of generated relations that are correct |
| Recall | 26.9% | Percentage of expected relations that were found |
| F1-Score | 28.8% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
**Input:** She wanted to go for a walk, but it started raining.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 11 | - |
| Correct Relations | 6 | 54.5% |
| Missing Relations | 5 | 45.5% |
| Over-specified Relations | 5 | 45.5% |

**✅ Correct Relations:**
- a → walk: constraint
- for → walk: predicate (preposition - object)
- go → walk: predicate (verb/preposition - object)
- it → started: predicate (subject - verb)
- she → wanted: predicate (subject - verb)
- to → wanted: constraint

**❌ Missing Relations:**
- but → started: predicate (verb/preposition - object)
- but → wanted: constraint
- for → go: constraint
- started → raining: predicate (verb/preposition - object)
- to → go: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- but → started: constraint
- started → raining: predicate (verb/proposition - object)
- started → wanted: connection
- to → go: predicate (preposition - object)
- wanted → go: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → walk: constraint
- but → started: predicate (verb/preposition - object)
- but → wanted: constraint
- for → go: constraint
- for → walk: predicate (preposition - object)
- go → walk: predicate (verb/preposition - object)
- it → started: predicate (subject - verb)
- she → wanted: predicate (subject - verb)
- started → raining: predicate (verb/preposition - object)
- to → go: predicate (verb/preposition - object)
- to → wanted: constraint

**Generated Relations:**
- She → wanted: Predicate (Subject - Verb) (UD: nsubj)
- a → walk: Constraint (UD: det)
- but → started: Constraint (UD: cc)
- for → walk: Predicate (Preposition - Object) (UD: case)
- go → walk: Predicate (Verb/Preposition - Object) (UD: obl)
- it → started: Predicate (Subject - Verb) (UD: nsubj)
- started → raining: Predicate (Verb/Proposition - Object) (UD: xcomp)
- started → wanted: Connection (UD: conj)
- to → go: Predicate (Preposition - Object) (UD: mark)
- to → go: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- to → wanted: Constraint (UD: mark(to)→main_verb_of(xcomp))
- wanted → go: Predicate (Verb/Proposition - Object) (UD: xcomp)

</details>

---

### Sentence 2
**Input:** The sky was clear; we decided to go stargazing.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 9 | - |
| Correct Relations | 4 | 44.4% |
| Missing Relations | 5 | 55.6% |
| Over-specified Relations | 5 | 55.6% |

**✅ Correct Relations:**
- sky → was: predicate (subject - verb)
- the → sky: constraint
- to → decided: constraint
- we → decided: predicate (subject - verb)

**❌ Missing Relations:**
- [∅] → decided: connection
- [∅] → was: connection (semicolon as structural connector)
- go → stargazing: predicate (verb/preposition - object)
- to → go: predicate (verb/preposition - object)
- was → clear: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- decided → clear: connection
- decided → go: predicate (verb/proposition - object)
- go → stargazing: predicate (verb/proposition - object)
- to → go: predicate (preposition - object)
- was → clear: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- [∅] → decided: connection
- [∅] → was: connection (semicolon as structural connector)
- go → stargazing: predicate (verb/preposition - object)
- sky → was: predicate (subject - verb)
- the → sky: constraint
- to → decided: constraint
- to → go: predicate (verb/preposition - object)
- was → clear: predicate (verb/preposition - object)
- we → decided: predicate (subject - verb)

**Generated Relations:**
- The → sky: Constraint (UD: det)
- decided → clear: Connection (UD: parataxis)
- decided → go: Predicate (Verb/Proposition - Object) (UD: xcomp)
- go → stargazing: Predicate (Verb/Proposition - Object) (UD: xcomp)
- sky → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- to → decided: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → go: Predicate (Preposition - Object) (UD: mark)
- to → go: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- was → clear: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- we → decided: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 3
**Input:** I was tired; however, I kept working.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 6 | - |
| Correct Relations | 2 | 33.3% |
| Missing Relations | 4 | 66.7% |
| Over-specified Relations | 4 | 66.7% |

**✅ Correct Relations:**
- i → kept: predicate (subject - verb)
- i → was: predicate (subject - verb)

**❌ Missing Relations:**
- however → kept: predicate (verb/preposition - object)
- however → was: constraint
- kept → working: predicate (verb/preposition - object)
- was → tired: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- however → kept: constraint
- kept → tired: connection
- kept → working: predicate (verb/proposition - object)
- was → tired: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- however → kept: predicate (verb/preposition - object)
- however → was: constraint
- i → kept: predicate (subject - verb)
- i → was: predicate (subject - verb)
- kept → working: predicate (verb/preposition - object)
- was → tired: predicate (verb/preposition - object)

**Generated Relations:**
- I → kept: Predicate (Subject - Verb) (UD: nsubj)
- I → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- however → kept: Constraint (UD: advmod)
- kept → tired: Connection (UD: parataxis)
- kept → working: Predicate (Verb/Proposition - Object) (UD: xcomp)
- was → tired: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 4
**Input:** She is both smart and creative.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 6 | - |
| Correct Relations | 1 | 14.3% |
| Missing Relations | 6 | 85.7% |
| Over-specified Relations | 5 | 83.3% |

**✅ Correct Relations:**
- she → is: predicate (subject - verb)

**❌ Missing Relations:**
- and → creative: predicate (verb/preposition - object)
- and → is: constraint
- both → is: constraint
- both → smart: predicate (verb/preposition - object)
- is → creative: predicate (verb/preposition - object)
- is → smart: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- and → creative: connection
- both → and: connection
- both → smart: constraint
- creative → smart: connection
- is → smart: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- and → creative: predicate (verb/preposition - object)
- and → is: constraint
- both → is: constraint
- both → smart: predicate (verb/preposition - object)
- is → creative: predicate (verb/preposition - object)
- is → smart: predicate (verb/preposition - object)
- she → is: predicate (subject - verb)

**Generated Relations:**
- She → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- and → creative: Connection (UD: cc)
- both → and: Connection (UD: correlative_both_and)
- both → smart: Constraint (UD: advmod)
- creative → smart: Connection (UD: conj)
- is → smart: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 5
**Input:** Both my brother and sister are engineers.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 3 | 33.3% |
| Missing Relations | 6 | 66.7% |
| Over-specified Relations | 4 | 57.1% |

**✅ Correct Relations:**
- both → and: connection
- brother → are: predicate (subject - verb)
- my → brother: constraint

**❌ Missing Relations:**
- and → are: constraint
- and → sister: predicate (verb/preposition - object)
- are → engineers: predicate (verb/preposition - object)
- both → are: constraint
- both → brother: predicate (verb/preposition - object)
- sister → are: predicate (subject - verb)

**➕ Over-specified Relations:**
- and → sister: connection
- are → engineers: predicate (verb/proposition - object)
- both → brother: connection
- sister → brother: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- and → are: constraint
- and → sister: predicate (verb/preposition - object)
- are → engineers: predicate (verb/preposition - object)
- both → and: connection
- both → are: constraint
- both → brother: predicate (verb/preposition - object)
- brother → are: predicate (subject - verb)
- my → brother: constraint
- sister → are: predicate (subject - verb)

**Generated Relations:**
- Both → and: Connection (UD: correlative_both_and)
- Both → brother: Connection (UD: cc:preconj)
- and → sister: Connection (UD: cc)
- are → engineers: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- brother → are: Predicate (Subject - Verb) (UD: nsubj→cop)
- my → brother: Constraint (UD: nmod:poss)
- sister → brother: Connection (UD: conj)

</details>

---

### Sentence 6
**Input:** Not only did he win, but he also broke the record.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 10 | - |
| Correct Relations | 2 | 28.6% |
| Missing Relations | 5 | 71.4% |
| Over-specified Relations | 8 | 80.0% |

**✅ Correct Relations:**
- he → broke: predicate (subject - verb)
- the → record: constraint

**❌ Missing Relations:**
- broke → record: predicate (verb/preposition - object)
- but also → broke: predicate (verb/preposition - object)
- he → won: predicate (subject - verb)
- not only → but also: connection
- not only → won: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- also → broke: constraint
- broke → record: predicate (verb/proposition - object)
- broke → win: connection
- but → broke: constraint
- did → win: constraint
- he → win: predicate (subject - verb)
- not → win: constraint
- only → win: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- broke → record: predicate (verb/preposition - object)
- but also → broke: predicate (verb/preposition - object)
- he → broke: predicate (subject - verb)
- he → won: predicate (subject - verb)
- not only → but also: connection
- not only → won: predicate (verb/preposition - object)
- the → record: constraint

**Generated Relations:**
- Not → win: Constraint (UD: advmod)
- also → broke: Constraint (UD: advmod)
- broke → record: Predicate (Verb/Proposition - Object) (UD: obj)
- broke → win: Connection (UD: conj)
- but → broke: Constraint (UD: cc)
- did → win: Constraint (UD: aux)
- he → broke: Predicate (Subject - Verb) (UD: nsubj)
- he → win: Predicate (Subject - Verb) (UD: nsubj)
- only → win: Constraint (UD: advmod)
- the → record: Constraint (UD: det)

</details>

---

### Sentence 7
**Input:** The movie was not only long but also boring.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 2 | 22.2% |
| Missing Relations | 7 | 77.8% |
| Over-specified Relations | 5 | 71.4% |

**✅ Correct Relations:**
- movie → was: predicate (subject - verb)
- the → movie: constraint

**❌ Missing Relations:**
- but also → boring: predicate (verb/preposition - object)
- but also → was: constraint
- not only → but also: connection
- not only → long: predicate (verb/preposition - object)
- not only → was: constraint
- was → boring: predicate (verb/preposition - object)
- was → long: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- also → boring: constraint
- boring → long: connection
- but → boring: predicate (conjunction - element)
- only → long: constraint
- was → long: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- but also → boring: predicate (verb/preposition - object)
- but also → was: constraint
- movie → was: predicate (subject - verb)
- not only → but also: connection
- not only → long: predicate (verb/preposition - object)
- not only → was: constraint
- the → movie: constraint
- was → boring: predicate (verb/preposition - object)
- was → long: predicate (verb/preposition - object)

**Generated Relations:**
- The → movie: Constraint (UD: det)
- also → boring: Constraint (UD: advmod)
- boring → long: Connection (UD: conj)
- but → boring: Predicate (Conjunction - Element) (UD: cc)
- movie → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- only → long: Constraint (UD: advmod)
- was → long: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 8
**Input:** You can either stay home or come with us.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 19 | - |
| Generated Relations | 9 | - |
| Correct Relations | 3 | 15.8% |
| Missing Relations | 16 | 84.2% |
| Over-specified Relations | 6 | 66.7% |

**✅ Correct Relations:**
- can → stay: constraint
- either → or: connection
- you → stay: predicate (subject - verb)

**❌ Missing Relations:**
- assistant → answered: predicate (subject - verb)
- can → come: constraint
- come → with: constraint
- either → stay: predicate (verb/preposition - object)
- manager → answered: predicate (subject - verb)
- neither → answered: constraint
- neither → manager: predicate (verb/preposition - object)
- neither → nor: connection
- nor → answered: constraint
- nor → assistant: predicate (verb/preposition - object)
- or → come: predicate (verb/preposition - object)
- stay → home: constraint
- the → assistant: constraint
- the → manager: constraint
- with → us: predicate (verb/preposition - object)
- you → come: predicate (subject - verb)

**➕ Over-specified Relations:**
- come → stay: connection
- come → us: predicate (verb/preposition - object)
- either → stay: connection
- home → stay: constraint
- or → come: connection
- with → us: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- assistant → answered: predicate (subject - verb)
- can → come: constraint
- can → stay: constraint
- come → with: constraint
- either → or: connection
- either → stay: predicate (verb/preposition - object)
- manager → answered: predicate (subject - verb)
- neither → answered: constraint
- neither → manager: predicate (verb/preposition - object)
- neither → nor: connection
- nor → answered: constraint
- nor → assistant: predicate (verb/preposition - object)
- or → come: predicate (verb/preposition - object)
- stay → home: constraint
- the → assistant: constraint
- the → manager: constraint
- with → us: predicate (verb/preposition - object)
- you → come: predicate (subject - verb)
- you → stay: predicate (subject - verb)

**Generated Relations:**
- You → stay: Predicate (Subject - Verb) (UD: nsubj)
- can → stay: Constraint (UD: aux)
- come → stay: Connection (UD: conj)
- come → us: Predicate (Verb/Preposition - Object) (UD: obl)
- either → or: Connection (UD: correlative_either_or)
- either → stay: Connection (UD: cc:preconj)
- home → stay: Constraint (UD: advmod)
- or → come: Connection (UD: cc)
- with → us: Predicate (Preposition - Object) (UD: case)

</details>

---

### Sentence 9
**Input:** Neither did he apologize, nor did he show any regret.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 9 | - |
| Correct Relations | 5 | 45.5% |
| Missing Relations | 6 | 54.5% |
| Over-specified Relations | 4 | 44.4% |

**✅ Correct Relations:**
- any → regret: constraint
- did → apologize: constraint
- did → show: constraint
- he → apologize: predicate (subject - verb)
- he → show: predicate (subject - verb)

**❌ Missing Relations:**
- neither → apologize: predicate (verb/preposition - object)
- neither → nor: connection
- nor → show: predicate (verb/preposition - object)
- not → apologize: constraint
- not → show: constraint
- show → regret: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- neither → apologize: connection
- nor → show: connection
- show → apologize: connection
- show → regret: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- any → regret: constraint
- did → apologize: constraint
- did → show: constraint
- he → apologize: predicate (subject - verb)
- he → show: predicate (subject - verb)
- neither → apologize: predicate (verb/preposition - object)
- neither → nor: connection
- nor → show: predicate (verb/preposition - object)
- not → apologize: constraint
- not → show: constraint
- show → regret: predicate (verb/preposition - object)

**Generated Relations:**
- Neither → apologize: Connection (UD: cc:preconj)
- any → regret: Constraint (UD: det)
- did → apologize: Constraint (UD: aux)
- did → show: Constraint (UD: aux)
- he → apologize: Predicate (Subject - Verb) (UD: nsubj)
- he → show: Predicate (Subject - Verb) (UD: nsubj)
- nor → show: Connection (UD: cc)
- show → apologize: Connection (UD: conj)
- show → regret: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---

### Sentence 10
**Input:** I don't know whether he’ll call or text.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 9 | - |
| Correct Relations | 2 | 18.2% |
| Missing Relations | 9 | 81.8% |
| Over-specified Relations | 7 | 77.8% |

**✅ Correct Relations:**
- he → call: predicate (subject - verb)
- i → know: predicate (subject - verb)

**❌ Missing Relations:**
- don't → know: constraint
- he → text: predicate (subject - verb)
- or → know: constraint
- or → text: predicate (verb/preposition - object)
- whether → call: predicate (verb/preposition - object)
- whether → know: constraint
- whether → or: connection
- will → call: constraint
- will → text: constraint

**➕ Over-specified Relations:**
- do → know: constraint
- know → call: predicate (verb/proposition - object)
- n't → know: constraint
- or → text: connection
- text → call: connection
- whether → call: connection
- ’ll → call: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- don't → know: constraint
- he → call: predicate (subject - verb)
- he → text: predicate (subject - verb)
- i → know: predicate (subject - verb)
- or → know: constraint
- or → text: predicate (verb/preposition - object)
- whether → call: predicate (verb/preposition - object)
- whether → know: constraint
- whether → or: connection
- will → call: constraint
- will → text: constraint

**Generated Relations:**
- I → know: Predicate (Subject - Verb) (UD: nsubj)
- do → know: Constraint (UD: aux)
- he → call: Predicate (Subject - Verb) (UD: nsubj)
- know → call: Predicate (Verb/Proposition - Object) (UD: ccomp)
- n't → know: Constraint (UD: advmod)
- or → text: Connection (UD: cc)
- text → call: Connection (UD: conj)
- whether → call: Connection (UD: mark)
- ’ll → call: Constraint (UD: aux)

</details>

---

### Sentence 11
**Input:** She’s unsure whether to accept the job or continue studying.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 9 | - |
| Correct Relations | 1 | 8.3% |
| Missing Relations | 11 | 91.7% |
| Over-specified Relations | 8 | 88.9% |

**✅ Correct Relations:**
- the → job: constraint

**❌ Missing Relations:**
- accept → job: predicate (verb/preposition - object)
- continue → studying: predicate (verb/preposition - object)
- is → unsure: predicate (verb/preposition - object)
- or → continue: predicate (verb/preposition - object)
- or → is: constraint
- she → is: predicate (subject - verb)
- to → accept: predicate (verb/preposition - object)
- to → continue: predicate (verb/preposition - object)
- whether → accept: predicate (verb/preposition - object)
- whether → is: constraint
- whether → or: connection

**➕ Over-specified Relations:**
- accept → job: predicate (verb/proposition - object)
- continue → accept: connection
- continue → studying: predicate (verb/proposition - object)
- or → continue: connection
- she → ’s: predicate (subject - verb)
- to → accept: predicate (preposition - object)
- whether → accept: connection
- ’s → unsure: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- accept → job: predicate (verb/preposition - object)
- continue → studying: predicate (verb/preposition - object)
- is → unsure: predicate (verb/preposition - object)
- or → continue: predicate (verb/preposition - object)
- or → is: constraint
- she → is: predicate (subject - verb)
- the → job: constraint
- to → accept: predicate (verb/preposition - object)
- to → continue: predicate (verb/preposition - object)
- whether → accept: predicate (verb/preposition - object)
- whether → is: constraint
- whether → or: connection

**Generated Relations:**
- She → ’s: Predicate (Subject - Verb) (UD: nsubj→cop)
- accept → job: Predicate (Verb/Proposition - Object) (UD: obj)
- continue → accept: Connection (UD: conj)
- continue → studying: Predicate (Verb/Proposition - Object) (UD: xcomp)
- or → continue: Connection (UD: cc)
- the → job: Constraint (UD: det)
- to → accept: Predicate (Preposition - Object) (UD: mark)
- to → accept: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- whether → accept: Connection (UD: mark)
- ’s → unsure: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 12
**Input:** She’s as tall as her brother.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 1 | 11.1% |
| Missing Relations | 8 | 88.9% |
| Over-specified Relations | 6 | 85.7% |

**✅ Correct Relations:**
- her → brother: constraint

**❌ Missing Relations:**
- as → as (2): connection
- as → is: constraint
- as → tall: predicate (verb/preposition - object)
- as (2) → is (2): predicate (verb/preposition - object)
- as (2) → tall: constraint
- brother → is: predicate (subject - verb)
- is → tall: predicate (verb/preposition - object)
- she → is: predicate (subject - verb)

**➕ Over-specified Relations:**
- as → as: connection
- as → brother: predicate (preposition - object)
- as → tall: constraint
- as → tall: predicate (verb/proposition - object)
- she → ’s: predicate (subject - verb)
- ’s → tall: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → as (2): connection
- as → is: constraint
- as → tall: predicate (verb/preposition - object)
- as (2) → is (2): predicate (verb/preposition - object)
- as (2) → tall: constraint
- brother → is: predicate (subject - verb)
- her → brother: constraint
- is → tall: predicate (verb/preposition - object)
- she → is: predicate (subject - verb)

**Generated Relations:**
- She → ’s: Predicate (Subject - Verb) (UD: nsubj→cop)
- as → as: Connection (UD: as...as_correlative)
- as → brother: Predicate (Preposition - Object) (UD: case)
- as → brother: Predicate (Preposition - Object) (UD: as→noun)
- as → tall: Constraint (UD: advmod)
- as → tall: Predicate (Verb/Proposition - Object) (UD: as→adj/adv)
- her → brother: Constraint (UD: nmod:poss)
- ’s → tall: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 13
**Input:** He ran as quickly as a professional athlete.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 8 | - |
| Correct Relations | 4 | 40.0% |
| Missing Relations | 6 | 60.0% |
| Over-specified Relations | 4 | 50.0% |

**✅ Correct Relations:**
- a → athlete: constraint
- he → ran: predicate (subject - verb)
- professional → athlete: constraint
- quickly → ran: constraint

**❌ Missing Relations:**
- as → as (2): connection
- as → quickly: predicate (verb/preposition - object)
- as → ran: constraint
- as (2) → quickly: constraint
- as (2) → ran (2): predicate (verb/preposition - object)
- athlete → ran (2): predicate (subject - verb)

**➕ Over-specified Relations:**
- as → as: connection
- as → athlete: predicate (preposition - object)
- as → quickly: predicate (verb/proposition - object)
- ran → athlete: predicate (verb/preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → athlete: constraint
- as → as (2): connection
- as → quickly: predicate (verb/preposition - object)
- as → ran: constraint
- as (2) → quickly: constraint
- as (2) → ran (2): predicate (verb/preposition - object)
- athlete → ran (2): predicate (subject - verb)
- he → ran: predicate (subject - verb)
- professional → athlete: constraint
- quickly → ran: constraint

**Generated Relations:**
- He → ran: Predicate (Subject - Verb) (UD: nsubj)
- a → athlete: Constraint (UD: det)
- as → as: Connection (UD: as...as_correlative)
- as → athlete: Predicate (Preposition - Object) (UD: case)
- as → athlete: Predicate (Preposition - Object) (UD: as→noun)
- as → quickly: Predicate (Verb/Proposition - Object) (UD: as→adj/adv)
- professional → athlete: Constraint (UD: amod)
- quickly → ran: Constraint (UD: advmod)
- ran → athlete: Predicate (Verb/Preposition - Object) (UD: obl)

</details>

---

### Sentence 14
**Input:** This task is not as easy as it looks.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 8 | - |
| Correct Relations | 3 | 30.0% |
| Missing Relations | 7 | 70.0% |
| Over-specified Relations | 5 | 62.5% |

**✅ Correct Relations:**
- it → looks: predicate (subject - verb)
- task → is: predicate (subject - verb)
- this → task: constraint

**❌ Missing Relations:**
- as → as (2): connection
- as → easy: predicate (verb/preposition - object)
- as → is: constraint
- as (2) → easy: constraint
- as (2) → looks: predicate (verb/preposition - object)
- is → easy: predicate (verb/preposition - object)
- not → easy: constraint

**➕ Over-specified Relations:**
- as → as: connection
- as → easy: constraint
- as → easy: predicate (verb/proposition - object)
- as → looks: predicate (conjunction - clause_verb)
- is → easy: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → as (2): connection
- as → easy: predicate (verb/preposition - object)
- as → is: constraint
- as (2) → easy: constraint
- as (2) → looks: predicate (verb/preposition - object)
- is → easy: predicate (verb/preposition - object)
- it → looks: predicate (subject - verb)
- not → easy: constraint
- task → is: predicate (subject - verb)
- this → task: constraint

**Generated Relations:**
- This → task: Constraint (UD: det)
- as → as: Connection (UD: as...as_correlative)
- as → easy: Constraint (UD: advmod)
- as → easy: Predicate (Verb/Proposition - Object) (UD: as→adj/adv)
- as → easy: Constraint (UD: mark→main_verb (mark))
- as → looks: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- is → easy: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- it → looks: Predicate (Subject - Verb) (UD: nsubj)
- task → is: Predicate (Subject - Verb) (UD: nsubj→cop)

</details>

---

### Sentence 15
**Input:** He doesn’t eat as much chocolate as his brother.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 11 | - |
| Correct Relations | 3 | 30.0% |
| Missing Relations | 7 | 70.0% |
| Over-specified Relations | 8 | 72.7% |

**✅ Correct Relations:**
- he → eat: predicate (subject - verb)
- his → brother: constraint
- much → chocolate: constraint

**❌ Missing Relations:**
- as → as (2): connection
- as → eat: constraint
- as → much: predicate (verb/preposition - object)
- as (2) → eat (2): predicate (verb/preposition - object)
- as (2) → much: constraint
- doesn’t → eat: constraint
- eat → chocolate: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- as → as: connection
- as → brother: predicate (preposition - object)
- as → much: constraint
- as → much: predicate (verb/proposition - object)
- does → eat: constraint
- eat → brother: predicate (verb/preposition - object)
- eat → chocolate: predicate (verb/proposition - object)
- n’t → eat: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → as (2): connection
- as → eat: constraint
- as → much: predicate (verb/preposition - object)
- as (2) → eat (2): predicate (verb/preposition - object)
- as (2) → much: constraint
- doesn’t → eat: constraint
- eat → chocolate: predicate (verb/preposition - object)
- he → eat: predicate (subject - verb)
- his → brother: constraint
- much → chocolate: constraint

**Generated Relations:**
- He → eat: Predicate (Subject - Verb) (UD: nsubj)
- as → as: Connection (UD: as...as_correlative)
- as → brother: Predicate (Preposition - Object) (UD: case)
- as → brother: Predicate (Preposition - Object) (UD: as→noun)
- as → much: Constraint (UD: advmod)
- as → much: Predicate (Verb/Proposition - Object) (UD: as→adj/adv)
- does → eat: Constraint (UD: aux)
- eat → brother: Predicate (Verb/Preposition - Object) (UD: obl)
- eat → chocolate: Predicate (Verb/Proposition - Object) (UD: obj)
- his → brother: Constraint (UD: nmod:poss)
- much → chocolate: Constraint (UD: amod)
- n’t → eat: Constraint (UD: advmod)

</details>

---

### Sentence 16
**Input:** She enjoys painting as much as she enjoys dancing.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 7 | - |
| Correct Relations | 1 | 10.0% |
| Missing Relations | 9 | 90.0% |
| Over-specified Relations | 6 | 85.7% |

**✅ Correct Relations:**
- she → enjoys: predicate (subject - verb)

**❌ Missing Relations:**
- as → as (2): connection
- as → enjoys: constraint
- as → much: predicate (verb/preposition - object)
- as (2) → enjoys: predicate (verb/preposition - object)
- as (2) → much: constraint
- enjoys → dancing: predicate (verb/preposition - object) (second clause)
- enjoys → painting: predicate (verb/preposition - object)
- much → painting: constraint
- she → enjoys: predicate (subject - verb) (second clause)

**➕ Over-specified Relations:**
- as → as: connection
- as → enjoys: predicate (conjunction - clause_verb)
- as → much: constraint
- as → much: predicate (verb/proposition - object)
- enjoys → dancing: predicate (verb/proposition - object)
- enjoys → painting: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → as (2): connection
- as → enjoys: constraint
- as → much: predicate (verb/preposition - object)
- as (2) → enjoys: predicate (verb/preposition - object)
- as (2) → much: constraint
- enjoys → dancing: predicate (verb/preposition - object) (second clause)
- enjoys → painting: predicate (verb/preposition - object)
- much → painting: constraint
- she → enjoys: predicate (subject - verb)
- she → enjoys: predicate (subject - verb) (second clause)

**Generated Relations:**
- She → enjoys: Predicate (Subject - Verb) (UD: nsubj)
- as → as: Connection (UD: as...as_correlative)
- as → enjoys: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- as → much: Constraint (UD: advmod)
- as → much: Predicate (Verb/Proposition - Object) (UD: as→adj/adv)
- as → much: Constraint (UD: mark→main_verb (mark))
- enjoys → dancing: Predicate (Verb/Proposition - Object) (UD: obj)
- enjoys → painting: Predicate (Verb/Proposition - Object) (UD: obj)
- she → enjoys: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 17
**Input:** Just as the moon affects the tides, so does the sun influence them.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 13 | - |
| Correct Relations | 6 | 50.0% |
| Missing Relations | 6 | 50.0% |
| Over-specified Relations | 7 | 53.8% |

**✅ Correct Relations:**
- does → influence: constraint
- moon → affects: predicate (subject - verb)
- sun → influence: predicate (subject - verb)
- the → moon: constraint
- the → sun: constraint
- the → tides: constraint

**❌ Missing Relations:**
- affects → tides: predicate (verb/preposition - object)
- as → affects: constraint
- as → so: connection
- influence → them: predicate (verb/preposition - object)
- just → as: constraint
- so → influence: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- affects → influence: constraint
- affects → tides: predicate (verb/proposition - object)
- as → affects: predicate (conjunction - clause_verb)
- as → influence: constraint
- influence → them: predicate (verb/proposition - object)
- just → affects: constraint
- so → influence: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- affects → tides: predicate (verb/preposition - object)
- as → affects: constraint
- as → so: connection
- does → influence: constraint
- influence → them: predicate (verb/preposition - object)
- just → as: constraint
- moon → affects: predicate (subject - verb)
- so → influence: predicate (verb/preposition - object)
- sun → influence: predicate (subject - verb)
- the → moon: constraint
- the → sun: constraint
- the → tides: constraint

**Generated Relations:**
- Just → affects: Constraint (UD: advmod)
- affects → influence: Constraint (UD: advcl)
- affects → tides: Predicate (Verb/Proposition - Object) (UD: obj)
- as → affects: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- as → influence: Constraint (UD: mark→main_verb (mark))
- does → influence: Constraint (UD: aux)
- influence → them: Predicate (Verb/Proposition - Object) (UD: obj)
- moon → affects: Predicate (Subject - Verb) (UD: nsubj)
- so → influence: Constraint (UD: advmod)
- sun → influence: Predicate (Subject - Verb) (UD: nsubj)
- the → moon: Constraint (UD: det)
- the → sun: Constraint (UD: det)
- the → tides: Constraint (UD: det)

</details>

---

### Sentence 18
**Input:** Just as honesty builds trust, so does kindness.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 1 | 11.1% |
| Missing Relations | 8 | 88.9% |
| Over-specified Relations | 7 | 87.5% |

**✅ Correct Relations:**
- honesty → builds: predicate (subject - verb)

**❌ Missing Relations:**
- as → builds: constraint
- as → so: connection
- builds → trust: predicate (verb/preposition - object)
- builds → trust: predicate (verb/preposition - object) (implied)
- does → builds: constraint
- just → so: constraint
- kindness → builds: predicate (subject - verb)
- so → builds: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- as → builds: predicate (conjunction - clause_verb)
- as → does: constraint
- builds → does: constraint
- builds → trust: predicate (verb/proposition - object)
- does → kindness: predicate (verb/proposition - object)
- just → builds: constraint
- so → does: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → builds: constraint
- as → so: connection
- builds → trust: predicate (verb/preposition - object)
- builds → trust: predicate (verb/preposition - object) (implied)
- does → builds: constraint
- honesty → builds: predicate (subject - verb)
- just → so: constraint
- kindness → builds: predicate (subject - verb)
- so → builds: predicate (verb/preposition - object)

**Generated Relations:**
- Just → builds: Constraint (UD: advmod)
- as → builds: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- as → does: Constraint (UD: mark→main_verb (mark))
- builds → does: Constraint (UD: advcl)
- builds → trust: Predicate (Verb/Proposition - Object) (UD: obj)
- does → kindness: Predicate (Verb/Proposition - Object) (UD: obj)
- honesty → builds: Predicate (Subject - Verb) (UD: nsubj)
- so → does: Constraint (UD: advmod)

</details>

---

### Sentence 19
**Input:** Just as we need water to survive, so do plants need sunlight.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 13 | - |
| Correct Relations | 4 | 36.4% |
| Missing Relations | 7 | 63.6% |
| Over-specified Relations | 9 | 69.2% |

**✅ Correct Relations:**
- as → need: constraint
- do → need: constraint
- plants → need: predicate (subject - verb)
- we → need: predicate (subject - verb)

**❌ Missing Relations:**
- as → so: connection
- just → so: constraint
- need → sunlight: predicate (verb/preposition - object)
- need → water: predicate (verb/preposition - object)
- so → need: predicate (verb/preposition - object)
- to → survive: constraint
- water → survive: constraint

**➕ Over-specified Relations:**
- as → need: predicate (conjunction - clause_verb)
- just → need: constraint
- need → need: constraint
- need → sunlight: predicate (verb/proposition - object)
- need → survive: predicate (verb/proposition - object)
- need → water: predicate (verb/proposition - object)
- so → need: constraint
- to → need: constraint
- to → survive: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- as → need: constraint
- as → so: connection
- do → need: constraint
- just → so: constraint
- need → sunlight: predicate (verb/preposition - object)
- need → water: predicate (verb/preposition - object)
- plants → need: predicate (subject - verb)
- so → need: predicate (verb/preposition - object)
- to → survive: constraint
- water → survive: constraint
- we → need: predicate (subject - verb)

**Generated Relations:**
- Just → need: Constraint (UD: advmod)
- as → need: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- as → need: Constraint (UD: mark→main_verb (mark))
- do → need: Constraint (UD: aux)
- need → need: Constraint (UD: advcl)
- need → sunlight: Predicate (Verb/Proposition - Object) (UD: obj)
- need → survive: Predicate (Verb/Proposition - Object) (UD: xcomp)
- need → water: Predicate (Verb/Proposition - Object) (UD: obj)
- plants → need: Predicate (Subject - Verb) (UD: nsubj)
- so → need: Constraint (UD: advmod)
- to → need: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → survive: Predicate (Preposition - Object) (UD: mark)
- to → survive: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- we → need: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 20
**Input:** No sooner had she sat down than the phone rang.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 9 | - |
| Correct Relations | 0 | 0.0% |
| Missing Relations | 8 | 100.0% |
| Over-specified Relations | 9 | 100.0% |

**❌ Missing Relations:**
- had → arrived: constraint
- it → started: predicate (subject - verb)
- no sooner → arrived: constraint
- no sooner → than: connection
- than → started: predicate (verb/preposition - object)
- to → rain: predicate (verb/preposition - object)
- to → started: constraint
- we → arrived: predicate (subject - verb)

**➕ Over-specified Relations:**
- had → sat: constraint
- phone → rang: predicate (subject - verb)
- rang → sat: constraint
- sat → down: constraint
- she → sat: predicate (subject - verb)
- sooner → sat: constraint
- than → rang: predicate (conjunction - clause_verb)
- than → sat: constraint
- the → phone: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- had → arrived: constraint
- it → started: predicate (subject - verb)
- no sooner → arrived: constraint
- no sooner → than: connection
- than → started: predicate (verb/preposition - object)
- to → rain: predicate (verb/preposition - object)
- to → started: constraint
- we → arrived: predicate (subject - verb)

**Generated Relations:**
- had → sat: Constraint (UD: aux)
- phone → rang: Predicate (Subject - Verb) (UD: nsubj)
- rang → sat: Constraint (UD: advcl)
- sat → down: Constraint (UD: compound:prt)
- she → sat: Predicate (Subject - Verb) (UD: nsubj)
- sooner → sat: Constraint (UD: advmod)
- than → rang: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- than → sat: Constraint (UD: mark→main_verb (mark))
- the → phone: Constraint (UD: det)

</details>

---

### Sentence 21
**Input:** I’d rather read a book than watch TV.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 3 | 33.3% |
| Missing Relations | 6 | 66.7% |
| Over-specified Relations | 4 | 57.1% |

**✅ Correct Relations:**
- a → book: constraint
- i → read: predicate (subject - verb)
- rather → read: constraint

**❌ Missing Relations:**
- i → watch: predicate (subject - verb)
- rather → than: connection
- read → book: predicate (verb/preposition - object)
- than → watch: predicate (verb/preposition - object)
- watch → tv: predicate (verb/preposition - object)
- would → read: constraint

**➕ Over-specified Relations:**
- read → book: predicate (verb/proposition - object)
- watch → read: constraint
- watch → tv: predicate (verb/proposition - object)
- ’d → read: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → book: constraint
- i → read: predicate (subject - verb)
- i → watch: predicate (subject - verb)
- rather → read: constraint
- rather → than: connection
- read → book: predicate (verb/preposition - object)
- than → watch: predicate (verb/preposition - object)
- watch → tv: predicate (verb/preposition - object)
- would → read: constraint

**Generated Relations:**
- I → read: Predicate (Subject - Verb) (UD: nsubj)
- a → book: Constraint (UD: det)
- rather → read: Constraint (UD: advmod)
- read → book: Predicate (Verb/Proposition - Object) (UD: obj)
- watch → TV: Predicate (Verb/Proposition - Object) (UD: obj)
- watch → read: Constraint (UD: advcl)
- ’d → read: Constraint (UD: aux)

</details>

---

### Sentence 22
**Input:** He chose to walk rather than drive.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 6 | - |
| Correct Relations | 2 | 22.2% |
| Missing Relations | 7 | 77.8% |
| Over-specified Relations | 4 | 66.7% |

**✅ Correct Relations:**
- he → chose: predicate (subject - verb)
- to → chose: constraint

**❌ Missing Relations:**
- chose → walk: predicate (verb/preposition - object)
- he → drive: predicate (subject - verb)
- rather → than: connection
- rather → walk: constraint
- than → drive: predicate (verb/preposition - object)
- to → drive: predicate (verb/preposition - object)
- to → walk: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- chose → walk: predicate (verb/proposition - object)
- drive → walk: connection
- than → rather: connection
- to → walk: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- chose → walk: predicate (verb/preposition - object)
- he → chose: predicate (subject - verb)
- he → drive: predicate (subject - verb)
- rather → than: connection
- rather → walk: constraint
- than → drive: predicate (verb/preposition - object)
- to → chose: constraint
- to → drive: predicate (verb/preposition - object)
- to → walk: predicate (verb/preposition - object)

**Generated Relations:**
- He → chose: Predicate (Subject - Verb) (UD: nsubj)
- chose → walk: Predicate (Verb/Proposition - Object) (UD: xcomp)
- drive → walk: Connection (UD: conj)
- than → rather: Connection (UD: fixed)
- to → chose: Constraint (UD: mark(to)→main_verb_of(xcomp))
- to → walk: Predicate (Preposition - Object) (UD: mark)
- to → walk: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)

</details>

---

### Sentence 23
**Input:** Rather than complain, she took action.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 5 | - |
| Generated Relations | 4 | - |
| Correct Relations | 1 | 20.0% |
| Missing Relations | 4 | 80.0% |
| Over-specified Relations | 3 | 75.0% |

**✅ Correct Relations:**
- she → took: predicate (subject - verb)

**❌ Missing Relations:**
- rather → took: constraint
- she → complain: predicate (subject - verb)
- than → complain: predicate (verb/preposition - object)
- took → action: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- complain → took: constraint
- than → rather: connection
- took → action: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- rather → took: constraint
- she → complain: predicate (subject - verb)
- she → took: predicate (subject - verb)
- than → complain: predicate (verb/preposition - object)
- took → action: predicate (verb/preposition - object)

**Generated Relations:**
- complain → took: Constraint (UD: advcl)
- she → took: Predicate (Subject - Verb) (UD: nsubj)
- than → Rather: Connection (UD: fixed)
- took → action: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---
