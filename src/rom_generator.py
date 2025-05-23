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
        Based on complete ROM documentation rules

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
            # Relative pronoun to antecedent: who → man: R1
            return 'Connection', False

        # R3: Predicate (Subject → Verb) - always subject to verb direction
        elif ud_relation in {'nsubj', 'nsubj:pass', 'nsubj:outer', 'csubj', 'csubj:pass', 'csubj:outer'}:
            return 'Predicate (subject - verb)', False

        # R4: Predicate (Verb/Prep → Object) - semantic head governs dependent
        elif ud_relation in {'obj', 'iobj', 'ccomp', 'xcomp'}:
            return 'Predicate (verb/proposition - object)', True  # Reverse: head → dependent

        elif ud_relation in {'obl', 'obl:agent', 'obl:arg'}:
            # Oblique: verb governs location/manner/etc
            return 'Predicate (verb/proposition - object)', True  # Reverse: head → dependent

        elif ud_relation in {'case'}:
            # Preposition governs its object: "on → table: R4"
            return 'Predicate (verb/proposition - object)', False  # Reverse: prep → object

        # COPULA CONSTRUCTION FIX: Predicate complements after copula
        elif ud_relation == 'amod' and head_lemma in {'be', 'is', 'are', 'was', 'were', 'am', 'being', 'been'}:
            # Predicate adjective after copula: "is → famous: R4"
            return 'Predicate (verb/proposition - object)', True  # Reverse: copula → predicate adjective

        elif ud_relation == 'nmod' and head_lemma in {'be', 'is', 'are', 'was', 'were', 'am', 'being', 'been'}:
            # Predicate nominative after copula: "is → friend: R4"
            return 'Predicate (verb/proposition - object)', True  # Reverse: copula → predicate nominative

        # CORRECTED: Auxiliaries and Copula should be R2 (Constraint)
        elif ud_relation in {'aux', 'aux:pass'}:
            # ROM doc: "Auxiliary/modal → verb: is → going: R2"
            return 'Constraint', True  # Reverse: aux → main verb

        elif ud_relation == 'cop':
            # Copula: "Is → famous: Predicate (verb/proposition - object)"
            # UD: famous --cop--> is, we want: is → famous
            return 'Predicate (verb/proposition - object)', False  # Keep: copula → predicate

        # REFINED: Mark - context-dependent mapping
        elif ud_relation == 'mark':
            # Check if it's a complementizer vs subordinating conjunction
            complementizers = {'that', 'whether', 'if', 'where', 'when', 'why', 'how', 'what'}
            if word_text and word_text.lower() in complementizers:
                # "Complementizer introducing dependent verb: whether → knew: R4"
                # "Adverbial adjunct/subordinating conjunction → dependent verb: where → slept: R4"
                return 'Predicate (verb/proposition - object)', False  # Keep: complementizer → verb
            else:
                # "Subordinating conjunction (modifier) → independent verb: because → stayed: R2"
                return 'Constraint', False  # Keep: conj → verb (modifier relationship)

        # Relative clause fix
        elif ud_relation == 'acl:relcl':
            # Relative clause: antecedent is subject of relative verb
            # UD: verb --acl:relcl--> antecedent
            # ROM: antecedent → verb: Predicate (subject - verb)
            return 'Predicate (subject - verb)', True  # Reverse: antecedent → verb

        elif ud_relation == 'acl':
            # Non-relative adnominal clause modifying noun
            return 'Constraint', False

        # R2: Constraint (Modifier/Qualifier) - modifier relationship
        elif ud_relation in {'det', 'amod', 'advmod', 'advmod:emph', 'advmod:lmod',
                             'nmod', 'nmod:poss', 'nmod:tmod', 'nummod', 'nummod:gov',
                             'fixed', 'flat', 'flat:foreign', 'flat:name',
                             'det:numgov', 'det:nummod', 'det:poss', 'clf', 'cc:preconj',
                             'obl:tmod', 'obl:lmod'}:
            return 'Constraint', False

        elif ud_relation in {'compound', 'compound:lvc', 'compound:prt', 'compound:redup',
                             'compound:svc'}:
            return 'Constraint', True

        elif ud_relation in {'advcl', 'advcl:relcl'}:
            # Adverbial clause modifying main clause
            return 'Constraint', False

        # Default: skip unknown relations
        return None, False

    def analyze_sentence(self, sentence: str) -> list:
        """
        Analyze a sentence and extract ROM relations from UD parsing.
        Updated to use corrected ROM mapping rules with copula construction fix.

        Args:
            sentence: Input sentence to analyze

        Returns:
            List of dictionaries with structure:
            [
                {
                    "from": word1,
                    "to": word2,
                    "rom relation": relation,
                    "stanza ud": ud
                }
            ]
        """
        # Process sentence
        doc = self.nlp(sentence)

        # Extract relations
        relations = []

        for sent in doc.sentences:
            for word in sent.words:
                if word.head == 0:  # Skip root
                    continue

                # Get head word
                head_word = sent.words[word.head - 1]

                # Special case: Skip nsubj relations when head has a copula (handle separately)
                if word.deprel == 'nsubj':
                    # Check if head has a copula
                    has_copula = any(child.head == head_word.id and child.deprel == 'cop'
                                     for child in sent.words)
                    if has_copula:
                        continue  # Skip this relation, will be handled in special cases

                # Get ROM mapping - now passing head lemma for copula detection
                rom_result = self.get_rom_mapping(
                    word.deprel,
                    word.text,
                    word.upos,
                    head_word.upos,
                    head_word.lemma
                )

                if rom_result[0] is None:  # Skip if no valid ROM mapping
                    continue

                rom_description, reverse_direction = rom_result

                # Determine direction based on mapping
                if reverse_direction:
                    # Semantic head → dependent
                    relation_dict = {
                        "from": head_word.text,
                        "to": word.text,
                        "rom relation": rom_description,
                        "stanza ud": word.deprel
                    }
                else:
                    # Keep original direction: dependent → head
                    relation_dict = {
                        "from": word.text,
                        "to": head_word.text,
                        "rom relation": rom_description,
                        "stanza ud": word.deprel
                    }

                relations.append(relation_dict)

            # Handle special cases for subordinating conjunctions
            # Need to add conjunction → main clause relationships for advcl
            for word in sent.words:
                if word.deprel == 'advcl':  # subordinate clause
                    # Find the marker (subordinating conjunction)
                    marker = None
                    for child in sent.words:
                        if child.head == word.id and child.deprel == 'mark':
                            marker = child
                            break

                    if marker:
                        # Add conjunction → main clause relationship
                        main_verb = sent.words[word.head - 1]
                        # Most subordinating conjunctions are R2 (Constraint) when linking to main clause
                        relation_dict = {
                            "from": marker.text,
                            "to": main_verb.text,
                            "rom relation": "Constraint",
                            "stanza ud": "mark→advcl"
                        }
                        relations.append(relation_dict)

            # Handle relative pronoun → antecedent connections
            for word in sent.words:
                if word.deprel == 'acl:relcl':  # This is the relative clause verb
                    # Find the relative pronoun (subject of this verb)
                    rel_pronoun = None
                    for child in sent.words:
                        if child.head == word.id and child.deprel == 'nsubj' and child.lemma.lower() in {'who', 'which',
                                                                                                         'that'}:
                            rel_pronoun = child
                            break

                    if rel_pronoun:
                        # Get the antecedent (head of the relative clause)
                        antecedent = sent.words[word.head - 1]
                        # Add relative pronoun → antecedent connection
                        relation_dict = {
                            "from": rel_pronoun.text,
                            "to": antecedent.text,
                            "rom relation": "Connection",
                            "stanza ud": "nsubj→acl:relcl"
                        }
                        relations.append(relation_dict)

            # Handle copula constructions: redirect subject to copula
            for word in sent.words:
                if word.deprel == 'nsubj':
                    head_word = sent.words[word.head - 1]
                    # Check if the head has a copula
                    copula = None
                    for child in sent.words:
                        if child.head == head_word.id and child.deprel == 'cop':
                            copula = child
                            break

                    if copula:
                        # Add subject → copula relationship (overrides the subject → predicate complement)
                        relation_dict = {
                            "from": word.text,
                            "to": copula.text,
                            "rom relation": "Predicate (subject - verb)",
                            "stanza ud": "nsubj"
                        }
                        relations.append(relation_dict)

        return relations

    @staticmethod
    def print_relations(relations: list) -> None:
        """
        Print ROM relations in a formatted way.

        Args:
            relations: List of relation dictionaries from analyze_sentence()
        """
        for relation in relations:
            from_word = relation["from"]
            to_word = relation["to"]
            rom_relation = relation["rom relation"]
            stanza_ud = relation["stanza ud"]

            print(f"  {from_word} → {to_word}: {rom_relation} (UD: {stanza_ud})")
