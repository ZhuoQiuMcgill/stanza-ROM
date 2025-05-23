# SBAR Sentences

This file contains sentences with SBAR (subordinate clause) structures that were extracted.

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

    - The girl whom I met is nice.

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
    - The movie that we watched was amazing.
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

    - This is the place where we stayed.

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

### Sentence 11:
* **Input**
    - I stayed home because it was raining.
* **Output**
    - I → stayed: Predicate (subject - verb)
    - Stayed → home: Predicate (verb/proposition - object)
    - Because → stayed: Constraint
    - Because → was: Predicate (verb/proposition - object)
    - It → was: Predicate (subject - verb)
    - Was → raining: Predicate (verb/proposition - object)

### Sentence 12:
* **Input**
    - Although she was tired, she finished the report.
* **Output**
    - Although → was: Predicate (verb/proposition - object)
    - Although → finished: Constraint
    - She → was: Predicate (subject - verb)
    - Was → tired: Predicate (verb/proposition - object)
    - She → finished: Predicate (subject - verb)
    - Finished → report: Predicate (verb/proposition - object)
    - The → report: Constraint

### Sentence 13:
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

### Sentence 14:
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

### Sentence 15:
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

### Sentence 16:
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

### Sentence 17:
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

### Sentence 18:
* **Input**
    - It is a lie that you love her.
* **Output**

    - It → is: Predicate (subject - verb)
    - Is → lie: Predicate (verb/proposition - object)
    - a → lie: Constraint
    - that → lie: connection
    - you → love: Predicate (subject - verb)
    - love → her: Predicate (verb/proposition - object)

### Sentence 19:
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

### Sentence 20:
* **Input**
    - Design a vacation house that can fly easily from one location to another.
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

### Sentence 21:
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

### Sentence 22:
* **Input**
    - I don't know whether he’ll call or text.
* **Output**
    - I → know: Predicate (subject - verb)
    - Don't → know: Constraint
    - Whether → call: Predicate (verb/preposition - object)
    - Or → text: Predicate (verb/preposition - object)
    - He → call: Predicate (subject - verb)
    - He → text: Predicate (subject - verb)
    - Will → call: Constraint
    - Will → text: Constraint
    - Whether → Or: Connection
    - Whether → know: Constraint
    - Or → know: Constraint

### Sentence 23:
* **Input**
    - She’s unsure whether to accept the job or continue studying.
* **Output**
    - She → is: Predicate (subject - verb)
    - Is → unsure: Predicate (verb/preposition - object)
    - Whether → accept: Predicate (verb/preposition - object)
    - Or → continue: Predicate (verb/preposition - object)
    - To → accept: Predicate (verb/preposition - object)
    - To → continue: Predicate (verb/preposition - object)
    - Accept → job: Predicate (verb/preposition - object)
    - The → job: Constraint
    - Continue → studying: Predicate (verb/preposition - object)
    - Whether → Or: Connection
    - Whether → is: Constraint
    - Or → is: Constraint

### Sentence 24:
* **Input**
    - This task is not as easy as it looks.
* **Output**
    - Task → is: Predicate (subject - verb)
    - This → task: Constraint
    - Is → easy: Predicate (verb/preposition - object)
    - Not → easy: Constraint
    - As → is: Constraint
    - As → easy: Predicate (verb/preposition - object)
    - As (2) → easy: Constraint
    - As (2) → looks: Predicate (verb/preposition - object)
    - It → looks: Predicate (subject - verb)
    - As → as (2): Connection

### Sentence 25:
* **Input**
    - She enjoys painting as much as she enjoys dancing.
* **Output**
    - She → enjoys: Predicate (subject - verb)
    - Enjoys → painting: Predicate (verb/preposition - object)
    - She → enjoys: Predicate (subject - verb) (second clause)
    - Enjoys → dancing: Predicate (verb/preposition - object) (second clause)
    - Much → painting: Constraint
    - As → enjoys: Constraint
    - As → much: Predicate (verb/preposition - object)
    - As (2) → much: Constraint
    - As (2) → enjoys: Predicate (verb/preposition - object)
    - As → as (2): Connection

### Sentence 26:
* **Input**
    - Just as the moon affects the tides, so does the sun influence them.
* **Output**
    - Moon → affects: Predicate (subject - verb)
    - Affects → tides: Predicate (verb/preposition - object)
    - The → moon: Constraint
    - The → tides: Constraint
    - Just → as: Constraint
    - As → affects: Constraint
    - Sun → influence: Predicate (subject - verb)
    - Influence → them: Predicate (verb/preposition - object)
    - The → sun: Constraint
    - So → influence: Predicate (verb/preposition - object)
    - Does → influence: Constraint
    - As → so: Connection

### Sentence 27:
* **Input**
    - Just as honesty builds trust, so does kindness.
