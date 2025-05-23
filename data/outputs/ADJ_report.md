# ROM Evaluation Report

**Date:** 2025-05-22 22:43:59
**Total Sentences:** 10
**Processed Sentences:** 10
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 10 |
| Total Expected Relations | 72 |
| Total Generated Relations | 70 |
| Total Correct Relations | 52 |
| Total Missing Relations | 20 |
| Total Over-specified Relations | 18 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **72.2%** |
| **Missing Rate** | **27.8%** |
| **Over-specification Rate** | **25.7%** |

### Performance Interpretation
**Overall Performance:** 🟠 Fair

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 74.3% | Percentage of generated relations that are correct |
| Recall | 72.2% | Percentage of expected relations that were found |
| F1-Score | 73.2% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
**Input:** The boy who sings is my friend.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 7 | - |
| Correct Relations | 6 | 75.0% |
| Missing Relations | 2 | 25.0% |
| Over-specified Relations | 1 | 14.3% |

**✅ Correct Relations:**
- boy → is: predicate (subject - verb)
- is → friend: predicate (verb/proposition - object)
- my → friend: constraint
- the → boy: constraint
- who → boy: connection
- who → sings: predicate (subject - verb)

**❌ Missing Relations:**
- boy → sings: predicate (subject - verb)
- the → friend: constraint

**➕ Over-specified Relations:**
- boy → sings: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- boy → is: predicate (subject - verb)
- boy → sings: predicate (subject - verb)
- is → friend: predicate (verb/proposition - object)
- my → friend: constraint
- the → boy: constraint
- the → friend: constraint
- who → boy: connection
- who → sings: predicate (subject - verb)

**Generated Relations:**
- The → boy: Constraint (UD: det)
- boy → is: Predicate (subject - verb) (UD: nsubj→cop)
- boy → sings: Connection (UD: acl:relcl)
- is → friend: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- my → friend: Constraint (UD: nmod:poss)
- who → boy: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → sings: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 2
**Input:** The artist who painted this is famous.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 7 | - |
| Correct Relations | 6 | 85.7% |
| Missing Relations | 1 | 14.3% |
| Over-specified Relations | 1 | 14.3% |

**✅ Correct Relations:**
- artist → is: predicate (subject - verb)
- is → famous: predicate (verb/proposition - object)
- painted → this: predicate (verb/proposition - object)
- the → artist: constraint
- who → artist: connection
- who → painted: predicate (subject - verb)

**❌ Missing Relations:**
- artist → painted: predicate (subject - verb)

**➕ Over-specified Relations:**
- artist → painted: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- artist → is: predicate (subject - verb)
- artist → painted: predicate (subject - verb)
- is → famous: predicate (verb/proposition - object)
- painted → this: predicate (verb/proposition - object)
- the → artist: constraint
- who → artist: connection
- who → painted: predicate (subject - verb)

**Generated Relations:**
- The → artist: Constraint (UD: det)
- artist → is: Predicate (subject - verb) (UD: nsubj→cop)
- artist → painted: Connection (UD: acl:relcl)
- is → famous: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- painted → this: Predicate (verb/proposition - object) (UD: obj)
- who → artist: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → painted: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 3
**Input:** The girl (whom) I met is nice.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 6 | - |
| Correct Relations | 5 | 83.3% |
| Missing Relations | 1 | 16.7% |
| Over-specified Relations | 1 | 16.7% |

**✅ Correct Relations:**
- girl → is: predicate (subject - verb)
- i → met: predicate (subject - verb)
- is → nice: predicate (verb/proposition - object)
- the → girl: constraint
- whom → girl: connection

**❌ Missing Relations:**
- met → whom: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- girl → met: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- girl → is: predicate (subject - verb)
- i → met: predicate (subject - verb)
- is → nice: predicate (verb/proposition - object)
- met → whom: predicate (verb/proposition - object)
- the → girl: constraint
- whom → girl: connection

**Generated Relations:**
- I → met: Predicate (subject - verb) (UD: nsubj)
- The → girl: Constraint (UD: det)
- girl → is: Predicate (subject - verb) (UD: nsubj→cop)
- girl → met: Connection (UD: acl:relcl)
- is → nice: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- whom → girl: Connection (UD: appos)

</details>

---

### Sentence 4
**Input:** The movie (that) we watched was amazing.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 6 | - |
| Generated Relations | 6 | - |
| Correct Relations | 5 | 83.3% |
| Missing Relations | 1 | 16.7% |
| Over-specified Relations | 1 | 16.7% |

