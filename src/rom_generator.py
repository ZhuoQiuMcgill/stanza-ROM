"""
Complete ROM to UD Relations Mapper - ENHANCED WITH POS-BASED ANALYSIS

Maps Universal Dependencies from Stanza to 4 ROM relation types and outputs
in a clean format showing word relationships with corrected semantic directions.
Incorporates comprehensive POS analysis based on bidirectional coverage analysis
for more accurate ROM relation generation.

MAJOR ENHANCEMENTS based on POS Pair Analysis:
- Enhanced bidirectional POS-based mapping logic
- Implemented specific ROM rules for high-coverage POS pairs
- Better handling based on empirical analysis results
- Improved accuracy for DET-NOUN, ADP-PRON, PRON-VERB, and other pairs
- Enhanced clause linking and connective analysis
"""

import stanza


class ROMGenerator:
    """
    A class for mapping Universal Dependencies relations to ROM (Relational Ontology Model) types.

    This class handles the initialization of the Stanza pipeline and provides methods
    to analyze sentences and extract ROM relations from UD parsing with enhanced POS analysis
    based on bidirectional coverage analysis.
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
                        head_pos: str = None, head_lemma: str = None, head_text: str = None) -> tuple:
        """
        Map UD relation to ROM type with enhanced POS-based logic based on bidirectional analysis

        Args:
            ud_relation: Universal Dependencies relation type
            word_text: Text of the dependent word
            word_pos: POS tag of the dependent word
            head_pos: POS tag of the head word
            head_lemma: Lemma of the head word
            head_text: Text of the head word

        Returns:
            tuple: (rom_description, reverse_direction)
        """
        word_lower = word_text.lower() if word_text else ""
        head_lower = head_text.lower() if head_text else ""

        # =============================================================================
        # ENHANCED POS-BASED MAPPINGS (Based on Bidirectional Analysis)
        # =============================================================================

        # DET ↔ NOUN (Perfect 1.000 coverage) - DET→NOUN: Constraint, NOUN→DET: det
        if ud_relation == 'det' and word_pos == 'DET' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # det → noun

        # ADP ↔ PROPN (Perfect 1.000 coverage) - ADP→PROPN: Predicate, PROPN→ADP: case
        elif ud_relation == 'case' and word_pos == 'ADP' and head_pos == 'PROPN':
            return 'Predicate (Preposition - Object)', False  # prep → propn

        # ADP ↔ PRON (Perfect 1.000 coverage) - ADP→PRON: Predicate, PRON→ADP: case
        elif ud_relation == 'case' and word_pos == 'ADP' and head_pos == 'PRON':
            return 'Predicate (Preposition - Object)', False  # prep → pron

        # ADP ↔ NOUN (High 0.917 coverage) - ADP→NOUN: Predicate, NOUN→ADP: case
        elif ud_relation == 'case' and word_pos == 'ADP' and head_pos in {'NOUN', 'PROPN'}:
            return 'Predicate (Preposition - Object)', False  # prep → noun

        # ADV ↔ NOUN (Perfect 1.000 coverage) - ADV→NOUN: Constraint, NOUN→ADV: advmod
        elif ud_relation == 'advmod' and word_pos == 'ADV' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # adv → noun

        # ADJ ↔ CCONJ (Perfect 1.000 coverage) - ADJ→CCONJ: cc, CCONJ→ADJ: Connection/Predicate
        elif ud_relation == 'cc' and word_pos == 'CCONJ' and head_pos == 'ADJ':
            if word_lower in {'and', 'or'}:
                return 'Connection', False  # conj → adj
            else:
                return 'Predicate (Conjunction - Element)', False  # conj → adj

        # NOUN ↔ PROPN (Perfect 1.000 coverage) - NOUN→PROPN: compound, PROPN→NOUN: Constraint
        elif ud_relation == 'compound' and word_pos == 'PROPN' and head_pos == 'NOUN':
            return 'Constraint', True  # head → modifier (PROPN → NOUN)

        # =============================================================================
        # PRON ↔ VERB (High 0.988 coverage) - Complex bidirectional mapping
        # =============================================================================

        # PRON → VERB: nsubj/obj patterns
        elif ud_relation in {'nsubj', 'nsubj:pass', 'nsubj:outer'} and word_pos == 'PRON' and head_pos in {'VERB',
                                                                                                           'AUX'}:
            return 'Predicate (Subject - Verb)', False  # pron → verb

        elif ud_relation in {'obj', 'iobj'} and word_pos == 'PRON' and head_pos == 'VERB':
            return 'Predicate (Verb/Proposition - Object)', True  # verb → pron

        elif ud_relation == 'obl' and word_pos == 'PRON' and head_pos == 'VERB':
            return 'Predicate (Verb/Preposition - Object)', True  # verb → pron

        # =============================================================================
        # ADJ ↔ AUX (High 0.938 coverage) - ADJ→AUX: cop, AUX→ADJ: Predicate
        # =============================================================================

        elif ud_relation == 'cop' and word_pos == 'AUX' and head_pos == 'ADJ':
            return 'Predicate (Verb/Proposition - Object)', False  # aux → adj

        # =============================================================================
        # ADV ↔ VERB (High 0.912 coverage) - Complex patterns
        # =============================================================================

        elif ud_relation == 'advmod' and word_pos == 'ADV' and head_pos == 'VERB':
            # Special cases based on adverb type
            if word_lower in {'when', 'where', 'how', 'why'}:
                return 'Predicate (Verb/Proposition - Object)', False  # wh-adv → verb
            else:
                return 'Constraint', False  # adv → verb

        elif ud_relation == 'mark' and word_pos == 'ADV' and head_pos == 'VERB':
            return 'Predicate (Verb/Proposition - Object)', False  # wh-adv → verb

        # =============================================================================
        # SCONJ ↔ VERB (High 0.905 coverage) - SCONJ→VERB: Constraint/Predicate, VERB→SCONJ: mark
        # =============================================================================

        elif ud_relation == 'mark' and word_pos == 'SCONJ' and head_pos == 'VERB':
            if word_lower in {'because', 'although', 'since', 'while', 'unless', 'until', 'before', 'after'}:
                return 'Constraint', False  # subordinating conj → verb (constrains main verb)
            elif word_lower in {'that', 'whether', 'if'}:
                return 'Connection', False  # complementizer
            else:
                return 'Predicate (Conjunction - Clause_Verb)', False  # other subordinating conjunctions

        # =============================================================================
        # CCONJ patterns (High coverage for NOUN and VERB)
        # =============================================================================

        elif ud_relation == 'cc' and word_pos == 'CCONJ':
            if word_lower in {'and', 'or'}:
                return 'Connection', False  # standard coordination
            elif word_lower in {'but', 'however', 'yet'}:
                return 'Constraint', False  # contrastive
            else:
                return 'Connection', False  # default coordination

        # =============================================================================
        # NOUN ↔ VERB (High 0.812 coverage) - Complex bidirectional patterns
        # =============================================================================

        elif ud_relation in {'nsubj', 'nsubj:pass', 'nsubj:outer'} and word_pos == 'NOUN' and head_pos in {'VERB',
                                                                                                           'AUX'}:
            return 'Predicate (Subject - Verb)', False  # noun → verb

        elif ud_relation in {'obj', 'iobj'} and word_pos == 'NOUN' and head_pos == 'VERB':
            return 'Predicate (Verb/Proposition - Object)', True  # verb → noun

        elif ud_relation in {'obl', 'obl:agent', 'obl:unmarked'} and word_pos == 'NOUN' and head_pos == 'VERB':
            return 'Predicate (Verb/Preposition - Object)', True  # verb → noun

        elif ud_relation == 'acl:relcl' and word_pos == 'VERB' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # relative clause verb → antecedent

        elif ud_relation == 'acl' and word_pos == 'VERB' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # adjectival clause

        # =============================================================================
        # PART ↔ VERB (Good 0.773 coverage) - PART→VERB: Constraint/Predicate, VERB→PART: mark/advmod
        # =============================================================================

        elif ud_relation == 'mark' and word_pos == 'PART' and head_pos == 'VERB':
            if word_lower == 'to':
                return 'Predicate (Preposition - Object)', False  # to → infinitive verb
            else:
                return 'Constraint', False  # other particles

        elif ud_relation == 'advmod' and word_pos == 'PART' and head_pos == 'VERB':
            if word_lower in {"n't", 'not'}:
                return 'Constraint', False  # negation particle
            else:
                return 'Constraint', False  # other particles

        # =============================================================================
        # AUX ↔ VERB (Good 0.677 coverage) - AUX→VERB: Constraint, VERB→AUX: aux/cop
        # =============================================================================

        elif ud_relation in {'aux', 'aux:pass'} and word_pos == 'AUX' and head_pos == 'VERB':
            return 'Constraint', False  # aux → main verb

        elif ud_relation == 'cop' and word_pos == 'AUX' and head_pos in {'NOUN', 'ADJ', 'NUM'}:
            return 'Predicate (Verb/Proposition - Object)', False  # copula → predicate

        # =============================================================================
        # ADJ patterns
        # =============================================================================

        elif ud_relation == 'amod' and word_pos == 'ADJ' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # adj → noun

        elif ud_relation == 'advmod' and word_pos == 'ADV' and head_pos == 'ADJ':
            return 'Constraint', False  # adv → adj

        # =============================================================================
        # Compound and fixed expressions
        # =============================================================================

        elif ud_relation in {'compound', 'compound:prt'} and word_pos in {'NOUN', 'PROPN'} and head_pos in {'NOUN',
                                                                                                            'PROPN'}:
            return 'Constraint', True  # head → modifier

        elif ud_relation == 'compound:prt' and word_pos in {'ADP', 'ADV'} and head_pos == 'VERB':
            return 'Constraint', True  # verb → particle

        elif ud_relation == 'fixed' and word_pos == 'ADP' and head_pos == 'ADV':
            return 'Connection', False  # fixed expression (like "rather than")

        # =============================================================================
        # Possession and modification patterns
        # =============================================================================

        elif ud_relation == 'nmod:poss' and word_pos == 'PRON' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # possessive pronoun → noun

        elif ud_relation == 'nmod' and word_pos in {'NOUN', 'PROPN'} and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # noun modifier

        elif ud_relation == 'nummod' and word_pos == 'NUM' and head_pos in {'NOUN', 'PROPN'}:
            return 'Constraint', False  # number → noun

        # =============================================================================
        # Coordination and conjunction patterns
        # =============================================================================

        elif ud_relation == 'conj':
            return 'Connection', False  # coordinated elements

        elif ud_relation == 'cc:preconj' and word_pos == 'CCONJ':
            return 'Connection', False  # pre-correlative conjunction

        # =============================================================================
        # Clausal patterns
        # =============================================================================

        elif ud_relation == 'ccomp' and head_pos == 'VERB':
            return 'Predicate (Verb/Proposition - Object)', True  # verb → complement clause

        elif ud_relation == 'xcomp' and head_pos == 'VERB':
            return 'Predicate (Verb/Proposition - Object)', True  # verb → controlled complement

        elif ud_relation == 'advcl' and head_pos == 'VERB':
            return 'Constraint', False  # adverbial clause

        elif ud_relation == 'csubj' and word_pos == 'VERB' and head_pos in {'VERB', 'ADJ'}:
            return 'Predicate (Subject - Verb)', False  # clausal subject

        # =============================================================================
        # Negation patterns
        # =============================================================================

        elif ud_relation == 'neg':
            return 'Constraint', False  # negation

        # =============================================================================
        # Discourse and other patterns
        # =============================================================================

        elif ud_relation in {'discourse', 'vocative', 'dislocated'}:
            return 'Connection', False  # discourse elements

        elif ud_relation in {'parataxis', 'list', 'appos'}:
            return 'Connection', False  # paratactic elements

        # =============================================================================
        # Default fallback patterns
        # =============================================================================

        # Default for unknown relations
        return None, False

    def analyze_sentence(self, sentence: str) -> list:
        """
        Analyze a sentence and extract ROM relations from UD parsing.
        Enhanced with comprehensive POS-based analysis based on bidirectional coverage analysis.

        Args:
            sentence: Input sentence to analyze

        Returns:
            List of dictionaries with ROM relations
        """
        doc = self.nlp(sentence)
        relations = []

        for sent in doc.sentences:
            # Standard dependency relations with enhanced POS analysis
            for word in sent.words:
                if word.head == 0:  # Skip root
                    continue

                head_word = sent.words[word.head - 1]

                # Skip nsubj when head has copula (handled by _handle_copula_constructions)
                if word.deprel == 'nsubj':
                    is_copula_construction = False
                    for potential_copula in sent.words:
                        if potential_copula.head == head_word.id and potential_copula.deprel == 'cop':
                            is_copula_construction = True
                            break
                    if is_copula_construction:
                        continue

                # Skip 'cop' relations here, handled by _handle_copula_constructions
                if word.deprel == 'cop':
                    continue

                # Skip 'mark' relations if they are part of an advcl that will be handled
                if word.deprel == 'mark':
                    is_advcl_mark = False
                    for w_advcl in sent.words:
                        if w_advcl.id == word.head and w_advcl.deprel == 'advcl':
                            is_advcl_mark = True
                            break
                    if is_advcl_mark:
                        if not (word.text.lower() == 'to' and head_word.upos == 'VERB'):
                            continue

                # Skip acl:relcl relations - let handlers deal with them
                if word.deprel == 'acl:relcl':
                    continue

                # Enhanced mapping with POS information
                rom_result = self.get_rom_mapping(
                    word.deprel, word.text, word.upos, head_word.upos, head_word.lemma, head_word.text
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

                # Avoid duplicate relations
                simple_rel = (relation_dict["from"], relation_dict["to"], relation_dict["rom relation"])
                already_exists = any(
                    (r["from"] == simple_rel[0] and r["to"] == simple_rel[1] and r["rom relation"] == simple_rel[2])
                    for r in relations
                )
                if not already_exists:
                    relations.append(relation_dict)

            # Special constructions handling with enhanced POS analysis
            relations.extend(self._handle_copula_constructions(sent, relations))
            relations.extend(self._handle_coordination(sent, relations))
            relations.extend(self._handle_correlative_conjunctions(sent, relations))
            relations.extend(self._handle_comparatives(sent, relations))
            relations.extend(self._handle_object_relatives(sent, relations))
            relations.extend(self._handle_possessive_relatives(sent, relations))
            relations.extend(self._handle_temporal_causal_noun_relatives(sent, relations))
            relations.extend(self._handle_subordinating_conjunctions(sent, relations))
            relations.extend(self._handle_infinitives(sent, relations))
            relations.extend(self._handle_negation(sent, relations))

            # Deduplicate relations
            final_relations = []
            seen_relations_tuples = set()
            for r in relations:
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
        """Enhanced coordinating conjunction handling with POS validation"""
        new_relations = []
        for word in sent.words:
            if word.deprel == 'cc' and word.upos == 'CCONJ':  # Coordinating conjunction
                coordinator = word.text.lower()
                head_of_cc = sent.words[word.head - 1]

                # Find conjuncts
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
                            "rom relation": "Predicate (Conjunction - Clause_Element)",
                            "stanza ud": f"cc({coordinator})→conj2"
                        })
                    elif coordinator in {'and', 'or'}:
                        # Standard coordination - per ROM rules: Connection
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
        """Handle correlative conjunctions with enhanced POS analysis"""
        new_relations = []

        # Look for correlative patterns
        words_text = [w.text.lower() for w in sent.words]

        # both...and
        if 'both' in words_text and 'and' in words_text:
            both_word = next(w for w in sent.words if w.text.lower() == 'both')
            and_word = next(w for w in sent.words if w.text.lower() == 'and' and w.upos == 'CCONJ')
            self._add_relation_if_new(new_relations, {
                "from": both_word.text, "to": and_word.text,
                "rom relation": "Connection", "stanza ud": "correlative_both_and"
            })

        # either...or
        if 'either' in words_text and 'or' in words_text:
            either_word = next(w for w in sent.words if w.text.lower() == 'either')
            or_word = next(w for w in sent.words if w.text.lower() == 'or' and w.upos == 'CCONJ')
            self._add_relation_if_new(new_relations, {
                "from": either_word.text, "to": or_word.text,
                "rom relation": "Connection", "stanza ud": "correlative_either_or"
            })

        return new_relations

    def _handle_comparatives(self, sent, existing_relations):
        """Handle comparative constructions with enhanced POS analysis"""
        new_relations = []
        as_words = [w for w in sent.words if w.text.lower() == 'as']

        if len(as_words) >= 2:
            first_as = as_words[0]
            second_as = as_words[1]

            # Connection between the two "as" words
            self._add_relation_if_new(new_relations, {
                "from": first_as.text, "to": second_as.text,
                "rom relation": "Connection", "stanza ud": "as...as_correlative"
            })

            # Find what each "as" modifies based on POS and dependencies
            if first_as.head != 0:
                first_head = sent.words[first_as.head - 1]
                if first_head.upos in {'ADJ', 'ADV'}:  # as → adjective/adverb
                    self._add_relation_if_new(new_relations, {
                        "from": first_as.text, "to": first_head.text,
                        "rom relation": "Predicate (Verb/Proposition - Object)", "stanza ud": "as→adj/adv"
                    })
                elif first_head.upos == 'VERB':  # as → verb
                    self._add_relation_if_new(new_relations, {
                        "from": first_as.text, "to": first_head.text,
                        "rom relation": "Constraint", "stanza ud": "as→verb"
                    })

            if second_as.head != 0:
                second_head = sent.words[second_as.head - 1]
                if second_head.upos in {'NOUN', 'PRON', 'PROPN'}:  # as → noun/pronoun
                    self._add_relation_if_new(new_relations, {
                        "from": second_as.text, "to": second_head.text,
                        "rom relation": "Predicate (Preposition - Object)", "stanza ud": "as→noun"
                    })

        return new_relations

    def _handle_object_relatives(self, sent, existing_relations):
        """Enhanced object relative clause handling with POS validation"""
        new_relations = []
        for word in sent.words:
            if word.deprel == 'acl:relcl' and word.upos == 'VERB':
                antecedent = sent.words[word.head - 1]

                # Find relative pronoun with POS validation
                relative_pronoun_word = None
                rel_pronoun_role = None
                for child in sent.words:
                    if child.head == word.id and child.upos == 'PRON':
                        if child.deprel in {'obj', 'nsubj'} and \
                                child.lemma.lower() in {'who', 'whom', 'which', 'that'}:
                            relative_pronoun_word = child
                            rel_pronoun_role = child.deprel
                            break

                if relative_pronoun_word:
                    if rel_pronoun_role == 'obj':
                        # Object relative: verb → relative pronoun
                        self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": relative_pronoun_word.text,
                            "rom relation": "Predicate (Verb/Proposition - Object)",
                            "stanza ud": f"relcl_verb→obj_pronoun({word.deprel})"
                        })
                    elif rel_pronoun_role == 'nsubj':
                        # Subject relative: antecedent → verb
                        self._add_relation_if_new(new_relations, {
                            "from": antecedent.text, "to": word.text,
                            "rom relation": "Predicate (Subject - Verb)",
                            "stanza ud": f"antecedent→relcl_verb({word.deprel})"
                        })

                    # Relative pronoun → antecedent (connection)
                    self._add_relation_if_new(new_relations, {
                        "from": relative_pronoun_word.text, "to": antecedent.text,
                        "rom relation": "Connection",
                        "stanza ud": f"rel_pronoun→antecedent({word.deprel})"
                    })
                else:
                    # Handle implicit relatives based on structure and POS
                    has_explicit_object = any(child.deprel == 'obj' for child in sent.words if child.head == word.id)
                    has_explicit_subject = any(
                        child.deprel.startswith('nsubj') for child in sent.words if child.head == word.id)

                    if not has_explicit_object and has_explicit_subject:
                        # Object relative with implicit pronoun
                        self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": antecedent.text,
                            "rom relation": "Predicate (Verb/Proposition - Object)",
                            "stanza ud": f"relcl_verb→implicit_obj({word.deprel})"
                        })
                    elif not has_explicit_subject:
                        # Subject relative with implicit pronoun
                        self._add_relation_if_new(new_relations, {
                            "from": antecedent.text, "to": word.text,
                            "rom relation": "Predicate (Subject - Verb)",
                            "stanza ud": f"antecedent→relcl_verb({word.deprel})"
                        })

        return new_relations

    def _handle_possessive_relatives(self, sent, existing_relations):
        """Handle possessive relatives with enhanced POS analysis"""
        new_relations = []
        for word in sent.words:
            if word.lemma.lower() == 'whose' and word.upos == 'PRON':
                possessed_noun = None
                if word.head != 0:
                    potential_possessed_noun = sent.words[word.head - 1]
                    if word.deprel == 'nmod:poss' and potential_possessed_noun.upos in {'NOUN', 'PROPN'}:
                        possessed_noun = potential_possessed_noun

                if possessed_noun:
                    # Find the relative clause and antecedent
                    antecedent_of_relcl = self._find_relative_clause_antecedent(possessed_noun, sent.words)

                    if antecedent_of_relcl:
                        self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": antecedent_of_relcl.text,
                            "rom relation": "Connection", "stanza ud": "whose→antecedent"
                        })

                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": possessed_noun.text,
                        "rom relation": "Constraint", "stanza ud": "whose→possessed_noun"
                    })
        return new_relations

    def _find_relative_clause_antecedent(self, start_word, all_words):
        """Helper to find the antecedent of a relative clause"""
        curr = start_word
        visited_heads = set()
        while curr.head != 0 and curr.id not in visited_heads:
            visited_heads.add(curr.id)
            parent_of_curr = all_words[curr.head - 1]
            if parent_of_curr.deprel == 'acl:relcl':
                if parent_of_curr.head != 0:
                    return all_words[parent_of_curr.head - 1]
                break
            if curr.deprel == 'acl:relcl':
                if curr.head != 0:
                    return all_words[curr.head - 1]
                break
            curr = parent_of_curr
        return None

    def _handle_temporal_causal_noun_relatives(self, sent, existing_relations):
        """Handle temporal/causal relatives with enhanced POS analysis"""
        new_relations = []
        for word in sent.words:
            if word.lemma.lower() in {'when', 'where', 'why'} and word.deprel == 'mark' and word.upos in {'SCONJ',
                                                                                                          'ADV'}:
                verb_of_relcl = sent.words[word.head - 1]
                if verb_of_relcl.deprel == 'acl:relcl' and verb_of_relcl.upos == 'VERB':
                    antecedent_noun = sent.words[verb_of_relcl.head - 1]

                    # Per ROM rules: marker → verb (R4), marker → antecedent (R2)
                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": verb_of_relcl.text,
                        "rom relation": "Predicate (Verb/Proposition - Object)",
                        "stanza ud": f"{word.lemma}→verb_of_relcl"
                    })

                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": antecedent_noun.text,
                        "rom relation": "Constraint",
                        "stanza ud": f"{word.lemma}→antecedent_noun"
                    })

                    # verb → antecedent constraint
                    self._add_relation_if_new(new_relations, {
                        "from": verb_of_relcl.text, "to": antecedent_noun.text,
                        "rom relation": "Constraint",
                        "stanza ud": f"relcl_verb→antecedent"
                    })
        return new_relations

    def _handle_subordinating_conjunctions(self, sent, existing_relations):
        """Enhanced subordinating conjunction handling with POS analysis"""
        new_relations = []
        for advcl_verb_word in sent.words:
            if advcl_verb_word.deprel == 'advcl':
                marker_word = None
                for child in sent.words:
                    if child.head == advcl_verb_word.id and child.deprel == 'mark' and child.upos == 'SCONJ':
                        marker_word = child
                        break

                if marker_word:
                    main_clause_verb_word = sent.words[advcl_verb_word.head - 1]

                    # Find actual verb in subordinate clause
                    verb_to_link_marker_to = self._find_clause_main_verb(advcl_verb_word, sent.words)

                    # Per ROM rules: conjunction → subordinate verb (R4)
                    self._add_relation_if_new(new_relations, {
                        "from": marker_word.text,
                        "to": verb_to_link_marker_to.text,
                        "rom relation": "Predicate (Conjunction - Clause_Verb)",
                        "stanza ud": f"mark→verb_of_advcl ({marker_word.deprel})"
                    })

                    # Per ROM rules: conjunction constrains main verb (R2)
                    self._add_relation_if_new(new_relations, {
                        "from": marker_word.text, "to": main_clause_verb_word.text,
                        "rom relation": "Constraint", "stanza ud": f"mark→main_verb ({marker_word.deprel})"
                    })
        return new_relations

    def _find_clause_main_verb(self, clause_head, all_words):
        """Find the main verb of a clause considering POS tags"""
        if clause_head.upos == 'VERB':
            return clause_head
        elif clause_head.upos == 'AUX':
            # Look for the main verb this auxiliary modifies
            for word in all_words:
                if word.head == clause_head.id and word.upos == 'VERB':
                    return word
            # If aux is head of predicative complement
            if clause_head.head != 0:
                head_word = all_words[clause_head.head - 1]
                if head_word.upos in {'ADJ', 'NOUN'}:
                    return clause_head  # The aux is the main predicate
        return clause_head

    def _handle_infinitives(self, sent, existing_relations):
        """Handle infinitive constructions with enhanced POS analysis"""
        new_relations = []
        for word in sent.words:
            if word.text.lower() == 'to' and word.deprel == 'mark' and word.upos in {'PART', 'ADP'}:
                infinitive_verb = sent.words[word.head - 1]
                if infinitive_verb.upos == 'VERB':
                    # Per ROM rules: "to" → verb (R4 for intention), "to" → matrix verb (R2 for modal/intent)
                    self._add_relation_if_new(new_relations, {
                        "from": word.text, "to": infinitive_verb.text,
                        "rom relation": "Predicate (Preposition - Object)",
                        "stanza ud": "mark(to)→inf_verb"
                    })

                    if infinitive_verb.head != 0:
                        main_verb_governing_inf = sent.words[infinitive_verb.head - 1]
                        if infinitive_verb.deprel in {'xcomp', 'acl',
                                                      'advcl'} and main_verb_governing_inf.upos == 'VERB':
                            self._add_relation_if_new(new_relations, {
                                "from": word.text, "to": main_verb_governing_inf.text,
                                "rom relation": "Constraint",
                                "stanza ud": f"mark(to)→main_verb_of({infinitive_verb.deprel})"
                            })
        return new_relations

    def _handle_negation(self, sent, existing_relations):
        """Enhanced negation handling with POS validation"""
        new_relations = []

        # Handle contractions with POS validation
        for word in sent.words:
            if word.text.lower() in {"don't", "doesn't", "didn't", "won't", "can't", "shouldn't", "isn't", "aren't"}:
                if word.head != 0:
                    head_word = sent.words[word.head - 1]
                    # Validate that this is actually negating a verb
                    if head_word.upos in {'VERB', 'AUX'} or word.upos == 'AUX':
                        self._add_relation_if_new(new_relations, {
                            "from": word.text, "to": head_word.text,
                            "rom relation": "Constraint",
                            "stanza ud": f"neg_contraction({word.deprel})"
                        })

        return new_relations

    def _handle_copula_constructions(self, sent, existing_relations):
        """Handle copula constructions with enhanced POS validation"""
        new_relations = []
        for subject_word in sent.words:
            if subject_word.deprel.startswith('nsubj'):
                predicative_complement_candidate = sent.words[subject_word.head - 1]

                copula_word = None
                for child_of_pred_cand in sent.words:
                    if child_of_pred_cand.head == predicative_complement_candidate.id and \
                            child_of_pred_cand.deprel == 'cop' and child_of_pred_cand.upos == 'AUX':
                        copula_word = child_of_pred_cand
                        break

                if copula_word:
                    # Subject → Copula (R3)
                    self._add_relation_if_new(new_relations, {
                        "from": subject_word.text, "to": copula_word.text,
                        "rom relation": "Predicate (Subject - Verb)", "stanza ud": f"{subject_word.deprel}→cop"
                    })
                    # Copula → Predicative Complement (R4)
                    self._add_relation_if_new(new_relations, {
                        "from": copula_word.text, "to": predicative_complement_candidate.text,
                        "rom relation": "Predicate (Verb/Proposition - Object)", "stanza ud": "cop→pred_complement"
                    })
        return new_relations

    @staticmethod
    def print_relations(relations: list) -> None:
        """Print ROM relations in a formatted way"""
        for relation in relations:
            from_word = relation["from"]
            to_word = relation["to"]
            rom_relation = relation["rom relation"]
            stanza_ud = relation["stanza ud"]

            print(f"  {from_word} → {to_word}: {rom_relation} (UD: {stanza_ud})")
