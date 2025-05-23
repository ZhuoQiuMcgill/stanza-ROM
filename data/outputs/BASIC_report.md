# ROM Evaluation Report

**Date:** 2025-05-22 22:18:03
**Total Sentences:** 21
**Processed Sentences:** 21
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total Sentences Processed | 21 |
| Total Expected Relations | 202 |
| Total Generated Relations | 203 |
| Total Correct Relations | 85 |
| Total Missing Relations | 117 |
| Total Over-specified Relations | 118 |

### Overall Performance
| Metric | Percentage |
|--------|------------|
| **Correct Rate** | **42.1%** |
| **Missing Rate** | **57.9%** |
| **Over-specification Rate** | **58.1%** |

### Performance Interpretation
**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics
| Metric | Value | Description |
|--------|-------|-------------|
| Precision | 41.9% | Percentage of generated relations that are correct |
| Recall | 42.1% | Percentage of expected relations that were found |
| F1-Score | 42.0% | Harmonic mean of precision and recall |

---

## Individual Sentence Results

### Sentence 1
**Input:** Inspired by those cherished memories, Sarah decided to start a journal to preserve them.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 14 | - |
| Correct Relations | 3 | 23.1% |
| Missing Relations | 10 | 76.9% |
| Over-specified Relations | 11 | 78.6% |

**✅ Correct Relations:**
- a → journal: constraint
- sarah → decided: predicate (subject - verb)
- those → memories: constraint

**❌ Missing Relations:**
- cherished → memories: predicate (verb - object)
- inspired → sarah: constraint
- journal → preserve: predicate (subject - verb)
- memories → inspired: predicate (subject - verb)
- sarah → cherished: predicate (subject - verb)
- start → journal: predicate (preposition - object)
- them → memories: connection
- to → decided: constraint
- to → preserve: predicate (preposition - object)
- to → start: predicate (preposition - object)

**➕ Over-specified Relations:**
- by → memories: predicate (verb/proposition - object)
- cherished → memories: constraint
- decided → start: predicate (verb/proposition - object)
- inspired → decided: constraint
- inspired → memories: predicate (verb/proposition - object)
- preserve → start: constraint
- preserve → them: predicate (verb/proposition - object)
- start → journal: predicate (verb/proposition - object)
- to → preserve: constraint
- to → preserve: predicate (verb/proposition - object)
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
- a → journal: constraint
- by → memories: predicate (verb/proposition - object)
- cherished → memories: constraint
- decided → start: predicate (verb/proposition - object)
- inspired → decided: constraint
- inspired → memories: predicate (verb/proposition - object)
- preserve → start: constraint
- preserve → them: predicate (verb/proposition - object)
- sarah → decided: predicate (subject - verb)
- start → journal: predicate (verb/proposition - object)
- those → memories: constraint
- to → preserve: constraint
- to → preserve: predicate (verb/proposition - object)
- to → start: constraint

</details>

---

### Sentence 2
**Input:** She described not only the stories her grandmother shared, but also the emotions they stirred.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 14 | - |
| Generated Relations | 15 | - |
| Correct Relations | 6 | 42.9% |
| Missing Relations | 8 | 57.1% |
| Over-specified Relations | 9 | 60.0% |

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
- emotions → stirred: predicate (subject - verb)
- emotions → stories: connection
- not → stories: constraint
- not only → but also: connection
- only → stories: constraint
- stories → shared: predicate (subject - verb)

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
- also → emotions: constraint
- but → emotions: connection
- described → stories: predicate (verb/proposition - object)
- emotions → stirred: predicate (subject - verb)
- emotions → stories: connection
- grandmother → shared: predicate (subject - verb)
- her → grandmother: constraint
- not → stories: constraint
- not only → but also: connection
- only → stories: constraint
- she → described: predicate (subject - verb)
- stories → shared: predicate (subject - verb)
- the → emotions: constraint
- the → stories: constraint
- they → stirred: predicate (subject - verb)

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
- of → nostalgia: predicate (verb/proposition - object)
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
- a → tone: constraint
- and → love: connection
- comfort → nostalgia: connection
- emotions → gave: predicate (subject - verb)
- gave → her: predicate (verb/proposition - object)
- gave → writing: predicate (verb/proposition - object)
- heartfelt → tone: constraint
- love → nostalgia: connection
- nostalgia → emotions: constraint
- of → nostalgia: predicate (verb/proposition - object)
- surprised → her: predicate (verb/proposition - object)
- that → surprised: predicate (subject - verb)
- that → tone: connection
- the → emotions: constraint
- tone → surprised: predicate (subject - verb)
- writing → tone: predicate (verb/proposition - object)

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
- by → sincerity: predicate (verb/proposition - object)
- details → sincerity: connection
- found → moved: predicate (verb/proposition - object)
- found → themselves: predicate (verb/proposition - object)
- its → sincerity: constraint
- moved → sincerity: predicate (verb/proposition - object)
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
- and → details: connection
- by → sincerity: predicate (verb/proposition - object)
- details → sincerity: connection
- found → moved: predicate (verb/proposition - object)
- found → themselves: predicate (verb/proposition - object)
- friends → found: predicate (subject - verb)
- friends → read: predicate (subject - verb)
- her → friends: constraint
- its → sincerity: constraint
- moved → sincerity: predicate (verb/proposition - object)
- read → journal: predicate (verb/proposition - object)
- the → journal: constraint
- vivid → details: constraint
- who → friends: connection
- who → read: predicate (subject - verb)

