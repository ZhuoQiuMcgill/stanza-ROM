# ROM Evaluation Report

**Date:** 2025-05-22 22:37:24
**Total Sentences:** 18
**Processed Sentences:** 18
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics

| Metric                         | Value |
|--------------------------------|-------|
| Total Sentences Processed      | 18    |
| Total Expected Relations       | 132   |
| Total Generated Relations      | 131   |
| Total Correct Relations        | 74    |
| Total Missing Relations        | 58    |
| Total Over-specified Relations | 57    |

### Overall Performance

| Metric                      | Percentage |
|-----------------------------|------------|
| **Correct Rate**            | **56.1%**  |
| **Missing Rate**            | **43.9%**  |
| **Over-specification Rate** | **43.5%**  |

### Performance Interpretation

**Overall Performance:** 🟠 Fair

### Additional Metrics

| Metric    | Value | Description                                        |
|-----------|-------|----------------------------------------------------|
| Precision | 56.5% | Percentage of generated relations that are correct |
| Recall    | 56.1% | Percentage of expected relations that were found   |
| F1-Score  | 56.3% | Harmonic mean of precision and recall              |

---

## Individual Sentence Results

### Sentence 1

**Input:** What she said surprised everyone.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 4     | -     |
| Generated Relations      | 4     | -     |
| Correct Relations        | 3     | 75.0% |
| Missing Relations        | 1     | 25.0% |
| Over-specified Relations | 1     | 25.0% |

**✅ Correct Relations:**

- she → said: predicate (subject - verb)
- surprised → everyone: predicate (verb/proposition - object)
- what → surprised: predicate (subject - verb)

**❌ Missing Relations:**

- said → what: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- what → said: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- said → what: predicate (verb/proposition - object)
- she → said: predicate (subject - verb)
- surprised → everyone: predicate (verb/proposition - object)
- what → surprised: predicate (subject - verb)

**Generated Relations:**

- she → said: predicate (subject - verb)
- surprised → everyone: predicate (verb/proposition - object)
- what → said: connection
- what → surprised: predicate (subject - verb)

</details>

---

### Sentence 2

**Input:** That he lied was obvious.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 5     | -     |
| Generated Relations      | 3     | -     |
| Correct Relations        | 1     | 20.0% |
| Missing Relations        | 4     | 80.0% |
| Over-specified Relations | 2     | 66.7% |

**✅ Correct Relations:**

- he → lied: predicate (subject - verb)

**❌ Missing Relations:**

- lied → was: predicate (subject - verb)
- that → lied: connection
- that → was: predicate (subject - verb)
- was → obvious: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- lied → obvious: predicate (subject - verb)
- that → obvious: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- he → lied: predicate (subject - verb)
- lied → was: predicate (subject - verb)
- that → lied: connection
- that → was: predicate (subject - verb)
- was → obvious: predicate (verb/proposition - object)

**Generated Relations:**

- he → lied: predicate (subject - verb)
- lied → obvious: predicate (subject - verb)
- that → obvious: connection

</details>

---

### Sentence 3

**Input:** Whether we will win depends on our effort.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 3     | 37.5% |
| Missing Relations        | 5     | 62.5% |
| Over-specified Relations | 5     | 62.5% |

**✅ Correct Relations:**

- our → effort: constraint
- we → win: predicate (subject - verb)
- will → win: constraint

**❌ Missing Relations:**

- on → depends: constraint
- on → effort: predicate (verb/proposition - object)
- whether → depends: predicate (subject - verb)
- whether → win: predicate (verb/proposition - object)
- win → depends: predicate (subject - verb)

**➕ Over-specified Relations:**

- depends → effort: predicate (verb - oblique)
- on → effort: predicate (preposition - object)
- whether → depends: constraint
- whether → win: predicate (conjunction - clause_verb)
- win → depends: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- on → depends: constraint
- on → effort: predicate (verb/proposition - object)
- our → effort: constraint
- we → win: predicate (subject - verb)
- whether → depends: predicate (subject - verb)
- whether → win: predicate (verb/proposition - object)
- will → win: constraint
- win → depends: predicate (subject - verb)

