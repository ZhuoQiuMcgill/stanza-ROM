### Sentence 1:

* **Input**
    - She wanted to go for a walk, but it started raining.
* **Output**
    - She → wanted: Predicate (subject - verb)
    - To → wanted: Constraint
    - To → go: Predicate (verb/preposition - object)
    - To → wanted: Constraint
    - Go → walk: Predicate (verb/preposition - object)
    - For → go: Constraint
    - For → walk: Predicate (preposition - object)
    - A → walk: Constraint
    - It → started: Predicate (subject - verb)
    - Started → raining: Predicate (verb/preposition - object)
    - But → wanted: Constraint
    - But → started: Predicate (verb/preposition - object)

### Sentence 2:

* **Input**
    - The sky was clear; we decided to go stargazing.
* **Output**
    - Sky → was: Predicate (subject - verb)
    - Was → clear: Predicate (verb/preposition - object)
    - The → sky: Constraint
    - We → decided: Predicate (subject - verb)
    - To→ decided: Constraint
    - To → go: Predicate (verb/preposition - object)
    - Go → stargazing: Predicate (verb/preposition - object)
    - [∅] → was: Connection (semicolon as structural connector)
    - [∅] → decided: Connection

### Sentence 3:

* **Input**
    - I was tired; however, I kept working.
* **Output**
    - I → was: Predicate (subject - verb)
    - Was → tired: Predicate (verb/preposition - object)
    - I → kept: Predicate (subject - verb)
    - Kept → working: Predicate (verb/preposition - object)
    - However → was: Constraint
    - However → kept: Predicate (verb/preposition - object)

### Sentence 4:

* **Input**
    - She is both smart and creative.
* **Output**
    - She → is: Predicate (subject - verb)
    - Is → smart: Predicate (verb/preposition - object)
    - Is → creative: Predicate (verb/preposition - object)
    - Both → smart: Predicate (verb/preposition - object)
    - And → creative: Predicate (verb/preposition - object)
    - both → is: Constraint
    - and → is: Constraint

### Sentence 5:

* **Input**
    - Both my brother and sister are engineers.
* **Output**
    - My → brother: Constraint
    - Both → brother: Predicate (verb/preposition - object)
    - And → sister: Predicate (verb/preposition - object)
    - Brother → are: Predicate (subject - verb)
    - Sister → are: Predicate (subject - verb)
    - Are → engineers: Predicate (verb/preposition - object)
    - both → and: connection
    - both → are: Constraint
    - and → are: Constraint

### Sentence 6:

* **Input**
    - Not only did he win, but he also broke the record.
* **Output**
    - He → won: Predicate (subject - verb)
    - Not only → won: Predicate (verb/preposition - object)
    - He → broke: Predicate (subject - verb)
    - Broke → record: Predicate (verb/preposition - object)
    - The → record: Constraint
    - But also → broke: Predicate (verb/preposition - object)
    - Not only → but also: connection

### Sentence 7:

* **Input**
    - The movie was not only long but also boring.
* **Output**
    - Movie → was: Predicate (subject - verb)
    - The → movie: Constraint
    - Was → long: Predicate (verb/preposition - object)
    - Was → boring: Predicate (verb/preposition - object)
    - Not only → long: Predicate (verb/preposition - object)
    - But also → boring: Predicate (verb/preposition - object)
    - Not only → but also: connection
    - Not only → was: Constraint
    - But also → was: Constraint

### Sentence 8:

* **Input**
    - You can either stay home or come with us.
* **Output**
    - You → stay: Predicate (subject - verb)
    - You → come: Predicate (subject - verb)
    - Can → stay: Constraint
    - Can → come: Constraint
    - Stay → home: Constraint
    - Come → with: Constraint
    - With → us: Predicate (verb/preposition - object)
    - Either → stay: Predicate (verb/preposition - object)
    - Or → come: Predicate (verb/preposition - object)
    - Either → or: connection
    - Input: Neither the manager nor the assistant answered.
    - The → manager: Constraint
    - The → assistant: Constraint
    - Manager → answered: Predicate (subject - verb)
    - Assistant → answered: Predicate (subject - verb)
    - Neither → manager: Predicate (verb/preposition - object)
    - Nor → assistant: Predicate (verb/preposition - object)
    - Neither → Nor: Connection
    - Neither → answered: Constraint
    - Nor → answered: Constraint

