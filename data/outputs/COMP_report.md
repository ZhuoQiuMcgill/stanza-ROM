# ROM Evaluation Report

**Date:** 2025-05-22 22:14:03
**Total Sentences:** 23
**Processed Sentences:** 23
**Skipped Sentences:** 0

## Individual Sentence Results

### Sentence 1
**Input:** She wanted to go for a walk, but it started raining.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 10 | - |
| Correct Relations | 3 | 27.3% |
| Missing Relations | 8 | 72.7% |
| Over-specified Relations | 7 | 70.0% |

**✅ Correct Relations:**
- a → walk: constraint
- it → started: predicate (subject - verb)
- she → wanted: predicate (subject - verb)

**❌ Missing Relations:**
- but → started: predicate (verb/preposition - object)
- but → wanted: constraint
- for → go: constraint
- for → walk: predicate (preposition - object)
- go → walk: predicate (verb/preposition - object)
- started → raining: predicate (verb/preposition - object)
- to → go: predicate (verb/preposition - object)
- to → wanted: constraint

**➕ Over-specified Relations:**
- but → started: connection
- for → walk: predicate (verb/proposition - object)
- go → walk: predicate (verb/proposition - object)
- started → raining: predicate (verb/proposition - object)
- started → wanted: connection
- to → go: constraint
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
- a → walk: constraint
- but → started: connection
- for → walk: predicate (verb/proposition - object)
- go → walk: predicate (verb/proposition - object)
- it → started: predicate (subject - verb)
- she → wanted: predicate (subject - verb)
- started → raining: predicate (verb/proposition - object)
- started → wanted: connection
- to → go: constraint
- wanted → go: predicate (verb/proposition - object)

</details>

---

### Sentence 2
**Input:** The sky was clear; we decided to go stargazing.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 9 | - |
| Correct Relations | 3 | 33.3% |
| Missing Relations | 6 | 66.7% |
| Over-specified Relations | 6 | 66.7% |

**✅ Correct Relations:**
- sky → was: predicate (subject - verb)
- the → sky: constraint
- we → decided: predicate (subject - verb)

**❌ Missing Relations:**
- [∅] → decided: connection
- [∅] → was: connection (semicolon as structural connector)
- go → stargazing: predicate (verb/preposition - object)
- to → decided: constraint
- to → go: predicate (verb/preposition - object)
- was → clear: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- decided → clear: connection
- decided → go: predicate (verb/proposition - object)
- go → stargazing: predicate (verb/proposition - object)
- to → go: constraint
- to → stargazing: predicate (verb/proposition - object)
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
- decided → clear: connection
- decided → go: predicate (verb/proposition - object)
- go → stargazing: predicate (verb/proposition - object)
- sky → was: predicate (subject - verb)
- the → sky: constraint
- to → go: constraint
- to → stargazing: predicate (verb/proposition - object)
- was → clear: predicate (verb/proposition - object)
- we → decided: predicate (subject - verb)

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
- however → kept: constraint
- i → kept: predicate (subject - verb)
- i → was: predicate (subject - verb)
- kept → tired: connection
- kept → working: predicate (verb/proposition - object)
- was → tired: predicate (verb/proposition - object)

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
- and → creative: connection
- both → and: connection
- both → smart: constraint
- creative → smart: connection
- is → smart: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)

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
- both → brother: constraint
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
- and → sister: connection
- are → engineers: predicate (verb/proposition - object)
- both → and: connection
- both → brother: constraint
- brother → are: predicate (subject - verb)
- my → brother: constraint
- sister → brother: connection

</details>

---

### Sentence 6
**Input:** Not only did he win, but he also broke the record.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 7 | - |
| Generated Relations | 11 | - |
| Correct Relations | 3 | 42.9% |
| Missing Relations | 4 | 57.1% |
| Over-specified Relations | 8 | 72.7% |

**✅ Correct Relations:**
- he → broke: predicate (subject - verb)
- not only → but also: connection
- the → record: constraint