**Generated Relations:**

- depends → effort: predicate (verb - oblique)
- on → effort: predicate (preposition - object)
- our → effort: constraint
- we → win: predicate (subject - verb)
- whether → depends: constraint
- whether → win: predicate (conjunction - clause_verb)
- will → win: constraint
- win → depends: constraint

</details>

---

### Sentence 4

**Input:** How she managed to escape is still a mystery.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 3     | 37.5% |
| Missing Relations        | 5     | 62.5% |
| Over-specified Relations | 5     | 62.5% |

**✅ Correct Relations:**

- a → mystery: constraint
- she → managed: predicate (subject - verb)
- to → managed: constraint

**❌ Missing Relations:**

- how → is: predicate (subject - verb)
- how → managed: constraint
- is → mystery: predicate (verb/proposition - object)
- still → is: constraint
- to → escape: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- how → mystery: constraint
- managed → escape: predicate (verb/proposition - object)
- managed → mystery: predicate (subject - verb)
- still → mystery: constraint
- to → escape: predicate (preposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- a → mystery: constraint
- how → is: predicate (subject - verb)
- how → managed: constraint
- is → mystery: predicate (verb/proposition - object)
- she → managed: predicate (subject - verb)
- still → is: constraint
- to → escape: predicate (verb/proposition - object)
- to → managed: constraint

**Generated Relations:**

- a → mystery: constraint
- how → mystery: constraint
- managed → escape: predicate (verb/proposition - object)
- managed → mystery: predicate (subject - verb)
- she → managed: predicate (subject - verb)
- still → mystery: constraint
- to → escape: predicate (preposition - object)
- to → managed: constraint

</details>

---

### Sentence 5

**Input:** When the meeting starts is still unknown.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 6     | -     |
| Generated Relations      | 5     | -     |
| Correct Relations        | 3     | 50.0% |
| Missing Relations        | 3     | 50.0% |
| Over-specified Relations | 2     | 40.0% |

**✅ Correct Relations:**

- meeting → starts: predicate (subject - verb)
- the → meeting: constraint
- when → starts: constraint

**❌ Missing Relations:**

- is → unknown: predicate (verb/proposition - object)
- still → is: constraint
- when → is: predicate (subject - verb)

**➕ Over-specified Relations:**

- starts → unknown: constraint
- still → unknown: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- is → unknown: predicate (verb/proposition - object)
- meeting → starts: predicate (subject - verb)
- still → is: constraint
- the → meeting: constraint
- when → is: predicate (subject - verb)
- when → starts: constraint

**Generated Relations:**

- meeting → starts: predicate (subject - verb)
- starts → unknown: constraint
- still → unknown: constraint
- the → meeting: constraint
- when → starts: constraint

</details>

---

### Sentence 6

**Input:** I know that she is right.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 5     | -     |
| Generated Relations      | 5     | -     |
| Correct Relations        | 3     | 60.0% |
| Missing Relations        | 2     | 40.0% |
| Over-specified Relations | 2     | 40.0% |

**✅ Correct Relations:**

- i → know: predicate (subject - verb)
- is → right: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)

**❌ Missing Relations:**

- know → is: predicate (verb/proposition - object)
- that → is: connection

**➕ Over-specified Relations:**

- know → right: predicate (verb/proposition - object)
- that → right: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- i → know: predicate (subject - verb)
- is → right: predicate (verb/proposition - object)
- know → is: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)
- that → is: connection

**Generated Relations:**

- i → know: predicate (subject - verb)
- is → right: predicate (verb/proposition - object)
- know → right: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)
- that → right: connection

</details>

---

### Sentence 7

**Input:** She didn’t tell me what had happened.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 4     | 57.1% |
| Missing Relations        | 3     | 42.9% |
| Over-specified Relations | 3     | 42.9% |

