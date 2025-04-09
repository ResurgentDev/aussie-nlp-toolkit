"""
Module: data_loader_json.py

Purpose:
- Handles the loading and parsing of JSON files, extracting structured data for downstream NLP tasks.
- Simplifies handling of nested or complex JSON structures, ensuring that extracted data is ready for preprocessing or analysis.

Frameworks/Tools:
- Built-in Python `json` library for parsing and validation.
- Optionally integrates with libraries like `pandas` for advanced manipulation.

Expected Inputs:
- Full file path to a JSON file as a string, including the filename (e.g., "/path/to/my_file.json").

Expected Outputs:
- Generates a temporary file in `data/loaded/` containing flattened or structured JSON data in a consistent format.
- Naming convention: `<original_filename>_loaded.json` (e.g., "my_file_loaded.json").

Behavior:
- Validates the JSON file for syntax errors and handles exceptions gracefully.
- Optionally flattens nested structures for easier downstream processing.

Planned Test Approach:
- Test with various JSON files, including:
  - Simple key-value pairs.
  - Deeply nested structures.
  - Large datasets.
- Verify that parsed JSON data is accurate and stored in the expected format.
- Ensure proper error handling for corrupted or invalid files.
"""
