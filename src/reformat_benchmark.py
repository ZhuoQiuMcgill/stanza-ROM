"""
Reformat benchmark files to extract sentences containing SBAR structures.

This module provides functionality to identify sentences with SBAR (subordinate clauses)
using stanza constituency parsing and extract them to new benchmark and input files,
while removing them from the original files.
"""

import os
import re
import stanza
from typing import List, Dict, Tuple
from tqdm import tqdm
import logging  # Import the logging module

# It's good practice to get a logger for your module
logger = logging.getLogger(__name__)


def reformat_benchmark(input_list: List[str],
                       benchmark_list: List[str],
                       input_dir: str,
                       benchmark_dir: str) -> None:
    """
    Extract sentences containing SBAR structures from existing benchmark and input files,
    create new files containing only SBAR sentences, and remove them from original files.

    Args:
        input_list: List of input filenames (e.g., ['file1.txt', 'file2.txt'])
        benchmark_list: List of benchmark filenames (e.g., ['benchmark1.md', 'benchmark2.md'])
        input_dir: Directory containing input .txt files
        benchmark_dir: Directory containing benchmark .md files

    Creates:
        - SBAR Sentences.md in benchmark_dir
        - sbar_sentences_input.txt in input_dir

    Modifies:
        - Removes SBAR sentences from original input files
        - Removes corresponding sections from original benchmark files
        - Renumbers remaining sentences in benchmark files
    """
    # Configure logging. This is a basic configuration.
    # For more complex applications, configure this at the application's entry point.
    # If logging is already configured elsewhere, this line might not be needed or could be conditional.
    if not logging.getLogger().hasHandlers():  # Configure only if no handlers are set
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    logger.info("Initializing stanza pipeline...")
    # Initialize stanza pipeline with constituency parser
    # Consider adding use_gpu=False if GPU is not always available or intended
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency', verbose=False, use_gpu=False)

    # Create file mapping by matching input files to benchmark files
    file_mapping = _create_file_mapping(input_dir, benchmark_dir, input_list, benchmark_list)

    sbar_sentences = []
    sbar_benchmark_data = []
    sbar_sentence_counter = 1
    total_lines_processed_from_txt = 0

    logger.info("Processing files...")
    # Iterate over the provided input_list
    for input_file_name in tqdm(input_list, desc="Processing input files"):
        if input_file_name not in file_mapping:
            logger.warning(f"No matching benchmark file found for {input_file_name}. Skipping.")
            continue

        benchmark_file_name = file_mapping[input_file_name]
        input_path = os.path.join(input_dir, input_file_name)
        benchmark_path = os.path.join(benchmark_dir, benchmark_file_name)

        if not os.path.exists(input_path):
            logger.error(f"Input file not found: {input_path}. Skipping.")
            continue
        if not os.path.exists(benchmark_path):
            logger.error(f"Benchmark file not found: {benchmark_path}. Skipping {input_file_name}.")
            continue

        # Read sentences from input file
        current_file_lines = []
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                current_file_lines = [line.strip() for line in f.readlines() if line.strip()]
        except Exception as e:
            logger.error(f"Error reading input file {input_path}: {e}. Skipping.", exc_info=True)
            continue

        logger.debug(f"File '{input_file_name}' contains {len(current_file_lines)} lines.")
        total_lines_processed_from_txt += len(current_file_lines)

        # Read benchmark data
        benchmark_content = ""
        try:
            with open(benchmark_path, 'r', encoding='utf-8') as f:
                benchmark_content = f.read()
        except Exception as e:
            logger.error(f"Error reading benchmark file {benchmark_path}: {e}. Skipping {input_file_name}.",
                         exc_info=True)
            continue

        # Parse benchmark content to extract sentence-relation mappings
        parsed_benchmark_entries = _parse_benchmark_content(benchmark_content, benchmark_file_name)

        # Separate SBAR and non-SBAR sentences
        sbar_sentences_in_file = []
        non_sbar_sentences = []

        for i, sentence_text in enumerate(tqdm(current_file_lines, desc=f"Analyzing {input_file_name}", leave=False)):
            if _contains_sbar(sentence_text, nlp):
                bench_data_entry_text = _find_benchmark_data(sentence_text, parsed_benchmark_entries)
                if bench_data_entry_text:
                    logger.debug(f"Adding to sbar_sentences from file '{input_file_name}': '{sentence_text}'")
                    sbar_sentences.append(sentence_text)
                    sbar_sentences_in_file.append(sentence_text)

                    first_line_of_bench_entry = bench_data_entry_text.split('\n')[0]
                    updated_bench_entry_text = bench_data_entry_text.replace(
                        first_line_of_bench_entry,
                        f"### Sentence {sbar_sentence_counter}:"
                    )
                    sbar_benchmark_data.append(updated_bench_entry_text)
                    sbar_sentence_counter += 1
                else:
                    logger.warning(
                        f"SBAR sentence in '{input_file_name}' but no benchmark data found: '{sentence_text}'")
                    non_sbar_sentences.append(sentence_text)
            else:
                non_sbar_sentences.append(sentence_text)

        # Update original input file (remove SBAR sentences)
        try:
            with open(input_path, 'w', encoding='utf-8') as f:
                for sentence_text in non_sbar_sentences:
                    f.write(sentence_text + '\n')
        except Exception as e:
            logger.error(f"Error writing updated input file {input_path}: {e}", exc_info=True)

        # Update original benchmark file (remove SBAR sections and renumber)
        _update_benchmark_file(benchmark_path, parsed_benchmark_entries, sbar_sentences_in_file, benchmark_file_name)

        logger.info(f"Processed {input_file_name}: {len(sbar_sentences_in_file)} SBAR sentences found and moved.")

    logger.debug(f"Total lines processed from all specified .txt files: {total_lines_processed_from_txt}")

    # Write new input file for SBAR sentences
    output_input_path = os.path.join(input_dir, 'sbar_sentences_input.txt')
    try:
        with open(output_input_path, 'w', encoding='utf-8') as f:
            for sentence_text in sbar_sentences:
                f.write(sentence_text + '\n')
    except Exception as e:
        logger.error(f"Error writing SBAR input file {output_input_path}: {e}", exc_info=True)

    # Write new benchmark file for SBAR sentences
    output_benchmark_path = os.path.join(benchmark_dir, 'SBAR Sentences.md')
    try:
        with open(output_benchmark_path, 'w', encoding='utf-8') as f:
            f.write("# SBAR Sentences\n\n")
            f.write("This file contains sentences with SBAR (subordinate clause) structures that were extracted.\n\n")
            for bench_data_text in sbar_benchmark_data:
                f.write(bench_data_text.strip() + '\n\n')  # Ensure two newlines between entries
    except Exception as e:
        logger.error(f"Error writing SBAR benchmark file {output_benchmark_path}: {e}", exc_info=True)

    logger.info("\nSummary:")  # Adding newline for readability in logs
    logger.info(f"Found {len(sbar_sentences)} sentences with SBAR structures from the processed files.")
    logger.info(f"Created: {output_input_path}")
    logger.info(f"Created: {output_benchmark_path}")
    logger.info(f"Original input and benchmark files have been updated to remove these SBAR sentences.")