**✅ Correct Relations:**

- had → happened: constraint
- she → tell: predicate (subject - verb)
- tell → me: predicate (verb/proposition - object)
- what → happened: predicate (subject - verb)

**❌ Missing Relations:**

- didn’t → tell: constraint
- me → what: constraint
- tell → what: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- did → tell: constraint
- n’t → tell: constraint
- tell → happened: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- didn’t → tell: constraint
- had → happened: constraint
- me → what: constraint
- she → tell: predicate (subject - verb)
- tell → me: predicate (verb/proposition - object)
- tell → what: predicate (verb/proposition - object)
- what → happened: predicate (subject - verb)

**Generated Relations:**

- did → tell: constraint
- had → happened: constraint
- n’t → tell: constraint
- she → tell: predicate (subject - verb)
- tell → happened: predicate (verb/proposition - object)
- tell → me: predicate (verb/proposition - object)
- what → happened: predicate (subject - verb)

</details>

---

### Sentence 8

**Input:** We’re thinking about how we can solve the problem.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 10    | -     |
| Correct Relations        | 7     | 77.8% |
| Missing Relations        | 2     | 22.2% |
| Over-specified Relations | 3     | 30.0% |

**✅ Correct Relations:**

- about → thinking: constraint
- can → solve: constraint
- how → solve: constraint
- solve → problem: predicate (verb/proposition - object)
- the → problem: constraint
- we → solve: predicate (subject - verb)
- we → thinking: predicate (subject - verb)

**❌ Missing Relations:**

- about → how: predicate (verb/proposition - object)
- are → thinking: constraint

**➕ Over-specified Relations:**

- about → solve: predicate (conjunction - clause_verb)
- solve → thinking: constraint
- ’re → thinking: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- about → how: predicate (verb/proposition - object)
- about → thinking: constraint
- are → thinking: constraint
- can → solve: constraint
- how → solve: constraint
- solve → problem: predicate (verb/proposition - object)
- the → problem: constraint
- we → solve: predicate (subject - verb)
- we → thinking: predicate (subject - verb)

**Generated Relations:**

- about → solve: predicate (conjunction - clause_verb)
- about → thinking: constraint
- can → solve: constraint
- how → solve: constraint
- solve → problem: predicate (verb/proposition - object)
- solve → thinking: constraint
- the → problem: constraint
- we → solve: predicate (subject - verb)
- we → thinking: predicate (subject - verb)
- ’re → thinking: constraint

</details>

---

### Sentence 9

**Input:** He’s not sure if he locked the door.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 4     | 50.0% |
| Missing Relations        | 4     | 50.0% |
| Over-specified Relations | 4     | 50.0% |

**✅ Correct Relations:**

- he → locked: predicate (subject - verb)
- locked → door: predicate (verb/proposition - object)
- not → sure: constraint
- the → door: constraint

**❌ Missing Relations:**

- he → is: predicate (subject - verb)
- if → is: constraint
- if → locked: predicate (verb/proposition - object)
- is → sure: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- he → ’s: predicate (subject - verb)
- if → locked: connection
- sure → locked: predicate (verb/proposition - object)
- ’s → sure: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- he → is: predicate (subject - verb)
- he → locked: predicate (subject - verb)
- if → is: constraint
- if → locked: predicate (verb/proposition - object)
- is → sure: predicate (verb/proposition - object)
- locked → door: predicate (verb/proposition - object)
- not → sure: constraint
- the → door: constraint

**Generated Relations:**

- he → locked: predicate (subject - verb)
- he → ’s: predicate (subject - verb)
- if → locked: connection
- locked → door: predicate (verb/proposition - object)
- not → sure: constraint
- sure → locked: predicate (verb/proposition - object)
- the → door: constraint
- ’s → sure: predicate (verb/proposition - object)

</details>

---

### Sentence 10

**Input:** I don’t know when the package will arrive.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 5     | 62.5% |
| Missing Relations        | 3     | 37.5% |
| Over-specified Relations | 3     | 37.5% |

