"""
Module: data_loader_html.py

Purpose:
- Loads and parses HTML files, extracting clean and readable text content for further processing in the Aussie NLP pipeline.
- Handles the complexities of HTML structures, such as embedded tags and inline scripts, to ensure meaningful content is extracted.

Frameworks/Tools:
- Utilizes `BeautifulSoup` from `bs4` for robust HTML parsing.
- Optionally integrates with `lxml` for advanced parsing tasks.

Expected Inputs:
- Full file path to an HTML file as a string, including the filename (e.g., "/path/to/my_file.html").

Expected Outputs:
- Generates a temporary file in `data/loaded/` containing the extracted text content as plain text.
- Naming convention: `<original_filename>_loaded.txt` (e.g., "my_file_loaded.txt").

Behavior:
- Parses the HTML structure to remove extraneous elements, such as scripts, styles, and navigation bars.
- Focuses on extracting meaningful content from body tags or specific HTML elements.

Planned Test Approach:
- Test with varied HTML files, including:
  - Well-structured and malformed HTML.
  - Files with embedded scripts, styles, or other extraneous elements.
  - Large HTML files representing complete web pages or documents.
- Verify that extracted text content is accurate, excluding noise and irrelevant tags.
- Benchmark performance on large files or batches of files.
"""