def _create_file_mapping(input_dir: str, benchmark_dir: str,
                         input_filenames: List[str],
                         benchmark_filenames: List[str]) -> Dict[str, str]:
    """
    Create mapping between input files and benchmark files by matching sentences.
    """
    file_mapping = {}
    for input_fname in tqdm(input_filenames, desc="Creating file mappings"):
        input_path = os.path.join(input_dir, input_fname)
        if not os.path.exists(input_path):
            logger.warning(f"Input file for mapping not found: {input_path}")
            continue

        input_sample_sentences = []
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                for line in f:
                    stripped_line = line.strip()
                    if stripped_line:
                        input_sample_sentences.append(stripped_line)
                    if len(input_sample_sentences) >= 3:  # Sample first 3 non-empty sentences
                        break
        except Exception as e:
            logger.error(f"Error reading input file {input_path} for mapping: {e}", exc_info=True)
            continue

        if not input_sample_sentences:
            logger.warning(f"No sentences found in {input_path} for mapping.")
            continue

        best_match_benchmark_fname = None
        highest_match_score = 0

        for benchmark_fname in benchmark_filenames:
            benchmark_path = os.path.join(benchmark_dir, benchmark_fname)
            if not os.path.exists(benchmark_path):
                continue  # Silently skip if benchmark file for mapping doesn't exist

            current_match_score = 0
            try:
                with open(benchmark_path, 'r', encoding='utf-8') as bf:
                    benchmark_content_lower = bf.read().lower()

                for sentence in input_sample_sentences:
                    sentence_clean_lower = sentence.lower().strip().rstrip('.')
                    if sentence_clean_lower in benchmark_content_lower:
                        current_match_score += 1
            except Exception as e:
                logger.error(f"Error reading benchmark file {benchmark_path} for mapping: {e}", exc_info=True)
                continue

            if current_match_score > highest_match_score:
                highest_match_score = current_match_score
                best_match_benchmark_fname = benchmark_fname

        if best_match_benchmark_fname and highest_match_score > 0:
            file_mapping[input_fname] = best_match_benchmark_fname
            logger.debug(
                f"Mapped input '{input_fname}' to benchmark '{best_match_benchmark_fname}' with score {highest_match_score}")
        else:
            logger.warning(
                f"No suitable benchmark file found for input file '{input_fname}' based on content matching.")
    return file_mapping