* **Output**
    - Honesty → builds: Predicate (subject - verb)
    - Builds → trust: Predicate (verb/preposition - object)
    - Just → so: Constraint
    - As → builds: Constraint
    - Kindness → builds: Predicate (subject - verb)
    - Builds → trust: Predicate (verb/preposition - object) (implied)
    - So → builds: Predicate (verb/preposition - object)
    - Does → builds: Constraint
    - As → so: Connection

### Sentence 28:
* **Input**
    - Just as we need water to survive, so do plants need sunlight.
* **Output**
    - We → need: Predicate (subject - verb)
    - Need → water: Predicate (verb/preposition - object)
    - Water → survive: Constraint
    - To → survive: Constraint
    - Just → so: Constraint
    - As → need: Constraint
    - Plants → need: Predicate (subject - verb)
    - Need → sunlight: Predicate (verb/preposition - object)
    - So → need: Predicate (verb/preposition - object)
    - Do → need: Constraint
    - As → so: Connection

### Sentence 29:
* **Input**
    - No sooner had she sat down than the phone rang.
* **Output**
    - We → arrived: Predicate (subject - verb)
    - Had → arrived: Constraint
    - No sooner → arrived: Constraint
    - It → started: Predicate (subject - verb)
    - To → started: Constraint
    - To → rain: Predicate (verb/preposition - object)
    - Than → started: Predicate (verb/preposition - object)
    - No sooner → than: Connection

### Sentence 30:
* **Input**
    - I’d rather read a book than watch TV.
* **Output**
    - I → read: Predicate (subject - verb)
    - Would → read: Constraint
    - Rather → read: Constraint
    - Read → book: Predicate (verb/preposition - object)
    - A → book: Constraint
    - Than → watch: Predicate (verb/preposition - object)
    - I → watch: Predicate (subject - verb)
    - Watch → TV: Predicate (verb/preposition - object)
    - Rather → than: Connection

### Sentence 31:
* **Input**
    - What she said surprised everyone.
* **Output**
    - She → said: Predicate (subject - verb)
    - said → What: Predicate (verb/proposition - object)
    - What → surprised: Predicate (subject - verb)
    - Surprised → everyone: Predicate (verb/proposition - object)

### Sentence 32:
* **Input**
    - That he lied was obvious.
* **Output**
    - He → lied: Predicate (subject - verb)
    - That → lied: connection
    - That → was: Predicate (subject - verb)
    - Was → obvious: Predicate (verb/proposition - object)
    - lied → was: Predicate (subject - verb)

### Sentence 33:
* **Input**
    - Whether we will win depends on our effort.
* **Output**
    - We → win: Predicate (subject - verb)
    - Will → win: Constraint
    - Whether → win: Predicate (verb/proposition - object)
    - Whether → depends: Predicate (subject - verb)
    - win → Depends: Predicate (subject - verb)
    - On → depends: Constraint
    - On → effort: Predicate (verb/proposition - object)
    - Our → effort: Constraint

### Sentence 34:
* **Input**
    - How she managed to escape is still a mystery.
* **Output**
    - She → managed: Predicate (subject - verb)
    - to → Managed: Constraint
    - To → escape: Predicate (verb/proposition - object)
    - How → managed: Constraint
    - How → is: Predicate (subject - verb)
    - Is → mystery: Predicate (verb/proposition - object)
    - A → mystery: Constraint
    - Still → is: Constraint

### Sentence 35:
* **Input**
    - When the meeting starts is still unknown.
* **Output**
    - The → meeting: Constraint
    - Meeting → starts: Predicate (subject - verb)
    - When → starts: constraint
    - When → is: Predicate (subject - verb)
    - Is → unknown: Predicate (verb/proposition - object)
    - Still → is: Constraint

## Object Clauses

### Sentence 36:
* **Input**
    - I know that she is right.
* **Output**
    - I → know: Predicate (subject - verb)
    - Know → is: Predicate (verb/proposition - object)
    - She → is: Predicate (subject - verb)
    - Is → right: Predicate (verb/proposition - object)
    - That → is: Connection

### Sentence 37:
* **Input**
    - She didn’t tell me what had happened.
* **Output**
    - She → tell: Predicate (subject - verb)
    - Didn’t → tell: Constraint
    - Tell → me: Predicate (verb/proposition - object)
    - Tell → what: Predicate (verb/proposition - object)
    - What → happened: Predicate (subject - verb)
    - Had → happened: Constraint
    - me → what: Constraint

### Sentence 38:
* **Input**
    - We’re thinking about how we can solve the problem.
