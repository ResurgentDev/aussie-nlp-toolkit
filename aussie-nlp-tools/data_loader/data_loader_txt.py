"""
Module: data_loader_txt.py

Purpose:
- Handles the loading of plain text files, preparing their raw content for further processing in the Aussie NLP pipeline.

Frameworks/Tools:
- Built-in Python libraries (`open`, `io`) for efficient text file handling.

Expected Inputs:
- Full file path to a plain text file as a string, including the filename (e.g., "/path/to/my_file.txt").

Expected Outputs:
- Generates a temporary file in `data/loaded/` containing the raw text content.
- Naming convention: `<original_filename>_loaded.txt` (e.g., "my_file_loaded.txt").

Behavior:
- Reads plain text files efficiently, ensuring compatibility with various encodings (e.g., UTF-8).
- Handles edge cases such as empty files, unsupported encodings, or corrupted content.

Planned Test Approach:
- Test with varied plain text files, including:
  - Small and large files.
  - Files with different encodings (e.g., UTF-8, Latin-1).
  - Files with special characters or unsupported formats.
- Verify that raw text content is accurately loaded with no data loss or corruption.
- Ensure robust error handling for problematic files.
"""