</details>

---

### Sentence 5
**Input:** Their encouragement pushed Sarah to consider turning the journal into a book.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 11 | - |
| Generated Relations | 12 | - |
| Correct Relations | 7 | 63.6% |
| Missing Relations | 4 | 36.4% |
| Over-specified Relations | 5 | 41.7% |

**✅ Correct Relations:**
- a → book: constraint
- consider → turning: predicate (verb/proposition - object)
- encouragement → pushed: predicate (subject - verb)
- pushed → sarah: predicate (verb/proposition - object)
- the → journal: constraint
- their → encouragement: constraint
- turning → journal: predicate (verb/proposition - object)

**❌ Missing Relations:**
- into → book: predicate (preposition - object)
- into → turning: constraint
- sarah → consider: predicate (subject - verb)
- sarah → turning: predicate (subject - verb)

**➕ Over-specified Relations:**
- consider → pushed: constraint
- into → book: predicate (verb/proposition - object)
- to → consider: constraint
- to → turning: predicate (verb/proposition - object)
- turning → book: predicate (verb/proposition - object)

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
- a → book: constraint
- consider → pushed: constraint
- consider → turning: predicate (verb/proposition - object)
- encouragement → pushed: predicate (subject - verb)
- into → book: predicate (verb/proposition - object)
- pushed → sarah: predicate (verb/proposition - object)
- the → journal: constraint
- their → encouragement: constraint
- to → consider: constraint
- to → turning: predicate (verb/proposition - object)
- turning → book: predicate (verb/proposition - object)
- turning → journal: predicate (verb/proposition - object)

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
- emily → received: predicate (subject - verb)
- last → week: constraint

**❌ Missing Relations:**
- from → friend: predicate (preposition - object)
- from → letter: constraint
- from → received: constraint
- received → letter: predicate (verb - object)
- week → received: constraint

**➕ Over-specified Relations:**
- a → letter: constraint
- best → friend: constraint
- friend → letter: constraint
- from → friend: predicate (verb/proposition - object)
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
- a → letter: constraint
- best → friend: constraint
- emily → received: predicate (subject - verb)
- friend → letter: constraint
- from → friend: predicate (verb/proposition - object)
- her → friend: constraint
- last → week: constraint
- received → letter: predicate (verb/proposition - object)

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
- about → adventures: predicate (verb/proposition - object)
- adventures → childhood: constraint
- adventures → stories: constraint
- filled → stories: predicate (verb/proposition - object)
- filled → was: constraint
- letter → filled: predicate (subject - verb)
- their → adventures: constraint
- with → stories: predicate (verb/proposition - object)

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
- about → adventures: predicate (verb/proposition - object)
- adventures → childhood: constraint
- adventures → stories: constraint
- filled → stories: predicate (verb/proposition - object)
- filled → was: constraint
- letter → filled: predicate (subject - verb)
- the → letter: constraint
- their → adventures: constraint
- with → stories: predicate (verb/proposition - object)

</details>

---

### Sentence 8
**Input:** She smiled as she read about the time they built a treehouse together.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 12 | - |
| Correct Relations | 5 | 41.7% |
| Missing Relations | 7 | 58.3% |
| Over-specified Relations | 7 | 58.3% |

**✅ Correct Relations:**
- she → read: predicate (subject - verb)
- she → smiled: predicate (subject - verb)
- the → time: constraint
- they → built: predicate (subject - verb)
- together → built: constraint

**❌ Missing Relations:**
- a → treehouse: constraint (determiner - noun)
- about → read: constraint
- about → time: predicate (preposition - object)
- as → read: predicate (verb - object)
- as → smiled: constraint
- built → treehouse: predicate (verb - object)
- time → built: constraint

