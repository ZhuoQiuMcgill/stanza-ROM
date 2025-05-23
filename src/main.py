"""
Main script demonstrating the usage of ROMGenerator class.

This script shows how to use the ROMGenerator to analyze sentences
and extract ROM relations from Universal Dependencies parsing.
"""

import json
from rom_generator import ROMGenerator


def main():
    """
    Main function demonstrating ROM analysis with example sentences.
    """
    # Initialize the ROM generator
    print("Initializing ROM Generator...")
    rom_gen = ROMGenerator(lang='en', verbose=False)
    print("ROM Generator initialized successfully.\n")

    # Test sentences
    test_sentences = [
        "I stayed home because it was raining.",
        "The man who lives next door is friendly.",
        "She is a talented musician.",
        "The book on the table belongs to me.",
        "They will arrive tomorrow morning."
    ]

    # Analyze each sentence
    for i, sentence in enumerate(test_sentences, 1):
        print("=" * 60)
        print(f"Example {i}:")
        print(f"Input: {sentence}")
        print("\nROM Relations:")

        try:
            relations = rom_gen.analyze_sentence(sentence)

            if relations:
                rom_gen.print_relations(relations)
            else:
                print("  No ROM relations found.")

        except Exception as e:
            print(f"  Error analyzing sentence: {e}")

        print()

    print("=" * 60)
    print("Analysis complete!")


if __name__ == "__main__":
    main()