**✅ Correct Relations:**

- i → know: predicate (subject - verb)
- package → arrive: predicate (subject - verb)
- the → package: constraint
- when → arrive: constraint
- will → arrive: constraint

**❌ Missing Relations:**

- don’t → know: constraint
- know → arrive: predicate (verb/proposition - object)
- when → know: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- arrive → know: constraint
- do → know: constraint
- n’t → know: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- don’t → know: constraint
- i → know: predicate (subject - verb)
- know → arrive: predicate (verb/proposition - object)
- package → arrive: predicate (subject - verb)
- the → package: constraint
- when → arrive: constraint
- when → know: predicate (verb/proposition - object)
- will → arrive: constraint

**Generated Relations:**

- arrive → know: constraint
- do → know: constraint
- i → know: predicate (subject - verb)
- n’t → know: constraint
- package → arrive: predicate (subject - verb)
- the → package: constraint
- when → arrive: constraint
- will → arrive: constraint

</details>

---

### Sentence 11

**Input:** The truth is that she never left.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 5     | 71.4% |
| Missing Relations        | 2     | 28.6% |
| Over-specified Relations | 2     | 28.6% |

**✅ Correct Relations:**

- is → left: predicate (verb/proposition - object)
- never → left: constraint
- that → left: connection
- the → truth: constraint
- truth → is: predicate (subject - verb)

**❌ Missing Relations:**

- is → that: predicate (verb/proposition - object)
- she → left: predicate (subject - verb)

**➕ Over-specified Relations:**

- she → is: predicate (subject - verb)
- truth → left: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- is → left: predicate (verb/proposition - object)
- is → that: predicate (verb/proposition - object)
- never → left: constraint
- she → left: predicate (subject - verb)
- that → left: connection
- the → truth: constraint
- truth → is: predicate (subject - verb)

**Generated Relations:**

- is → left: predicate (verb/proposition - object)
- never → left: constraint
- she → is: predicate (subject - verb)
- that → left: connection
- the → truth: constraint
- truth → is: predicate (subject - verb)
- truth → left: predicate (subject - verb)

</details>

---

### Sentence 12

**Input:** My suggestion is that we take a break.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 6     | 75.0% |
| Missing Relations        | 2     | 25.0% |
| Over-specified Relations | 2     | 25.0% |

**✅ Correct Relations:**

- a → break: constraint
- is → take: predicate (verb/proposition - object)
- my → suggestion: constraint
- suggestion → is: predicate (subject - verb)
- take → break: predicate (verb/proposition - object)
- that → take: connection

**❌ Missing Relations:**

- is → that: predicate (verb/proposition - object)
- we → take: predicate (subject - verb)

**➕ Over-specified Relations:**

- suggestion → take: predicate (subject - verb)
- we → is: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- a → break: constraint
- is → take: predicate (verb/proposition - object)
- is → that: predicate (verb/proposition - object)
- my → suggestion: constraint
- suggestion → is: predicate (subject - verb)
- take → break: predicate (verb/proposition - object)
- that → take: connection
- we → take: predicate (subject - verb)

**Generated Relations:**

- a → break: constraint
- is → take: predicate (verb/proposition - object)
- my → suggestion: constraint
- suggestion → is: predicate (subject - verb)
- suggestion → take: predicate (subject - verb)
- take → break: predicate (verb/proposition - object)
- that → take: connection
- we → is: predicate (subject - verb)

</details>

---

### Sentence 13

**Input:** The problem is how we can get there.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 4     | 50.0% |
| Missing Relations        | 4     | 50.0% |
| Over-specified Relations | 4     | 50.0% |

**✅ Correct Relations:**

- can → get: constraint
- how → get: constraint
- problem → is: predicate (subject - verb)
- the → problem: constraint

**❌ Missing Relations:**

- get → there: predicate (verb/proposition - object)
- how → is: connection
- is → how: predicate (verb/proposition - object)
- we → get: predicate (subject - verb)