**❌ Missing Relations:**
- broke → record: predicate (verb/preposition - object)
- but also → broke: predicate (verb/preposition - object)
- he → won: predicate (subject - verb)
- not only → won: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- also → broke: constraint
- broke → record: predicate (verb/proposition - object)
- broke → win: connection
- but → broke: connection
- he → win: predicate (subject - verb)
- not → win: constraint
- only → win: constraint
- win → did: constraint

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
- also → broke: constraint
- broke → record: predicate (verb/proposition - object)
- broke → win: connection
- but → broke: connection
- he → broke: predicate (subject - verb)
- he → win: predicate (subject - verb)
- not → win: constraint
- not only → but also: connection
- only → win: constraint
- the → record: constraint
- win → did: constraint

</details>

---

### Sentence 7
**Input:** The movie was not only long but also boring.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 9 | - |
| Correct Relations | 3 | 33.3% |
| Missing Relations | 6 | 66.7% |
| Over-specified Relations | 6 | 66.7% |

**✅ Correct Relations:**
- movie → was: predicate (subject - verb)
- not only → but also: connection
- the → movie: constraint

**❌ Missing Relations:**
- but also → boring: predicate (verb/preposition - object)
- but also → was: constraint
- not only → long: predicate (verb/preposition - object)
- not only → was: constraint
- was → boring: predicate (verb/preposition - object)
- was → long: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- also → boring: constraint
- boring → long: connection
- but → boring: connection
- not → long: constraint
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
- also → boring: constraint
- boring → long: connection
- but → boring: connection
- movie → was: predicate (subject - verb)
- not → long: constraint
- not only → but also: connection
- only → long: constraint
- the → movie: constraint
- was → long: predicate (verb/proposition - object)

</details>

---

### Sentence 8
**Input:** You can either stay home or come with us.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 19 | - |
| Generated Relations | 8 | - |
| Correct Relations | 1 | 5.3% |
| Missing Relations | 18 | 94.7% |
| Over-specified Relations | 7 | 87.5% |

**✅ Correct Relations:**
- you → stay: predicate (subject - verb)

**❌ Missing Relations:**
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

**➕ Over-specified Relations:**
- come → stay: connection
- come → us: predicate (verb/proposition - object)
- either → stay: constraint
- home → stay: constraint
- or → come: connection
- stay → can: constraint
- with → us: predicate (verb/proposition - object)

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
- come → stay: connection
- come → us: predicate (verb/proposition - object)
- either → stay: constraint
- home → stay: constraint
- or → come: connection
- stay → can: constraint
- with → us: predicate (verb/proposition - object)
- you → stay: predicate (subject - verb)

</details>

---

### Sentence 9
**Input:** Neither did he apologize, nor did he show any regret.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 9 | - |
| Correct Relations | 3 | 27.3% |
| Missing Relations | 8 | 72.7% |
| Over-specified Relations | 6 | 66.7% |

**✅ Correct Relations:**
- any → regret: constraint
- he → apologize: predicate (subject - verb)
- he → show: predicate (subject - verb)

**❌ Missing Relations:**
- did → apologize: constraint
- did → show: constraint
- neither → apologize: predicate (verb/preposition - object)
- neither → nor: connection
- nor → show: predicate (verb/preposition - object)
- not → apologize: constraint
- not → show: constraint
- show → regret: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- apologize → did: constraint
- neither → apologize: constraint
- nor → show: connection
- show → apologize: connection
- show → did: constraint
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
- any → regret: constraint
- apologize → did: constraint
- he → apologize: predicate (subject - verb)
- he → show: predicate (subject - verb)
- neither → apologize: constraint
- nor → show: connection
- show → apologize: connection
- show → did: constraint
- show → regret: predicate (verb/proposition - object)

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
- call → ’ll: constraint
- know → call: predicate (verb/proposition - object)
- know → do: constraint
- n't → know: constraint
- or → text: connection
- text → call: connection
- whether → call: predicate (verb/proposition - object)

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
- call → ’ll: constraint
- he → call: predicate (subject - verb)
- i → know: predicate (subject - verb)
- know → call: predicate (verb/proposition - object)
- know → do: constraint
- n't → know: constraint
- or → text: connection
- text → call: connection
- whether → call: predicate (verb/proposition - object)

