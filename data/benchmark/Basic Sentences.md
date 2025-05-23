### Sentence 1:

* **Input**
    - Inspired by those cherished memories, Sarah decided to start a journal to preserve them.
* **Output**
    - Inspired → Sarah: Constraint
    - memories → inspired: Predicate (subject - verb)
    - those → memories: Constraint
    - cherished → memories: Predicate (verb - object)
    - Sarah → decided: Predicate (subject - verb)
    - Sarah → cherished: Predicate (subject - verb)
    - to → decided: Constraint
    - to → preserve: Predicate (preposition - object)
    - Start → journal: Predicate (preposition - object)
    - a → journal: Constraint
    - to → decided: Constraint
    - to → start: Predicate (preposition - object)
    - journal → preserve: Predicate (subject - verb)
    - them → memories: Connection

### Sentence 2:

* **Input**
    - She described not only the stories her grandmother shared, but also the emotions they stirred.
* **Output**
    - she → described: Predicate (subject - verb)
    - described → stories: Predicate (verb/preposition - object)
    - the → stories: Constraint
    - her → grandmother: Constraint
    - grandmother → shared: Predicate (subject - verb)
    - shared → stories: Predicate (verb/preposition - object)
    - described → emotions: Predicate (verb/preposition - object)
    - the → emotions: Constraint
    - stirred → emotions: Predicate (verb/preposition - object)
    - they → stirred: Predicate (subject - verb)
    - not only → described: constraint
    - not only → stories: Predicate (verb/preposition - object)
    - but also → described: constraint
    - but also → emotions: Predicate (verb/preposition - object)

### Sentence 3:

* **Input**
    - The emotions of nostalgia, comfort, and love gave her writing a heartfelt tone that surprised her.
* **Output**
    - emotions → gave: Predicate (subject - verb)
    - gave → writing: Predicate (verb/preposition - object)
    - her → writing: constraint
    - gave → tone: Predicate (verb/preposition - object)
    - a→ tone: Constraint
    - writing → tone: Constraint
    - heartfelt →tone: Constraint
    - tone → that: Connection
    - tone → surprised: Predicate (subject - verb)
    - that → surprised: Predicate (subject - verb)
    - surprised → her: Predicate (verb/preposition - object)
    - of → emotion: constraint
    - of → nostalgia: Predicate (verb/preposition - object)
    - of → comfort: Predicate (verb/preposition - object)
    - of → love: Predicate (verb/preposition - object)
    - nostalgia → and: Connection
    - comfort → and: Connection
    - love → and: Connection

### Sentence 4:

* **Input**
    - Her friends who read the journal found themselves moved by its sincerity and vivid details.
* **Output**
    - Her → friends: Constraint
    - friends → found: Predicate (subject - verb)
    - found → themselves: Predicate (verb - object)
    - moved→ friends: Predicate (verb - object)
    - details →moved: Predicate (subject - verb)
    - its → details: Constraint
    - sincerity → and: Connection
    - sincerity → details: Constraint
    - and → vivid: connection
    - vivid → details: Constraint
    - who → read: Predicate (subject - verb)
    - friends →read: Predicate (subject - verb)
    - friends →who: connection
    - read → journal: Predicate (verb - object)
    - the → journal: Constraint
    - its →journal: connection

### Sentence 5:

* **Input**
    - Their encouragement pushed Sarah to consider turning the journal into a book.
* **Output**
    - Their → encouragement: Constraint
    - encouragement → pushed: Predicate (subject - verb)
    - pushed → Sarah: Predicate (verb/proposition - object)
    - Sarah → consider: Predicate (subject - verb)
    - Sarah → turning: Predicate (subject - verb)
    - consider → turning: Predicate (verb/proposition - object)
    - turning → journal: Predicate (verb/proposition - object)
    - the → journal: Constraint
    - into → turning: constraint
    - into → book: Predicate (preposition - object)
    - a → book: Constraint

### Sentence 6:

* **Input**
    - Emily received a letter from her best friend last week.
* **Output**
    - Emily → received: Predicate (subject - verb)
    - received → letter: Predicate (verb - object)
    - from → friend: Predicate (preposition - object)
    - from → received: Constraint
    - from → letter: Constraint
    - week → received: Constraint
    - last→week: Constraint

### Sentence 7:

* **Input**
    - The letter was filled with stories about their childhood adventures.
* **Output**
    - The → letter: Constraint
    - stories → filled: Predicate (subject - verb)
    - the → letter: Constraint
    - with → filled: constraint
    - with → letter: Predicate (verb/preposition - object)
    - about → stories: constraint
    - about → adventures: Predicate (verb/preposition - object)
    - their → childhood: Constraint
    - childhood → adventures: Constraint

### Sentence 8:

* **Input**
    - She smiled as she read about the time they built a treehouse together.
* **Output**
    - She → smiled: Predicate (subject - verb)
    - she → read: Predicate (subject - verb)
    - about → read: constraint
    - about → time: Predicate (preposition - object)
    - The → time: constraint
    - time → built: constraint
    - they → built: Predicate (subject - verb)
    - built → treehouse: Predicate (verb - object)
    - together → built: constraint
    - a → treehouse: Constraint (determiner - noun)
    - as → read: Predicate (verb - object)
    - as → smiled: Constraint

### Sentence 9:

* **Input**
    - It was one of the happiest moments of her life.