def _update_benchmark_file(benchmark_path: str,
                           original_benchmark_entries: List[Dict[str, str]],
                           sbar_sentences_to_remove: List[str],
                           benchmark_filename_for_log: str) -> None:
    """
    Update original benchmark file by removing SBAR sections and renumbering remaining sections.
    """
    sbar_sentences_normalized_set = set()
    for sentence_text in sbar_sentences_to_remove:
        norm_text = sentence_text.lower().strip().rstrip('.')
        norm_text_no_parens = re.sub(r'\([^)]*\)', '', norm_text).strip()
        sbar_sentences_normalized_set.add(norm_text)
        if norm_text_no_parens:
            sbar_sentences_normalized_set.add(norm_text_no_parens)

    remaining_benchmark_data_dicts = []
    for entry_dict in original_benchmark_entries:
        bench_sentence_text = entry_dict['sentence']
        bench_sentence_clean_lower = bench_sentence_text.lower().strip().rstrip('.')
        bench_sentence_no_parens_lower = re.sub(r'\([^)]*\)', '', bench_sentence_clean_lower).strip()

        is_sbar_to_remove = (bench_sentence_clean_lower in sbar_sentences_normalized_set or
                             (
                                         bench_sentence_no_parens_lower and bench_sentence_no_parens_lower in sbar_sentences_normalized_set))

        if not is_sbar_to_remove:
            remaining_benchmark_data_dicts.append(entry_dict)
        else:
            logger.debug(
                f"Removing SBAR-associated entry for sentence '{bench_sentence_text}' from '{benchmark_filename_for_log}'")

    original_full_content = ""
    try:
        with open(benchmark_path, 'r', encoding='utf-8') as f:
            original_full_content = f.read()
    except Exception as e:
        logger.error(f"Error reading benchmark file {benchmark_path} for update: {e}. Skipping update.", exc_info=True)
        return

    header_match = re.match(r'^(.*?)(\n### Sentence \d+:|\Z)', original_full_content, re.DOTALL)
    file_header = header_match.group(1).strip() if header_match and header_match.group(1) else ""

    try:
        with open(benchmark_path, 'w', encoding='utf-8') as f:
            if file_header:
                f.write(file_header + '\n\n')

            for i, entry_dict in enumerate(remaining_benchmark_data_dicts, 1):
                section_text = entry_dict['full_data']
                updated_section_header = f"### Sentence {i}:"
                updated_section_text = re.sub(r'^### Sentence \d+:', updated_section_header, section_text, count=1,
                                              flags=re.MULTILINE)
                f.write(updated_section_text.strip() + '\n\n')
    except Exception as e:
        logger.error(f"Error writing updated benchmark file {benchmark_path}: {e}", exc_info=True)


