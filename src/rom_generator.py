"""
Complete ROM to UD Relations Mapper

Maps Universal Dependencies from Stanza to 4 ROM relation types and outputs
in a clean format showing word relationships with corrected semantic directions.
Includes original UD relation information for debugging and verification.
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
        Map UD relation to ROM type and determine semantic direction
        Enhanced to handle complex constructions and coordination

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
        elif ud_relation in {'nsubj:relcl', 'obj:relcl'} or (ud_relation == 'nmod' and word_pos == 'PRON'):
            return 'Connection', False

        # R3: Predicate (Subject → Verb) - always subject to verb direction
        elif ud_relation in {'nsubj', 'nsubj:pass', 'nsubj:outer', 'csubj', 'csubj:pass', 'csubj:outer'}:
            return 'Predicate (subject - verb)', False

        # R4: Predicate (Verb/Prep → Object) - semantic head governs dependent
        elif ud_relation in {'obj', 'iobj', 'ccomp', 'xcomp'}:
            return 'Predicate (verb/proposition - object)', True  # Reverse: head → dependent

        elif ud_relation in {'obl', 'obl:agent', 'obl:arg', 'obl:tmod', 'obl:lmod'}:
            # Oblique: verb governs location/manner/time
            return 'Predicate (verb/proposition - object)', True  # Reverse: head → dependent

        elif ud_relation in {'case'}:
            # Preposition governs its object: "on → table: R4"
            return 'Predicate (verb/proposition - object)', False

        # COPULA CONSTRUCTION: Predicate complements after copula
        elif ud_relation == 'amod' and head_lemma in {'be', 'is', 'are', 'was', 'were', 'am', 'being', 'been'}:
            return 'Predicate (verb/proposition - object)', True  # Reverse: copula → predicate adjective

        elif ud_relation == 'nmod' and head_lemma in {'be', 'is', 'are', 'was', 'were', 'am', 'being', 'been'}:
            return 'Predicate (verb/proposition - object)', True  # Reverse: copula → predicate nominative

        # ENHANCED: Auxiliaries with proper direction
        elif ud_relation in {'aux', 'aux:pass'}:
            # Auxiliary → main verb: is → going: R2
            return 'Constraint', True  # Reverse: aux → main verb

        elif ud_relation == 'cop':
            # Copula: Is → famous: Predicate
            return 'Predicate (verb/proposition - object)', False

        # ENHANCED: Mark relations with better context awareness
        elif ud_relation == 'mark':
            temporal_causal_markers = {'when', 'where', 'why'}
            complementizers = {'that', 'whether', 'if', 'how', 'what'}
            subordinating_conj = {'because', 'although', 'since', 'while', 'unless', 'until'}

            if word_text and word_text.lower() in temporal_causal_markers:
                # Temporal/causal markers in relative clauses: when → moved: R4
                return 'Predicate (verb/proposition - object)', False
            elif word_text and word_text.lower() in complementizers:
                # Complementizers: that → knew: R4
                return 'Predicate (verb/proposition - object)', False
            elif word_text and word_text.lower() in subordinating_conj:
                # Subordinating conjunctions: because → stayed: R2
                return 'Constraint', False
            else:
                # Default subordinating conjunction behavior
                return 'Constraint', False

        # Relative clause handling
        elif ud_relation == 'acl:relcl':
            return 'Predicate (subject - verb)', True  # Reverse: antecedent → verb

        elif ud_relation == 'acl':
            return 'Constraint', False

        # R2: Constraint (Modifier/Qualifier) - enhanced coverage
        elif ud_relation in {'det', 'amod', 'advmod', 'advmod:emph', 'advmod:lmod',
                             'nmod', 'nmod:poss', 'nmod:tmod', 'nummod', 'nummod:gov',
                             'fixed', 'flat', 'flat:foreign', 'flat:name',
                             'det:numgov', 'det:nummod', 'det:poss', 'clf', 'cc:preconj'}:
            return 'Constraint', False

        elif ud_relation in {'compound', 'compound:lvc', 'compound:prt', 'compound:redup',
                             'compound:svc'}:
            return 'Constraint', True

        elif ud_relation in {'advcl', 'advcl:relcl'}:
            return 'Constraint', False

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

                # Skip nsubj when head has copula (handle separately)
                if word.deprel == 'nsubj':
                    has_copula = any(child.head == head_word.id and child.deprel == 'cop'
                                     for child in sent.words)
                    if has_copula:
                        continue

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

                relations.append(relation_dict)

            # ENHANCED: Coordinating conjunction handling
            relations.extend(self._handle_coordination(sent))

            # ENHANCED: Correlative conjunctions
            relations.extend(self._handle_correlative_conjunctions(sent))

            # ENHANCED: Comparative constructions
            relations.extend(self._handle_comparatives(sent))

            # ENHANCED: Object relative clauses
            relations.extend(self._handle_object_relatives(sent))

            # ENHANCED: Possessive relatives with antecedents
            relations.extend(self._handle_possessive_relatives(sent))

            # ENHANCED: Temporal/causal relatives
            relations.extend(self._handle_temporal_relatives(sent))

            # ENHANCED: Subordinating conjunctions
            relations.extend(self._handle_subordinating_conjunctions(sent))

            # ENHANCED: Infinitive constructions
            relations.extend(self._handle_infinitives(sent))

            # ENHANCED: Negation handling
            relations.extend(self._handle_negation(sent))

            # Copula constructions (existing)
            relations.extend(self._handle_copula_constructions(sent))

        return relations

    def _handle_coordination(self, sent):
        """Handle coordinating conjunctions (and, but, or)"""
        relations = []
        for word in sent.words:
            if word.deprel == 'cc':  # coordinating conjunction
                # Find the conjuncts this connects
                head_word = sent.words[word.head - 1]
                # Find the second conjunct
                for other_word in sent.words:
                    if other_word.head == head_word.id and other_word.deprel == 'conj':
                        # Add conjunction → both conjuncts relationships
                        relations.append({
                            "from": word.text,
                            "to": head_word.text,
                            "rom relation": "Connection",
                            "stanza ud": "cc→conj"
                        })
                        relations.append({
                            "from": word.text,
                            "to": other_word.text,
                            "rom relation": "Connection",
                            "stanza ud": "cc→conj"
                        })
                        break
        return relations

    def _handle_correlative_conjunctions(self, sent):
        """Handle correlative conjunctions like both...and, not only...but also"""
        relations = []
        words_text = [w.text.lower() for w in sent.words]

        # Handle "both...and"
        if 'both' in words_text and 'and' in words_text:
            both_idx = next(i for i, w in enumerate(sent.words) if w.text.lower() == 'both')
            and_idx = next(i for i, w in enumerate(sent.words) if w.text.lower() == 'and')

            relations.append({
                "from": sent.words[both_idx].text,
                "to": sent.words[and_idx].text,
                "rom relation": "Connection",
                "stanza ud": "both→and"
            })

        # Handle "not only...but also"
        if any('only' in w.text.lower() for w in sent.words) and any('also' in w.text.lower() for w in sent.words):
            try:
                only_idx = next(i for i, w in enumerate(sent.words) if 'only' in w.text.lower())
                also_idx = next(i for i, w in enumerate(sent.words) if 'also' in w.text.lower())

                relations.append({
                    "from": f"not only",
                    "to": f"but also",
                    "rom relation": "Connection",
                    "stanza ud": "correlative"
                })
            except StopIteration:
                pass

        return relations

    def _handle_comparatives(self, sent):
        """Handle comparative constructions like as...as"""
        relations = []
        as_words = [i for i, w in enumerate(sent.words) if w.text.lower() == 'as']

        if len(as_words) >= 2:
            # Find the two "as" words
            first_as = sent.words[as_words[0]]
            second_as = sent.words[as_words[1]]

            # Connect the two "as" words
            relations.append({
                "from": first_as.text,
                "to": second_as.text,
                "rom relation": "Connection",
                "stanza ud": "as→as"
            })

        return relations

    def _handle_object_relatives(self, sent):
        """Enhanced object relative clause handling"""
        relations = []
        for word in sent.words:
            if word.deprel == 'acl:relcl':
                antecedent = sent.words[word.head - 1]

                # Find object relative pronouns
                for child in sent.words:
                    if child.head == word.id and child.deprel == 'obj':
                        if child.lemma.lower() in {'whom', 'that', 'which'}:
                            # verb → relative pronoun: R4
                            relations.append({
                                "from": word.text,
                                "to": child.text,
                                "rom relation": "Predicate (verb/proposition - object)",
                                "stanza ud": "obj→relcl"
                            })
                            # relative pronoun → antecedent: R1
                            relations.append({
                                "from": child.text,
                                "to": antecedent.text,
                                "rom relation": "Connection",
                                "stanza ud": "rel→antecedent"
                            })

                    # Handle subject relatives too
                    elif child.head == word.id and child.deprel == 'nsubj':
                        if child.lemma.lower() in {'who', 'which', 'that'}:
                            relations.append({
                                "from": child.text,
                                "to": antecedent.text,
                                "rom relation": "Connection",
                                "stanza ud": "rel→antecedent"
                            })

        return relations

    def _handle_possessive_relatives(self, sent):
        """Enhanced possessive relative handling with antecedent connections"""
        relations = []
        for word in sent.words:
            if word.lemma.lower() == 'whose':
                # Find the relative clause this "whose" belongs to
                for rel_verb in sent.words:
                    if rel_verb.deprel == 'acl:relcl':
                        # Check if "whose" is in this relative clause
                        if self._is_in_relative_clause(word, rel_verb, sent.words):
                            antecedent = sent.words[rel_verb.head - 1]
                            relations.append({
                                "from": word.text,
                                "to": antecedent.text,
                                "rom relation": "Connection",
                                "stanza ud": "whose→antecedent"
                            })
                            break
        return relations

    def _handle_temporal_relatives(self, sent):
        """Handle temporal/causal relatives like when/why with nouns"""
        relations = []
        for word in sent.words:
            if word.lemma.lower() in {'when', 'why'} and word.deprel == 'mark':
                marked_clause = None
                for clause in sent.words:
                    if clause.id == word.head:
                        marked_clause = clause
                        break

                if marked_clause and marked_clause.deprel == 'acl:relcl':
                    antecedent = sent.words[marked_clause.head - 1]
                    relations.append({
                        "from": word.text,
                        "to": antecedent.text,
                        "rom relation": "Constraint",
                        "stanza ud": "temporal→noun"
                    })
        return relations

    def _handle_subordinating_conjunctions(self, sent):
        """Enhanced subordinating conjunction handling"""
        relations = []
        for word in sent.words:
            if word.deprel == 'advcl':
                # Find subordinating conjunction
                marker = None
                for child in sent.words:
                    if child.head == word.id and child.deprel == 'mark':
                        marker = child
                        break

                if marker:
                    main_verb = sent.words[word.head - 1]

                    # Different mapping based on conjunction type
                    if marker.text.lower() in {'because', 'although', 'since', 'while'}:
                        # Subordinating conjunction → dependent clause: R4
                        relations.append({
                            "from": marker.text,
                            "to": word.text,
                            "rom relation": "Predicate (verb/proposition - object)",
                            "stanza ud": "mark→advcl"
                        })
                        # Subordinating conjunction → main clause: R2
                        relations.append({
                            "from": marker.text,
                            "to": main_verb.text,
                            "rom relation": "Constraint",
                            "stanza ud": "mark→main"
                        })
        return relations

    def _handle_infinitives(self, sent):
        """Handle infinitive constructions"""
        relations = []
        for word in sent.words:
            if word.text.lower() == 'to' and word.deprel == 'mark':
                # Find the infinitive verb
                inf_verb = None
                for verb in sent.words:
                    if verb.head == word.head and verb.upos == 'VERB':
                        inf_verb = verb
                        break

                if inf_verb:
                    # to → verb: R4
                    relations.append({
                        "from": word.text,
                        "to": inf_verb.text,
                        "rom relation": "Predicate (verb/proposition - object)",
                        "stanza ud": "to→infinitive"
                    })

                    # Find the main verb that takes this infinitive
                    main_verb = sent.words[word.head - 1] if word.head > 0 else None
                    if main_verb:
                        # to → main verb: R2
                        relations.append({
                            "from": word.text,
                            "to": main_verb.text,
                            "rom relation": "Constraint",
                            "stanza ud": "to→main"
                        })
        return relations

    def _handle_negation(self, sent):
        """Enhanced negation handling for contracted forms"""
        relations = []
        for word in sent.words:
            # Handle contracted negation
            if word.text.lower() in {"don't", "doesn't", "didn't", "won't", "can't", "shouldn't"}:
                # Find the verb this negation modifies
                for verb in sent.words:
                    if verb.head == word.id or word.head == verb.id:
                        if verb.upos == 'VERB':
                            relations.append({
                                "from": word.text,
                                "to": verb.text,
                                "rom relation": "Constraint",
                                "stanza ud": "neg→verb"
                            })
                            break
        return relations

    def _handle_copula_constructions(self, sent):
        """Handle copula constructions: redirect subject to copula"""
        relations = []
        for word in sent.words:
            if word.deprel == 'nsubj':
                head_word = sent.words[word.head - 1]
                copula = None
                for child in sent.words:
                    if child.head == head_word.id and child.deprel == 'cop':
                        copula = child
                        break

                if copula:
                    relations.append({
                        "from": word.text,
                        "to": copula.text,
                        "rom relation": "Predicate (subject - verb)",
                        "stanza ud": "nsubj→cop"
                    })
        return relations

    def _is_in_relative_clause(self, word, rel_verb, all_words):
        """Check if a word is part of a relative clause headed by rel_verb"""
        current = word
        visited = set()
        while current.head != 0 and current.id not in visited:
            visited.add(current.id)
            if current.head == rel_verb.id:
                return True
            current = all_words[current.head - 1]
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