**✅ Correct Relations:**
- movie → was: predicate (subject - verb)
- that → movie: connection
- the → movie: constraint
- was → amazing: predicate (verb/proposition - object)
- we → watched: predicate (subject - verb)

**❌ Missing Relations:**
- watched → that: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- movie → watched: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- movie → was: predicate (subject - verb)
- that → movie: connection
- the → movie: constraint
- was → amazing: predicate (verb/proposition - object)
- watched → that: predicate (verb/proposition - object)
- we → watched: predicate (subject - verb)

**Generated Relations:**
- The → movie: Constraint (UD: det)
- movie → was: Predicate (subject - verb) (UD: nsubj→cop)
- movie → watched: Connection (UD: acl:relcl)
- that → movie: Connection (UD: appos)
- was → amazing: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- we → watched: Predicate (subject - verb) (UD: nsubj)

</details>

---

### Sentence 5
**Input:** The man whose car broke down.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 5 | - |
| Generated Relations | 6 | - |
| Correct Relations | 5 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 1 | 16.7% |

**✅ Correct Relations:**
- broke → down: constraint
- car → broke: predicate (subject - verb)
- the → man: constraint
- whose → car: constraint
- whose → man: connection

**➕ Over-specified Relations:**
- man → broke: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- broke → down: constraint
- car → broke: predicate (subject - verb)
- the → man: constraint
- whose → car: constraint
- whose → man: connection

**Generated Relations:**
- The → man: Constraint (UD: det)
- broke → down: Constraint (UD: compound:prt)
- car → broke: Predicate (subject - verb) (UD: nsubj)
- man → broke: Connection (UD: acl:relcl)
- whose → car: Constraint (UD: nmod:poss)
- whose → car: Constraint (UD: whose→possessed_noun)
- whose → man: Connection (UD: whose→antecedent)

</details>

---

### Sentence 6
**Input:** The boy whose father is a doctor is my classmate.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 10 | - |
| Correct Relations | 9 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 1 | 10.0% |

**✅ Correct Relations:**
- a → doctor: constraint
- boy → is: predicate (subject - verb)
- father → is: predicate (subject - verb)
- is → classmate: predicate (verb/proposition - object)
- is → doctor: predicate (verb/proposition - object)
- my → classmate: constraint
- the → boy: constraint
- whose → boy: connection
- whose → father: constraint

**➕ Over-specified Relations:**
- boy → doctor: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- a → doctor: constraint
- boy → is: predicate (subject - verb)
- father → is: predicate (subject - verb)
- is → classmate: predicate (verb/proposition - object)
- is → doctor: predicate (verb/proposition - object)
- my → classmate: constraint
- the → boy: constraint
- whose → boy: connection
- whose → father: constraint

**Generated Relations:**
- The → boy: Constraint (UD: det)
- a → doctor: Constraint (UD: det)
- boy → doctor: Connection (UD: acl:relcl)
- boy → is: Predicate (subject - verb) (UD: nsubj→cop)
- father → is: Predicate (subject - verb) (UD: nsubj→cop)
- is → classmate: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- is → doctor: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- my → classmate: Constraint (UD: nmod:poss)
- whose → boy: Connection (UD: whose→antecedent)
- whose → father: Constraint (UD: nmod:poss)
- whose → father: Constraint (UD: whose→possessed_noun)

</details>

---

### Sentence 7
**Input:** 2018 was the year when I moved to Canada.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 4 | 44.4% |
| Missing Relations | 5 | 55.6% |
| Over-specified Relations | 4 | 50.0% |

**✅ Correct Relations:**
- 2018 → was: predicate (subject - verb)
- i → moved: predicate (subject - verb)
- the → year: constraint
- was → year: predicate (verb/proposition - object)

**❌ Missing Relations:**
- move → year: constraint
- moved → to: constraint
- to → canada: predicate (verb/proposition - object)
- when → moved: predicate (verb/proposition - object)
- when → year: constraint

**➕ Over-specified Relations:**
- moved → canada: predicate (verb - oblique)
- moved → year: constraint
- to → canada: predicate (preposition - object)
- when → moved: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- 2018 → was: predicate (subject - verb)
- i → moved: predicate (subject - verb)
- move → year: constraint
- moved → to: constraint
- the → year: constraint
- to → canada: predicate (verb/proposition - object)
- was → year: predicate (verb/proposition - object)
- when → moved: predicate (verb/proposition - object)
- when → year: constraint