def _contains_sbar(sentence: str, nlp) -> bool:
    """
    Check if a sentence contains SBAR structure.
    """
    try:
        doc = nlp(sentence)
        for sent_obj in doc.sentences:
            if hasattr(sent_obj, 'constituency') and sent_obj.constituency:
                if _traverse_tree_for_sbar(sent_obj.constituency):
                    return True
        return False
    except Exception as e:
        logger.error(f"Stanza error processing sentence for SBAR check: '{sentence[:50]}...': {e}",
                     exc_info=False)  # exc_info=False to avoid too much noise for common parsing issues
        return False


def _traverse_tree_for_sbar(tree_node) -> bool:
    """
    Recursively traverse constituency tree to find SBAR.
    """
    if not tree_node:
        return False
    if hasattr(tree_node, 'label') and tree_node.label == 'SBAR':
        return True
    if hasattr(tree_node, 'children'):
        for child in tree_node.children:
            if _traverse_tree_for_sbar(child):
                return True
    return False


def _parse_benchmark_content(content: str, benchmark_filename_for_log: str) -> List[Dict[str, str]]:
    """
    Parse benchmark content to extract sentence-relation mappings.
    """
    benchmark_entries = []
    section_starts = list(re.finditer(r'^### Sentence \d+:', content, re.MULTILINE))

    if not section_starts:
        logger.warning(f"No '### Sentence X:' sections found in benchmark content of '{benchmark_filename_for_log}'.")
        return benchmark_entries

    for i, match_obj in enumerate(section_starts):
        section_header = match_obj.group(0)
        start_index = match_obj.end()  # Content after the header

        end_index = section_starts[i + 1].start() if (i + 1) < len(section_starts) else len(content)

        section_body_with_newline = content[start_index:end_index]  # Includes leading newline if present
        section_body = section_body_with_newline.lstrip('\n')  # Remove leading newline from body

        full_section_text = f"{section_header}\n{section_body.rstrip()}"  # Reconstruct, rstrip body to remove trailing space

        input_match = re.search(r'\* \*\*Input\*\*\s*\n\s*-\s*(.+?)(?=\n\* \*\*|\Z)', section_body, re.DOTALL)
        if input_match:
            sentence_text = input_match.group(1).strip()
            benchmark_entries.append({
                'sentence': sentence_text,
                'full_data': full_section_text
            })
        else:
            pass
    return benchmark_entries


def _find_benchmark_data(sentence_to_find: str,
                         parsed_benchmark_entries: List[Dict[str, str]]) -> str:
    """
    Find benchmark data (full section string) for a specific sentence.
    """
    norm_sentence_to_find = sentence_to_find.lower().strip().rstrip('.')
    norm_sentence_to_find_no_parens = re.sub(r'\([^)]*\)', '', norm_sentence_to_find).strip()

    for entry_dict in parsed_benchmark_entries:
        bench_sentence_text = entry_dict['sentence']
        norm_bench_sentence = bench_sentence_text.lower().strip().rstrip('.')
        norm_bench_sentence_no_parens = re.sub(r'\([^)]*\)', '', norm_bench_sentence).strip()

        if norm_sentence_to_find == norm_bench_sentence:
            return entry_dict['full_data']
        if norm_sentence_to_find_no_parens and norm_sentence_to_find_no_parens == norm_bench_sentence_no_parens:
            return entry_dict['full_data']


    return None
