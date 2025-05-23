"""
Utility functions for ROM Generator

This module provides helper functions for reading input files, saving ROM analysis results,
and evaluating ROM generator performance against benchmark data.
"""

from typing import List, Dict, Any
import logging

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


def save_rom_results_to_txt(rom_results_list: List[List[Dict[str, Any]]],
                            output_filepath: str,
                            sentences: List[str] = None) -> None:
    """
    Save a list of ROM results into a .txt file with formatted output.

    Args:
        rom_results_list: List of ROM analysis results, where each element is a list
                         of relation dictionaries (as returned by analyze_sentence)
        output_filepath: Path where the output .txt file will be saved
        sentences: Optional list of original sentences for reference in output

    Raises:
        IOError: If there's an error writing to the file
    """
    try:
        with open(output_filepath, 'w', encoding='utf-8') as file:
            for i, relations in enumerate(rom_results_list, 1):
                # Write sentence header
                if sentences and i <= len(sentences):
                    file.write(f"Sentence {i}: {sentences[i - 1]}\n")
                else:
                    file.write(f"Sentence {i}:\n")

                # Write ROM relations using the same format as print_relations
                if relations:
                    for relation in relations:
                        from_word = relation["from"]
                        to_word = relation["to"]
                        rom_relation = relation["rom relation"]
                        stanza_ud = relation["stanza ud"]
                        file.write(f"  {from_word} → {to_word}: {rom_relation} (UD: {stanza_ud})\n")
                else:
                    file.write("  No ROM relations found.\n")

                # Add blank line between sentences
                file.write("\n")

        print(f"ROM results saved to: {output_filepath}")

    except IOError as e:
        raise IOError(f"Error writing to file {output_filepath}: {e}")


def format_rom_relations(relations: List[Dict[str, Any]]) -> str:
    """
    Format ROM relations into a string representation.

    Args:
        relations: List of relation dictionaries from analyze_sentence

    Returns:
        Formatted string representation of the relations
    """
    if not relations:
        return "  No ROM relations found."

    formatted_lines = []
    for relation in relations:
        from_word = relation["from"]
        to_word = relation["to"]
        rom_relation = relation["rom relation"]
        stanza_ud = relation["stanza ud"]
        formatted_lines.append(f"  {from_word} → {to_word}: {rom_relation} (UD: {stanza_ud})")

    return "\n".join(formatted_lines)


def evaluate_rom(sentences: List[str], benchmark: str, save: str = None, log: bool = False) -> tuple:
    """
    Evaluate ROM generator results against benchmark data for multiple sentences.

    Args:
        sentences: List of input sentences to analyze
        benchmark: Path to the benchmark .md file containing expected relations
        save: Optional path to save the evaluation report as a markdown file
        log: Whether to print the report to console (default: False)

    Returns:
        tuple: (correct_rate, missing_rate, over_spec_rate) as percentages (0-100) for all sentences combined

    Raises:
        FileNotFoundError: If the benchmark file doesn't exist
        IOError: If there's an error reading the benchmark file or writing the report
    """
    from rom_generator import ROMGenerator
    import re

    # Read benchmark file
    try:
        with open(benchmark, 'r', encoding='utf-8') as file:
            benchmark_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Benchmark file not found: {benchmark}")
    except IOError as e:
        raise IOError(f"Error reading benchmark file {benchmark}: {e}")

    # Initialize ROM generator
    rom_gen = ROMGenerator(lang='en', verbose=False)

    # Collect results for all sentences
    all_results = []
    total_correct = 0
    total_missing = 0
    total_over_spec = 0
    total_expected = 0
    total_generated = 0
    processed_count = 0
    skipped_sentences = []

    # Process each sentence
    for sentence in sentences:
        # Check if sentence exists in benchmark
        expected_relations = _parse_benchmark_relations(sentence, benchmark_content)

        if not expected_relations:
            # Sentence not found in benchmark, skip it
            skipped_sentences.append(sentence)
            continue

        # Generate relations for the input sentence
        generated_relations = rom_gen.analyze_sentence(sentence)

        # Normalize relations to comparable format: (from_word, to_word, relation_type)
        def normalize_relation(from_word, to_word, relation_type):
            return (from_word.lower().strip(), to_word.lower().strip(), relation_type.lower().strip())

        # Convert generated relations to normalized tuples
        generated_set = set()
        for rel in generated_relations:
            normalized = normalize_relation(rel["from"], rel["to"], rel["rom relation"])
            generated_set.add(normalized)

        # Convert expected relations to normalized tuples
        expected_set = set()
        for rel in expected_relations:
            normalized = normalize_relation(rel[0], rel[1], rel[2])
            expected_set.add(normalized)

        # Calculate metrics for this sentence
        correct_relations = generated_set & expected_set
        missing_relations = expected_set - generated_set
        over_spec_relations = generated_set - expected_set

        # Store results for this sentence
        sentence_result = {
            'sentence': sentence,
            'expected_count': len(expected_set),
            'generated_count': len(generated_set),
            'correct_count': len(correct_relations),
            'missing_count': len(missing_relations),
            'over_spec_count': len(over_spec_relations),
            'correct_relations': correct_relations,
            'missing_relations': missing_relations,
            'over_spec_relations': over_spec_relations,
            'expected_set': expected_set,
            'generated_set': generated_set
        }
        all_results.append(sentence_result)

        # Add to totals
        total_expected += len(expected_set)
        total_generated += len(generated_set)
        total_correct += len(correct_relations)
        total_missing += len(missing_relations)
        total_over_spec += len(over_spec_relations)
        processed_count += 1

    # Calculate overall rates
    if total_expected == 0:
        correct_rate = 0.0
        missing_rate = 0.0
    else:
        correct_rate = (total_correct / total_expected) * 100
        missing_rate = (total_missing / total_expected) * 100

    if total_generated == 0:
        over_spec_rate = 0.0
    else:
        over_spec_rate = (total_over_spec / total_generated) * 100

    # Generate markdown report
    report = _generate_markdown_report(all_results, skipped_sentences,
                                       total_expected, total_generated, total_correct,
                                       total_missing, total_over_spec, processed_count,
                                       correct_rate, missing_rate, over_spec_rate)

    # Print report to console only if log is True
    if log:
        print(report)

    # Save report if path provided
    if save:
        try:
            with open(save, 'w', encoding='utf-8') as file:
                file.write(report)
                logging.info(f"\nReport saved to: {save}")
        except IOError as e:
            raise IOError(f"Error writing report to file {save}: {e}")

    return correct_rate, missing_rate, over_spec_rate


