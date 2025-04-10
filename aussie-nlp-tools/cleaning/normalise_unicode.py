"""
Module: normalise_unicode.py

Purpose:
- Standardizes text content by normalizing Unicode characters to ensure consistency across the Aussie NLP pipeline.
- Handles variations such as accented characters, special symbols, and non-standard encodings.

Frameworks/Tools:
- Utilizes Python's built-in `unicodedata` module for Unicode normalization.

Expected Inputs:
- File path to a cleaned text file in `data/cleaned/`, created by a previous cleaning module.
  - Example: "data/cleaned/<original_filename>_cleaned.txt".

Expected Outputs:
- A normalized text file in `data/cleaned/`, where all Unicode characters are standardized.
  - Example: "data/cleaned/<original_filename>_unicode_normalized.txt".
- Deletes the input file in `data/cleaned/` after successful normalization.

Behavior:
- Converts accented characters (e.g., "é" to "e") to their closest ASCII equivalents if required.
- Ensures consistent handling of special symbols, whitespace, and encoding across text data.
- Handles edge cases such as malformed input or unsupported encodings.

Planned Test Approach:
- Test with varied text files containing:
  - Accented characters (e.g., `é`, `ü`).
  - Special symbols (e.g., currency symbols, mathematical notations).
  - Texts in multiple encodings (e.g., UTF-8, ISO-8859-1).
- Verify that normalized text matches the expected standard.
- Confirm that the original cleaned file is deleted after processing.
"""