**➕ Over-specified Relations:**

- is → get: predicate (verb/proposition - object)
- problem → get: predicate (subject - verb)
- there → get: constraint
- we → is: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- can → get: constraint
- get → there: predicate (verb/proposition - object)
- how → get: constraint
- how → is: connection
- is → how: predicate (verb/proposition - object)
- problem → is: predicate (subject - verb)
- the → problem: constraint
- we → get: predicate (subject - verb)

**Generated Relations:**

- can → get: constraint
- how → get: constraint
- is → get: predicate (verb/proposition - object)
- problem → get: predicate (subject - verb)
- problem → is: predicate (subject - verb)
- the → problem: constraint
- there → get: constraint
- we → is: predicate (subject - verb)

</details>

---

### Sentence 14

**Input:** The question is whether he will accept the offer.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 9     | -     |
| Correct Relations        | 5     | 62.5% |
| Missing Relations        | 3     | 37.5% |
| Over-specified Relations | 4     | 44.4% |

**✅ Correct Relations:**

- accept → offer: predicate (verb/proposition - object)
- question → is: predicate (subject - verb)
- the → offer: constraint
- the → question: constraint
- will → accept: constraint

**❌ Missing Relations:**

- he → accept: predicate (subject - verb)
- is → whether: predicate (verb/proposition - object)
- whether → accept: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- he → is: predicate (subject - verb)
- is → accept: predicate (verb/proposition - object)
- question → accept: predicate (subject - verb)
- whether → accept: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- accept → offer: predicate (verb/proposition - object)
- he → accept: predicate (subject - verb)
- is → whether: predicate (verb/proposition - object)
- question → is: predicate (subject - verb)
- the → offer: constraint
- the → question: constraint
- whether → accept: predicate (verb/proposition - object)
- will → accept: constraint

**Generated Relations:**

- accept → offer: predicate (verb/proposition - object)
- he → is: predicate (subject - verb)
- is → accept: predicate (verb/proposition - object)
- question → accept: predicate (subject - verb)
- question → is: predicate (subject - verb)
- the → offer: constraint
- the → question: constraint
- whether → accept: connection
- will → accept: constraint

</details>

---

### Sentence 15

**Input:** I heard the news that she got married.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 3     | 42.9% |
| Missing Relations        | 4     | 57.1% |
| Over-specified Relations | 4     | 57.1% |

**✅ Correct Relations:**

- heard → news: predicate (verb/proposition - object)
- i → heard: predicate (subject - verb)
- the → news: constraint

**❌ Missing Relations:**

- got → married: predicate (verb/proposition - object)
- she → got: predicate (subject - verb)
- that → got: predicate (verb/proposition - object)
- that → news: constraint

**➕ Over-specified Relations:**

- got → married: constraint
- married → news: constraint
- she → married: predicate (subject - verb)
- that → married: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- got → married: predicate (verb/proposition - object)
- heard → news: predicate (verb/proposition - object)
- i → heard: predicate (subject - verb)
- she → got: predicate (subject - verb)
- that → got: predicate (verb/proposition - object)
- that → news: constraint
- the → news: constraint

**Generated Relations:**

- got → married: constraint
- heard → news: predicate (verb/proposition - object)
- i → heard: predicate (subject - verb)
- married → news: constraint
- she → married: predicate (subject - verb)
- that → married: connection
- the → news: constraint

</details>

---

### Sentence 16

**Input:** The idea that hard work brings success is widely accepted.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 9     | -     |
| Correct Relations        | 5     | 55.6% |
| Missing Relations        | 4     | 44.4% |
| Over-specified Relations | 4     | 44.4% |

**✅ Correct Relations:**

- brings → success: predicate (verb/proposition - object)
- hard → work: constraint
- the → idea: constraint
- widely → accepted: constraint
- work → brings: predicate (subject - verb)

**❌ Missing Relations:**

