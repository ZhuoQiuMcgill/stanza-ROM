# ROM Evaluation Report

**Date:** 2025-05-23 15:26:56
**Total Sentences:** 48
**Processed Sentences:** 48
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics

| Metric                         | Value |
|--------------------------------|-------|
| Total Sentences Processed      | 48    |
| Total Expected Relations       | 422   |
| Total Generated Relations      | 396   |
| Total Correct Relations        | 210   |
| Total Missing Relations        | 212   |
| Total Over-specified Relations | 186   |

### Overall Performance

| Metric                      | Percentage |
|-----------------------------|------------|
| **Correct Rate**            | **49.8%**  |
| **Missing Rate**            | **50.2%**  |
| **Over-specification Rate** | **47.0%**  |

### Performance Interpretation

**Overall Performance:** 🔴 Needs Improvement

### Additional Metrics

| Metric    | Value | Description                                        |
|-----------|-------|----------------------------------------------------|
| Precision | 53.0% | Percentage of generated relations that are correct |
| Recall    | 49.8% | Percentage of expected relations that were found   |
| F1-Score  | 51.3% | Harmonic mean of precision and recall              |

---

## Individual Sentence Results

### Sentence 1

**Input:** The boy who sings is my friend.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 7     | 87.5% |
| Missing Relations        | 1     | 12.5% |
| Over-specified Relations | 0     | 0.0%  |

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

- The → boy: Constraint (UD: det)
- boy → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- boy → sings: Predicate (Subject - Verb) (UD: antecedent→relcl_verb(acl:relcl))
- is → friend: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- my → friend: Constraint (UD: nmod:poss)
- who → boy: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → sings: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 2

**Input:** The artist who painted this is famous.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 7     | -      |
| Generated Relations      | 7     | -      |
| Correct Relations        | 7     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 0     | 0.0%   |

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

- The → artist: Constraint (UD: det)
- artist → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- artist → painted: Predicate (Subject - Verb) (UD: antecedent→relcl_verb(acl:relcl))
- is → famous: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- painted → this: Predicate (Verb/Proposition - Object) (UD: obj)
- who → artist: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- who → painted: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 3

**Input:** The girl whom I met is nice.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 6     | -      |
| Generated Relations      | 6     | -      |
| Correct Relations        | 6     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 0     | 0.0%   |

**✅ Correct Relations:**

- girl → is: predicate (subject - verb)
- i → met: predicate (subject - verb)
- is → nice: predicate (verb/proposition - object)
- met → whom: predicate (verb/proposition - object)
- the → girl: constraint
- whom → girl: connection

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

- I → met: Predicate (Subject - Verb) (UD: nsubj)
- The → girl: Constraint (UD: det)
- girl → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- is → nice: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- met → whom: Predicate (Verb/Proposition - Object) (UD: obj)
- met → whom: Predicate (Verb/Proposition - Object) (UD: relcl_verb→obj_pronoun(acl:relcl))
- whom → girl: Connection (UD: rel_pronoun→antecedent(acl:relcl))

</details>

---

### Sentence 4

**Input:** The movie that we watched was amazing.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 6     | -      |
| Generated Relations      | 6     | -      |
| Correct Relations        | 6     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 0     | 0.0%   |

**✅ Correct Relations:**

- movie → was: predicate (subject - verb)
- that → movie: connection
- the → movie: constraint
- was → amazing: predicate (verb/proposition - object)
- watched → that: predicate (verb/proposition - object)
- we → watched: predicate (subject - verb)

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
- movie → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- that → movie: Connection (UD: rel_pronoun→antecedent(acl:relcl))
- was → amazing: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- watched → that: Predicate (Verb/Proposition - Object) (UD: obj)
- watched → that: Predicate (Verb/Proposition - Object) (UD: relcl_verb→obj_pronoun(acl:relcl))
- we → watched: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 5

**Input:** The man whose car broke down.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 5     | -      |
| Generated Relations      | 6     | -      |
| Correct Relations        | 5     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 1     | 16.7%  |