**➕ Over-specified Relations:**
- a → treehouse: constraint
- about → time: predicate (verb/proposition - object)
- as → read: constraint
- built → treehouse: predicate (verb/proposition - object)
- read → smiled: constraint
- read → time: predicate (verb/proposition - object)
- time → built: predicate (subject - verb)

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
- a → treehouse: constraint
- about → time: predicate (verb/proposition - object)
- as → read: constraint
- built → treehouse: predicate (verb/proposition - object)
- read → smiled: constraint
- read → time: predicate (verb/proposition - object)
- she → read: predicate (subject - verb)
- she → smiled: predicate (subject - verb)
- the → time: constraint
- they → built: predicate (subject - verb)
- time → built: predicate (subject - verb)
- together → built: constraint

</details>

---

### Sentence 9
**Input:** It was one of the happiest moments of her life.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 9 | - |
| Correct Relations | 4 | 44.4% |
| Missing Relations | 5 | 55.6% |
| Over-specified Relations | 5 | 55.6% |

**✅ Correct Relations:**
- happiest → moments: constraint
- her → life: constraint
- it → was: predicate (subject - verb)
- the → moments: constraint

**❌ Missing Relations:**
- of → life: predicate (preposition - object)
- of → moments: constraint
- of → moments: predicate (preposition - object)
- of → one: constraint
- was → moments: predicate (verb - object)

**➕ Over-specified Relations:**
- life → moments: constraint
- moments → one: constraint
- of → life: predicate (verb/proposition - object)
- of → moments: predicate (verb/proposition - object)
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
- happiest → moments: constraint
- her → life: constraint
- it → was: predicate (subject - verb)
- life → moments: constraint
- moments → one: constraint
- of → life: predicate (verb/proposition - object)
- of → moments: predicate (verb/proposition - object)
- the → moments: constraint
- was → one: predicate (verb/proposition - object)

</details>

---

### Sentence 10
**Input:** That memory, like many others, stayed with her even today.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 8 | - |
| Generated Relations | 8 | - |
| Correct Relations | 6 | 75.0% |
| Missing Relations | 2 | 25.0% |
| Over-specified Relations | 2 | 25.0% |

**✅ Correct Relations:**
- even → today: constraint
- like → others: predicate (verb/proposition - object)
- many → others: constraint
- memory → stayed: predicate (subject - verb)
- that → memory: constraint
- with → her: predicate (verb/proposition - object)

**❌ Missing Relations:**
- like → memory: constraint
- with → stayed: constraint

**➕ Over-specified Relations:**
- others → memory: constraint
- stayed → her: predicate (verb/proposition - object)

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
- even → today: constraint
- like → others: predicate (verb/proposition - object)
- many → others: constraint
- memory → stayed: predicate (subject - verb)
- others → memory: constraint
- stayed → her: predicate (verb/proposition - object)
- that → memory: constraint
- with → her: predicate (verb/proposition - object)

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
- she → was: predicate (subject - verb)
- very → sad: constraint
- was → sad: predicate (verb/proposition - object)

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
- lie → love: predicate (subject - verb)
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
- a → lie: constraint
- is → lie: predicate (verb/proposition - object)
- it → is: predicate (subject - verb)
- lie → love: predicate (subject - verb)
- love → her: predicate (verb/proposition - object)
- love → that: predicate (verb/proposition - object)
- that → lie: connection
- you → love: predicate (subject - verb)

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
- again → broke: constraint
- broke → heart: predicate (verb/proposition - object)
- her → heart: constraint
- that → truth: constraint
- truth → broke: predicate (subject - verb)

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
- full → story: constraint
- nobody → told: predicate (subject - verb)
- the → story: constraint
- told → her: predicate (verb/proposition - object)
- told → story: predicate (verb/proposition - object)

</details>

---

### Sentence 15
**Input:** She waited by the window, hoping you would return.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 9 | - |
| Generated Relations | 8 | - |
| Correct Relations | 4 | 44.4% |
| Missing Relations | 5 | 55.6% |
| Over-specified Relations | 4 | 50.0% |

**✅ Correct Relations:**
- hoping → waited: constraint
- she → waited: predicate (subject - verb)
- the → window: constraint
- you → return: predicate (subject - verb)

**❌ Missing Relations:**
- by → waited: constraint
- by → window: predicate (preposition - object)
- hoping → return: predicate (verb - object)
- she → hoping: predicate (subject - verb)
- would → return: constraint (auxiliary - main verb)

**➕ Over-specified Relations:**
- by → window: predicate (verb/proposition - object)
- hoping → return: predicate (verb/proposition - object)
- return → would: constraint
- waited → window: predicate (verb/proposition - object)

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
- by → window: predicate (verb/proposition - object)
- hoping → return: predicate (verb/proposition - object)
- hoping → waited: constraint
- return → would: constraint
- she → waited: predicate (subject - verb)
- the → window: constraint
- waited → window: predicate (verb/proposition - object)
- you → return: predicate (subject - verb)

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
- but → happened: connection
- it → happened: predicate (subject - verb)
- never → happened: constraint

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
- settled → her: predicate (verb/proposition - object)
- within → her: predicate (verb/proposition - object)

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
- before → settled: constraint
- deep → settled: constraint
- like → before: connection
- pain → settled: predicate (subject - verb)
- settled → her: predicate (verb/proposition - object)
- the → pain: constraint
- within → her: predicate (verb/proposition - object)