**Generated Relations:**
- 2018 → was: Predicate (subject - verb) (UD: nsubj→cop)
- I → moved: Predicate (subject - verb) (UD: nsubj)
- moved → Canada: Predicate (verb - oblique) (UD: obl)
- moved → year: Constraint (UD: advcl)
- the → year: Constraint (UD: det)
- to → Canada: Predicate (preposition - object) (UD: case)
- was → year: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- when → moved: Constraint (UD: advmod)

</details>

---

### Sentence 8
**Input:** I remember the day when we met.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 6 | - |
| Correct Relations | 4 | 57.1% |
| Missing Relations | 3 | 42.9% |
| Over-specified Relations | 2 | 33.3% |

**✅ Correct Relations:**
- i → remember: predicate (subject - verb)
- remember → day: predicate (verb/proposition - object)
- the → day: constraint
- we → met: predicate (subject - verb)

**❌ Missing Relations:**
- met → day: constraint
- when → day: constraint
- when → met: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- met → remember: constraint
- when → met: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- i → remember: predicate (subject - verb)
- met → day: constraint
- remember → day: predicate (verb/proposition - object)
- the → day: constraint
- we → met: predicate (subject - verb)
- when → day: constraint
- when → met: predicate (verb/proposition - object)

**Generated Relations:**
- I → remember: Predicate (subject - verb) (UD: nsubj)
- met → remember: Constraint (UD: advcl)
- remember → day: Predicate (verb/proposition - object) (UD: obj)
- the → day: Constraint (UD: det)
- we → met: Predicate (subject - verb) (UD: nsubj)
- when → met: Constraint (UD: advmod)

</details>

---

### Sentence 9
**Input:** This is the place where we stayed.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 6 | - |
| Correct Relations | 4 | 57.1% |
| Missing Relations | 3 | 42.9% |
| Over-specified Relations | 2 | 33.3% |

**✅ Correct Relations:**
- is → place: predicate (verb/proposition - object)
- the → place: constraint
- this → is: predicate (subject - verb)
- we → stayed: predicate (subject - verb)

**❌ Missing Relations:**
- stayed → place: constraint
- where → place: constraint
- where → stayed: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- place → stayed: connection
- where → stayed: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- is → place: predicate (verb/proposition - object)
- stayed → place: constraint
- the → place: constraint
- this → is: predicate (subject - verb)
- we → stayed: predicate (subject - verb)
- where → place: constraint
- where → stayed: predicate (verb/proposition - object)

**Generated Relations:**
- This → is: Predicate (subject - verb) (UD: nsubj→cop)
- is → place: Predicate (verb/proposition - object) (UD: cop→pred_complement)
- place → stayed: Connection (UD: acl:relcl)
- the → place: Constraint (UD: det)
- we → stayed: Predicate (subject - verb) (UD: nsubj)
- where → stayed: Constraint (UD: advmod)

</details>

---

### Sentence 10
**Input:** I don’t know the reason why he left.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 8 | - |
| Correct Relations | 4 | 50.0% |
| Missing Relations | 4 | 50.0% |
| Over-specified Relations | 4 | 50.0% |

**✅ Correct Relations:**
- he → left: predicate (subject - verb)
- i → know: predicate (subject - verb)
- know → reason: predicate (verb/proposition - object)
- the → reason: constraint

**❌ Missing Relations:**
- don’t → know: constraint
- left → reason: constraint
- why → left: predicate (verb/proposition - object)
- why → reason: constraint

**➕ Over-specified Relations:**
- do → know: constraint
- n’t → know: constraint
- reason → left: connection
- why → left: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- don’t → know: constraint
- he → left: predicate (subject - verb)
- i → know: predicate (subject - verb)
- know → reason: predicate (verb/proposition - object)
- left → reason: constraint
- the → reason: constraint
- why → left: predicate (verb/proposition - object)
- why → reason: constraint

**Generated Relations:**
- I → know: Predicate (subject - verb) (UD: nsubj)
- do → know: Constraint (UD: aux)
- he → left: Predicate (subject - verb) (UD: nsubj)
- know → reason: Predicate (verb/proposition - object) (UD: obj)
- n’t → know: Constraint (UD: advmod)
- reason → left: Connection (UD: acl:relcl)
- the → reason: Constraint (UD: det)
- why → left: Constraint (UD: advmod)

</details>

---