**✅ Correct Relations:**

- broke → down: constraint
- car → broke: predicate (subject - verb)
- the → man: constraint
- whose → car: constraint
- whose → man: connection

**➕ Over-specified Relations:**

- broke → man: predicate (verb/proposition - object)

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
- broke → man: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- car → broke: Predicate (Subject - Verb) (UD: nsubj)
- whose → car: Constraint (UD: nmod:poss)
- whose → car: Constraint (UD: whose→possessed_noun)
- whose → man: Connection (UD: whose→antecedent)

</details>

---

### Sentence 6

**Input:** The boy whose father is a doctor is my classmate.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 9     | -      |
| Generated Relations      | 9     | -      |
| Correct Relations        | 9     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 0     | 0.0%   |

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
- boy → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- father → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- is → classmate: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- is → doctor: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- my → classmate: Constraint (UD: nmod:poss)
- whose → boy: Connection (UD: whose→antecedent)
- whose → father: Constraint (UD: nmod:poss)
- whose → father: Constraint (UD: whose→possessed_noun)

</details>

---

### Sentence 7

**Input:** 2018 was the year when I moved to Canada.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 6     | -     |
| Correct Relations        | 5     | 55.6% |
| Missing Relations        | 4     | 44.4% |
| Over-specified Relations | 1     | 16.7% |

**✅ Correct Relations:**

- 2018 → was: predicate (subject - verb)
- i → moved: predicate (subject - verb)
- the → year: constraint
- was → year: predicate (verb/proposition - object)
- when → moved: predicate (verb/proposition - object)

**❌ Missing Relations:**

- move → year: constraint
- moved → to: constraint
- to → canada: predicate (verb/proposition - object)
- when → year: constraint

**➕ Over-specified Relations:**

- to → canada: predicate (preposition - object)

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

- 2018 → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- I → moved: Predicate (Subject - Verb) (UD: nsubj)
- the → year: Constraint (UD: det)
- to → Canada: Predicate (Preposition - Object) (UD: case)
- was → year: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- when → moved: Predicate (Verb/Proposition - Object) (UD: advmod)

</details>

---

### Sentence 8

**Input:** I remember the day when we met.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 6     | -     |
| Correct Relations        | 5     | 71.4% |
| Missing Relations        | 2     | 28.6% |
| Over-specified Relations | 1     | 16.7% |

**✅ Correct Relations:**

- i → remember: predicate (subject - verb)
- remember → day: predicate (verb/proposition - object)
- the → day: constraint
- we → met: predicate (subject - verb)
- when → met: predicate (verb/proposition - object)

**❌ Missing Relations:**

- met → day: constraint
- when → day: constraint

**➕ Over-specified Relations:**

- met → remember: constraint

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

- I → remember: Predicate (Subject - Verb) (UD: nsubj)
- met → remember: Constraint (UD: advcl)
- remember → day: Predicate (Verb/Proposition - Object) (UD: obj)
- the → day: Constraint (UD: det)
- we → met: Predicate (Subject - Verb) (UD: nsubj)
- when → met: Predicate (Verb/Proposition - Object) (UD: advmod)

</details>

---

### Sentence 9

**Input:** This is the place where we stayed.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 6     | -     |
| Correct Relations        | 5     | 71.4% |
| Missing Relations        | 2     | 28.6% |
| Over-specified Relations | 1     | 16.7% |

**✅ Correct Relations:**

- is → place: predicate (verb/proposition - object)
- the → place: constraint
- this → is: predicate (subject - verb)
- we → stayed: predicate (subject - verb)
- where → stayed: predicate (verb/proposition - object)

**❌ Missing Relations:**

- stayed → place: constraint
- where → place: constraint

**➕ Over-specified Relations:**

- stayed → place: predicate (verb/proposition - object)

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

