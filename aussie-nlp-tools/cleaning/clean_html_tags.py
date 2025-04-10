"""
Module: clean_html_tags.py

Purpose:
- Cleans and removes unnecessary HTML tags from text content, ensuring only meaningful content remains for further processing in the Aussie NLP pipeline.

Frameworks/Tools:
- Utilizes `BeautifulSoup` from `bs4` for parsing and cleaning HTML structures.

Expected Inputs:
- Raw HTML text as a string, typically loaded from a file or directly from web scraping.

Expected Outputs:
- Returns a clean text string, free of extraneous HTML tags and attributes.

Behavior:
- Strips all HTML tags, leaving plain text content.
- Handles nested tags and edge cases, such as incomplete or malformed HTML.
- Optionally retains specific tags or attributes if needed (e.g., `<a>` for links).
- Removes whitespace and other artifacts left behind after cleaning.

Planned Test Approach:
- Test with varied HTML content, including:
  - Well-formed and malformed HTML.
  - HTML with embedded JavaScript, CSS, or complex nested structures.
  - Simple HTML content with minimal tags.
- Verify that plain text output is clean, consistent, and accurate.
- Benchmark performance with large HTML files or bulk operations.
"""
