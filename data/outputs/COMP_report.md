# ROM Evaluation Report

**Date:** 2025-05-23 15:26:49
**Total Sentences:** 14
**Processed Sentences:** 14
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 14 |
| Total Expected Relations | 131 |
| Total Generated Relations | 110 |
| Total Correct Relations | 39 |
| Total Missing Relations | 92 |
| Total Over-specified Relations | 71 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **29.8%** |
| **Missing Rate** | **70.2%** |
| **Over-specification Rate** | **64.5%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 35.5% | Percentage of generated relations that are correct |
| Recall | 29.8% | Percentage of expected relations that were found |
| F1-Score | 32.4% | Harmonic mean of precision and recall |

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

### Sentence 11
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

### Sentence 12
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

### Sentence 13
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

### Sentence 14
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
