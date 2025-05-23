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

            # Extract POS-ROM tuples from benchmark (normalize case)
            pos_rom_tuples = []
            for from_word, to_word, rom_relation in expected_relations:
                from_pos = word_to_pos.get(from_word.lower())
                to_pos = word_to_pos.get(to_word.lower())
                if from_pos and to_pos:
                    # Normalize ROM relation to title case for consistent processing
                    normalized_rom_relation = rom_relation.strip().title()
                    pos_rom_tuple = (from_pos, to_pos, normalized_rom_relation)
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

        # Extract POS-ROM tuples from benchmark (normalize case)
        pos_rom_tuples = []
        for from_word, to_word, rom_relation in expected_relations:
            from_pos = word_to_pos.get(from_word.lower())
            to_pos = word_to_pos.get(to_word.lower())
            if from_pos and to_pos:
                # Normalize ROM relation to title case for consistent processing
                normalized_rom_relation = rom_relation.strip().title()
                # Create tuple as (from_POS, to_POS, ROM_relation) following benchmark direction
                pos_rom_tuple = (from_pos, to_pos, normalized_rom_relation)
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

    # Calculate match rates with overlap analysis
    match_statistics = _calculate_match_rates(all_pos_ud_tuples, all_pos_rom_tuples)

    # Calculate overall overlap rates
    overall_overlap_1, overall_overlap_2, overall_max_overlap = _calculate_global_overlap_rates(all_pos_rom_tuples,
                                                                                                all_pos_ud_tuples)

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
    report.append("### Global Overlap Rates (Mathematical Formula)")
    report.append("| Pattern | Overlap Rate | Description |")
    report.append("|---------|--------------|-------------|")
    report.append(
        f"| Forward Matching (Pattern 1) | {overall_overlap_1:.3f} | ROM pairs match UD pairs in same direction |")
    report.append(
        f"| Reverse Matching (Pattern 2) | {overall_overlap_2:.3f} | ROM pairs match UD pairs in reverse direction |")
    report.append(
        f"| **Maximum Overall Overlap** | **{overall_max_overlap:.3f}** | **Best matching pattern globally** |")
    report.append("")

    # Enhanced bidirectional POS Pair Analysis Section
    report.append("## 🔍 Detailed POS Pair Analysis (Combined) - Bidirectional")
    report.append("")
    report.append(
        "This section shows bidirectional POS pair analysis with overlap rates calculated using mathematical formula:")
    report.append("**overlap_rate_k = (∑_{i ∈ M_k} 1(R_i = U_{j(i)})) / |M_k|**")
    report.append("- Pattern 1 (Forward): M₁ = {i : ∃j, (A_i, B_i) = (A_j', B_j')}")
    report.append("- Pattern 2 (Reverse): M₂ = {i : ∃j, (A_i, B_i) = (B_j', A_j')}")
    report.append("- **Max Overlap Rate = max{overlap_rate_1, overlap_rate_2}**")
    report.append("Blocks are sorted by maximum overlap rate (highest first).")
    report.append("")

    # Group bidirectional pairs and calculate ratios
    bidirectional_groups = _group_bidirectional_pairs(pos_pair_analysis, all_pos_ud_tuples, all_pos_rom_tuples)

    for group_data in bidirectional_groups:
        canonical_key = group_data['canonical_key']
        pos1, pos2 = canonical_key
        forward_data = group_data['forward_data']
        reverse_data = group_data['reverse_data']
        forward_ratio = group_data['forward_ratio']
        reverse_ratio = group_data['reverse_ratio']
        cross_ratio = group_data['cross_ratio']
        reverse_cross_ratio = group_data['reverse_cross_ratio']
        forward_overlap_1 = group_data['forward_overlap_1']
        forward_overlap_2 = group_data['forward_overlap_2']
        forward_max_overlap = group_data['forward_max_overlap']
        reverse_overlap_1 = group_data['reverse_overlap_1']
        reverse_overlap_2 = group_data['reverse_overlap_2']
        reverse_max_overlap = group_data['reverse_max_overlap']
        overall_max_overlap = group_data['overall_max_overlap']

        report.append(f"### {pos1} ↔ {pos2} (Max Overlap Rate: {overall_max_overlap:.3f})")
        report.append("")

        # Forward direction (A → B)
        report.append(f"#### {pos1} → {pos2}")
        if forward_data.get('ud_relations'):
            report.append("**UD Relations:**")
            for ud_rel, count in sorted(forward_data['ud_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {ud_rel} ({count} occurrences)")
            report.append("")

        if forward_data.get('rom_relations'):
            report.append("**ROM Relations:**")
            for rom_rel, count in sorted(forward_data['rom_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {rom_rel} ({count} occurrences)")
            report.append("")

        # Reverse direction (B → A)
        report.append(f"#### {pos2} → {pos1}")
        if reverse_data.get('ud_relations'):
            report.append("**UD Relations:**")
            for ud_rel, count in sorted(reverse_data['ud_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {ud_rel} ({count} occurrences)")
            report.append("")

        if reverse_data.get('rom_relations'):
            report.append("**ROM Relations:**")
            for rom_rel, count in sorted(reverse_data['rom_relations'].items(), key=lambda x: x[1], reverse=True):
                report.append(f"- {rom_rel} ({count} occurrences)")
            report.append("")

        # Examples section (combined from both directions)
        report.append("**Examples:**")

        # Forward UD Examples
        if forward_data.get('ud_examples'):
            report.append(f"*{pos1}→{pos2} UD Examples:*")
            example_count = 0
            for ud_rel, examples in forward_data['ud_examples'].items():
                if example_count >= 3:
                    break
                for example in examples[:1]:  # 1 example per UD relation
                    if example_count >= 3:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{ud_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        # Forward ROM Examples
        if forward_data.get('rom_examples'):
            report.append(f"*{pos1}→{pos2} ROM Examples:*")
            example_count = 0
            for rom_rel, examples in forward_data['rom_examples'].items():
                if example_count >= 3:
                    break
                for example in examples[:1]:  # 1 example per ROM relation
                    if example_count >= 3:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{rom_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        # Reverse UD Examples
        if reverse_data.get('ud_examples'):
            report.append(f"*{pos2}→{pos1} UD Examples:*")
            example_count = 0
            for ud_rel, examples in reverse_data['ud_examples'].items():
                if example_count >= 3:
                    break
                for example in examples[:1]:  # 1 example per UD relation
                    if example_count >= 3:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{ud_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        # Reverse ROM Examples
        if reverse_data.get('rom_examples'):
            report.append(f"*{pos2}→{pos1} ROM Examples:*")
            example_count = 0
            for rom_rel, examples in reverse_data['rom_examples'].items():
                if example_count >= 3:
                    break
                for example in examples[:1]:  # 1 example per ROM relation
                    if example_count >= 3:
                        break
                    word_pairs_str = ", ".join(example['word_pairs']) if example[
                        'word_pairs'] else "word pairs not identified"
                    report.append(
                        f"  - **{rom_rel}**: {word_pairs_str} in \"{example['sentence']}\" ({example.get('file_source', 'unknown')})")
                    example_count += 1
            report.append("")

        # Comprehensive analysis with overlap rates
        report.append("**Mathematical Overlap Analysis:**")
        forward_ud_count = sum(forward_data.get('ud_relations', {}).values())
        forward_rom_count = sum(forward_data.get('rom_relations', {}).values())
        reverse_ud_count = sum(reverse_data.get('ud_relations', {}).values())
        reverse_rom_count = sum(reverse_data.get('rom_relations', {}).values())

        report.append(f"- {pos1}→{pos2}: {forward_ud_count} UD, {forward_rom_count} ROM")
        report.append(f"- {pos2}→{pos1}: {reverse_ud_count} UD, {reverse_rom_count} ROM")
        report.append("")
        report.append("**Overlap Rates (Mathematical Formula):**")
        report.append(f"- {pos1}→{pos2} Pattern 1 (Forward): {forward_overlap_1:.3f}")
        report.append(f"- {pos1}→{pos2} Pattern 2 (Reverse): {forward_overlap_2:.3f}")
        report.append(f"- {pos1}→{pos2} Max Overlap: {forward_max_overlap:.3f}")
        report.append(f"- {pos2}→{pos1} Pattern 1 (Forward): {reverse_overlap_1:.3f}")
        report.append(f"- {pos2}→{pos1} Pattern 2 (Reverse): {reverse_overlap_2:.3f}")
        report.append(f"- {pos2}→{pos1} Max Overlap: {reverse_max_overlap:.3f}")
        report.append(f"- **Overall Maximum Overlap Rate: {overall_max_overlap:.3f}**")
        report.append("")
        report.append("**Traditional Ratios (for reference):**")
        report.append(f"- Forward ROM/UD ratio: {forward_ratio:.2f}")
        report.append(f"- Reverse ROM/UD ratio: {reverse_ratio:.2f}")
        report.append(f"- Cross ratio ({pos1}→{pos2} UD)/({pos2}→{pos1} ROM): {cross_ratio:.2f}")
        report.append(f"- Reverse cross ratio ({pos2}→{pos1} UD)/({pos1}→{pos2} ROM): {reverse_cross_ratio:.2f}")

        # Status analysis
        if forward_ud_count > 0 and forward_rom_count > 0 and reverse_ud_count > 0 and reverse_rom_count > 0:
            report.append("- **Status: Full bidirectional coverage (both directions have UD and ROM relations)**")
        elif (forward_ud_count > 0 or forward_rom_count > 0) and (reverse_ud_count > 0 or reverse_rom_count > 0):
            report.append("- **Status: Partial bidirectional coverage**")
        else:
            report.append("- **Status: Unidirectional coverage only**")

        # Overlap rate interpretation
        if overall_max_overlap >= 0.8:
            overlap_status = "🟢 Excellent overlap"
        elif overall_max_overlap >= 0.6:
            overlap_status = "🟡 Good overlap"
        elif overall_max_overlap >= 0.3:
            overlap_status = "🟠 Moderate overlap"
        elif overall_max_overlap > 0:
            overlap_status = "🔴 Low overlap"
        else:
            overlap_status = "⚫ No overlap"

        report.append(f"- **Overlap Assessment: {overlap_status}**")

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
        # Normalize case for consistent grouping
        normalized_rom_rel = rom_rel.strip().title()
        rom_summary[normalized_rom_rel] += 1

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
    for pos1, pos2, rom_rel in all_pos_rom_tuples:
        # Note: ROM relations are already normalized during tuple creation
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
            # Normalize case for consistent grouping
            normalized_rom_rel = rom_rel.strip().title()
            file_rom_summary[normalized_rom_rel] += 1

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


def _group_bidirectional_pairs(pos_pair_analysis: Dict, all_pos_ud_tuples: List[Tuple],
                               all_pos_rom_tuples: List[Tuple]) -> List[Dict]:
    """
    Group POS pairs into bidirectional pairs and calculate overlap rates using cross ratios.

    The overlap rate is now calculated as the maximum of cross ratios:
    - Cross ratio = min(1.0, forward_ud_count / reverse_rom_count)
    - Reverse cross ratio = min(1.0, reverse_ud_count / forward_rom_count)
    - Max Overlap Rate = max(cross_ratio, reverse_cross_ratio)

    Args:
        pos_pair_analysis: Dictionary with POS pair analysis
        all_pos_ud_tuples: All POS-UD tuples (S₂)
        all_pos_rom_tuples: All POS-ROM tuples (S₁)

    Returns:
        List of dictionaries with bidirectional group data, sorted by max overlap rate
    """
    bidirectional_groups = {}

    # Group pairs into bidirectional sets
    for pos_pair, data in pos_pair_analysis.items():
        canonical_key = tuple(sorted([pos_pair[0], pos_pair[1]]))
        if canonical_key not in bidirectional_groups:
            bidirectional_groups[canonical_key] = {}
        bidirectional_groups[canonical_key][pos_pair] = data

    # Calculate overlap rates and prepare sorting data
    group_data_list = []

    for canonical_key, pair_data in bidirectional_groups.items():
        pos1, pos2 = canonical_key

        # Get data for both directions
        forward_data = pair_data.get((pos1, pos2), {'ud_relations': {}, 'rom_relations': {}})
        reverse_data = pair_data.get((pos2, pos1), {'ud_relations': {}, 'rom_relations': {}})

        # Calculate counts
        forward_ud_count = sum(forward_data.get('ud_relations', {}).values())
        forward_rom_count = sum(forward_data.get('rom_relations', {}).values())
        reverse_ud_count = sum(reverse_data.get('ud_relations', {}).values())
        reverse_rom_count = sum(reverse_data.get('rom_relations', {}).values())

        # Calculate traditional ratios for backward compatibility
        forward_ratio = forward_rom_count / forward_ud_count if forward_ud_count > 0 else 0
        reverse_ratio = reverse_rom_count / reverse_ud_count if reverse_ud_count > 0 else 0
        cross_ratio = forward_ud_count / reverse_rom_count if reverse_rom_count > 0 else 0
        reverse_cross_ratio = reverse_ud_count / forward_rom_count if forward_rom_count > 0 else 0

        # NEW OVERLAP CALCULATION: Use cross ratios capped at 1.0
        # This measures structural alignment between UD and ROM patterns
        cross_alignment = min(1.0, cross_ratio) if reverse_rom_count > 0 else 0
        reverse_cross_alignment = min(1.0, reverse_cross_ratio) if forward_rom_count > 0 else 0

        # The maximum overlap rate is the best structural alignment
        max_overlap_rate = max(cross_alignment, reverse_cross_alignment)

        # For individual direction analysis, calculate direct alignment rates
        forward_direct_alignment = min(1.0, forward_rom_count / forward_ud_count) if forward_ud_count > 0 else 0
        reverse_direct_alignment = min(1.0, reverse_rom_count / reverse_ud_count) if reverse_ud_count > 0 else 0

        # Calculate per-direction max overlap (combining direct and cross alignments)
        forward_max_overlap = max(forward_direct_alignment, cross_alignment)
        reverse_max_overlap = max(reverse_direct_alignment, reverse_cross_alignment)

        # Overall maximum overlap rate for this bidirectional pair
        overall_max_overlap = max_overlap_rate

        group_data_list.append({
            'canonical_key': canonical_key,
            'forward_data': forward_data,
            'reverse_data': reverse_data,
            'forward_ratio': forward_ratio,
            'reverse_ratio': reverse_ratio,
            'cross_ratio': cross_ratio,
            'reverse_cross_ratio': reverse_cross_ratio,
            'forward_overlap_1': forward_direct_alignment,  # Renamed for clarity
            'forward_overlap_2': cross_alignment,  # Cross alignment for forward direction
            'forward_max_overlap': forward_max_overlap,
            'reverse_overlap_1': reverse_direct_alignment,  # Direct alignment for reverse direction
            'reverse_overlap_2': reverse_cross_alignment,  # Cross alignment for reverse direction
            'reverse_max_overlap': reverse_max_overlap,
            'overall_max_overlap': overall_max_overlap,
            'max_ratio': overall_max_overlap  # Use overlap rate as sorting criterion
        })

    # Sort by overall max overlap rate (descending)
    group_data_list.sort(key=lambda x: x['overall_max_overlap'], reverse=True)

    return group_data_list


def _calculate_global_overlap_rates(rom_data: List[Tuple], ud_data: List[Tuple]) -> Tuple[float, float, float]:
    """
    Calculate global overlap rates using cross ratio approach.

    Args:
        rom_data: List of (A_i, B_i, R_i) tuples from ROM data (S₁)
        ud_data: List of (A_j', B_j', U_j) tuples from UD data (S₂)

    Returns:
        Tuple of (cross_alignment, reverse_cross_alignment, max_global_overlap_rate)
    """
    if not rom_data or not ud_data:
        return 0.0, 0.0, 0.0

    # Count by direction
    rom_forward_count = {}
    rom_reverse_count = {}
    ud_forward_count = {}
    ud_reverse_count = {}

    # Count ROM relations by direction
    for a, b, r in rom_data:
        pair_key = (a, b)
        rom_forward_count[pair_key] = rom_forward_count.get(pair_key, 0) + 1

        reverse_pair_key = (b, a)
        rom_reverse_count[reverse_pair_key] = rom_reverse_count.get(reverse_pair_key, 0) + 1

    # Count UD relations by direction
    for a, b, u in ud_data:
        pair_key = (a, b)
        ud_forward_count[pair_key] = ud_forward_count.get(pair_key, 0) + 1

        reverse_pair_key = (b, a)
        ud_reverse_count[reverse_pair_key] = ud_reverse_count.get(reverse_pair_key, 0) + 1

    # Calculate cross alignments
    total_cross_alignment = 0
    total_reverse_cross_alignment = 0
    cross_pairs = 0
    reverse_cross_pairs = 0

    all_pairs = set(rom_forward_count.keys()) | set(ud_forward_count.keys())

    for pair in all_pairs:
        rom_forward = rom_forward_count.get(pair, 0)
        ud_forward = ud_forward_count.get(pair, 0)

        reverse_pair = (pair[1], pair[0])
        rom_reverse = rom_reverse_count.get(pair, 0)  # This is rom_forward_count for reverse_pair
        ud_reverse = ud_reverse_count.get(pair, 0)  # This is ud_forward_count for reverse_pair

        # Cross alignment: UD forward vs ROM reverse
        if rom_reverse > 0:
            cross_alignment = min(1.0, ud_forward / rom_reverse)
            total_cross_alignment += cross_alignment
            cross_pairs += 1

        # Reverse cross alignment: UD reverse vs ROM forward
        if rom_forward > 0:
            reverse_cross_alignment = min(1.0, ud_reverse / rom_forward)
            total_reverse_cross_alignment += reverse_cross_alignment
            reverse_cross_pairs += 1

    global_cross_alignment = total_cross_alignment / cross_pairs if cross_pairs > 0 else 0.0
    global_reverse_cross_alignment = total_reverse_cross_alignment / reverse_cross_pairs if reverse_cross_pairs > 0 else 0.0
    max_global_overlap_rate = max(global_cross_alignment, global_reverse_cross_alignment)

    return global_cross_alignment, global_reverse_cross_alignment, max_global_overlap_rate


def _calculate_overlap_rates(rom_data: List[Tuple], ud_data: List[Tuple], pos1: str, pos2: str) -> Tuple[
    float, float, float]:
    """
    Calculate overlap rates using cross ratio approach for a specific POS pair.

    Args:
        rom_data: List of (A_i, B_i, R_i) tuples from ROM data (S₁)
        ud_data: List of (A_j', B_j', U_j) tuples from UD data (S₂)
        pos1: First POS tag of the canonical pair
        pos2: Second POS tag of the canonical pair

    Returns:
        Tuple of (direct_alignment, cross_alignment, max_overlap_rate)
    """
    # Count relations for this specific POS pair in both directions
    rom_forward_count = sum(1 for a, b, r in rom_data if (a, b) == (pos1, pos2))
    rom_reverse_count = sum(1 for a, b, r in rom_data if (a, b) == (pos2, pos1))
    ud_forward_count = sum(1 for a, b, u in ud_data if (a, b) == (pos1, pos2))
    ud_reverse_count = sum(1 for a, b, u in ud_data if (a, b) == (pos2, pos1))

    # Direct alignment: same direction
    direct_alignment = min(1.0, rom_forward_count / ud_forward_count) if ud_forward_count > 0 else 0

    # Cross alignment: opposite directions
    cross_alignment = min(1.0, ud_forward_count / rom_reverse_count) if rom_reverse_count > 0 else 0

    # Max alignment for this POS pair
    max_overlap_rate = max(direct_alignment, cross_alignment)

    return direct_alignment, cross_alignment, max_overlap_rate


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

    # Calculate match rates with overlap analysis
    match_statistics = _calculate_match_rates(all_pos_ud_tuples, all_pos_rom_tuples)

    # Calculate overall overlap rates
    overall_overlap_1, overall_overlap_2, overall_max_overlap = _calculate_global_overlap_rates(all_pos_rom_tuples,
                                                                                                all_pos_ud_tuples)

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
    report.append("### Global Overlap Rates (Mathematical Formula)")
    report.append("| Pattern | Overlap Rate | Description |")
    report.append("|---------|--------------|-------------|")
    report.append(
        f"| Forward Matching (Pattern 1) | {overall_overlap_1:.3f} | ROM pairs match UD pairs in same direction |")
    report.append(
        f"| Reverse Matching (Pattern 2) | {overall_overlap_2:.3f} | ROM pairs match UD pairs in reverse direction |")
    report.append(
        f"| **Maximum Overall Overlap** | **{overall_max_overlap:.3f}** | **Best matching pattern globally** |")
    report.append("")

    # POS Pair Analysis Section with Mathematical Overlap Rates
    report.append("## 🔍 Detailed POS Pair Analysis")
    report.append("")
    report.append("This section shows for each POS pair what UD relations and ROM relations appeared.")
    report.append("Overlap rates are calculated using the mathematical formula:")
    report.append("**overlap_rate_k = (∑_{i ∈ M_k} 1(R_i = U_{j(i)})) / |M_k|**")
    report.append("")

    # Create a list of pos pairs with their overlap rates for sorting
    pos_pairs_with_overlap = []
    for pos_pair, data in pos_pair_analysis.items():
        pos1, pos2 = pos_pair
        overlap_rate_1, overlap_rate_2, max_overlap_rate = _calculate_overlap_rates(
            all_pos_rom_tuples, all_pos_ud_tuples, pos1, pos2
        )
        pos_pairs_with_overlap.append((pos_pair, data, overlap_rate_1, overlap_rate_2, max_overlap_rate))

    # Sort by max overlap rate (descending)
    pos_pairs_with_overlap.sort(key=lambda x: x[4], reverse=True)

    for pos_pair, data, overlap_rate_1, overlap_rate_2, max_overlap_rate in pos_pairs_with_overlap:
        report.append(f"### {pos_pair[0]} → {pos_pair[1]} (Max Overlap Rate: {max_overlap_rate:.3f})")
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

        # Match analysis with overlap rates
        report.append("**Analysis:**")
        ud_count = sum(data['ud_relations'].values())
        rom_count = sum(data['rom_relations'].values())

        report.append(f"- Total UD instances: {ud_count}")
        report.append(f"- Total ROM instances: {rom_count}")

        # Add overlap rate analysis
        report.append("")
        report.append("**Overlap Rate Analysis:**")
        report.append(f"- Pattern 1 (Forward Matching): {overlap_rate_1:.3f}")
        report.append(f"- Pattern 2 (Reverse Matching): {overlap_rate_2:.3f}")
        report.append(f"- **Maximum Overlap Rate: {max_overlap_rate:.3f}**")

        if ud_count > 0 and rom_count > 0:
            ratio = rom_count / ud_count
            report.append(f"- Traditional ROM/UD ratio: {ratio:.2f}")
            report.append("- **Status: Both UD and ROM relations exist for this POS pair**")
        elif ud_count > 0:
            report.append("- **Status: Only UD relations exist (no ROM coverage)**")
        elif rom_count > 0:
            report.append("- **Status: Only ROM relations exist (no UD match)**")

        # Overlap rate interpretation
        if max_overlap_rate >= 0.8:
            overlap_status = "🟢 Excellent overlap"
        elif max_overlap_rate >= 0.6:
            overlap_status = "🟡 Good overlap"
        elif max_overlap_rate >= 0.3:
            overlap_status = "🟠 Moderate overlap"
        elif max_overlap_rate > 0:
            overlap_status = "🔴 Low overlap"
        else:
            overlap_status = "⚫ No overlap"

        report.append(f"- **Overlap Assessment: {overlap_status}**")

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
        # Normalize case for consistent grouping
        normalized_rom_rel = rom_rel.strip().title()
        rom_summary[normalized_rom_rel] += 1

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
    for pos1, pos2, rom_rel in all_pos_rom_tuples:
        # Note: ROM relations are already normalized during tuple creation
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

        # Process ROM relations with examples (normalize case)
        for pos1, pos2, rom_rel in result['pos_rom_tuples']:
            pos_pair = (pos1, pos2)
            # Normalize ROM relation to title case for consistent grouping
            normalized_rom_rel = rom_rel.strip().title()
            analysis[pos_pair]['rom_relations'][normalized_rom_rel] += 1

            # Find actual word examples from expected relations
            matching_word_pairs = []
            for from_word, to_word, expected_rom_rel in result['expected_relations']:
                # Normalize both for comparison
                if expected_rom_rel.strip().title() == normalized_rom_rel:
                    from_pos = result['word_to_pos'].get(from_word.lower())
                    to_pos = result['word_to_pos'].get(to_word.lower())
                    if from_pos == pos1 and to_pos == pos2:
                        matching_word_pairs.append(f"{from_word} → {to_word}")
                        if len(matching_word_pairs) >= 2:  # Limit to 2 examples
                            break

            if matching_word_pairs and len(analysis[pos_pair]['rom_examples'][normalized_rom_rel]) < 2:
                example_info = {
                    'sentence': sentence,
                    'word_pairs': matching_word_pairs,
                    'pos_pair': f"{pos1} → {pos2}",
                    'rom_relation': normalized_rom_rel,
                    'file_source': result.get('file_source', 'unknown')
                }
                analysis[pos_pair]['rom_examples'][normalized_rom_rel].append(example_info)

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