### Sentence 9:

* **Input**
    - Neither did he apologize, nor did he show any regret.
* **Output**
    - He → apologize: Predicate (subject - verb)
    - Did → apologize: Constraint
    - Not → apologize: Constraint
    - Neither → apologize: Predicate (verb/preposition - object)
    - He → show: Predicate (subject - verb)
    - Did → show: Constraint
    - Not → show: Constraint
    - Show → regret: Predicate (verb/preposition - object)
    - Any → regret: Constraint
    - Nor → show: Predicate (verb/preposition - object)
    - Neither → Nor: Connection

### Sentence 10:

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

### Sentence 11:

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

### Sentence 12:

* **Input**
    - She’s as tall as her brother.
* **Output**
    - She → is: Predicate (subject - verb)
    - Is → tall: Predicate (verb/preposition - object)
    - As → tall: Predicate (verb/preposition - object)
    - As → is: Constraint
    - Her → brother: Constraint
    - brother → is: Predicate (subject - verb)
    - As (2) → is (2): Predicate (verb/preposition - object)
    - As (2)→ tall: Constraint
    - As → as (2): Connection

### Sentence 13:

* **Input**
    - He ran as quickly as a professional athlete.
* **Output**
    - He → ran: Predicate (subject - verb)
    - Quickly → ran: Constraint
    - As → ran: Constraint
    - As → quickly: Predicate (verb/preposition - object)
    - A → athlete: Constraint
    - Professional → athlete: Constraint
    - athlete→ ran (2): Predicate (subject - verb)
    - As (2) → quickly: Constraint
    - As (2) → ran (2): Predicate (verb/preposition - object)
    - As → as (2): Connection

### Sentence 14:

* **Input**
    - She’s as tall as her brother.
* **Output**
    - She → is: Predicate (subject - verb)
    - Is → tall: Predicate (verb/preposition - object)
    - As → tall: Predicate (verb/preposition - object)
    - As → is: Constraint
    - Her → brother: Constraint
    - brother → is: Predicate (subject - verb)
    - As (2) → is (2): Predicate (verb/preposition - object)
    - As (2)→ tall: Constraint
    - As → as (2): Connection

### Sentence 15:

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

### Sentence 16:

* **Input**
    - He doesn’t eat as much chocolate as his brother.
* **Output**
    - He → eat: Predicate (subject - verb)
    - Doesn’t → eat: Constraint
    - Eat → chocolate: Predicate (verb/preposition - object)
    - Much → chocolate: Constraint
    - As → eat: Constraint
    - As → much: Predicate (verb/preposition - object)
    - As (2) → much: Constraint
    - As (2) → eat (2): Predicate (verb/preposition - object)
    - His → brother: Constraint
    - As → as (2): Connection

### Sentence 17:

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

### Sentence 18:

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

### Sentence 19:

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

### Sentence 20:

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

### Sentence 21:

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

### Sentence 22:

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

### Sentence 23:

* **Input**
    - He chose to walk rather than drive.
* **Output**
    - He → chose: Predicate (subject - verb)
    - Chose → walk: Predicate (verb/preposition - object)
    - To → chose: Constraint
    - To → walk: Predicate (verb/preposition - object)
    - To → drive: Predicate (verb/preposition - object)
    - Rather → walk: Constraint
    - Than → drive: Predicate (verb/preposition - object)
    - He → drive: Predicate (subject - verb)
    - Rather → than: Connection

### Sentence 24:

* **Input**
    - Rather than complain, she took action.
* **Output**
    - She → took: Predicate (subject - verb)
    - Took → action: Predicate (verb/preposition - object)
    - Rather → took: Constraint
    - Than → complain: Predicate (verb/preposition - object)
    - She → complain: Predicate (subject - verb)


