- This → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- is → place: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- stayed → place: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- the → place: Constraint (UD: det)
- we → stayed: Predicate (Subject - Verb) (UD: nsubj)
- where → stayed: Predicate (Verb/Proposition - Object) (UD: advmod)

</details>

---

### Sentence 10

**Input:** I don’t know the reason why he left.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 5     | 62.5% |
| Missing Relations        | 3     | 37.5% |
| Over-specified Relations | 3     | 37.5% |

**✅ Correct Relations:**

- he → left: predicate (subject - verb)
- i → know: predicate (subject - verb)
- know → reason: predicate (verb/proposition - object)
- the → reason: constraint
- why → left: predicate (verb/proposition - object)

**❌ Missing Relations:**

- don’t → know: constraint
- left → reason: constraint
- why → reason: constraint

**➕ Over-specified Relations:**

- do → know: constraint
- left → reason: predicate (verb/proposition - object)
- n’t → know: constraint

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

- I → know: Predicate (Subject - Verb) (UD: nsubj)
- do → know: Constraint (UD: aux)
- he → left: Predicate (Subject - Verb) (UD: nsubj)
- know → reason: Predicate (Verb/Proposition - Object) (UD: obj)
- left → reason: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- n’t → know: Constraint (UD: advmod)
- the → reason: Constraint (UD: det)
- why → left: Predicate (Verb/Proposition - Object) (UD: advmod)

</details>

---

### Sentence 11

**Input:** I stayed home because it was raining.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 6     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 2     | 33.3% |
| Missing Relations        | 4     | 66.7% |
| Over-specified Relations | 5     | 71.4% |

**✅ Correct Relations:**

- because → stayed: constraint
- i → stayed: predicate (subject - verb)

**❌ Missing Relations:**

- because → was: predicate (verb/proposition - object)
- it → was: predicate (subject - verb)
- stayed → home: predicate (verb/proposition - object)
- was → raining: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- because → raining: predicate (conjunction - clause_verb)
- home → stayed: constraint
- it → raining: predicate (subject - verb)
- raining → stayed: constraint
- was → raining: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- because → stayed: constraint
- because → was: predicate (verb/proposition - object)
- i → stayed: predicate (subject - verb)
- it → was: predicate (subject - verb)
- stayed → home: predicate (verb/proposition - object)
- was → raining: predicate (verb/proposition - object)

**Generated Relations:**

- I → stayed: Predicate (Subject - Verb) (UD: nsubj)
- because → raining: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- because → stayed: Constraint (UD: mark→main_verb (mark))
- home → stayed: Constraint (UD: advmod)
- it → raining: Predicate (Subject - Verb) (UD: nsubj)
- raining → stayed: Constraint (UD: advcl)
- was → raining: Constraint (UD: aux)

</details>

---

### Sentence 12

**Input:** Although she was tired, she finished the report.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 7     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 6     | 85.7% |
| Missing Relations        | 1     | 14.3% |
| Over-specified Relations | 2     | 25.0% |

**✅ Correct Relations:**

- although → finished: constraint
- finished → report: predicate (verb/proposition - object)
- she → finished: predicate (subject - verb)
- she → was: predicate (subject - verb)
- the → report: constraint
- was → tired: predicate (verb/proposition - object)

**❌ Missing Relations:**

- although → was: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- although → tired: predicate (conjunction - clause_verb)
- tired → finished: constraint

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- although → finished: constraint
- although → was: predicate (verb/proposition - object)
- finished → report: predicate (verb/proposition - object)
- she → finished: predicate (subject - verb)
- she → was: predicate (subject - verb)
- the → report: constraint
- was → tired: predicate (verb/proposition - object)

**Generated Relations:**

- Although → finished: Constraint (UD: mark→main_verb (mark))
- Although → tired: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- finished → report: Predicate (Verb/Proposition - Object) (UD: obj)
- she → finished: Predicate (Subject - Verb) (UD: nsubj)
- she → was: Predicate (Subject - Verb) (UD: nsubj→cop)
- the → report: Constraint (UD: det)
- tired → finished: Constraint (UD: advcl)
- was → tired: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 13