</details>

---

### Sentence 11
**Input:** She’s unsure whether to accept the job or continue studying.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 11 | - |
| Correct Relations | 1 | 8.3% |
| Missing Relations | 11 | 91.7% |
| Over-specified Relations | 10 | 90.9% |

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
- to → accept: constraint
- to → continue: predicate (verb/proposition - object)
- unsure → accept: predicate (verb/proposition - object)
- whether → accept: predicate (verb/proposition - object)
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
- accept → job: predicate (verb/proposition - object)
- continue → accept: connection
- continue → studying: predicate (verb/proposition - object)
- or → continue: connection
- she → ’s: predicate (subject - verb)
- the → job: constraint
- to → accept: constraint
- to → continue: predicate (verb/proposition - object)
- unsure → accept: predicate (verb/proposition - object)
- whether → accept: predicate (verb/proposition - object)
- ’s → unsure: predicate (verb/proposition - object)

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
- as → brother: predicate (verb/proposition - object)
- as → tall: constraint
- she → ’s: predicate (subject - verb)
- tall → brother: predicate (verb/proposition - object)
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
- as → as: connection
- as → brother: predicate (verb/proposition - object)
- as → tall: constraint
- her → brother: constraint
- she → ’s: predicate (subject - verb)
- tall → brother: predicate (verb/proposition - object)
- ’s → tall: predicate (verb/proposition - object)

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
- as → athlete: predicate (verb/proposition - object)
- as → quickly: constraint
- ran → athlete: predicate (verb/proposition - object)

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
- a → athlete: constraint
- as → as: connection
- as → athlete: predicate (verb/proposition - object)
- as → quickly: constraint
- he → ran: predicate (subject - verb)
- professional → athlete: constraint
- quickly → ran: constraint
- ran → athlete: predicate (verb/proposition - object)

</details>

---

### Sentence 14
**Input:** This task is not as easy as it looks.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 9 | - |
| Correct Relations | 4 | 40.0% |
| Missing Relations | 6 | 60.0% |
| Over-specified Relations | 5 | 55.6% |

**✅ Correct Relations:**
- it → looks: predicate (subject - verb)
- not → easy: constraint
- task → is: predicate (subject - verb)
- this → task: constraint

**❌ Missing Relations:**
- as → as (2): connection
- as → easy: predicate (verb/preposition - object)
- as → is: constraint
- as (2) → easy: constraint
- as (2) → looks: predicate (verb/preposition - object)
- is → easy: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- as → as: connection
- as → easy: constraint
- as → looks: constraint
- is → easy: predicate (verb/proposition - object)
- looks → easy: constraint

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
- as → as: connection
- as → easy: constraint
- as → looks: constraint
- is → easy: predicate (verb/proposition - object)
- it → looks: predicate (subject - verb)
- looks → easy: constraint
- not → easy: constraint
- task → is: predicate (subject - verb)
- this → task: constraint

</details>

---

### Sentence 15
**Input:** He doesn’t eat as much chocolate as his brother.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 10 | - |
| Correct Relations | 3 | 30.0% |
| Missing Relations | 7 | 70.0% |
| Over-specified Relations | 7 | 70.0% |

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
- as → brother: predicate (verb/proposition - object)
- as → much: constraint
- eat → brother: predicate (verb/proposition - object)
- eat → chocolate: predicate (verb/proposition - object)
- eat → does: constraint
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
- as → as: connection
- as → brother: predicate (verb/proposition - object)
- as → much: constraint
- eat → brother: predicate (verb/proposition - object)
- eat → chocolate: predicate (verb/proposition - object)
- eat → does: constraint
- he → eat: predicate (subject - verb)
- his → brother: constraint
- much → chocolate: constraint
- n’t → eat: constraint

</details>

---

### Sentence 16
**Input:** She enjoys painting as much as she enjoys dancing.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 10 | - |
| Generated Relations | 8 | - |
| Correct Relations | 2 | 20.0% |
| Missing Relations | 8 | 80.0% |
| Over-specified Relations | 6 | 75.0% |

