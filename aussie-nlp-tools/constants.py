"""
constants.py

Defines all constants used across the Aussie NLP Toolkit.
These constants are primarily file type codes, which guide the behavior of file detection and processing modules.

"""

# Constants for file type detection and processing in the Aussie NLP Toolkit.
# These constants are used to identify the type of file being processed and determine the appropriate handling method.
# - 0 represents unsupported file types.
# - 1-N represent supported file types.
# - 999 is used for corrupted files where content does not match the expected structure.

# Supported File Type Codes
FILETYPE_CORRUPT = 999      # File extension and contents do not match.
FILETYPE_UNSUPPORTED = 0    # File type is unsupported by the toolkit.
FILETYPE_HTML = 1           # HTML files, typically used for web scraping or document processing.
FILETYPE_JSON = 2           # JSON files, common for structured data exchange.
FILETYPE_CSV = 3            # CSV files, used for tabular data representation.
FILETYPE_PDF = 4            # PDF documents, often requiring OCR or parsing.
FILETYPE_TEXT = 5           # Plain text files, e.g., .txt.
# Future File Types to Support
# FILETYPE_DOCX = 6           # Microsoft Word documents (modern format).
# FILETYPE_DOC = 7            # Microsoft Word documents (legacy format).
# FILETYPE_XML = 8            # XML files, often used for metadata or structured datasets.
# FILETYPE_MARKDOWN = 9       # Markdown files, common for documentation or lightweight text.
# FILETYPE_YAML = 10          # YAML configuration files, e.g., for pipeline setups.
# FILETYPE_SQLITE = 11        # SQLite database files.

# Additional constants can be added here as needed.