**Input:** Inspired by those cherished memories, Sarah decided to start a journal to preserve them.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 13    | -     |
| Generated Relations      | 13    | -     |
| Correct Relations        | 5     | 38.5% |
| Missing Relations        | 8     | 61.5% |
| Over-specified Relations | 8     | 61.5% |

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

### Sentence 14

**Input:** She described not only the stories her grandmother shared, but also the emotions they stirred.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 14    | -     |
| Generated Relations      | 13    | -     |
| Correct Relations        | 6     | 42.9% |
| Missing Relations        | 8     | 57.1% |
| Over-specified Relations | 7     | 53.8% |

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

### Sentence 15

**Input:** The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 18    | -     |
| Generated Relations      | 16    | -     |
| Correct Relations        | 5     | 27.8% |
| Missing Relations        | 13    | 72.2% |
| Over-specified Relations | 11    | 68.8% |

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

### Sentence 16

**Input:** Her friends who read the journal found themselves moved by its sincerity and vivid details.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 16    | -     |
| Generated Relations      | 15    | -     |
| Correct Relations        | 6     | 37.5% |
| Missing Relations        | 10    | 62.5% |
| Over-specified Relations | 9     | 60.0% |

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

### Sentence 17

**Input:** She smiled as she read about the time they built a treehouse together.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 12    | -     |
| Generated Relations      | 12    | -     |
| Correct Relations        | 7     | 58.3% |
| Missing Relations        | 5     | 41.7% |
| Over-specified Relations | 5     | 41.7% |

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

### Sentence 18

**Input:** It is a lie that you love her.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 6     | -      |
| Generated Relations      | 7     | -      |
| Correct Relations        | 6     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 1     | 14.3%  |

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

### Sentence 19

**Input:** She waited by the window, hoping you would return.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 5     | 55.6% |
| Missing Relations        | 4     | 44.4% |
| Over-specified Relations | 3     | 37.5% |

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

### Sentence 20

**Input:** Design a vacation house that can fly easily from one location to another.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 13    | -     |
| Generated Relations      | 11    | -     |
| Correct Relations        | 4     | 30.8% |
| Missing Relations        | 9     | 69.2% |
| Over-specified Relations | 7     | 63.6% |

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

### Sentence 21

**Input:** Design a web system to manage the editorial workflow of the JIDPS journal.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 12    | -     |
| Generated Relations      | 13    | -     |
| Correct Relations        | 7     | 58.3% |
| Missing Relations        | 5     | 41.7% |
| Over-specified Relations | 6     | 46.2% |

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

### Sentence 22

**Input:** I don't know whether he’ll call or text.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 11    | -     |
| Generated Relations      | 9     | -     |
| Correct Relations        | 2     | 18.2% |
| Missing Relations        | 9     | 81.8% |
| Over-specified Relations | 7     | 77.8% |

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

### Sentence 23

**Input:** She’s unsure whether to accept the job or continue studying.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 12    | -     |
| Generated Relations      | 9     | -     |
| Correct Relations        | 1     | 8.3%  |
| Missing Relations        | 11    | 91.7% |
| Over-specified Relations | 8     | 88.9% |

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

### Sentence 24

**Input:** This task is not as easy as it looks.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 10    | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 3     | 30.0% |
| Missing Relations        | 7     | 70.0% |
| Over-specified Relations | 5     | 62.5% |

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

### Sentence 25

**Input:** She enjoys painting as much as she enjoys dancing.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 10    | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 1     | 10.0% |
| Missing Relations        | 9     | 90.0% |
| Over-specified Relations | 6     | 85.7% |

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

### Sentence 26

**Input:** Just as the moon affects the tides, so does the sun influence them.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 12    | -     |
| Generated Relations      | 13    | -     |
| Correct Relations        | 6     | 50.0% |
| Missing Relations        | 6     | 50.0% |
| Over-specified Relations | 7     | 53.8% |

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

