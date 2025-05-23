## Subject:

### Sentence 1:

* **Input**

    - The boy who sings is my friend.

* **Output**

    - The → boy: Constraint
    - Who → boy: Connection
    - Who → sings: Predicate (subject - verb)
    - boy → sings: Predicate (subject - verb)
    - Boy → is: Predicate (subject - verb)
    - Is → friend: Predicate (verb/proposition - object)
    - My → friend: Constraint
    - The → friend: Constraint

### Sentence 2:

* **Input**

    - The artist who painted this is famous.

* **Output**

    - The → artist: Constraint
    - Who → artist: Connection
    - Who → painted: Predicate (subject - verb)
    - artist→ painted: Predicate (subject - verb)
    - Painted → this: Predicate (verb/proposition - object)
    - Artist → is: Predicate (subject - verb)
    - Is → famous: Predicate (verb/proposition - object)

## Object:

### Sentence 3:

* **Input**

    - The girl (whom) I met is nice.

* **Output**

    - The → girl: Constraint
    - Whom → girl: Connection
    - I → met: Predicate (subject - verb)
    - Met → whom: Predicate (verb/proposition - object)
    - Girl → is: Predicate (subject - verb)
    - Is → nice: Predicate (verb/proposition - object)
    -

### Sentence 4:

* **Input**
    - The movie (that) we watched was amazing.
* **Output**

    - The → movie: Constraint
    - That → movie: Connection
    - We → watched: Predicate (subject - verb)
    - Watched → that: Predicate (verb/proposition - object)
    - Movie → was: Predicate (subject - verb)
    - Was → amazing: Predicate (verb/proposition - object)

## Possession:

### Sentence 5:

* **Input**

    - The man whose car broke down.

* **Output**

    - The → man: Constraint
    - Whose → man: Connection
    - Whose → car: Constraint
    - Car → broke: Predicate (subject - verb)
    - Broke → down: Constraint

### Sentence 6:

* **Input**
    - The boy whose father is a doctor is my classmate.
* **Output**
    - The → boy: Constraint
    - Whose → boy: Connection
    - Whose → father: Constraint
    - Father → is: Predicate (subject - verb)
    - Is → doctor: Predicate (verb/proposition - object)
    - A → doctor: Constraint
    - Boy → is: Predicate (subject - verb)
    - Is → classmate: Predicate (verb/proposition - object)
    - My → classmate: Constraint

## When:

### Sentence 7:

* **Input**

    - 2018 was the year when I moved to Canada.

* **Output**

    - 2018 → was: Predicate (subject - verb)
    - Was → year: Predicate (verb/proposition - object)
    - The → year: Constraint
    - When → year: Constraint
    - When → moved: Predicate (verb/proposition - object)
    - move→ year: Constraint
    - I → moved: Predicate (subject - verb)
    - Moved → to: Constraint
    - To → Canada: Predicate (verb/proposition - object)

### Sentence 8:

* **Input**
    - I remember the day when we met.
* **Output**
    - I → remember: Predicate (subject - verb)
    - Remember → day: Predicate (verb/proposition - object)
    - The → day: Constraint
    - When → day: Constraint
    - When → met: Predicate (verb/proposition - object)
    - met → day: Constraint
    - We → met: Predicate (subject - verb)

## Where:

### Sentence 9:

* **Input**

    - This is the place where we stayed

* **Output**

    - This → is: Predicate (subject - verb)
    - Is → place: Predicate (verb/proposition - object)
    - The → place: Constraint
    - Where → place: Constraint
    - We → stayed: Predicate (subject - verb)
    - Where → stayed: Predicate (verb/proposition - object)
    - stayed → place: Constraint

## Why:

### Sentence 10:

* **Input**

    - I don’t know the reason why he left.

* **Output**
    - I → know: Predicate (subject - verb)
    - Don’t → know: Constraint
    - Know → reason: Predicate (verb/proposition - object)
    - The → reason: Constraint
    - Why → reason: Constraint
    - He → left: Predicate (subject - verb)
    - Why → left: Predicate (verb/proposition - object)
    - left→ reason: Constraint
