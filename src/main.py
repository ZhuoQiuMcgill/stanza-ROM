"""
Main script demonstrating the usage of ROMGenerator class.

This script shows how to use the ROMGenerator to analyze sentences
and extract ROM relations from Universal Dependencies parsing.
"""

import json
import os.path
from tqdm import tqdm

from rom_generator import ROMGenerator
from utils import evaluate_rom, read_txt_lines
from pos_analysis import analyze_pos_ud_rom_relations, analyze_multiple_pos_ud_rom_relations


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


def comparison():
    input_dir = os.path.join(os.getcwd(), 'data', 'inputs')
    output_dir = os.path.join(os.getcwd(), 'data', 'outputs')
    benchmark_dir = os.path.join(os.getcwd(), 'data', 'benchmark')

    input_list = [
        'adjective_clauses_sentences_input.txt',
        'adverb_clauses_sentence_input.txt',
        'basic_sentences_input.txt',
        'compound_sentences_input.txt',
        'noun_clauses_sentences_input.txt'
    ]
    benchmark_list = [
        'Adjective clauses.md',
        'Adverb clauses.md',
        'Basic Sentences.md',
        'Compound Sentences.md',
        'Noun clauses.md'
    ]
    output_list = [
        'ADJ', 'ADV', 'BASIC', 'COMP', 'NOUN'
    ]

    for i, input_file_name in enumerate(tqdm(input_list)):
        benchmark_file_name = benchmark_list[i]
        input_file = os.path.join(input_dir, input_file_name)
        output_file = os.path.join(output_dir, output_list[i] + "_report.md")
        benchmark_file = os.path.join(benchmark_dir, benchmark_file_name)
        sentences = read_txt_lines(input_file)

        evaluate_rom(sentences, benchmark_file, save=output_file)


def analys_data():
    input_dir = os.path.join(os.getcwd(), 'data', 'inputs')
    output_dir = os.path.join(os.getcwd(), 'data', 'outputs')
    benchmark_dir = os.path.join(os.getcwd(), 'data', 'benchmark')

    input_list = [
        'adjective_clauses_sentences_input.txt',
        'adverb_clauses_sentence_input.txt',
        'basic_sentences_input.txt',
        'compound_sentences_input.txt',
        'noun_clauses_sentences_input.txt'
    ]
    benchmark_list = [
        'Adjective clauses.md',
        'Adverb clauses.md',
        'Basic Sentences.md',
        'Compound Sentences.md',
        'Noun clauses.md'
    ]
    output_list = [
        'ADJ', 'ADV', 'BASIC', 'COMP', 'NOUN'
    ]
    for i, input_file_name in enumerate(tqdm(input_list)):
        benchmark_file_name = benchmark_list[i]
        input_file = os.path.join(input_dir, input_file_name)
        output_file = os.path.join(output_dir, output_list[i] + "_ud_analysis.md")
        benchmark_file = os.path.join(benchmark_dir, benchmark_file_name)
        sentences = read_txt_lines(input_file)

        analyze_pos_ud_rom_relations(sentences, benchmark_file, save=output_file)


def batch_analys():
    input_dir = os.path.join(os.getcwd(), 'data', 'inputs')
    output_dir = os.path.join(os.getcwd(), 'data', 'outputs')
    benchmark_dir = os.path.join(os.getcwd(), 'data', 'benchmark')
    input_list = [
        'adjective_clauses_sentences_input.txt',
        'adverb_clauses_sentence_input.txt',
        'basic_sentences_input.txt',
        'compound_sentences_input.txt',
        'noun_clauses_sentences_input.txt'
    ]
    benchmark_list = [
        'Adjective clauses.md',
        'Adverb clauses.md',
        'Basic Sentences.md',
        'Compound Sentences.md',
        'Noun clauses.md'
    ]
    analyze_multiple_pos_ud_rom_relations(input_list=input_list,
                                          benchmark_list=benchmark_list,
                                          input_dir=input_dir,
                                          benchmark_dir=benchmark_dir,
                                          save=os.path.join(output_dir, 'combined_report.md'))


if __name__ == "__main__":
    batch_analys()