### Sentence 27

**Input:** Just as honesty builds trust, so does kindness.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 1     | 11.1% |
| Missing Relations        | 8     | 88.9% |
| Over-specified Relations | 7     | 87.5% |

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

### Sentence 28

**Input:** Just as we need water to survive, so do plants need sunlight.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 11    | -     |
| Generated Relations      | 13    | -     |
| Correct Relations        | 4     | 36.4% |
| Missing Relations        | 7     | 63.6% |
| Over-specified Relations | 9     | 69.2% |

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

### Sentence 29

**Input:** No sooner had she sat down than the phone rang.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 8     | -      |
| Generated Relations      | 9     | -      |
| Correct Relations        | 0     | 0.0%   |
| Missing Relations        | 8     | 100.0% |
| Over-specified Relations | 9     | 100.0% |

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

### Sentence 30

**Input:** I’d rather read a book than watch TV.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 3     | 33.3% |
| Missing Relations        | 6     | 66.7% |
| Over-specified Relations | 4     | 57.1% |

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

### Sentence 31

**Input:** What she said surprised everyone.

| Metric                   | Count | Rate   |
|--------------------------|-------|--------|
| Expected Relations       | 4     | -      |
| Generated Relations      | 4     | -      |
| Correct Relations        | 4     | 100.0% |
| Missing Relations        | 0     | 0.0%   |
| Over-specified Relations | 0     | 0.0%   |

**✅ Correct Relations:**

- said → what: predicate (verb/proposition - object)
- she → said: predicate (subject - verb)
- surprised → everyone: predicate (verb/proposition - object)
- what → surprised: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- said → what: predicate (verb/proposition - object)
- she → said: predicate (subject - verb)
- surprised → everyone: predicate (verb/proposition - object)
- what → surprised: predicate (subject - verb)

**Generated Relations:**

- What → surprised: Predicate (Subject - Verb) (UD: nsubj)
- said → What: Predicate (Verb/Proposition - Object) (UD: relcl_verb→implicit_obj(acl:relcl))
- she → said: Predicate (Subject - Verb) (UD: nsubj)
- surprised → everyone: Predicate (Verb/Proposition - Object) (UD: obj)

</details>

---

### Sentence 32

**Input:** That he lied was obvious.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 5     | -     |
| Generated Relations      | 2     | -     |
| Correct Relations        | 1     | 20.0% |
| Missing Relations        | 4     | 80.0% |
| Over-specified Relations | 1     | 50.0% |

**✅ Correct Relations:**

- he → lied: predicate (subject - verb)

**❌ Missing Relations:**

- lied → was: predicate (subject - verb)
- that → lied: connection
- that → was: predicate (subject - verb)
- was → obvious: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- lied → obvious: predicate (subject - verb)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- he → lied: predicate (subject - verb)
- lied → was: predicate (subject - verb)
- that → lied: connection
- that → was: predicate (subject - verb)
- was → obvious: predicate (verb/proposition - object)

**Generated Relations:**

- he → lied: Predicate (Subject - Verb) (UD: nsubj)
- lied → obvious: Predicate (Subject - Verb) (UD: csubj)

</details>

---

### Sentence 33

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

- depends → effort: predicate (verb/preposition - object)
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

- Whether → depends: Constraint (UD: mark→main_verb (mark))
- Whether → win: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- depends → effort: Predicate (Verb/Preposition - Object) (UD: obl)
- on → effort: Predicate (Preposition - Object) (UD: case)
- our → effort: Constraint (UD: nmod:poss)
- we → win: Predicate (Subject - Verb) (UD: nsubj)
- will → win: Constraint (UD: aux)
- win → depends: Constraint (UD: advcl)

</details>

---

### Sentence 34

**Input:** How she managed to escape is still a mystery.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 3     | 37.5% |
| Missing Relations        | 5     | 62.5% |
| Over-specified Relations | 4     | 57.1% |

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