**✅ Correct Relations:**
- as → enjoys: constraint
- she → enjoys: predicate (subject - verb)

**❌ Missing Relations:**
- as → as (2): connection
- as → much: predicate (verb/preposition - object)
- as (2) → enjoys: predicate (verb/preposition - object)
- as (2) → much: constraint
- enjoys → dancing: predicate (verb/preposition - object) (second clause)
- enjoys → painting: predicate (verb/preposition - object)
- much → painting: constraint
- she → enjoys: predicate (subject - verb) (second clause)

**➕ Over-specified Relations:**
- as → as: connection
- as → much: constraint
- enjoys → dancing: predicate (verb/proposition - object)
- enjoys → much: constraint
- enjoys → painting: predicate (verb/proposition - object)
- much → enjoys: constraint

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
- as → as: connection
- as → enjoys: constraint
- as → much: constraint
- enjoys → dancing: predicate (verb/proposition - object)
- enjoys → much: constraint
- enjoys → painting: predicate (verb/proposition - object)
- much → enjoys: constraint
- she → enjoys: predicate (subject - verb)

</details>

---

### Sentence 17
**Input:** Just as the moon affects the tides, so does the sun influence them.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 12 | - |
| Correct Relations | 6 | 50.0% |
| Missing Relations | 6 | 50.0% |
| Over-specified Relations | 6 | 50.0% |

**✅ Correct Relations:**
- as → affects: constraint
- moon → affects: predicate (subject - verb)
- sun → influence: predicate (subject - verb)
- the → moon: constraint
- the → sun: constraint
- the → tides: constraint

**❌ Missing Relations:**
- affects → tides: predicate (verb/preposition - object)
- as → so: connection
- does → influence: constraint
- influence → them: predicate (verb/preposition - object)
- just → as: constraint
- so → influence: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- affects → influence: constraint
- affects → tides: predicate (verb/proposition - object)
- influence → does: constraint
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
- affects → influence: constraint
- affects → tides: predicate (verb/proposition - object)
- as → affects: constraint
- influence → does: constraint
- influence → them: predicate (verb/proposition - object)
- just → affects: constraint
- moon → affects: predicate (subject - verb)
- so → influence: constraint
- sun → influence: predicate (subject - verb)
- the → moon: constraint
- the → sun: constraint
- the → tides: constraint

</details>

---

### Sentence 18
**Input:** Just as honesty builds trust, so does kindness.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 2 | 22.2% |
| Missing Relations | 7 | 77.8% |
| Over-specified Relations | 5 | 71.4% |

**✅ Correct Relations:**
- as → builds: constraint
- honesty → builds: predicate (subject - verb)

**❌ Missing Relations:**
- as → so: connection
- builds → trust: predicate (verb/preposition - object)
- builds → trust: predicate (verb/preposition - object) (implied)
- does → builds: constraint
- just → so: constraint
- kindness → builds: predicate (subject - verb)
- so → builds: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
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
- as → builds: constraint
- builds → does: constraint
- builds → trust: predicate (verb/proposition - object)
- does → kindness: predicate (verb/proposition - object)
- honesty → builds: predicate (subject - verb)
- just → builds: constraint
- so → does: constraint

</details>

---

### Sentence 19
**Input:** Just as we need water to survive, so do plants need sunlight.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 11 | - |
| Correct Relations | 4 | 36.4% |
| Missing Relations | 7 | 63.6% |
| Over-specified Relations | 7 | 63.6% |

**✅ Correct Relations:**
- as → need: constraint
- plants → need: predicate (subject - verb)
- to → survive: constraint
- we → need: predicate (subject - verb)

**❌ Missing Relations:**
- as → so: connection
- do → need: constraint
- just → so: constraint
- need → sunlight: predicate (verb/preposition - object)
- need → water: predicate (verb/preposition - object)
- so → need: predicate (verb/preposition - object)
- water → survive: constraint

