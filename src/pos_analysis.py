"""
Helper functions for POS-based ROM analysis and comparison.

This module provides functions to analyze sentences using POS tags and compare
Universal Dependencies relations with ROM relations at the POS level.
"""

import stanza
from typing import List, Tuple, Dict, Any
import re
from collections import defaultdict
import os


def read_txt_lines(filepath: str) -> List[str]:
    """
    Read a .txt file line by line and return a list containing each line as elements.

    Args:
        filepath: Path to the .txt file to read

    Returns:
        List of strings, each representing a line from the file (with whitespace stripped)

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file {filepath}: {e}")


def analyze_multiple_pos_ud_rom_relations(input_list: List[str], benchmark_list: List[str],
                                          input_dir: str = None, benchmark_dir: str = None,
                                          save: str = None, log: bool = False) -> tuple:
    """
    Analyze POS-UD relations and POS-ROM relations for multiple input files and benchmarks.

    Args:
        input_list: List of input text file names
        benchmark_list: List of benchmark .md file names
        input_dir: Directory containing input files (optional)
        benchmark_dir: Directory containing benchmark files (optional)
        save: Optional path to save the combined evaluation report as a markdown file
        log: Whether to print the report to console (default: False)

    Returns:
        tuple: (all_combined_results, all_pos_ud_tuples, all_pos_rom_tuples, file_breakdown)
    """
    if len(input_list) != len(benchmark_list):
        raise ValueError("Input list and benchmark list must have the same length")

    # Initialize Stanza pipeline once
    nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse', verbose=False)

    # Collect results from all files
    all_combined_results = []
    all_pos_ud_tuples = []
    all_pos_rom_tuples = []
    file_breakdown = []
    total_processed_sentences = 0
    total_skipped_sentences = 0

    for i, (input_file, benchmark_file) in enumerate(zip(input_list, benchmark_list)):
        print(f"Processing {input_file} with {benchmark_file}...")

        # Construct full paths
        input_path = os.path.join(input_dir, input_file) if input_dir else input_file
        benchmark_path = os.path.join(benchmark_dir, benchmark_file) if benchmark_dir else benchmark_file

        # Read input sentences
        try:
            with open(input_path, 'r', encoding='utf-8') as file:
                sentences = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"Warning: Input file not found: {input_path}")
            continue
        except IOError as e:
            print(f"Warning: Error reading input file {input_path}: {e}")
            continue

        # Read benchmark file
        try:
            with open(benchmark_path, 'r', encoding='utf-8') as file:
                benchmark_content = file.read()
        except FileNotFoundError:
            print(f"Warning: Benchmark file not found: {benchmark_path}")
            continue
        except IOError as e:
            print(f"Warning: Error reading benchmark file {benchmark_path}: {e}")
            continue

        # Process this file pair
        file_results = []
        file_pos_ud_tuples = []
        file_pos_rom_tuples = []
        file_skipped = []

        for sentence in sentences:
            # Check if sentence exists in benchmark
            expected_relations = _parse_benchmark_relations(sentence, benchmark_content)

            if not expected_relations:
                file_skipped.append(sentence)
                continue

            # Analyze sentence with Stanza
            doc = nlp(sentence)

            # Extract POS-UD tuples and create word-to-POS mapping
            pos_ud_tuples = []
            word_to_pos = {}
            word_positions = {}

            for sent in doc.sentences:
                for word in sent.words:
                    # Handle duplicate words by adding position info
                    word_key = word.text.lower()
                    if word_key in word_positions:
                        word_positions[word_key].append(word.id)
                    else:
                        word_positions[word_key] = [word.id]
                    word_to_pos[f"{word.text.lower()}_{word.id}"] = word.upos
                    word_to_pos[word.text.lower()] = word.upos

                    if word.head != 0:  # Skip root
                        head_word = sent.words[word.head - 1]
                        pos_ud_tuple = (head_word.upos, word.upos, word.deprel)
                        pos_ud_tuples.append(pos_ud_tuple)

            # Extract POS-ROM tuples from benchmark
            pos_rom_tuples = []
            for from_word, to_word, rom_relation in expected_relations:
                from_pos = word_to_pos.get(from_word.lower())
                to_pos = word_to_pos.get(to_word.lower())
                if from_pos and to_pos:
                    pos_rom_tuple = (from_pos, to_pos, rom_relation)
                    pos_rom_tuples.append(pos_rom_tuple)

            # Store results for this sentence
            sentence_result = {
                'sentence': sentence,
                'pos_ud_tuples': pos_ud_tuples,
                'pos_rom_tuples': pos_rom_tuples,
                'expected_relations': expected_relations,
                'word_to_pos': word_to_pos,
                'word_positions': word_positions,
                'file_source': input_file,
                'benchmark_source': benchmark_file
            }
            file_results.append(sentence_result)

            # Add to file collections
            file_pos_ud_tuples.extend(pos_ud_tuples)
            file_pos_rom_tuples.extend(pos_rom_tuples)

        # Store file breakdown information
        file_info = {
            'input_file': input_file,
            'benchmark_file': benchmark_file,
            'processed_sentences': len(file_results),
            'skipped_sentences': len(file_skipped),
            'total_sentences': len(sentences),
            'pos_ud_count': len(file_pos_ud_tuples),
            'pos_rom_count': len(file_pos_rom_tuples),
            'results': file_results,
            'skipped': file_skipped
        }
        file_breakdown.append(file_info)

        # Add to overall collections
        all_combined_results.extend(file_results)
        all_pos_ud_tuples.extend(file_pos_ud_tuples)
        all_pos_rom_tuples.extend(file_pos_rom_tuples)
        total_processed_sentences += len(file_results)
        total_skipped_sentences += len(file_skipped)

        print(f"  - Processed: {len(file_results)} sentences")
        print(f"  - Skipped: {len(file_skipped)} sentences")
        print(f"  - POS-UD relations: {len(file_pos_ud_tuples)}")
        print(f"  - POS-ROM relations: {len(file_pos_rom_tuples)}")

    print(f"\nOverall Summary:")
    print(f"  - Total processed sentences: {total_processed_sentences}")
    print(f"  - Total skipped sentences: {total_skipped_sentences}")
    print(f"  - Total POS-UD relations: {len(all_pos_ud_tuples)}")
    print(f"  - Total POS-ROM relations: {len(all_pos_rom_tuples)}")

    # Generate combined analysis report
    report = _generate_combined_pos_analysis_report(all_combined_results, file_breakdown,
                                                    all_pos_ud_tuples, all_pos_rom_tuples)

    # Print report to console if log is True
    if log:
        print(report)

    # Save report if path provided
    if save:
        try:
            with open(save, 'w', encoding='utf-8') as file:
                file.write(report)
                print(f"Combined POS analysis report saved to: {save}")
        except IOError as e:
            raise IOError(f"Error writing report to file {save}: {e}")

    return all_combined_results, all_pos_ud_tuples, all_pos_rom_tuples, file_breakdown


def analyze_pos_ud_rom_relations(sentences: List[str], benchmark: str, save: str = None, log: bool = False) -> tuple:
    """
    Analyze POS-UD relations and POS-ROM relations for comparison.

    Args:
        sentences: List of input sentences to analyze
        benchmark: Path to the benchmark .md file containing expected relations
        save: Optional path to save the evaluation report as a markdown file
        log: Whether to print the report to console (default: False)

    Returns:
        tuple: (all_results, all_pos_ud_tuples, all_pos_rom_tuples)
    """
    # Initialize Stanza pipeline
    nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse', verbose=False)

    # Read benchmark file
    try:
        with open(benchmark, 'r', encoding='utf-8') as file:
            benchmark_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Benchmark file not found: {benchmark}")
    except IOError as e:
        raise IOError(f"Error reading benchmark file {benchmark}: {e}")

    all_results = []
    skipped_sentences = []

    # Collect all POS-UD and POS-ROM tuples across all sentences
    all_pos_ud_tuples = []
    all_pos_rom_tuples = []

    for sentence in sentences:
        # Check if sentence exists in benchmark
        expected_relations = _parse_benchmark_relations(sentence, benchmark_content)

        if not expected_relations:
            skipped_sentences.append(sentence)
            continue

        # Analyze sentence with Stanza
        doc = nlp(sentence)

        # Extract POS-UD tuples and create word-to-POS mapping
        pos_ud_tuples = []
        word_to_pos = {}  # Map word text to POS for ROM mapping
        word_positions = {}  # Map word text to its position for handling duplicates

        for sent in doc.sentences:
            for word in sent.words:
                # Handle duplicate words by adding position info
                word_key = word.text.lower()
                if word_key in word_positions:
                    word_positions[word_key].append(word.id)
                else:
                    word_positions[word_key] = [word.id]
                word_to_pos[f"{word.text.lower()}_{word.id}"] = word.upos
                word_to_pos[word.text.lower()] = word.upos  # Keep simple mapping for last occurrence

                if word.head != 0:  # Skip root
                    head_word = sent.words[word.head - 1]
                    # Create tuple as (head_POS, dependent_POS, UD_relation)
                    pos_ud_tuple = (head_word.upos, word.upos, word.deprel)
                    pos_ud_tuples.append(pos_ud_tuple)

        # Extract POS-ROM tuples from benchmark
        pos_rom_tuples = []
        for from_word, to_word, rom_relation in expected_relations:
            from_pos = word_to_pos.get(from_word.lower())
            to_pos = word_to_pos.get(to_word.lower())
            if from_pos and to_pos:
                # Create tuple as (from_POS, to_POS, ROM_relation) following benchmark direction
                pos_rom_tuple = (from_pos, to_pos, rom_relation)
                pos_rom_tuples.append(pos_rom_tuple)

        # Store results for this sentence
        sentence_result = {
            'sentence': sentence,
            'pos_ud_tuples': pos_ud_tuples,
            'pos_rom_tuples': pos_rom_tuples,
            'expected_relations': expected_relations,
            'word_to_pos': word_to_pos,
            'word_positions': word_positions
        }
        all_results.append(sentence_result)

        # Add to overall collections
        all_pos_ud_tuples.extend(pos_ud_tuples)
        all_pos_rom_tuples.extend(pos_rom_tuples)

    # Generate analysis report
    report = _generate_pos_analysis_report(all_results, skipped_sentences,
                                           all_pos_ud_tuples, all_pos_rom_tuples)

    # Print report to console if log is True
    if log:
        print(report)

    # Save report if path provided
    if save:
        try:
            with open(save, 'w', encoding='utf-8') as file:
                file.write(report)
                print(f"POS analysis report saved to: {save}")
        except IOError as e:
            raise IOError(f"Error writing report to file {save}: {e}")

    return all_results, all_pos_ud_tuples, all_pos_rom_tuples


def _parse_benchmark_relations(sentence: str, benchmark: str) -> List[Tuple[str, str, str]]:
    """
    Parse benchmark content to extract expected relations for a given sentence.

    Args:
        sentence: The input sentence to find in benchmark
        benchmark: Benchmark content in markdown format

    Returns:
        List of tuples: [(from_word, to_word, relation_type), ...]
    """
    lines = benchmark.strip().split('\n')
    relations = []

    # Find the section containing this sentence
    in_target_section = False
    in_output_section = False

    for line in lines:
        line = line.strip()

        # Check if this line contains our target sentence
        if sentence.lower().strip() in line.lower():
            in_target_section = True
            continue

        # If we're in the target section, look for output section
        if in_target_section and '* **Output**' in line:
            in_output_section = True
            continue

        # If we hit another input section, we're done with this sentence
        if in_target_section and '* **Input**' in line and in_output_section:
            break

        # If we hit another main section (##), we're done
        if in_target_section and line.startswith('##'):
            break

        # Parse relation lines in output section
        if in_output_section and '→' in line:
            # Extract relation in format: "word1 → word2: relation_type"
            match = re.search(r'([^→]+)→([^:]+):(.+)', line)
            if match:
                from_word = match.group(1).strip().lstrip('- ')
                to_word = match.group(2).strip()
                relation_type = match.group(3).strip()
                relations.append((from_word, to_word, relation_type))

    return relations


def _generate_combined_pos_analysis_report(all_results: List[Dict], file_breakdown: List[Dict],
                                           all_pos_ud_tuples: List[Tuple], all_pos_rom_tuples: List[Tuple]) -> str:
    """
    Generate a markdown formatted combined POS analysis report for multiple files.

    Args:
        all_results: List of all sentence analysis results from all files
        file_breakdown: List of file-specific breakdown information
        all_pos_ud_tuples: All POS-UD tuples from all sentences
        all_pos_rom_tuples: All POS-ROM tuples from all benchmarks

    Returns:
        Formatted markdown report string
    """
    report = []

    # Header
    report.append("# Combined POS-based UD vs ROM Relations Analysis Report")
    report.append("")
    report.append(f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Total Files Processed:** {len(file_breakdown)}")
    report.append(f"**Total Sentences Processed:** {len(all_results)}")
    total_skipped = sum(len(fb['skipped']) for fb in file_breakdown)
    report.append(f"**Total Sentences Skipped:** {total_skipped}")
    report.append("")

    # File Breakdown Summary
    report.append("## 📁 File Processing Summary")
    report.append("")
    report.append("| Input File | Benchmark File | Processed | Skipped | Total | POS-UD | POS-ROM |")
    report.append("|------------|----------------|-----------|---------|-------|--------|---------|")

    for fb in file_breakdown:
        report.append(f"| {fb['input_file']} | {fb['benchmark_file']} | {fb['processed_sentences']} | "
                      f"{fb['skipped_sentences']} | {fb['total_sentences']} | {fb['pos_ud_count']} | {fb['pos_rom_count']} |")
    report.append("")

    # Overall Statistics
    report.append("## 📊 Overall Combined Statistics")
    report.append("")
    report.append("| Metric | Count |")
    report.append("|--------|-------|")
    report.append(f"| Total POS-UD Relations | {len(all_pos_ud_tuples)} |")
    report.append(f"| Total POS-ROM Relations | {len(all_pos_rom_tuples)} |")
    report.append("")

    # Analyze POS pairs and their relations with examples
    pos_pair_analysis = _analyze_pos_pairs_with_examples(all_results)

    # Calculate match rates
    match_statistics = _calculate_match_rates(all_pos_ud_tuples, all_pos_rom_tuples)

    # Match Rate Analysis
    report.append("## 📈 Overall Match Rate Analysis")
    report.append("")
    report.append("| Metric | Value |")
    report.append("|--------|-------|")
    report.append(f"| Unique POS Pairs in UD | {match_statistics['unique_ud_pairs']} |")
    report.append(f"| Unique POS Pairs in ROM | {match_statistics['unique_rom_pairs']} |")
    report.append(f"| Common POS Pairs | {match_statistics['common_pairs']} |")
    report.append(f"| POS Pair Overlap Rate | {match_statistics['pair_overlap_rate']:.1f}% |")
    report.append("")

    # POS Pair Analysis Section
    report.append("## 🔍 Detailed POS Pair Analysis (Combined)")
    report.append("")
    report.append("This section shows for each POS pair what UD relations and ROM relations appeared across all files.")
    report.append("")

    for pos_pair, data in sorted(pos_pair_analysis.items()):
        report.append(f"### {pos_pair[0]} → {pos_pair[1]}")
        report.append("")

        # UD Relations for this POS pair
        if data['ud_relations']:
            report.append("**UD Relations:**")
            for ud_rel, count in sorted(data['ud_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {ud_rel} ({count} occurrences)")
            report.append("")

        # ROM Relations for this POS pair
        if data['rom_relations']:
            report.append("**ROM Relations:**")
            for rom_rel, count in sorted(data['rom_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {rom_rel} ({count} occurrences)")
            report.append("")

        # Examples section
        report.append("**Examples:**")

        # UD Examples
        if data['ud_examples']:
            report.append("*UD Examples:*")
            example_count = 0
            for ud_rel, examples in data['ud_examples'].items():
                if example_count >= 6:  # Limit total examples per POS pair
                    break
                for example in examples[:2]:  # Max 2 examples per UD relation
                    if example_count >= 6:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{ud_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        # ROM Examples
        if data['rom_examples']:
            report.append("*ROM Examples:*")
            example_count = 0
            for rom_rel, examples in data['rom_examples'].items():
                if example_count >= 6:  # Limit total examples per POS pair
                    break
                for example in examples[:2]:  # Max 2 examples per ROM relation
                    if example_count >= 6:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{rom_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        if not data['ud_examples'] and not data['rom_examples']:
            report.append("- No examples available")
            report.append("")

        # Match analysis
        report.append("**Analysis:**")
        ud_count = sum(data['ud_relations'].values())
        rom_count = sum(data['rom_relations'].values())

        report.append(f"- Total UD instances: {ud_count}")
        report.append(f"- Total ROM instances: {rom_count}")

        if ud_count > 0 and rom_count > 0:
            ratio = rom_count / ud_count
            report.append(f"- ROM/UD ratio: {ratio:.2f}")
            report.append("- **Status: Both UD and ROM relations exist for this POS pair**")
        elif ud_count > 0:
            report.append("- **Status: Only UD relations exist (no ROM coverage)**")
        elif rom_count > 0:
            report.append("- **Status: Only ROM relations exist (no UD match)**")

        report.append("")
        report.append("---")
        report.append("")

    # Summary tables
    report.append("## 📋 Combined Summary Tables")
    report.append("")

    # UD Relations Summary
    report.append("### UD Relations Summary (All Files)")
    ud_summary = defaultdict(int)
    for _, _, ud_rel in all_pos_ud_tuples:
        ud_summary[ud_rel] += 1

    report.append("| UD Relation | Count | Percentage |")
    report.append("|-------------|-------|------------|")
    total_ud = len(all_pos_ud_tuples)
    for ud_rel, count in sorted(ud_summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_ud * 100) if total_ud > 0 else 0
        report.append(f"| {ud_rel} | {count} | {percentage:.1f}% |")
    report.append("")

    # ROM Relations Summary
    report.append("### ROM Relations Summary (All Files)")
    rom_summary = defaultdict(int)
    for _, _, rom_rel in all_pos_rom_tuples:
        rom_summary[rom_rel] += 1

    report.append("| ROM Relation | Count | Percentage |")
    report.append("|--------------|-------|------------|")
    total_rom = len(all_pos_rom_tuples)
    for rom_rel, count in sorted(rom_summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_rom * 100) if total_rom > 0 else 0
        report.append(f"| {rom_rel} | {count} | {percentage:.1f}% |")
    report.append("")

    # POS Pairs Summary
    report.append("### POS Pairs Distribution (All Files)")
    pos_pair_counts = defaultdict(int)
    for pos1, pos2, _ in all_pos_ud_tuples:
        pos_pair_counts[(pos1, pos2)] += 1

    rom_pair_counts = defaultdict(int)
    for pos1, pos2, _ in all_pos_rom_tuples:
        rom_pair_counts[(pos1, pos2)] += 1

    report.append("| POS Pair | UD Count | ROM Count | Status |")
    report.append("|----------|----------|-----------|--------|")

    all_pairs = set(pos_pair_counts.keys()) | set(rom_pair_counts.keys())
    for pair in sorted(all_pairs, key=lambda x: (pos_pair_counts.get(x, 0) + rom_pair_counts.get(x, 0)), reverse=True):
        ud_count = pos_pair_counts.get(pair, 0)
        rom_count = rom_pair_counts.get(pair, 0)

        if ud_count > 0 and rom_count > 0:
            status = "Both"
        elif ud_count > 0:
            status = "UD Only"
        else:
            status = "ROM Only"

        report.append(f"| {pair[0]} → {pair[1]} | {ud_count} | {rom_count} | {status} |")
    report.append("")

    # File-specific breakdown analysis
    report.append("## 📂 File-Specific Analysis")
    report.append("")

    for fb in file_breakdown:
        report.append(f"### {fb['input_file']} ↔ {fb['benchmark_file']}")
        report.append("")

        # Get file-specific tuples
        file_pos_ud = []
        file_pos_rom = []
        for result in fb['results']:
            file_pos_ud.extend(result['pos_ud_tuples'])
            file_pos_rom.extend(result['pos_rom_tuples'])

        # File statistics
        report.append("| Metric | Count |")
        report.append("|--------|-------|")
        report.append(f"| Processed Sentences | {fb['processed_sentences']} |")
        report.append(f"| Skipped Sentences | {fb['skipped_sentences']} |")
        report.append(f"| POS-UD Relations | {len(file_pos_ud)} |")
        report.append(f"| POS-ROM Relations | {len(file_pos_rom)} |")
        report.append("")

        # Top UD relations for this file
        file_ud_summary = defaultdict(int)
        for _, _, ud_rel in file_pos_ud:
            file_ud_summary[ud_rel] += 1

        if file_ud_summary:
            report.append("**Top UD Relations:**")
            for ud_rel, count in sorted(file_ud_summary.items(), key=lambda x: x[1], reverse=True)[:5]:
                report.append(f"- {ud_rel}: {count}")
            report.append("")

        # Top ROM relations for this file
        file_rom_summary = defaultdict(int)
        for _, _, rom_rel in file_pos_rom:
            file_rom_summary[rom_rel] += 1

        if file_rom_summary:
            report.append("**Top ROM Relations:**")
            for rom_rel, count in sorted(file_rom_summary.items(), key=lambda x: x[1], reverse=True)[:5]:
                report.append(f"- {rom_rel}: {count}")
            report.append("")

        # Skipped sentences for this file
        if fb['skipped']:
            report.append("<details>")
            report.append("<summary>Skipped Sentences</summary>")
            report.append("")
            for sentence in fb['skipped']:
                report.append(f"- {sentence}")
            report.append("")
            report.append("</details>")

        report.append("---")
        report.append("")

    # Detailed sentence analysis (optional, can be collapsed)
    report.append("## 📝 Detailed Sentence Analysis")
    report.append("")
    report.append("<details>")
    report.append("<summary>Click to expand individual sentence analysis</summary>")
    report.append("")

    for i, result in enumerate(all_results, 1):
        report.append(f"### Sentence {i} ({result['file_source']})")
        report.append(f"**Input:** {result['sentence']}")
        report.append("")

        report.append("**POS-UD Relations:**")
        if result['pos_ud_tuples']:
            for pos1, pos2, ud_rel in result['pos_ud_tuples']:
                report.append(f"- {pos1} → {pos2}: {ud_rel}")
        else:
            report.append("- No UD relations found")
        report.append("")

        report.append("**POS-ROM Relations:**")
        if result['pos_rom_tuples']:
            for pos1, pos2, rom_rel in result['pos_rom_tuples']:
                report.append(f"- {pos1} → {pos2}: {rom_rel}")
        else:
            report.append("- No ROM relations found")
        report.append("")

        if i % 10 == 0:  # Add separator every 10 sentences for readability
            report.append("---")
            report.append("")

    report.append("</details>")
    report.append("")

    return "\n".join(report)


def _generate_pos_analysis_report(all_results: List[Dict], skipped_sentences: List[str],
                                  all_pos_ud_tuples: List[Tuple], all_pos_rom_tuples: List[Tuple]) -> str:
    """
    Generate a markdown formatted POS analysis report.

    Args:
        all_results: List of sentence analysis results
        skipped_sentences: List of sentences that were skipped
        all_pos_ud_tuples: All POS-UD tuples from sentences
        all_pos_rom_tuples: All POS-ROM tuples from benchmark

    Returns:
        Formatted markdown report string
    """
    report = []

    # Header
    report.append("# POS-based UD vs ROM Relations Analysis Report")
    report.append("")
    report.append(f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Total Sentences:** {len(all_results) + len(skipped_sentences)}")
    report.append(f"**Processed Sentences:** {len(all_results)}")
    report.append(f"**Skipped Sentences:** {len(skipped_sentences)}")
    report.append("")

    # Overall Statistics
    report.append("## 📊 Overall Statistics")
    report.append("")
    report.append("| Metric | Count |")
    report.append("|--------|-------|")
    report.append(f"| Total POS-UD Relations | {len(all_pos_ud_tuples)} |")
    report.append(f"| Total POS-ROM Relations | {len(all_pos_rom_tuples)} |")
    report.append("")

    # Analyze POS pairs and their relations with examples
    pos_pair_analysis = _analyze_pos_pairs_with_examples(all_results)

    # Calculate match rates
    match_statistics = _calculate_match_rates(all_pos_ud_tuples, all_pos_rom_tuples)

    # Match Rate Analysis
    report.append("## 📈 Overall Match Rate Analysis")
    report.append("")
    report.append("| Metric | Value |")
    report.append("|--------|-------|")
    report.append(f"| Unique POS Pairs in UD | {match_statistics['unique_ud_pairs']} |")
    report.append(f"| Unique POS Pairs in ROM | {match_statistics['unique_rom_pairs']} |")
    report.append(f"| Common POS Pairs | {match_statistics['common_pairs']} |")
    report.append(f"| POS Pair Overlap Rate | {match_statistics['pair_overlap_rate']:.1f}% |")
    report.append("")

    # POS Pair Analysis Section
    report.append("## 🔍 Detailed POS Pair Analysis")
    report.append("")
    report.append("This section shows for each POS pair what UD relations and ROM relations appeared.")
    report.append("")

    for pos_pair, data in sorted(pos_pair_analysis.items()):
        report.append(f"### {pos_pair[0]} → {pos_pair[1]}")
        report.append("")

        # UD Relations for this POS pair
        if data['ud_relations']:
            report.append("**UD Relations:**")
            for ud_rel, count in sorted(data['ud_relations'].items()):
                report.append(f"- {ud_rel} ({count} occurrences)")
            report.append("")

        # ROM Relations for this POS pair
        if data['rom_relations']:
            report.append("**ROM Relations:**")
            for rom_rel, count in sorted(data['rom_relations'].items()):
                report.append(f"- {rom_rel} ({count} occurrences)")
            report.append("")

        # Examples section
        report.append("**Examples:**")

        # UD Examples
        if data.get('ud_examples'):
            report.append("*UD Examples:*")
            example_count = 0
            for ud_rel, examples in data['ud_examples'].items():
                if example_count >= 4:  # Limit total examples per POS pair
                    break
                for example in examples[:2]:  # Max 2 examples per UD relation
                    if example_count >= 4:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(f"  - **{ud_rel}**: {word_pairs_str} in \"{example['sentence']}\"")
                    example_count += 1
            report.append("")

        # ROM Examples
        if data.get('rom_examples'):
            report.append("*ROM Examples:*")
            example_count = 0
            for rom_rel, examples in data['rom_examples'].items():
                if example_count >= 4:  # Limit total examples per POS pair
                    break
                for example in examples[:2]:  # Max 2 examples per ROM relation
                    if example_count >= 4:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(f"  - **{rom_rel}**: {word_pairs_str} in \"{example['sentence']}\"")
                    example_count += 1
            report.append("")

        if not data.get('ud_examples') and not data.get('rom_examples'):
            report.append("- No examples available")
            report.append("")

        # Match analysis
        report.append("**Analysis:**")
        ud_count = sum(data['ud_relations'].values())
        rom_count = sum(data['rom_relations'].values())

        report.append(f"- Total UD instances: {ud_count}")
        report.append(f"- Total ROM instances: {rom_count}")

        if ud_count > 0 and rom_count > 0:
            ratio = rom_count / ud_count
            report.append(f"- ROM/UD ratio: {ratio:.2f}")
            report.append("- **Status: Both UD and ROM relations exist for this POS pair**")
        elif ud_count > 0:
            report.append("- **Status: Only UD relations exist (no ROM coverage)**")
        elif rom_count > 0:
            report.append("- **Status: Only ROM relations exist (no UD match)**")

        report.append("")
        report.append("---")
        report.append("")

    # Summary tables
    report.append("## 📋 Summary Tables")
    report.append("")

    # UD Relations Summary
    report.append("### UD Relations Summary")
    ud_summary = defaultdict(int)
    for _, _, ud_rel in all_pos_ud_tuples:
        ud_summary[ud_rel] += 1

    report.append("| UD Relation | Count | Percentage |")
    report.append("|-------------|-------|------------|")
    total_ud = len(all_pos_ud_tuples)
    for ud_rel, count in sorted(ud_summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_ud * 100) if total_ud > 0 else 0
        report.append(f"| {ud_rel} | {count} | {percentage:.1f}% |")
    report.append("")

    # ROM Relations Summary
    report.append("### ROM Relations Summary")
    rom_summary = defaultdict(int)
    for _, _, rom_rel in all_pos_rom_tuples:
        rom_summary[rom_rel] += 1

    report.append("| ROM Relation | Count | Percentage |")
    report.append("|--------------|-------|------------|")
    total_rom = len(all_pos_rom_tuples)
    for rom_rel, count in sorted(rom_summary.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_rom * 100) if total_rom > 0 else 0
        report.append(f"| {rom_rel} | {count} | {percentage:.1f}% |")
    report.append("")

    # POS Pairs Summary
    report.append("### POS Pairs Distribution")
    pos_pair_counts = defaultdict(int)
    for pos1, pos2, _ in all_pos_ud_tuples:
        pos_pair_counts[(pos1, pos2)] += 1

    report.append("| POS Pair | UD Count | ROM Count | Status |")
    report.append("|----------|----------|-----------|--------|")

    rom_pair_counts = defaultdict(int)
    for pos1, pos2, _ in all_pos_rom_tuples:
        rom_pair_counts[(pos1, pos2)] += 1

    all_pairs = set(pos_pair_counts.keys()) | set(rom_pair_counts.keys())
    for pair in sorted(all_pairs):
        ud_count = pos_pair_counts.get(pair, 0)
        rom_count = rom_pair_counts.get(pair, 0)

        if ud_count > 0 and rom_count > 0:
            status = "Both"
        elif ud_count > 0:
            status = "UD Only"
        else:
            status = "ROM Only"

        report.append(f"| {pair[0]} → {pair[1]} | {ud_count} | {rom_count} | {status} |")
    report.append("")

    # Individual sentence details
    report.append("## 📝 Individual Sentence Analysis")
    report.append("")

    for i, result in enumerate(all_results, 1):
        report.append(f"### Sentence {i}")
        report.append(f"**Input:** {result['sentence']}")
        report.append("")

        report.append("**POS-UD Relations:**")
        if result['pos_ud_tuples']:
            for pos1, pos2, ud_rel in result['pos_ud_tuples']:
                report.append(f"- {pos1} → {pos2}: {ud_rel}")
        else:
            report.append("- No UD relations found")
        report.append("")

        report.append("**POS-ROM Relations:**")
        if result['pos_rom_tuples']:
            for pos1, pos2, rom_rel in result['pos_rom_tuples']:
                report.append(f"- {pos1} → {pos2}: {rom_rel}")
        else:
            report.append("- No ROM relations found")
        report.append("")

        report.append("<details>")
        report.append("<summary>Word-POS Mapping & Expected Relations</summary>")
        report.append("")
        report.append("**Word-POS Mapping:**")
        unique_mappings = {}
        for word, pos in result['word_to_pos'].items():
            if '_' not in word:  # Only show simple mappings
                unique_mappings[word] = pos
        for word, pos in sorted(unique_mappings.items()):
            report.append(f"- {word}: {pos}")
        report.append("")

        report.append("**Expected Relations from Benchmark:**")
        for from_word, to_word, rom_rel in result['expected_relations']:
            report.append(f"- {from_word} → {to_word}: {rom_rel}")
        report.append("")
        report.append("</details>")
        report.append("")

        report.append("---")
        report.append("")

    # Skipped sentences section
    if skipped_sentences:
        report.append("## ⚠️ Skipped Sentences")
        report.append("*(Sentences not found in benchmark)*")
        report.append("")
        for sentence in skipped_sentences:
            report.append(f"- {sentence}")
        report.append("")

    return "\n".join(report)


def _analyze_pos_pairs_with_examples(all_results: List[Dict]) -> Dict:
    """
    Analyze POS pairs and their associated UD and ROM relations with actual examples.

    Args:
        all_results: List of sentence analysis results containing POS tuples and word mappings

    Returns:
        Dictionary with POS pair analysis including examples
    """
    analysis = defaultdict(lambda: {
        'ud_relations': defaultdict(int),
        'rom_relations': defaultdict(int),
        'ud_examples': defaultdict(list),
        'rom_examples': defaultdict(list)
    })

    # Initialize Stanza pipeline once for efficiency
    import stanza
    nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse', verbose=False)

    for result in all_results:
        sentence = result['sentence']

        # Re-parse sentence to get word-level UD relations for examples
        # This is needed because we need to map POS tuples back to actual words
        doc = nlp(sentence)

        # Create mapping from POS tuples to actual word pairs
        ud_word_examples = {}
        for sent in doc.sentences:
            for word in sent.words:
                if word.head != 0:
                    head_word = sent.words[word.head - 1]
                    pos_tuple = (head_word.upos, word.upos, word.deprel)
                    word_pair = f"{head_word.text} → {word.text}"

                    if pos_tuple not in ud_word_examples:
                        ud_word_examples[pos_tuple] = []
                    if len(ud_word_examples[pos_tuple]) < 3:  # Limit stored examples
                        ud_word_examples[pos_tuple].append(word_pair)

        # Process UD relations with examples
        for pos1, pos2, ud_rel in result['pos_ud_tuples']:
            pos_pair = (pos1, pos2)
            analysis[pos_pair]['ud_relations'][ud_rel] += 1

            # Find actual word examples for this POS-UD combination
            word_examples = ud_word_examples.get((pos1, pos2, ud_rel), [])

            if word_examples and len(analysis[pos_pair]['ud_examples'][ud_rel]) < 2:
                example_info = {
                    'sentence': sentence,
                    'word_pairs': word_examples[:2],  # Limit to 2 word pairs
                    'pos_pair': f"{pos1} → {pos2}",
                    'ud_relation': ud_rel,
                    'file_source': result.get('file_source', 'unknown')
                }
                analysis[pos_pair]['ud_examples'][ud_rel].append(example_info)

        # Process ROM relations with examples
        for pos1, pos2, rom_rel in result['pos_rom_tuples']:
            pos_pair = (pos1, pos2)
            analysis[pos_pair]['rom_relations'][rom_rel] += 1

            # Find actual word examples from expected relations
            matching_word_pairs = []
            for from_word, to_word, expected_rom_rel in result['expected_relations']:
                if expected_rom_rel == rom_rel:
                    from_pos = result['word_to_pos'].get(from_word.lower())
                    to_pos = result['word_to_pos'].get(to_word.lower())
                    if from_pos == pos1 and to_pos == pos2:
                        matching_word_pairs.append(f"{from_word} → {to_word}")
                        if len(matching_word_pairs) >= 2:  # Limit to 2 examples
                            break

            if matching_word_pairs and len(analysis[pos_pair]['rom_examples'][rom_rel]) < 2:
                example_info = {
                    'sentence': sentence,
                    'word_pairs': matching_word_pairs,
                    'pos_pair': f"{pos1} → {pos2}",
                    'rom_relation': rom_rel,
                    'file_source': result.get('file_source', 'unknown')
                }
                analysis[pos_pair]['rom_examples'][rom_rel].append(example_info)

    return dict(analysis)


def _analyze_pos_pairs(pos_ud_tuples: List[Tuple], pos_rom_tuples: List[Tuple]) -> Dict:
    """
    Analyze POS pairs and their associated UD and ROM relations.

    Args:
        pos_ud_tuples: List of (POS1, POS2, UD_relation) tuples
        pos_rom_tuples: List of (POS1, POS2, ROM_relation) tuples

    Returns:
        Dictionary with POS pair analysis
    """
    analysis = defaultdict(lambda: {'ud_relations': defaultdict(int), 'rom_relations': defaultdict(int)})

    # Count UD relations by POS pair
    for pos1, pos2, ud_rel in pos_ud_tuples:
        pos_pair = (pos1, pos2)
        analysis[pos_pair]['ud_relations'][ud_rel] += 1

    # Count ROM relations by POS pair
    for pos1, pos2, rom_rel in pos_rom_tuples:
        pos_pair = (pos1, pos2)
        analysis[pos_pair]['rom_relations'][rom_rel] += 1

    return dict(analysis)


def _calculate_match_rates(pos_ud_tuples: List[Tuple], pos_rom_tuples: List[Tuple]) -> Dict:
    """
    Calculate various match rate statistics between UD and ROM relations.

    Args:
        pos_ud_tuples: List of (POS1, POS2, UD_relation) tuples
        pos_rom_tuples: List of (POS1, POS2, ROM_relation) tuples

    Returns:
        Dictionary with match statistics
    """
    # Get unique POS pairs
    ud_pairs = set((pos1, pos2) for pos1, pos2, _ in pos_ud_tuples)
    rom_pairs = set((pos1, pos2) for pos1, pos2, _ in pos_rom_tuples)

    # Calculate overlap
    common_pairs = ud_pairs & rom_pairs
    total_unique_pairs = len(ud_pairs | rom_pairs)

    # Calculate rates
    pair_overlap_rate = (len(common_pairs) / total_unique_pairs * 100) if total_unique_pairs > 0 else 0

    return {
        'unique_ud_pairs': len(ud_pairs),
        'unique_rom_pairs': len(rom_pairs),
        'common_pairs': len(common_pairs),
        'total_unique_pairs': total_unique_pairs,
        'pair_overlap_rate': pair_overlap_rate
    }