- How → mystery: Constraint (UD: advmod)
- a → mystery: Constraint (UD: det)
- managed → escape: Predicate (Verb/Proposition - Object) (UD: xcomp)
- she → managed: Predicate (Subject - Verb) (UD: nsubj)
- still → mystery: Constraint (UD: advmod)
- to → escape: Predicate (Preposition - Object) (UD: mark)
- to → escape: Predicate (Preposition - Object) (UD: mark(to)→inf_verb)
- to → managed: Constraint (UD: mark(to)→main_verb_of(xcomp))

</details>

---

### Sentence 35

**Input:** When the meeting starts is still unknown.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 6     | -     |
| Generated Relations      | 4     | -     |
| Correct Relations        | 2     | 33.3% |
| Missing Relations        | 4     | 66.7% |
| Over-specified Relations | 2     | 50.0% |

**✅ Correct Relations:**

- meeting → starts: predicate (subject - verb)
- the → meeting: constraint

**❌ Missing Relations:**

- is → unknown: predicate (verb/proposition - object)
- still → is: constraint
- when → is: predicate (subject - verb)
- when → starts: constraint

**➕ Over-specified Relations:**

- still → unknown: constraint
- when → starts: predicate (verb/proposition - object)

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

- When → starts: Predicate (Verb/Proposition - Object) (UD: advmod)
- meeting → starts: Predicate (Subject - Verb) (UD: nsubj)
- still → unknown: Constraint (UD: advmod)
- the → meeting: Constraint (UD: det)

</details>

---

### Sentence 36

**Input:** I know that she is right.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 5     | -     |
| Generated Relations      | 4     | -     |
| Correct Relations        | 3     | 60.0% |
| Missing Relations        | 2     | 40.0% |
| Over-specified Relations | 1     | 25.0% |

**✅ Correct Relations:**

- i → know: predicate (subject - verb)
- is → right: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)

**❌ Missing Relations:**

- know → is: predicate (verb/proposition - object)
- that → is: connection

**➕ Over-specified Relations:**

- know → right: predicate (verb/proposition - object)

<details>
<summary>Detailed Comparison</summary>

**Expected Relations:**

- i → know: predicate (subject - verb)
- is → right: predicate (verb/proposition - object)
- know → is: predicate (verb/proposition - object)
- she → is: predicate (subject - verb)
- that → is: connection

**Generated Relations:**

- I → know: Predicate (Subject - Verb) (UD: nsubj)
- is → right: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- know → right: Predicate (Verb/Proposition - Object) (UD: ccomp)
- she → is: Predicate (Subject - Verb) (UD: nsubj→cop)

</details>

---

### Sentence 37

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

- She → tell: Predicate (Subject - Verb) (UD: nsubj)
- did → tell: Constraint (UD: aux)
- had → happened: Constraint (UD: aux)
- n’t → tell: Constraint (UD: advmod)
- tell → happened: Predicate (Verb/Proposition - Object) (UD: ccomp)
- tell → me: Predicate (Verb/Proposition - Object) (UD: iobj)
- what → happened: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 38

**Input:** We’re thinking about how we can solve the problem.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 10    | -     |
| Correct Relations        | 6     | 66.7% |
| Missing Relations        | 3     | 33.3% |
| Over-specified Relations | 4     | 40.0% |

**✅ Correct Relations:**

- about → thinking: constraint
- can → solve: constraint
- solve → problem: predicate (verb/proposition - object)
- the → problem: constraint
- we → solve: predicate (subject - verb)
- we → thinking: predicate (subject - verb)

**❌ Missing Relations:**

- about → how: predicate (verb/proposition - object)
- are → thinking: constraint
- how → solve: constraint

**➕ Over-specified Relations:**

- about → solve: predicate (conjunction - clause_verb)
- how → solve: predicate (verb/proposition - object)
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

