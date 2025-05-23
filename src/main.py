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
from reformat_benchmark import reformat_benchmark

input_dir = os.path.join(os.getcwd(), 'data', 'inputs')
output_dir = os.path.join(os.getcwd(), 'data', 'outputs')
benchmark_dir = os.path.join(os.getcwd(), 'data', 'benchmark')


def comparison():
    input_list = [
        'basic_sentences_input.txt',
        'compound_sentences_input.txt',
        'sbar_sentences_input.txt'
    ]
    benchmark_list = [
        'Basic Sentences.md',
        'Compound Sentences.md',
        'SBAR Sentences.md'
    ]
    output_list = [
        'BASIC', 'COMP', 'SBAR'
    ]

    for i, input_file_name in enumerate(tqdm(input_list)):
        benchmark_file_name = benchmark_list[i]
        input_file = os.path.join(input_dir, input_file_name)
        output_file = os.path.join(output_dir, output_list[i] + "_report.md")
        benchmark_file = os.path.join(benchmark_dir, benchmark_file_name)
        sentences = read_txt_lines(input_file)

        evaluate_rom(sentences, benchmark_file, save=output_file)


def analys_data():
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


def reformat():
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
    reformat_benchmark(input_list=input_list,
                       benchmark_list=benchmark_list,
                       input_dir=input_dir,
                       benchmark_dir=benchmark_dir)


if __name__ == "__main__":
    comparison()
