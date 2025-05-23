"""
Complete ROM to UD Relations Mapper - FIXED VERSION

Maps Universal Dependencies from Stanza to 4 ROM relation types and outputs
in a clean format showing word relationships with corrected semantic directions.
Includes original UD relation information for debugging and verification.

MAJOR FIXES APPLIED based on evaluation reports:
- Standardized predicate relation type to "Predicate (verb/proposition - object)" for objects and complements.
- Corrected copula relation mapping.
- Refined handling of relative clauses (acl:relcl).
- Adjusted mapping for complementizer 'mark' relations.
- Updated specific handlers for copula, object relatives, and subordinating conjunctions.
"""

import stanza


class ROMGenerator:
    """
    A class for mapping Universal Dependencies relations to ROM (Relational Ontology Model) types.

    This class handles the initialization of the Stanza pipeline and provides methods
    to analyze sentences and extract ROM relations from UD parsing.
    """

    def __init__(self, lang: str = 'en', verbose: bool = False):
        """
        Initialize the ROM Generator with a Stanza pipeline.

        Args:
            lang: Language code (default: 'en')
            verbose: Whether to show verbose output from Stanza (default: False)
        """
        self.lang = lang
        self.nlp = stanza.Pipeline(
            lang,
            processors='tokenize,pos,lemma,depparse',
            verbose=verbose
        )

    @staticmethod
    def get_rom_mapping(ud_relation: str, word_text: str = None, word_pos: str = None,
                        head_pos: str = None, head_lemma: str = None) -> tuple:
        """
        Map UD relation to ROM type and determine semantic direction - FIXED VERSION
        Enhanced to handle complex constructions and coordination with proper directions

        Args:
            ud_relation: Universal Dependencies relation type
            word_text: Text of the dependent word
            word_pos: POS tag of the dependent word
            head_pos: POS tag of the head word
            head_lemma: Lemma of the head word

        Returns:
            tuple: (rom_description, reverse_direction)
        """

        # R1: Connection (Semantic/Functional Link)
        if ud_relation in {'cc', 'conj', 'parataxis', 'list', 'appos', 'dislocated',
                           'vocative', 'discourse', 'goeswith', 'reparandum'}:
            return 'Connection', False

        # Special case: Relative pronouns to antecedent (R1)
        # also handles 'that', 'if', 'whether' as complementizers connecting to their clause verb
        elif ud_relation in {'nsubj:relcl', 'obj:relcl'} or \
             (ud_relation == 'nmod' and word_pos == 'PRON') or \
             (ud_relation == 'mark' and word_text and word_text.lower() in {'that', 'whether', 'if'}):
            return 'Connection', False # marker -> verb_of_clause

        # R3: Predicate (Subject → Verb) - always subject to verb direction
        elif ud_relation in {'nsubj', 'nsubj:pass', 'nsubj:outer', 'csubj', 'csubj:pass', 'csubj:outer'}:
            return 'Predicate (subject - verb)', False

        # R4: Predicate (Verb/Prep → Object) - semantic head governs dependent
        # Changed "Predicate (verb - object)" to "Predicate (verb/proposition - object)"
        elif ud_relation in {'obj', 'iobj', 'ccomp', 'xcomp'}:
            return 'Predicate (verb/proposition - object)', True  # Reverse: head → dependent

        # Preposition handling - preposition governs its object
        elif ud_relation == 'case':
            # Preposition governs its object: "from → friend", "to → store"
            return 'Predicate (preposition - object)', False

        # Oblique relations - verb governs prepositional phrase or nominal
        # Changed "Predicate (verb - prepositional_phrase)" to "Predicate (verb - oblique)"
        elif ud_relation in {'obl', 'obl:agent', 'obl:arg', 'obl:tmod', 'obl:lmod'}:
            return 'Predicate (verb - oblique)', True  # Reverse: verb → PP head or nominal

        # Auxiliary verbs - auxiliary helps main verb (not reversed)
        elif ud_relation in {'aux', 'aux:pass'}:
            # Auxiliary → main verb: "will → go", "is → running"
            return 'Constraint', False

        # Copula verbs
        # Changed "Predicate (verb - object)" to "Predicate (verb/proposition - object)"
        elif ud_relation == 'cop':
            # Copula → predicate: "is → happy"
            return 'Predicate (verb/proposition - object)', False # copula -> predicative_complement

        # Mark relations with better context awareness
        elif ud_relation == 'mark':
            if word_text and word_text.lower() == 'to': # Infinitive marker
                # to → verb (handled by _handle_infinitives for more context)
                # Defaulting to a constraint here, specific handlers might override
                return 'Predicate (preposition - object)', False # 'to' acts like a preposition to the verb
            # 'that', 'whether', 'if' are now Connection above.
            elif word_text and word_text.lower() in {'because', 'although', 'since', 'while', 'unless', 'until'}:
                # Subordinating conjunctions: because → clause_verb (constraint on main verb is handled by _handle_subordinating_conjunctions)
                return 'Constraint', False # marker -> verb_of_its_clause
            elif word_text and word_text.lower() in {'when', 'where', 'why'}:
                # Temporal/causal markers: when → clause_verb
                return 'Constraint', False # marker -> verb_of_its_clause (specific handlers for relcl cases)
            else:
                # Default subordinating conjunction behavior
                return 'Constraint', False

        # Relative clause handling: acl:relcl
        # Changed from "Predicate (subject - verb)" to "Connection"
        # Specific handlers (_handle_object_relatives, etc.) should create more detailed relations.
        # This provides a basic link: antecedent → verb_of_relative_clause
        elif ud_relation == 'acl:relcl':
            return 'Connection', True  # Reverse: antecedent → verb_of_relcl

        # Adjectival clause (non-relative)
        elif ud_relation == 'acl':
            return 'Constraint', False # modifier -> head

        # R2: Constraint (Modifier/Qualifier) - enhanced coverage
        elif ud_relation in {'det', 'amod', 'advmod', 'advmod:emph', 'advmod:lmod',
                             'nmod', 'nmod:poss', 'nmod:tmod', 'nummod', 'nummod:gov',
                             'fixed', 'flat', 'flat:foreign', 'flat:name',
                             'det:numgov', 'det:nummod', 'det:poss', 'clf', 'cc:preconj'}:
            return 'Constraint', False

        # Compound words - typically modifier -> head, but Stanza has head -> modifier
        elif ud_relation in {'compound', 'compound:lvc', 'compound:prt', 'compound:redup',
                             'compound:svc'}:
            return 'Constraint', True # Reverse: head_of_compound -> modifier_part

        # Adverbial clause relation (main link, marker handled separately)
        elif ud_relation in {'advcl', 'advcl:relcl'}:
            # advcl_verb -> main_verb
            return 'Constraint', False # dependent_clause_verb -> main_clause_verb

        # Negation
        elif ud_relation == 'neg':
            return 'Constraint', False # neg_word -> modified_word

        # Default: skip unknown relations
        return None, False

    def analyze_sentence(self, sentence: str) -> list:
        """
        Analyze a sentence and extract ROM relations from UD parsing.
        Enhanced to handle coordination, comparatives, and complex constructions.

        Args:
            sentence: Input sentence to analyze

        Returns:
            List of dictionaries with ROM relations
        """
        doc = self.nlp(sentence)
        relations = []

        for sent in doc.sentences:
            # Standard dependency relations
            for word in sent.words:
                if word.head == 0:  # Skip root
                    continue

                head_word = sent.words[word.head - 1]

                # Skip nsubj when head has copula (handled by _handle_copula_constructions)
                if word.deprel == 'nsubj':
                    is_copula_construction = False
                    # Check if head_word is the predicative complement in a copula construction
                    for potential_copula in sent.words:
                        if potential_copula.head == head_word.id and potential_copula.deprel == 'cop':
                            # This 'word' (nsubj) is the subject of 'head_word' which has a 'copula'
                            # This will be handled by _handle_copula_constructions
                            is_copula_construction = True
                            break
                    if is_copula_construction:
                        continue

                # Skip 'cop' relations here, handled by _handle_copula_constructions
                if word.deprel == 'cop':
                    continue

                # Skip 'mark' relations if they are part of an advcl that will be handled
                if word.deprel == 'mark':
                    # If this mark belongs to an advcl, _handle_subordinating_conjunctions will deal with it
                    is_advcl_mark = False
                    for w_advcl in sent.words:
                        if w_advcl.id == word.head and w_advcl.deprel == 'advcl':
                            is_advcl_mark = True
                            break
                    if is_advcl_mark:
                        # Check if it's 'to' for infinitives, which might need separate handling
                        if not (word.text.lower() == 'to' and head_word.upos == 'VERB'): # allow 'to' for xcomp
                           continue # Skip other advcl marks

                rom_result = self.get_rom_mapping(
                    word.deprel, word.text, word.upos, head_word.upos, head_word.lemma
                )

                if rom_result[0] is None:
                    continue

                rom_description, reverse_direction = rom_result

                if reverse_direction:
                    relation_dict = {
                        "from": head_word.text,
                        "to": word.text,
                        "rom relation": rom_description,
                        "stanza ud": word.deprel
                    }
                else:
                    relation_dict = {
                        "from": word.text,
                        "to": head_word.text,
                        "rom relation": rom_description,
                        "stanza ud": word.deprel
                    }

                # Avoid duplicate relations that might be added by specific handlers
                # A simple check based on from, to, and ROM type (excluding UD for this check)
                simple_rel = (relation_dict["from"], relation_dict["to"], relation_dict["rom relation"])
                already_exists = any(
                    (r["from"] == simple_rel[0] and r["to"] == simple_rel[1] and r["rom relation"] == simple_rel[2])
                    for r in relations
                )
                if not already_exists:
                    relations.append(relation_dict)


            # Special constructions handling
            relations.extend(self._handle_copula_constructions(sent, relations))
            relations.extend(self._handle_coordination(sent, relations))
            relations.extend(self._handle_correlative_conjunctions(sent, relations)) # Needs review based on reports
            relations.extend(self._handle_comparatives(sent, relations)) # Needs review
            relations.extend(self._handle_object_relatives(sent, relations))
            relations.extend(self._handle_possessive_relatives(sent, relations))
            relations.extend(self._handle_temporal_causal_noun_relatives(sent, relations))
            relations.extend(self._handle_subordinating_conjunctions(sent, relations))
            relations.extend(self._handle_infinitives(sent, relations))
            relations.extend(self._handle_negation(sent, relations))

            # Deduplicate relations again after handlers
            final_relations = []
            seen_relations_tuples = set()
            for r in relations:
                # Using a tuple of (from, to, rom_relation, ud_relation) for uniqueness
                rel_tuple = (r["from"], r["to"], r["rom relation"], r["stanza ud"])
                if rel_tuple not in seen_relations_tuples:
                    final_relations.append(r)
                    seen_relations_tuples.add(rel_tuple)
            relations = final_relations


        return relations

    def _add_relation_if_new(self, relations_list: list, new_relation: dict):
        """Adds a relation only if it's not already present (based on from, to, rom_relation)."""
        simple_new_rel = (new_relation["from"], new_relation["to"], new_relation["rom relation"])
        is_present = any(
            r["from"] == simple_new_rel[0] and \
            r["to"] == simple_new_rel[1] and \
            r["rom relation"] == simple_new_rel[2]
            for r in relations_list
        )
        if not is_present:
            relations_list.append(new_relation)


    def _handle_coordination(self, sent, existing_relations):
        """Enhanced coordinating conjunction handling with proper semantic roles"""
        new_relations = []
        for word in sent.words:
            if word.deprel == 'cc':  # coordinating conjunction
                coordinator = word.text.lower()
                # The head of 'cc' is typically the first conjunct or the verb phrase it coordinates
                head_of_cc = sent.words[word.head - 1]

                # Find the conjuncts this 'cc' connects.
                # One conjunct is head_of_cc. The other is linked by 'conj' to head_of_cc.
                conjunct1 = head_of_cc
                conjunct2 = None
                for other_word in sent.words:
                    if other_word.deprel == 'conj' and other_word.head == head_of_cc.id:
                        conjunct2 = other_word
                        break

                if conjunct1 and conjunct2:
                    if coordinator in {'but', 'however', 'yet'}:
                        # Contrastive coordination
                        self._add_relation_if_new(new_relations, {
                            "from": coordinator, "to": conjunct1.text,
                            "rom relation": "Constraint", "stanza ud": f"cc({coordinator})→conj1"
                        })
                        self._add_relation_if_new(new_relations, {
                            "from": coordinator, "to": conjunct2.text,
                            "rom relation": "Predicate (conjunction - clause_element)", "stanza ud": f"cc({coordinator})→conj2"
                        })
                    elif coordinator in {'and', 'or'}:
                        # Standard coordination
                        self._add_relation_if_new(new_relations, {
                            "from": coordinator, "to": conjunct1.text,
                            "rom relation": "Connection", "stanza ud": f"cc({coordinator})→conj1"
                        })
                        self._add_relation_if_new(new_relations, {
                            "from": coordinator, "to": conjunct2.text,
                            "rom relation": "Connection", "stanza ud": f"cc({coordinator})→conj2"
                        })
        return new_relations


    def _handle_correlative_conjunctions(self, sent, existing_relations):
        """Handle correlative conjunctions like both...and, not only...but also"""
        # This handler needs significant review based on COMP_report.
        # The current implementation is too simplistic.
        # For now, returning empty to avoid adding possibly incorrect relations.
        new_relations = []
        # Example: "not only...but also"
        # COMP_report Sent 6: "Not only did he win, but he also broke the record."
        # Expected: "not only → but also: connection" (this is one part)
        # Expected: "not only → won: predicate (verb/preposition - object)"
        # Expected: "but also → broke: predicate (verb/preposition - object)"
        # This requires identifying the two parts of the correlative and the elements they modify.
        return new_relations


    def _handle_comparatives(self, sent, existing_relations):
        """Handle comparative constructions like as...as"""
        # This handler also needs review based on COMP_report.
        # Current: "as -> as: Connection"
        # Expected for "She’s as tall as her brother":
        # "as → tall: predicate (verb/preposition - object)"
        # "as → is: constraint" (linking 'as' to the verb of its clause)
        # "as (2) → brother: predicate (preposition - object)" (if 'as' acts like a prep)
        # "as (2) → is (implied verb of second part): predicate..."
        new_relations = []
        as_indices = [i for i, w in enumerate(sent.words) if w.text.lower() == 'as']
        if len(as_indices) >= 2:
            first_as_word = sent.words[as_indices[0]]
            second_as_word = sent.words[as_indices[1]]
            self._add_relation_if_new(new_relations, {
                "from": first_as_word.text, "to": second_as_word.text,
                "rom relation": "Connection", "stanza ud": "as...as_correlative"
            })
        return new_relations

    def _get_clause_verb(self, clause_head_word, sentence_words):
        """Helper to find the main verb of a clause, possibly navigating auxiliaries."""
        if clause_head_word.upos == 'VERB':
            # Check if it has a copula, then the head is the predicative complement
            for word in sentence_words:
                if word.head == clause_head_word.id and word.deprel == 'cop':
                    return clause_head_word # The predicative complement is the semantic head
            return clause_head_word
        # If clause_head_word is an AUX, find the verb it modifies
        if clause_head_word.upos == 'AUX':
            for word in sentence_words:
                if word.head == clause_head_word.id and word.upos == 'VERB': # Stanza might point verb to aux
                    return word
                # Or aux points to verb
                if clause_head_word.head == word.id and word.upos == 'VERB' and clause_head_word.deprel.startswith('aux'):
                     return word # This case seems less likely with Stanza's typical output
            # If it's a copula auxiliary, the head is the predicative complement
            if clause_head_word.deprel == 'cop':
                 return sentence_words[clause_head_word.head -1]


        # Fallback if not a verb or aux, or structure is complex
        return clause_head_word # Return itself, might be a nominal predicate etc.


    def _handle_object_relatives(self, sent, existing_relations):
        """Enhanced object relative clause handling (acl:relcl)"""
        new_relations = []
        for word in sent.words: # word is potential verb of relcl
            if word.deprel == 'acl:relcl':
                antecedent = sent.words[word.head - 1] # Noun that acl:relcl modifies

                # Find relative pronoun (obj or nsubj of the relcl verb 'word')
                relative_pronoun_word = None
                for child in sent.words:
                    if child.head == word.id: # child is dependent of relcl verb
                        if child.deprel in {'obj', 'nsubj'} and child.upos == 'PRON' and \
                           child.lemma.lower() in {'who', 'whom', 'which', 'that'}: # Common relative pronouns
                            relative_pronoun_word = child
                            break

                if relative_pronoun_word:
                    # Verb of relcl → relative pronoun
                    if relative_pronoun_word.deprel == 'obj':
                         self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": relative_pronoun_word.text,
                            "rom relation": "Predicate (verb/proposition - object)", "stanza ud": f"relcl_verb→obj_pronoun({word.deprel})"
                        })
                    # Relative pronoun → antecedent
                    self._add_relation_if_new(new_relations, {
                        "from": relative_pronoun_word.text, "to": antecedent.text,
                        "rom relation": "Connection", "stanza ud": f"rel_pronoun→antecedent({word.deprel})"
                    })
        return new_relations


    def _handle_possessive_relatives(self, sent, existing_relations):
        """Handle possessive relatives like 'whose'."""
        new_relations = []
        for word in sent.words:
            if word.lemma.lower() == 'whose':
                # 'whose' typically has 'nmod:poss' relation to the possessed noun
                # and its head (the possessed noun) is part of an acl:relcl
                possessed_noun = None
                if word.head != 0:
                    potential_possessed_noun = sent.words[word.head -1]
                    if word.deprel == 'nmod:poss': # Stanza often uses nmod:poss for whose -> noun
                         possessed_noun = potential_possessed_noun

                if possessed_noun:
                    # Find the acl:relcl this 'whose' construction is part of
                    # The possessed_noun is usually the subject or object within the relcl
                    verb_of_relcl = None
                    antecedent_of_relcl = None

                    # Search upwards from possessed_noun to find acl:relcl
                    curr = possessed_noun
                    visited_heads = set()
                    while curr.head != 0 and curr.id not in visited_heads:
                        visited_heads.add(curr.id)
                        parent_of_curr = sent.words[curr.head -1]
                        if parent_of_curr.deprel == 'acl:relcl':
                            verb_of_relcl = parent_of_curr
                            if verb_of_relcl.head != 0:
                                antecedent_of_relcl = sent.words[verb_of_relcl.head -1]
                            break
                        # If current is the head of acl:relcl itself
                        if curr.deprel == 'acl:relcl':
                            verb_of_relcl = curr
                            if verb_of_relcl.head != 0:
                                antecedent_of_relcl = sent.words[verb_of_relcl.head -1]
                            break
                        curr = parent_of_curr


                    if antecedent_of_relcl:
                        self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": antecedent_of_relcl.text,
                            "rom relation": "Connection", "stanza ud": "whose→antecedent"
                        })
                    if possessed_noun: # Should always be true if we got here
                         self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": possessed_noun.text,
                            "rom relation": "Constraint", "stanza ud": "whose→possessed_noun"
                        })
        return new_relations

    def _handle_temporal_causal_noun_relatives(self, sent, existing_relations):
        """Handle temporal/causal relatives like 'when'/'why' modifying nouns (e.g. "the year when...")"""
        new_relations = []
        for word in sent.words: # word is the marker e.g. 'when', 'why'
            if word.lemma.lower() in {'when', 'where', 'why'} and word.deprel == 'mark':
                # The head of 'mark' is the verb of the relative clause
                verb_of_relcl = sent.words[word.head - 1]
                if verb_of_relcl.deprel == 'acl:relcl':
                    # The head of 'acl:relcl' is the antecedent noun
                    antecedent_noun = sent.words[verb_of_relcl.head - 1]

                    # Marker -> Antecedent Noun
                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": antecedent_noun.text,
                        "rom relation": "Constraint", "stanza ud": f"{word.lemma}→antecedent_noun"
                    })
                    # Marker -> Verb of its clause (as per benchmark pattern for ADJ Sent 7 "when -> moved: predicate")
                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": verb_of_relcl.text,
                        "rom relation": "Predicate (marker - clause_verb)", # A more specific type
                        "stanza ud": f"{word.lemma}→verb_of_relcl"
                    })
        return new_relations


    def _handle_subordinating_conjunctions(self, sent, existing_relations):
        """Enhanced subordinating conjunction handling for advcl."""
        new_relations = []
        for advcl_verb_word in sent.words: # This is the head of the advcl (often a verb or aux)
            if advcl_verb_word.deprel == 'advcl':
                marker_word = None
                for child in sent.words:
                    if child.head == advcl_verb_word.id and child.deprel == 'mark':
                        marker_word = child
                        break

                if marker_word:
                    main_clause_verb_word = sent.words[advcl_verb_word.head - 1] # Verb that advcl modifies

                    # Find the true verb of the subordinate clause, not just advcl_verb_word if it's an aux
                    sub_clause_actual_verb = advcl_verb_word
                    # If advcl_verb_word is AUX or COP, find its main verb or predicative complement
                    if advcl_verb_word.upos == 'AUX':
                        found_verb = False
                        for w in sent.words: # look for verb governed by this aux
                            if w.head == advcl_verb_word.id and w.upos == 'VERB':
                                sub_clause_actual_verb = w
                                found_verb = True
                                break
                        if not found_verb and advcl_verb_word.deprel == 'cop': # if it's a copula aux
                             sub_clause_actual_verb = sent.words[advcl_verb_word.head-1] # the predicative complement


                    # Relation: marker -> verb_of_its_clause
                    # ADV report "because it was raining", expected "because -> was: predicate..."
                    # 'was' is copula for 'raining'. Here sub_clause_actual_verb would be 'raining' (if cop is head)
                    # or 'was' if we trace from 'raining' to its copula.
                    # Let's find the verb associated with the mark's head (advcl_verb_word)

                    verb_to_link_marker_to = advcl_verb_word # Default to head of mark
                    if advcl_verb_word.upos != 'VERB': # If head of mark is not a verb (e.g. AUX, ADJ)
                        # Try to find the main verb or copula of the subordinate clause
                        q = [advcl_verb_word]
                        visited_q = {advcl_verb_word.id}
                        verb_found_in_subclause = False
                        while q:
                            curr = q.pop(0)
                            if curr.upos == 'VERB':
                                verb_to_link_marker_to = curr
                                verb_found_in_subclause = True
                                break
                            # Check children for verbs or copulas
                            for child_w in sent.words:
                                if child_w.head == curr.id and child_w.id not in visited_q:
                                    if child_w.upos == 'VERB' or child_w.deprel == 'cop':
                                        verb_to_link_marker_to = child_w if child_w.upos == 'VERB' else curr # link to cop's head
                                        verb_found_in_subclause = True
                                        break
                                    q.append(child_w)
                                    visited_q.add(child_w.id)
                            if verb_found_in_subclause: break
                            # Check head if current is aux
                            if curr.upos == 'AUX' and curr.head != 0:
                                head_of_aux = sent.words[curr.head-1]
                                if head_of_aux.id not in visited_q:
                                     if head_of_aux.upos == 'VERB':
                                          verb_to_link_marker_to = head_of_aux
                                          break
                                     q.append(head_of_aux)
                                     visited_q.add(head_of_aux.id)


                    self._add_relation_if_new(new_relations, {
                        "from": marker_word.text,
                        "to": verb_to_link_marker_to.text,
                        "rom relation": "Predicate (conjunction - clause_verb)", # As per ADV report needs "verb/proposition - object"
                        "stanza ud": f"mark→verb_of_advcl ({marker_word.deprel})"
                    })

                    # Relation: marker -> main_clause_verb
                    self._add_relation_if_new(new_relations, {
                        "from": marker_word.text, "to": main_clause_verb_word.text,
                        "rom relation": "Constraint", "stanza ud": f"mark→main_verb ({marker_word.deprel})"
                    })
        return new_relations


    def _handle_infinitives(self, sent, existing_relations):
        """Handle infinitive constructions with 'to' mark."""
        new_relations = []
        for word in sent.words: # word is 'to'
            if word.text.lower() == 'to' and word.deprel == 'mark':
                # Head of 'to' (mark) is the infinitive verb itself
                infinitive_verb = sent.words[word.head - 1]
                if infinitive_verb.upos == 'VERB':
                    # Relation: to → infinitive_verb
                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": infinitive_verb.text,
                        "rom relation": "Predicate (preposition - object)", # 'to' acts as preposition to verb
                        "stanza ud": "mark(to)→inf_verb"
                    })

                    # Find the main verb that governs this xcomp/acl (headed by infinitive_verb)
                    # The infinitive_verb (head of 'to') is usually an xcomp or acl of a main verb.
                    if infinitive_verb.head != 0:
                        main_verb_governing_inf = sent.words[infinitive_verb.head - 1]
                        # Check if infinitive_verb is indeed a clausal complement of main_verb_governing_inf
                        if infinitive_verb.deprel in {'xcomp', 'acl', 'advcl'}: # advcl for "to preserve" in Basic S1
                             self._add_relation_if_new(new_relations, {
                                "from": word.text, "to": main_verb_governing_inf.text,
                                "rom relation": "Constraint",
                                "stanza ud": f"mark(to)→main_verb_of({infinitive_verb.deprel})"
                            })
        return new_relations


    def _handle_negation(self, sent, existing_relations):
        """Enhanced negation handling for contracted forms if not split by Stanza."""
        new_relations = []
        # Standard 'neg' deprel is handled by get_rom_mapping.
        # This is for contractions Stanza might not split, or specific patterns.
        # ADJ Sent 10: "I don’t know..." expected "don’t → know: constraint".
        # If Stanza gives "don’t" as a single token with deprel 'aux' or 'advmod' and it's negative.
        for word in sent.words:
            # Check for common negative contractions that might not be 'neg' deprel
            if word.text.lower() in {"don’t", "doesn’t", "didn’t", "won’t", "can’t", "shouldn’t", "isn’t", "aren’t"}:
                # Assume it modifies its head if it's an aux or part of verb phrase
                if word.head != 0:
                    head_word = sent.words[word.head -1]
                    # If the head is a verb, or if this word is an aux to a verb
                    if head_word.upos == 'VERB' or \
                       (word.upos == 'AUX' and head_word.upos == 'VERB') or \
                       (word.deprel == 'advmod' and head_word.upos == 'VERB'): # 'not' can be advmod

                        # Check if a more specific 'neg' relation already exists from a part of it
                        has_explicit_neg_part = False
                        if word.text.lower() == "don’t": # Stanza usually splits this to "do" and "n't"
                            for w_part in sent.words:
                                if w_part.text.lower() == "n’t" and w_part.head == word.head and w_part.deprel == 'neg':
                                    has_explicit_neg_part = True
                                    break

                        if not has_explicit_neg_part:
                            self._add_relation_if_new(new_relations, {
                                "from": word.text, "to": head_word.text,
                                "rom relation": "Constraint", "stanza ud": f"neg_contraction→{head_word.deprel}"
                            })
        return new_relations


    def _handle_copula_constructions(self, sent, existing_relations):
        """Handle copula constructions with proper directions and ROM types."""
        new_relations = []
        for subject_word in sent.words:
            if subject_word.deprel.startswith('nsubj'): # nsubj, nsubj:pass
                # head_of_subject is the predicative complement (e.g., 'happy' in 'He is happy')
                # OR it's the main verb if the nsubj is for a non-copular verb.
                # We are only interested if head_of_subject has a copula.
                predicative_complement_candidate = sent.words[subject_word.head - 1]

                copula_word = None
                for child_of_pred_cand in sent.words:
                    if child_of_pred_cand.head == predicative_complement_candidate.id and \
                       child_of_pred_cand.deprel == 'cop':
                        copula_word = child_of_pred_cand
                        break

                if copula_word: # This is a copula construction
                    # Subject → Copula
                    self._add_relation_if_new(new_relations, {
                        "from": subject_word.text, "to": copula_word.text,
                        "rom relation": "Predicate (subject - verb)", "stanza ud": f"{subject_word.deprel}→cop"
                    })
                    # Copula → Predicative Complement
                    # Changed from "Predicate (verb - object)"
                    self._add_relation_if_new(new_relations, {
                        "from": copula_word.text, "to": predicative_complement_candidate.text,
                        "rom relation": "Predicate (verb/proposition - object)", "stanza ud": "cop→pred_complement"
                    })
        return new_relations


    def _is_in_relative_clause(self, word, rel_verb, all_words):
        """Check if a word is part of a relative clause headed by rel_verb"""
        # This helper might not be needed if acl:relcl handling is robust
        current = word
        visited = set()
        while current.head != 0 and current.id not in visited:
            visited.add(current.id)
            if current.head == rel_verb.id and rel_verb.deprel == 'acl:relcl': # Ensure rel_verb is indeed acl:relcl
                # Further check: is 'word' governed by 'rel_verb' or one of its dependents?
                # This simple check assumes 'word' is a descendant of 'rel_verb's head (the antecedent)
                # and 'word' itself is headed by 'rel_verb' or a word within the clause.
                return True # Simplified
            # Check if current word itself is the rel_verb
            if current.id == rel_verb.id and rel_verb.deprel == 'acl:relcl':
                return True

            # If word's head is the rel_verb, it's in the clause
            if word.head == rel_verb.id:
                 return True

            current = all_words[current.head - 1] if current.head -1 < len(all_words) else None
            if not current: break
        return False


    @staticmethod
    def print_relations(relations: list) -> None:
        """Print ROM relations in a formatted way"""
        for relation in relations:
            from_word = relation["from"]
            to_word = relation["to"]
            rom_relation = relation["rom relation"]
            stanza_ud = relation["stanza ud"]

            print(f"  {from_word} → {to_word}: {rom_relation} (UD: {stanza_ud})")

