# Complete Universal Dependencies Relations Provided by Stanza

Stanza follows the **Universal Dependencies v2.5 standard** and provides all **37 core universal syntactic relations**. Here's the complete list organized by functional categories:

## Core Relations (37 Universal Relations)

### **1. Core Arguments of Clausal Predicates**

| Relation | Description | Example |
|----------|-------------|---------|
| **nsubj** | Nominal subject | "**John** runs" → nsubj(runs, John) |
| **nsubj:pass** | Passive nominal subject | "**John** was seen" → nsubj:pass(seen, John) |
| **nsubj:outer** | Outer clause nominal subject | "That **he** left is obvious" → nsubj:outer(obvious, he) |
| **obj** | Object | "John sees **Mary**" → obj(sees, Mary) |
| **iobj** | Indirect object | "John gave **Mary** a book" → iobj(gave, Mary) |
| **csubj** | Clausal subject | "**That he left** is obvious" → csubj(obvious, left) |
| **csubj:pass** | Clausal passive subject | "**That he left** was reported" → csubj:pass(reported, left) |
| **csubj:outer** | Outer clause clausal subject | Complex clausal constructions |

### **2. Non-Core Dependents of Clausal Predicates**

| Relation | Description | Example |
|----------|-------------|---------|
| **obl** | Oblique nominal | "John went **home**" → obl(went, home) |
| **obl:agent** | Oblique agent in passive | "John was seen **by Mary**" → obl:agent(seen, Mary) |
| **obl:arg** | Oblique argument | Language-specific oblique arguments |
| **obl:lmod** | Locative modifier | "John lives **in Paris**" → obl:lmod(lives, Paris) |
| **obl:tmod** | Temporal modifier | "John left **yesterday**" → obl:tmod(left, yesterday) |
| **vocative** | Vocative | "**John**, come here!" → vocative(come, John) |
| **expl** | Expletive | "**There** are books" → expl(are, There) |
| **expl:impers** | Impersonal expletive | Impersonal constructions |
| **expl:pass** | Reflexive passive marker | Reflexive passive constructions |
| **expl:pv** | Reflexive clitic | Inherently reflexive verbs |
| **dislocated** | Dislocated elements | Topicalized elements |
| **advcl** | Adverbial clause modifier | "John left **when Mary arrived**" → advcl(left, arrived) |
| **advcl:relcl** | Adverbial relative clause | Relative clauses modifying predicates |
| **advmod** | Adverbial modifier | "John runs **fast**" → advmod(runs, fast) |
| **advmod:emph** | Emphasizing word | "John **really** likes it" → advmod:emph(likes, really) |
| **advmod:lmod** | Locative adverbial | "John is **here**" → advmod:lmod(is, here) |
| **discourse** | Discourse element | "**Well**, I think..." → discourse(think, Well) |

### **3. Dependents of Nominals**

| Relation | Description | Example |
|----------|-------------|---------|
| **nmod** | Nominal modifier | "the book **of John**" → nmod(book, John) |
| **nmod:poss** | Possessive nominal modifier | "**John's** book" → nmod:poss(book, John) |
| **nmod:tmod** | Temporal modifier | "**yesterday's** news" → nmod:tmod(news, yesterday) |
| **appos** | Appositional modifier | "John, **the teacher**" → appos(John, teacher) |
| **nummod** | Numeric modifier | "**three** books" → nummod(books, three) |
| **nummod:gov** | Numeric modifier (governing) | Language-specific numeric constructions |
| **acl** | Adnominal clause | "the book **I read**" → acl(book, read) |
| **acl:relcl** | Relative clause modifier | "the book **that I read**" → acl:relcl(book, read) |
| **amod** | Adjectival modifier | "**red** book" → amod(book, red) |

### **4. Case-Marking, Prepositions, Possessive Clitics**

