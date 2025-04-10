"""
Module: aussie_spelling_normaliser.py

Purpose:
- Converts text to standard Australian English spelling and conventions to ensure consistency across the Aussie NLP pipeline.
- Handles common spelling variations and regional differences (e.g., American or British English to Australian English).

Frameworks/Tools:
- Utilizes custom dictionaries and rules for Australian English spelling normalization.
- Optionally integrates with libraries like `pyspellchecker` for broader spell-checking support.

Expected Inputs:
- File path to a cleaned text file in `data/cleaned/`.
  - Example: "data/cleaned/<original_filename>_cleaned.txt".

Expected Outputs:
- A normalized text file in `data/cleaned/`, adhering to Australian English conventions.
  - Example: "data/cleaned/<original_filename>_aus_normalised.txt".
- Deletes the input file in `data/cleaned/` after successful normalization.

Behavior:
- Detects and replaces non-Australian spellings with their Australian equivalents (e.g., "color" to "colour").
- Handles edge cases such as ambiguous or context-dependent words (e.g., "program" vs. "programme").
- Logs any unhandled or skipped changes for manual review.

Planned Test Approach:
- Test with text files containing:
  - American English spellings (e.g., "color," "honor").
  - British English spellings (e.g., "tyre," "organisation").
  - Mixed regional variations within the same text.
- Verify that output text adheres to Australian English conventions.
- Confirm that the original cleaned file is deleted after processing.
"""
