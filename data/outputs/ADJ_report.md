# ROM Evaluation Report

**Date:** 2025-05-22 22:13:52
**Total Sentences:** 10
**Processed Sentences:** 10
**Skipped Sentences:** 0

## Individual Sentence Results

### Sentence 1
**Input:** The boy who sings is my friend.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 7 | - |
| Correct Relations | 7 | 87.5% |
| Missing Relations | 1 | 12.5% |
| Over-specified Relations | 0 | 0.0% |

**✅ Correct Relations:**
- boy → is: predicate (subject - verb)
- boy → sings: predicate (subject - verb)
- is → friend: predicate (verb/proposition - object)
- my → friend: constraint
- the → boy: constraint
- who → boy: connection
- who → sings: predicate (subject - verb)

**❌ Missing Relations:**
- the → friend: constraint

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
- boy → is: predicate (subject - verb)
- boy → sings: predicate (subject - verb)
- is → friend: predicate (verb/proposition - object)
- my → friend: constraint
- the → boy: constraint
- who → boy: connection
- who → sings: predicate (subject - verb)

</details>

---

### Sentence 2
**Input:** The artist who painted this is famous.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 7 | - |
| Correct Relations | 7 | 100.0% |
| Missing Relations | 0 | 0.0% |
| Over-specified Relations | 0 | 0.0% |

**✅ Correct Relations:**
- artist → is: predicate (subject - verb)
- artist → painted: predicate (subject - verb)
- is → famous: predicate (verb/proposition - object)
- painted → this: predicate (verb/proposition - object)
- the → artist: constraint
- who → artist: connection
- who → painted: predicate (subject - verb)

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
- artist → is: predicate (subject - verb)
- artist → painted: predicate (subject - verb)
- is → famous: predicate (verb/proposition - object)
- painted → this: predicate (verb/proposition - object)
- the → artist: constraint
- who → artist: connection
- who → painted: predicate (subject - verb)

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
- girl → met: predicate (subject - verb)

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
- girl → is: predicate (subject - verb)
- girl → met: predicate (subject - verb)
- i → met: predicate (subject - verb)
- is → nice: predicate (verb/proposition - object)
- the → girl: constraint
- whom → girl: connection

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
- movie → watched: predicate (subject - verb)

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
- movie → was: predicate (subject - verb)
- movie → watched: predicate (subject - verb)
- that → movie: connection
- the → movie: constraint
- was → amazing: predicate (verb/proposition - object)
- we → watched: predicate (subject - verb)

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
- man → broke: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**
- broke → down: constraint
- car → broke: predicate (subject - verb)
- the → man: constraint
- whose → car: constraint
- whose → man: connection

**Generated Relations:**
- broke → down: constraint
- car → broke: predicate (subject - verb)
- man → broke: predicate (subject - verb)
- the → man: constraint
- whose → car: constraint
- whose → man: connection

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
- boy → doctor: predicate (subject - verb)

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
- a → doctor: constraint
- boy → doctor: predicate (subject - verb)
- boy → is: predicate (subject - verb)
- father → is: predicate (subject - verb)
- is → classmate: predicate (verb/proposition - object)
- is → doctor: predicate (verb/proposition - object)
- my → classmate: constraint
- the → boy: constraint
- whose → boy: connection
- whose → father: constraint

</details>

---

### Sentence 7
**Input:** 2018 was the year when I moved to Canada.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 5 | 55.6% |
| Missing Relations | 4 | 44.4% |
| Over-specified Relations | 3 | 37.5% |

**✅ Correct Relations:**
- 2018 → was: predicate (subject - verb)
- i → moved: predicate (subject - verb)
- the → year: constraint
- to → canada: predicate (verb/proposition - object)
- was → year: predicate (verb/proposition - object)

**❌ Missing Relations:**
- move → year: constraint
- moved → to: constraint
- when → moved: predicate (verb/proposition - object)
- when → year: constraint

**➕ Over-specified Relations:**
- moved → canada: predicate (verb/proposition - object)
- moved → year: constraint
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
- 2018 → was: predicate (subject - verb)
- i → moved: predicate (subject - verb)
- moved → canada: predicate (verb/proposition - object)
- moved → year: constraint
- the → year: constraint
- to → canada: predicate (verb/proposition - object)
- was → year: predicate (verb/proposition - object)
- when → moved: constraint

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
- i → remember: predicate (subject - verb)
- met → remember: constraint
- remember → day: predicate (verb/proposition - object)
- the → day: constraint
- we → met: predicate (subject - verb)
- when → met: constraint

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
- place → stayed: predicate (subject - verb)
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
- is → place: predicate (verb/proposition - object)
- place → stayed: predicate (subject - verb)
- the → place: constraint
- this → is: predicate (subject - verb)
- we → stayed: predicate (subject - verb)
- where → stayed: constraint

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
- know → do: constraint
- n’t → know: constraint
- reason → left: predicate (subject - verb)
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
- he → left: predicate (subject - verb)
- i → know: predicate (subject - verb)
- know → do: constraint
- know → reason: predicate (verb/proposition - object)
- n’t → know: constraint
- reason → left: predicate (subject - verb)
- the → reason: constraint
- why → left: constraint

</details>

---

## 📊 Total Data Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 10 |
| Total Expected Relations | 72 |
| Total Generated Relations | 70 |
| Total Correct Relations | 55 |
| Total Missing Relations | 17 |
| Total Over-specified Relations | 15 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **76.4%** |
| **Missing Rate** | **23.6%** |
| **Over-specification Rate** | **21.4%** |

### Performance Interpretation
**Overall Performance:** 🟡 Good

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 78.6% | Percentage of generated relations that are correct |
| Recall | 76.4% | Percentage of expected relations that were found |
| F1-Score | 77.5% | Harmonic mean of precision and recall |