* **Output**
    - We → thinking: Predicate (subject - verb)
    - Are → thinking: Constraint
    - about → Thinking: Constraint
    - About → how: Predicate (verb/proposition - object)
    - How → solve: Constraint
    - We → solve: Predicate (subject - verb)
    - Can → solve: Constraint
    - Solve → problem: Predicate (verb/proposition - object)
    - The → problem: Constraint

### Sentence 39:
* **Input**
    - He’s not sure if he locked the door.
* **Output**
    - He → is: Predicate (subject - verb)
    - Is → sure: Predicate (verb/proposition - object)
    - Not → sure: Constraint
    - If → locked: Predicate (verb/proposition - object)
    - If → is: Constraint
    - He → locked: Predicate (subject - verb)
    - Locked → door: Predicate (verb/proposition - object)
    - The → door: Constraint

### Sentence 40:
* **Input**
    - I don’t know when the package will arrive.
* **Output**
    - I → know: Predicate (subject - verb)
    - Don’t → know: Constraint
    - Know → arrive: Predicate (verb/proposition - object)
    - When → arrive: Constraint
    - When → know: Predicate (verb/proposition - object)
    - The → package: Constraint
    - Package → arrive: Predicate (subject - verb)
    - Will → arrive: Constraint

## Predicative (Complement) Clauses

### Sentence 41:
* **Input**
    - The truth is that she never left.
* **Output**
    - The → truth: Constraint
    - Truth → is: Predicate (subject - verb)
    - Is → left: Predicate (verb/proposition - object)
    - Is → that: Predicate (verb/proposition - object)
    - That → left: Connection
    - She → left: Predicate (subject - verb)
    - Never → left: Constraint

### Sentence 42:
* **Input**
    - My suggestion is that we take a break.
* **Output**
    - My → suggestion: Constraint
    - Suggestion → is: Predicate (subject - verb)
    - Is → take: Predicate (verb/proposition - object)
    - Is → that: Predicate (verb/proposition - object)
    - That → take: Connection
    - We → take: Predicate (subject - verb)
    - Take → break: Predicate (verb/proposition - object)
    - A → break: Constraint

### Sentence 43:
* **Input**
    - The problem is how we can get there.
* **Output**
    - The → problem: Constraint
    - Problem → is: Predicate (subject - verb)
    - Is → how: Predicate (verb/proposition - object)
    - How → get: Constraint
    - How → is: Connection
    - We → get: Predicate (subject - verb)
    - Can → get: Constraint
    - Get → there: Predicate (verb/proposition - object)

### Sentence 44:
* **Input**
    - The question is whether he will accept the offer.
* **Output**
    - The → question: Constraint
    - Question → is: Predicate (subject - verb)
    - Is → Whether: Predicate (verb/proposition - object)
    - Whether → accept: Predicate (verb/proposition - object)
    - He → accept: Predicate (subject - verb)
    - Will → accept: Constraint
    - Accept → offer: Predicate (verb/proposition - object)
    - The → offer: Constraint

## Appositive Clauses

### Sentence 45:
* **Input**
    - I heard the news that she got married.
* **Output**
    - I → heard: Predicate (subject - verb)
    - Heard → news: Predicate (verb/proposition - object)
    - The → news: Constraint
    - that → News: Constraint
    - That → got: Predicate (verb/proposition - object)
    - She → got: Predicate (subject - verb)
    - Got → married: Predicate (verb/proposition - object)

### Sentence 46:
* **Input**
    - The idea that hard work brings success is widely accepted.
* **Output**
    - The → idea: Constraint
    - Idea → is: Predicate (subject - verb)
    - Is → accepted: Predicate (verb/proposition - object)
    - Widely → accepted: Constraint
    - That → idea: Constraint
    - That → brings: Predicate (verb/proposition - object)
    - Hard → work: Constraint
    - Work → brings: Predicate (subject - verb)
    - Brings → success: Predicate (verb/proposition - object)

### Sentence 47:
* **Input**
    - She rejected the suggestion that we cancel the meeting.
* **Output**
    - She → rejected: Predicate (subject - verb)
    - Rejected → suggestion: Predicate (verb/proposition - object)
    - The → suggestion: Constraint
    - That → suggestion: Constraint
    - That → cancel: Predicate (verb/proposition - object)
    - We → cancel: Predicate (subject - verb)
    - Cancel → meeting: Predicate (verb/proposition - object)
    - The → meeting: Constraint

### Sentence 48:
* **Input**
    - We faced the fact that we were out of time.
* **Output**
    - We → faced: Predicate (subject - verb)
    - Faced → fact: Predicate (verb/proposition - object)
    - The → fact: Constraint
    - That → fact: Constraint
    - That → were: Predicate (verb/proposition - object)
    - We → were: Predicate (subject - verb)
    - Were → out: Predicate (verb/proposition - object)
    - Out → of: Constraint
    - Of → time: Predicate (verb/proposition - object)