- idea → is: predicate (subject - verb)
- is → accepted: predicate (verb/proposition - object)
- that → brings: predicate (verb/proposition - object)
- that → idea: constraint

**➕ Over-specified Relations:**

- brings → idea: constraint
- idea → accepted: predicate (subject - verb)
- is → accepted: constraint
- that → brings: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- brings → success: predicate (verb/proposition - object)
- hard → work: constraint
- idea → is: predicate (subject - verb)
- is → accepted: predicate (verb/proposition - object)
- that → brings: predicate (verb/proposition - object)
- that → idea: constraint
- the → idea: constraint
- widely → accepted: constraint
- work → brings: predicate (subject - verb)

**Generated Relations:**

- brings → idea: constraint
- brings → success: predicate (verb/proposition - object)
- hard → work: constraint
- idea → accepted: predicate (subject - verb)
- is → accepted: constraint
- that → brings: connection
- the → idea: constraint
- widely → accepted: constraint
- work → brings: predicate (subject - verb)

</details>

---

### Sentence 17

**Input:** She rejected the suggestion that we cancel the meeting.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 6     | 75.0% |
| Missing Relations        | 2     | 25.0% |
| Over-specified Relations | 2     | 25.0% |

**✅ Correct Relations:**

- cancel → meeting: predicate (verb/proposition - object)
- rejected → suggestion: predicate (verb/proposition - object)
- she → rejected: predicate (subject - verb)
- the → meeting: constraint
- the → suggestion: constraint
- we → cancel: predicate (subject - verb)

**❌ Missing Relations:**

- that → cancel: predicate (verb/proposition - object)
- that → suggestion: constraint

**➕ Over-specified Relations:**

- cancel → suggestion: constraint
- that → cancel: connection

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- cancel → meeting: predicate (verb/proposition - object)
- rejected → suggestion: predicate (verb/proposition - object)
- she → rejected: predicate (subject - verb)
- that → cancel: predicate (verb/proposition - object)
- that → suggestion: constraint
- the → meeting: constraint
- the → suggestion: constraint
- we → cancel: predicate (subject - verb)

**Generated Relations:**

- cancel → meeting: predicate (verb/proposition - object)
- cancel → suggestion: constraint
- rejected → suggestion: predicate (verb/proposition - object)
- she → rejected: predicate (subject - verb)
- that → cancel: connection
- the → meeting: constraint
- the → suggestion: constraint
- we → cancel: predicate (subject - verb)

</details>

---

### Sentence 18

**Input:** We faced the fact that we were out of time.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 9     | -     |
| Correct Relations        | 4     | 44.4% |
| Missing Relations        | 5     | 55.6% |
| Over-specified Relations | 5     | 55.6% |

**✅ Correct Relations:**

- faced → fact: predicate (verb/proposition - object)
- the → fact: constraint
- we → faced: predicate (subject - verb)
- we → were: predicate (subject - verb)

**❌ Missing Relations:**

- of → time: predicate (verb/proposition - object)
- out → of: constraint
- that → fact: constraint
- that → were: predicate (verb/proposition - object)
- were → out: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- of → time: predicate (preposition - object)
- out → time: predicate (preposition - object)
- that → time: connection
- time → fact: constraint
- were → time: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- faced → fact: predicate (verb/proposition - object)
- of → time: predicate (verb/proposition - object)
- out → of: constraint
- that → fact: constraint
- that → were: predicate (verb/proposition - object)
- the → fact: constraint
- we → faced: predicate (subject - verb)
- we → were: predicate (subject - verb)
- were → out: predicate (verb/proposition - object)

**Generated Relations:**

- faced → fact: predicate (verb/proposition - object)
- of → time: predicate (preposition - object)
- out → time: predicate (preposition - object)
- that → time: connection
- the → fact: constraint
- time → fact: constraint
- we → faced: predicate (subject - verb)
- we → were: predicate (subject - verb)
- were → time: predicate (verb/proposition - object)

</details>

---