* **Output**
    - It → was: Predicate (subject - verb)
    - was → moments: Predicate (verb - object)
    - of → one: Constraint
    - of → moments: Predicate (preposition - object)
    - the → moments: Constraint
    - happiest → moments: Constraint
    - of → moments: Constraint
    - of → life: Predicate (preposition - object)
    - her → life: Constraint

### Sentence 10:

* **Input**
    - That memory, like many others, stayed with her even today.
* **Output**

    - That → memory: Constraint
    - memory → stayed: Predicate (subject - verb)
    - with → stayed: constraint
    - with → her: Predicate (verb/proposition - object)
    - even → today: Constraint
    - Like → memory: constraint
    - Like → others: Predicate (verb/proposition - object)
    - Many → others: constraint

### Sentence 11:

* **Input**
    - She was very sad yesterday.
* **Output**

    - She → was: Predicate (subject - verb)
    - was → sad: Predicate (verb - object)
    - very → sad: Constraint
    - yesterday → was: Constraint

### Sentence 12:

* **Input**
    - It is a lie that you love her.
* **Output**

    - It → is: Predicate (subject - verb)
    - Is → lie: Predicate (verb/proposition - object)
    - a → lie: Constraint
    - that → lie: connection
    - you → love: Predicate (subject - verb)
    - love → her: Predicate (verb/proposition - object)

### Sentence 13:

* **Input**
    - That truth broke her heart again.
* **Output**
    - That → truth: constraint
    - truth → broke: Predicate (subject - verb)
    - broke → heart: Predicate (verb/proposition - object)
    - her → heart: Constraint
    - again→ broke: Constraint

### Sentence 14:

* **Input**
    - Nobody told her the full story.
* **Output**
    - Nobody → told: Predicate (subject - verb)
    - told → her: Predicate (verb - object)
    - told → story: Predicate (verb - object)
    - story → her: constraint
    - the → story: Constraint
    - full → story: Constraint

### Sentence 15:

* **Input**
    - She waited by the window, hoping you would return.
* **Output**
    - She → waited: Predicate (subject - verb)
    - by → waited: constraint
    - by → window: Predicate (preposition - object)
    - The → window: constraint
    - She → hoping: Predicate (subject - verb)
    - hoping → return: Predicate (verb - object)
    - hoping → waited: constraint
    - you→ return: Predicate (subject - verb)
    - would → return: Constraint (auxiliary - main verb)

### Sentence 16:

* **Input**
    - But it never happened.
* **Output**
    - But → happened: Constraint
    - it → happened: Predicate (subject - verb)
    - Never → happened: constraint

### Sentence 17:

* **Input**
    - The pain, like before, settled deep within her.
* **Output**
    - The → pain: constraint
    - pain → settled: Predicate (subject - verb)
    - Like → pain: constraint
    - Like → before: Predicate (prep - object)
    - deep → settled: Constraint
    - within → settled: constraint
    - within → her: Predicate (prep - object)

### Sentence 18:

* **Input**
    - Design a vacation house that can fly easily from one location to another
* **Output**
    - Design → house: Predicate (verb/preposition - object)
    - A → house: Constraint
    - Vacation → House: Constraint
    - House → that: Connection
    - That → fly: Predicate (subject - verb)
    - Can → fly: Constraint
    - from → Fly: Constraint
    - From → location: Predicate (verb/preposition - object)
    - One → location: Constraint
    - To → fly: Constraint
    - To → location: Predicate (verb/preposition - object)
    - Another → location: Constraint
    - From → to: Connection

### Sentence 19:

* **Input**
    - Upscale 5 MW wind turbine_1 to 10 MW wind turbine_2
* **Output**
    - Upscale → turbine: Predicate (verb/preposition - object)
    - wind → turbine_1: Constraint
    - wind → turbine_2: Constraint
    - 5 MW → turbine_1: Constraint
    - To → upscale: Constraint
    - To → turbine_2: Predicate (verb/preposition - object)
    - 10 MW → turbine_2: Constraint

### Sentence 20:

* **Input**
    - Design a web system to manage the editorial workflow of the JIDPS journal.

* **Output**

    - Design → system: Predicate (verb/proposition - object)
    - A → system: Constraint
    - Web → system: Constraint
    - To → design: Constraint
    - To → manage: Predicate (verb/proposition - object)
    - Manage → workflow: Predicate (verb/proposition - object)
    - Editorial → workflow: Constraint
    - The → workflow: Constraint
    - of →Workflow: Constraint
    - Of → journal: Predicate (verb/proposition - object)
    - JIDPS → journal: Constraint
    - The → journal: Constraint

### Sentence 21:

* **Input**
    - Driver needs to stop and slow down a vehicle effectively and efficiently.
* **Output**
    - Driver → needs: Predicate (subject - verb)
    - To → needs: Constraint
    - to → stop: Predicate (verb/proposition - object)
    - Effectively → stop: Constraint
    - Efficiently → stop: Constraint
    - and → stop: connect
    - and → slow: connect
    - To → slow: Predicate (verb/proposition - object)
    - down → slow: Constraint
    - Effectively → slow: Constraint
    - Efficiently → slow: Constraint
    - Stop → vehicle: Predicate (verb/proposition - object)
    - slow → vehicle: Predicate (verb/proposition - object)
    - A → vehicle: Constraint
