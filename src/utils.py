"""
Utility functions for ROM Generator

This module provides helper functions for reading input files and saving ROM analysis results.
"""

from typing import List, Dict, Any


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