- We → thinking: Predicate (Subject - Verb) (UD: nsubj)
- about → solve: Predicate (Conjunction - Clause_Verb) (UD: mark→verb_of_advcl (mark))
- about → thinking: Constraint (UD: mark→main_verb (mark))
- can → solve: Constraint (UD: aux)
- how → solve: Predicate (Verb/Proposition - Object) (UD: advmod)
- solve → problem: Predicate (Verb/Proposition - Object) (UD: obj)
- solve → thinking: Constraint (UD: advcl)
- the → problem: Constraint (UD: det)
- we → solve: Predicate (Subject - Verb) (UD: nsubj)
- ’re → thinking: Constraint (UD: aux)

</details>

---

### Sentence 39

**Input:** He’s not sure if he locked the door.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 6     | -     |
| Correct Relations        | 3     | 37.5% |
| Missing Relations        | 5     | 62.5% |
| Over-specified Relations | 3     | 50.0% |

**✅ Correct Relations:**

- he → locked: predicate (subject - verb)
- locked → door: predicate (verb/proposition - object)
- the → door: constraint

**❌ Missing Relations:**

- he → is: predicate (subject - verb)
- if → is: constraint
- if → locked: predicate (verb/proposition - object)
- is → sure: predicate (verb/proposition - object)
- not → sure: constraint

**➕ Over-specified Relations:**

- he → ’s: predicate (subject - verb)
- if → locked: connection
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

- He → ’s: Predicate (Subject - Verb) (UD: nsubj→cop)
- he → locked: Predicate (Subject - Verb) (UD: nsubj)
- if → locked: Connection (UD: mark)
- locked → door: Predicate (Verb/Proposition - Object) (UD: obj)
- the → door: Constraint (UD: det)
- ’s → sure: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---

### Sentence 40

**Input:** I don’t know when the package will arrive.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 4     | 50.0% |
| Missing Relations        | 4     | 50.0% |
| Over-specified Relations | 4     | 50.0% |

**✅ Correct Relations:**

- i → know: predicate (subject - verb)
- package → arrive: predicate (subject - verb)
- the → package: constraint
- will → arrive: constraint

**❌ Missing Relations:**

- don’t → know: constraint
- know → arrive: predicate (verb/proposition - object)
- when → arrive: constraint
- when → know: predicate (verb/proposition - object)

**➕ Over-specified Relations:**

- arrive → know: constraint
- do → know: constraint
- n’t → know: constraint
- when → arrive: predicate (verb/proposition - object)

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

- I → know: Predicate (Subject - Verb) (UD: nsubj)
- arrive → know: Constraint (UD: advcl)
- do → know: Constraint (UD: aux)
- n’t → know: Constraint (UD: advmod)
- package → arrive: Predicate (Subject - Verb) (UD: nsubj)
- the → package: Constraint (UD: det)
- when → arrive: Predicate (Verb/Proposition - Object) (UD: advmod)
- will → arrive: Constraint (UD: aux)

</details>

---

### Sentence 41

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

- The → truth: Constraint (UD: det)
- is → left: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- never → left: Constraint (UD: advmod)
- she → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- that → left: Connection (UD: mark)
- truth → is: Predicate (Subject - Verb) (UD: nsubj:outer→cop)
- truth → left: Predicate (Subject - Verb) (UD: nsubj:outer)

</details>

---

### Sentence 42

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

- My → suggestion: Constraint (UD: nmod:poss)
- a → break: Constraint (UD: det)
- is → take: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- suggestion → is: Predicate (Subject - Verb) (UD: nsubj:outer→cop)
- suggestion → take: Predicate (Subject - Verb) (UD: nsubj:outer)
- take → break: Predicate (Verb/Proposition - Object) (UD: obj)
- that → take: Connection (UD: mark)
- we → is: Predicate (Subject - Verb) (UD: nsubj→cop)

</details>

---

### Sentence 43

**Input:** The problem is how we can get there.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 8     | -     |
| Generated Relations      | 8     | -     |
| Correct Relations        | 3     | 37.5% |
| Missing Relations        | 5     | 62.5% |
| Over-specified Relations | 5     | 62.5% |

