# ROM Evaluation Report

**Date:** 2025-05-22 22:37:12
**Total Sentences:** 2
**Processed Sentences:** 2
**Skipped Sentences:** 0

## 📊 Overall Performance Metrics

### Summary Statistics

| Metric                         | Value |
|--------------------------------|-------|
| Total Sentences Processed      | 2     |
| Total Expected Relations       | 13    |
| Total Generated Relations      | 15    |
| Total Correct Relations        | 8     |
| Total Missing Relations        | 5     |
| Total Over-specified Relations | 7     |

### Overall Performance

| Metric                      | Percentage |
|-----------------------------|------------|
| **Correct Rate**            | **61.5%**  |
| **Missing Rate**            | **38.5%**  |
| **Over-specification Rate** | **46.7%**  |

### Performance Interpretation

**Overall Performance:** 🟠 Fair

### Additional Metrics

| Metric    | Value | Description                                        |
|-----------|-------|----------------------------------------------------|
| Precision | 53.3% | Percentage of generated relations that are correct |
| Recall    | 61.5% | Percentage of expected relations that were found   |
| F1-Score  | 57.1% | Harmonic mean of precision and recall              |

---

## Individual Sentence Results

### Sentence 1

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

- because → raining: predicate (conjunction - clause_verb)
- because → stayed: constraint
- home → stayed: constraint
- i → stayed: predicate (subject - verb)
- it → raining: predicate (subject - verb)
- raining → stayed: constraint
- was → raining: constraint

</details>

---

### Sentence 2

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

- although → finished: constraint
- although → tired: predicate (conjunction - clause_verb)
- finished → report: predicate (verb/proposition - object)
- she → finished: predicate (subject - verb)
- she → was: predicate (subject - verb)
- the → report: constraint
- tired → finished: constraint
- was → tired: predicate (verb/proposition - object)

</details>

---