</details>

---

### Sentence 18
**Input:** Design a vacation house that can fly easily from one location to another.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 13 | - |
| Generated Relations | 13 | - |
| Correct Relations | 3 | 23.1% |
| Missing Relations | 10 | 76.9% |
| Over-specified Relations | 10 | 76.9% |

**✅ Correct Relations:**
- a → house: constraint
- one → location: constraint
- that → fly: predicate (subject - verb)

**❌ Missing Relations:**
- another → location: constraint
- can → fly: constraint
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
- fly → another: predicate (verb/proposition - object)
- fly → can: constraint
- fly → location: predicate (verb/proposition - object)
- from → location: predicate (verb/proposition - object)
- house → fly: predicate (subject - verb)
- house → vacation: constraint
- that → house: connection
- to → another: predicate (verb/proposition - object)

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
- a → house: constraint
- design → house: predicate (verb/proposition - object)
- easily → fly: constraint
- fly → another: predicate (verb/proposition - object)
- fly → can: constraint
- fly → location: predicate (verb/proposition - object)
- from → location: predicate (verb/proposition - object)
- house → fly: predicate (subject - verb)
- house → vacation: constraint
- one → location: constraint
- that → fly: predicate (subject - verb)
- that → house: connection
- to → another: predicate (verb/proposition - object)

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
- to → turbine_2: predicate (verb/proposition - object)
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
- 10 → mw: constraint
- 5 → mw: constraint
- to → turbine_2: predicate (verb/proposition - object)
- turbine_1 → mw: constraint
- turbine_1 → wind: constraint
- turbine_2 → mw: constraint
- turbine_2 → turbine_1: constraint
- turbine_2 → wind: constraint
- upscale → turbine_1: constraint

</details>

---

### Sentence 20
**Input:** Design a web system to manage the editorial workflow of the JIDPS journal.

| Metric | Count | Rate |
|--------|-------|------|
| Expected Relations | 12 | - |
| Generated Relations | 12 | - |
| Correct Relations | 7 | 58.3% |
| Missing Relations | 5 | 41.7% |
| Over-specified Relations | 5 | 41.7% |

**✅ Correct Relations:**
- a → system: constraint
- design → system: predicate (verb/proposition - object)
- editorial → workflow: constraint
- manage → workflow: predicate (verb/proposition - object)
- of → journal: predicate (verb/proposition - object)
- the → journal: constraint
- the → workflow: constraint

**❌ Missing Relations:**
- jidps → journal: constraint
- of → workflow: constraint
- to → design: constraint
- to → manage: predicate (verb/proposition - object)
- web → system: constraint

**➕ Over-specified Relations:**
- journal → jidps: constraint
- journal → workflow: constraint
- manage → design: constraint
- system → web: constraint
- to → manage: constraint

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
- a → system: constraint
- design → system: predicate (verb/proposition - object)
- editorial → workflow: constraint
- journal → jidps: constraint
- journal → workflow: constraint
- manage → design: constraint
- manage → workflow: predicate (verb/proposition - object)
- of → journal: predicate (verb/proposition - object)
- system → web: constraint
- the → journal: constraint
- the → workflow: constraint
- to → manage: constraint

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
- to → slow: predicate (verb/proposition - object)

**❌ Missing Relations:**
- and → slow: connect
- and → stop: connect
- down → slow: constraint
- effectively → stop: constraint
- efficiently → slow: constraint
- efficiently → stop: constraint
- stop → vehicle: predicate (verb/proposition - object)
- to → needs: constraint
- to → stop: predicate (verb/proposition - object)

**➕ Over-specified Relations:**
- and → efficiently: connection
- and → slow: connection
- efficiently → effectively: connection
- needs → stop: predicate (verb/proposition - object)
- slow → down: constraint
- slow → stop: connection
- to → stop: constraint

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
- a → vehicle: constraint
- and → efficiently: connection
- and → slow: connection
- driver → needs: predicate (subject - verb)
- effectively → slow: constraint
- efficiently → effectively: connection
- needs → stop: predicate (verb/proposition - object)
- slow → down: constraint
- slow → stop: connection
- slow → vehicle: predicate (verb/proposition - object)
- to → slow: predicate (verb/proposition - object)
- to → stop: constraint

</details>

---