**✅ Correct Relations:**

- can → get: constraint
- problem → is: predicate (subject - verb)
- the → problem: constraint

**❌ Missing Relations:**

- get → there: predicate (verb/proposition - object)
- how → get: constraint
- how → is: connection
- is → how: predicate (verb/proposition - object)
- we → get: predicate (subject - verb)

**➕ Over-specified Relations:**

- how → get: predicate (verb/proposition - object)
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

- The → problem: Constraint (UD: det)
- can → get: Constraint (UD: aux)
- how → get: Predicate (Verb/Proposition - Object) (UD: advmod)
- is → get: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- problem → get: Predicate (Subject - Verb) (UD: nsubj:outer)
- problem → is: Predicate (Subject - Verb) (UD: nsubj:outer→cop)
- there → get: Constraint (UD: advmod)
- we → is: Predicate (Subject - Verb) (UD: nsubj→cop)

</details>

---

### Sentence 44

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

- The → question: Constraint (UD: det)
- accept → offer: Predicate (Verb/Proposition - Object) (UD: obj)
- he → is: Predicate (Subject - Verb) (UD: nsubj→cop)
- is → accept: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)
- question → accept: Predicate (Subject - Verb) (UD: nsubj:outer)
- question → is: Predicate (Subject - Verb) (UD: nsubj:outer→cop)
- the → offer: Constraint (UD: det)
- whether → accept: Connection (UD: mark)
- will → accept: Constraint (UD: aux)

</details>

---

### Sentence 45

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

- I → heard: Predicate (Subject - Verb) (UD: nsubj)
- got → married: Constraint (UD: aux:pass)
- heard → news: Predicate (Verb/Proposition - Object) (UD: obj)
- married → news: Constraint (UD: acl)
- she → married: Predicate (Subject - Verb) (UD: nsubj:pass)
- that → married: Connection (UD: mark)
- the → news: Constraint (UD: det)

</details>

---

### Sentence 46

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

- The → idea: Constraint (UD: det)
- brings → idea: Constraint (UD: acl)
- brings → success: Predicate (Verb/Proposition - Object) (UD: obj)
- hard → work: Constraint (UD: amod)
- idea → accepted: Predicate (Subject - Verb) (UD: nsubj:pass)
- is → accepted: Constraint (UD: aux:pass)
- that → brings: Connection (UD: mark)
- widely → accepted: Constraint (UD: advmod)
- work → brings: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 47

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

- She → rejected: Predicate (Subject - Verb) (UD: nsubj)
- cancel → meeting: Predicate (Verb/Proposition - Object) (UD: obj)
- cancel → suggestion: Constraint (UD: acl)
- rejected → suggestion: Predicate (Verb/Proposition - Object) (UD: obj)
- that → cancel: Connection (UD: mark)
- the → meeting: Constraint (UD: det)
- the → suggestion: Constraint (UD: det)
- we → cancel: Predicate (Subject - Verb) (UD: nsubj)

</details>

---

### Sentence 48

**Input:** We faced the fact that we were out of time.

| Metric                   | Count | Rate  |
|--------------------------|-------|-------|
| Expected Relations       | 9     | -     |
| Generated Relations      | 7     | -     |
| Correct Relations        | 4     | 44.4% |
| Missing Relations        | 5     | 55.6% |
| Over-specified Relations | 3     | 42.9% |

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

- We → faced: Predicate (Subject - Verb) (UD: nsubj)
- faced → fact: Predicate (Verb/Proposition - Object) (UD: obj)
- of → time: Predicate (Preposition - Object) (UD: case)
- out → time: Predicate (Preposition - Object) (UD: case)
- the → fact: Constraint (UD: det)
- we → were: Predicate (Subject - Verb) (UD: nsubj→cop)
- were → time: Predicate (Verb/Proposition - Object) (UD: cop→pred_complement)

</details>

---