| Relation | Description | Example |
|----------|-------------|---------|
| **case** | Case marking | "in **the** house" → case(house, in) |
| **det** | Determiner | "**the** book" → det(book, the) |
| **det:numgov** | Pronominal quantifier (governing) | Language-specific constructions |
| **det:nummod** | Pronominal quantifier (agreeing) | Language-specific constructions |
| **det:poss** | Possessive determiner | "**my** book" → det:poss(book, my) |
| **clf** | Classifier | "three **本** books" (Chinese) → clf(three, 本) |

### **5. Coordination**

| Relation | Description | Example |
|----------|-------------|---------|
| **conj** | Conjunct | "John **and** Mary" → conj(John, Mary) |
| **cc** | Coordinating conjunction | "John **and** Mary" → cc(Mary, and) |
| **cc:preconj** | Preconjunct | "**both** John and Mary" → cc:preconj(John, both) |

### **6. Multiword Expressions**

| Relation | Description | Example |
|----------|-------------|---------|
| **fixed** | Fixed multiword expression | "**as well as**" → fixed(as, well), fixed(as, as) |
| **flat** | Flat expression | "**John Smith**" → flat(John, Smith) |
| **flat:foreign** | Foreign words | "**per se**" → flat:foreign(per, se) |
| **flat:name** | Names | "**New York**" → flat:name(New, York) |
| **compound** | Compound | "**dog house**" → compound(house, dog) |
| **compound:lvc** | Light verb construction | Language-specific LVCs |
| **compound:prt** | Phrasal verb particle | "give **up**" → compound:prt(give, up) |
| **compound:redup** | Reduplicated compounds | Language-specific reduplication |
| **compound:svc** | Serial verb compounds | Language-specific serial verbs |

### **7. Loose Joining Relations**

| Relation | Description | Example |
|----------|-------------|---------|
| **list** | List | "a, b, c" → list(a, b), list(a, c) |
| **parataxis** | Parataxis | "John came, Mary left" → parataxis(came, left) |
| **orphan** | Orphan | Elliptical constructions |
| **goeswith** | Goes with | Broken tokens that belong together |
| **reparandum** | Overridden disfluency | Speech repairs |

### **8. Special Clausal Dependents**

| Relation | Description | Example |
|----------|-------------|---------|
| **aux** | Auxiliary | "John **has** arrived" → aux(arrived, has) |
| **aux:pass** | Passive auxiliary | "John **was** seen" → aux:pass(seen, was) |
| **cop** | Copula | "John **is** tall" → cop(tall, is) |
| **mark** | Marker | "I think **that** he left" → mark(left, that) |
| **ccomp** | Clausal complement | "I think **he left**" → ccomp(think, left) |
| **xcomp** | Open clausal complement | "I want **to go**" → xcomp(want, go) |

### **9. Special Relations**

| Relation | Description | Example |
|----------|-------------|---------|
| **punct** | Punctuation | "John runs**.**" → punct(runs, .) |
| **root** | Root | Root of the dependency tree |
| **dep** | Unspecified dependency | Fallback for unclear relations |

## Semi-Mandatory Subtypes

Stanza also supports these important subtypes when the phenomenon exists in the language:

- **nsubj:pass** - for passive subjects
- **aux:pass** - for passive auxiliaries  
- **expl:impers** - for impersonal expletives
- **acl:relcl** - for relative clauses
- **obl:agent** - for passive agents

## Usage in Stanza

All these relations are automatically detected when you run Stanza's dependency parser:

```python
import stanza
nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse')
doc = nlp("The quick brown fox jumps over the lazy dog.")

for sent in doc.sentences:
    for word in sent.words:
        print(f"{word.text} --{word.deprel}--> {sent.words[word.head-1].text if word.head > 0 else 'ROOT'}")
```

## Key Features

- **Universal**: Works consistently across 100+ languages
- **Hierarchical**: Subtypes provide language-specific detail
- **Complete**: Covers all grammatical phenomena
- **Standardized**: Based on Universal Dependencies v2.5 specification
- **Linguistically Motivated**: Reflects cross-linguistic grammatical universals

This comprehensive set of 37 core relations plus subtypes allows Stanza to capture the full range of syntactic relationships in human languages while maintaining cross-linguistic consistency.