def _generate_markdown_report(all_results: List[Dict], skipped_sentences: List[str],
                              total_expected: int, total_generated: int, total_correct: int,
                              total_missing: int, total_over_spec: int, processed_count: int,
                              correct_rate: float, missing_rate: float, over_spec_rate: float) -> str:
    """
    Generate a markdown formatted evaluation report.

    Args:
        all_results: List of sentence evaluation results
        skipped_sentences: List of sentences that were skipped
        total_expected, total_generated, total_correct, total_missing, total_over_spec: Total counts
        processed_count: Number of sentences processed
        correct_rate, missing_rate, over_spec_rate: Overall rates

    Returns:
        Formatted markdown report string
    """
    report = []

    # Header
    report.append("# ROM Evaluation Report")
    report.append("")
    report.append(f"**Date:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Total Sentences:** {len(all_results) + len(skipped_sentences)}")
    report.append(f"**Processed Sentences:** {processed_count}")
    report.append(f"**Skipped Sentences:** {len(skipped_sentences)}")
    report.append("")

    # MOVED UP: Total metrics at the top
    report.append("## 📊 Overall Performance Metrics")
    report.append("")

    # Summary Statistics
    report.append("### Summary Statistics")
    report.append("| Metric | Value |")
    report.append("|--------|-------|")
    report.append(f"| Total Sentences Processed | {processed_count} |")
    report.append(f"| Total Expected Relations | {total_expected} |")
    report.append(f"| Total Generated Relations | {total_generated} |")
    report.append(f"| Total Correct Relations | {total_correct} |")
    report.append(f"| Total Missing Relations | {total_missing} |")
    report.append(f"| Total Over-specified Relations | {total_over_spec} |")
    report.append("")

    # Overall Performance
    report.append("### Overall Performance")
    report.append("| Metric | Percentage |")
    report.append("|--------|------------|")
    report.append(f"| **Correct Rate** | **{correct_rate:.1f}%** |")
    report.append(f"| **Missing Rate** | **{missing_rate:.1f}%** |")
    report.append(f"| **Over-specification Rate** | **{over_spec_rate:.1f}%** |")
    report.append("")

    # Performance interpretation
    report.append("### Performance Interpretation")
    if correct_rate >= 90:
        performance = "🟢 Excellent"
    elif correct_rate >= 75:
        performance = "🟡 Good"
    elif correct_rate >= 50:
        performance = "🟠 Fair"
    else:
        performance = "🔴 Needs Improvement"

    report.append(f"**Overall Performance:** {performance}")
    report.append("")

    precision = (total_correct / total_generated * 100) if total_generated > 0 else 0
    recall = correct_rate  # Same as correct rate
    f1_score = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0

    # Additional Metrics
    report.append("### Additional Metrics")
    report.append("| Metric | Value | Description |")
    report.append("|--------|-------|-------------|")
    report.append(f"| Precision | {precision:.1f}% | Percentage of generated relations that are correct |")
    report.append(f"| Recall | {recall:.1f}% | Percentage of expected relations that were found |")
    report.append(f"| F1-Score | {f1_score:.1f}% | Harmonic mean of precision and recall |")
    report.append("")
    report.append("---")
    report.append("")

    # Skipped sentences section
    if skipped_sentences:
        report.append("## Skipped Sentences")
        report.append("*(Sentences not found in benchmark)*")
        report.append("")
        for sentence in skipped_sentences:
            report.append(f"- {sentence}")
        report.append("")

    # Individual sentence results
    report.append("## Individual Sentence Results")
    report.append("")

    for i, result in enumerate(all_results, 1):
        sentence = result['sentence']
        expected_count = result['expected_count']
        generated_count = result['generated_count']
        correct_count = result['correct_count']
        missing_count = result['missing_count']
        over_spec_count = result['over_spec_count']

        # Calculate rates for this sentence
        sentence_correct_rate = (correct_count / expected_count * 100) if expected_count > 0 else 0
        sentence_missing_rate = (missing_count / expected_count * 100) if expected_count > 0 else 0
        sentence_over_spec_rate = (over_spec_count / generated_count * 100) if generated_count > 0 else 0

        report.append(f"### Sentence {i}")
        report.append(f"**Input:** {sentence}")
        report.append("")
        report.append("| Metric | Count | Rate |")
        report.append("|--------|-------|------|")
        report.append(f"| Expected Relations | {expected_count} | - |")
        report.append(f"| Generated Relations | {generated_count} | - |")
        report.append(f"| Correct Relations | {correct_count} | {sentence_correct_rate:.1f}% |")
        report.append(f"| Missing Relations | {missing_count} | {sentence_missing_rate:.1f}% |")
        report.append(f"| Over-specified Relations | {over_spec_count} | {sentence_over_spec_rate:.1f}% |")
        report.append("")

        # Correct relations
        if result['correct_relations']:
            report.append("**✅ Correct Relations:**")
            for rel in sorted(result['correct_relations']):
                report.append(f"- {rel[0]} → {rel[1]}: {rel[2]}")
            report.append("")

        # Missing relations
        if result['missing_relations']:
            report.append("**❌ Missing Relations:**")
            for rel in sorted(result['missing_relations']):
                report.append(f"- {rel[0]} → {rel[1]}: {rel[2]}")
            report.append("")

        # Over-specified relations
        if result['over_spec_relations']:
            report.append("**➕ Over-specified Relations:**")
            for rel in sorted(result['over_spec_relations']):
                report.append(f"- {rel[0]} → {rel[1]}: {rel[2]}")
            report.append("")

        # Detailed comparison
        report.append("<details>")
        report.append("<summary>Detailed Comparison</summary>")
        report.append("")
        report.append("**Expected Relations:**")
        for rel in sorted(result['expected_set']):
            report.append(f"- {rel[0]} → {rel[1]}: {rel[2]}")
        report.append("")
        report.append("**Generated Relations:**")
        for rel in sorted(result['generated_set']):
            report.append(f"- {rel[0]} → {rel[1]}: {rel[2]}")
        report.append("")
        report.append("</details>")
        report.append("")
        report.append("---")
        report.append("")

    return "\n".join(report)


def _parse_benchmark_relations(sentence: str, benchmark: str) -> List[tuple]:
    """
    Parse benchmark content to extract expected relations for a given sentence.

    Args:
        sentence: The input sentence to find in benchmark
        benchmark: Benchmark content in markdown format

    Returns:
        List of tuples: [(from_word, to_word, relation_type), ...]
    """
    import re

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
            # Handle lines like "    - The → boy: Constraint"
            match = re.search(r'([^→]+)→([^:]+):(.+)', line)
            if match:
                from_word = match.group(1).strip().lstrip('- ')
                to_word = match.group(2).strip()
                relation_type = match.group(3).strip()
                relations.append((from_word, to_word, relation_type))

    return relations