**➕ Over-specified Relations:**
- just → need: constraint
- need → do: constraint
- need → need: constraint
- need → sunlight: predicate (verb/proposition - object)
- need → survive: predicate (verb/proposition - object)
- need → water: predicate (verb/proposition - object)
- so → need: constraint

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
- as → need: constraint
- just → need: constraint
- need → do: constraint
- need → need: constraint
- need → sunlight: predicate (verb/proposition - object)
- need → survive: predicate (verb/proposition - object)
- need → water: predicate (verb/proposition - object)
- plants → need: predicate (subject - verb)
- so → need: constraint
- to → survive: constraint
- we → need: predicate (subject - verb)

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
- no → sooner: constraint
- phone → rang: predicate (subject - verb)
- rang → sat: constraint
- sat → down: constraint
- sat → had: constraint
- she → sat: predicate (subject - verb)
- sooner → sat: constraint
- than → rang: constraint
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
- no → sooner: constraint
- phone → rang: predicate (subject - verb)
- rang → sat: constraint
- sat → down: constraint
- sat → had: constraint
- she → sat: predicate (subject - verb)
- sooner → sat: constraint
- than → rang: constraint
- the → phone: constraint

</details>

---

### Sentence 21
**Input:** I’d rather read a book than watch TV.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 3 | 33.3% |
| Missing Relations | 6 | 66.7% |
| Over-specified Relations | 5 | 62.5% |

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
- read → ’d: constraint
- than → watch: constraint
- watch → read: constraint
- watch → tv: predicate (verb/proposition - object)

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
- a → book: constraint
- i → read: predicate (subject - verb)
- rather → read: constraint
- read → book: predicate (verb/proposition - object)
- read → ’d: constraint
- than → watch: constraint
- watch → read: constraint
- watch → tv: predicate (verb/proposition - object)

</details>

---

### Sentence 22
**Input:** He chose to walk rather than drive.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 7 | - |
| Correct Relations | 1 | 11.1% |
| Missing Relations | 8 | 88.9% |
| Over-specified Relations | 6 | 85.7% |

**✅ Correct Relations:**
- he → chose: predicate (subject - verb)

**❌ Missing Relations:**
- chose → walk: predicate (verb/preposition - object)
- he → drive: predicate (subject - verb)
- rather → than: connection
- rather → walk: constraint
- than → drive: predicate (verb/preposition - object)
- to → chose: constraint
- to → drive: predicate (verb/preposition - object)
- to → walk: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- chose → walk: predicate (verb/proposition - object)
- drive → walk: connection
- rather → drive: connection
- than → rather: constraint
- to → drive: predicate (verb/proposition - object)
- to → walk: constraint

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
- chose → walk: predicate (verb/proposition - object)
- drive → walk: connection
- he → chose: predicate (subject - verb)
- rather → drive: connection
- than → rather: constraint
- to → drive: predicate (verb/proposition - object)
- to → walk: constraint

</details>

---

### Sentence 23
**Input:** Rather than complain, she took action.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 5 | - |
| Generated Relations | 5 | - |
| Correct Relations | 1 | 20.0% |
| Missing Relations | 4 | 80.0% |
| Over-specified Relations | 4 | 80.0% |

**✅ Correct Relations:**
- she → took: predicate (subject - verb)

**❌ Missing Relations:**
- rather → took: constraint
- she → complain: predicate (subject - verb)
- than → complain: predicate (verb/preposition - object)
- took → action: predicate (verb/preposition - object)

**➕ Over-specified Relations:**
- complain → took: constraint
- rather → complain: constraint
- than → rather: constraint
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
- complain → took: constraint
- rather → complain: constraint
- she → took: predicate (subject - verb)
- than → rather: constraint
- took → action: predicate (verb/proposition - object)

</details>

---

## 📊 Total Data Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 23 |
| Total Expected Relations | 223 |
| Total Generated Relations | 196 |
| Total Correct Relations | 56 |
| Total Missing Relations | 167 |
| Total Over-specified Relations | 140 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **25.1%** |
| **Missing Rate** | **74.9%** |
| **Over-specification Rate** | **71.4%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 28.6% | Percentage of generated relations that are correct |
| Recall | 25.1% | Percentage of expected relations that were found |
| F1-Score | 26.7% | Harmonic mean of precision and recall |