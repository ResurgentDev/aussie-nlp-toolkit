"""
Module: clean_html_tags.py

Purpose:
- Removes unnecessary HTML tags from loaded text files, ensuring that only meaningful content remains for further processing.
- Deletes intermediate files from `data/loaded/` once their content is successfully cleaned.

Frameworks/Tools:
- Utilizes `BeautifulSoup` from `bs4` for robust HTML parsing and tag removal.

Expected Inputs:
- File path to a temporary text file in `data/loaded/`, created by `data_loader_html.py`.
  - Example: "data/loaded/<original_filename>_loaded.txt".

Expected Outputs:
- A cleaned text file in `data/cleaned/`, free of HTML tags and artifacts.
  - Example: "data/cleaned/<original_filename>_cleaned.txt".
- The input file in `data/loaded/` is deleted after successful cleaning.

Behavior:
- Reads the loaded text file and processes its content to remove all HTML tags.
- Handles edge cases such as incomplete or malformed HTML.
- Outputs a plain text file, ensuring consistent formatting.
- Ensures intermediate files are deleted to maintain a clean pipeline.

Planned Test Approach:
- Test with text files containing varied HTML content, including:
  - Well-formed and malformed HTML.
  - Text with embedded JavaScript or CSS.
  - Large files with extensive nested tags.
- Verify that cleaned text output matches expected results, free of noise or artifacts.
- Confirm that the original intermediate file is deleted after successful cleaning.
"""
