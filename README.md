# Aussie NLP Toolkit

## Overview
The Aussie NLP Toolkit is a modular Python library designed for cleaning, processing, and preparing datasets for training large language models (LLMs), with a focus on Australian-specific contexts. Its modular design encourages contributions, simplifies debugging, and ensures scalability, making it a perfect foundation for collaborative NLP research and projects.

Whether you're processing `.au` domain websites, legal archives, scientific publications, or news datasets, this toolkit provides highly customizable tools tailored for an "Aussie-flavored" dataset preparation pipeline.

---

## Features
- **Modular Design**: Highly focused modules for each task make debugging easier and allow seamless scalability.
- **Beginner-Friendly**: Comprehensive documentation and guides provide an approachable framework for contributors.
- **Error Handling**: Custom exceptions and centralized error-handling mechanisms ensure stability and robustness.
- **Automated Testing and CI/CD**: Integrated testing workflows to maintain code quality across contributions.
- **Australian-Specific Preprocessing**: Tools to handle Aussie slang, regional spelling nuances, `.au` domains, and more.

---

## Pipeline Overview

The Aussie NLP Toolkit processes data through distinct stages, ensuring flexibility, modularity, and scalability. Each stage consists of sub-pipelines managed by dispatchers and specialized modules.

### Stages in the Pipeline
1. **Data Loading**
   - Extracts raw data from `data/raw/`, routes files to the appropriate loader modules.
   - Outputs temporary files into `data/loaded/`.

2. **Cleaning**
   - Refines loaded data by removing noise, normalizing formats, deduplicating, and filtering content.
   - Outputs cleaned files into `data/cleaned/`.

3. **Tokenisation**
   - Converts cleaned text into smaller, meaningful units (sentences, tokens, slang terms).
   - Outputs tokenised files into `data/processed/`.

4. **Validation**
   - Verifies data integrity, correctness, and format compliance.
   - Outputs validated files into `data/validated/`.

5. **Data Generation**
   - Produces final datasets in user-specified formats (e.g., JSON, CSV, SQLite).
   - Outputs final files into `data/generated/`.

**NOTE:** 
   - Files detected as corrupted are moved into `data/failed/corrupt/`
   - Unsupported file types are moved into `data/failed/unsupported/`  
---

### Detailed Pipeline Documentation
For a complete breakdown of each stage, including module details and file flow, refer to [pipeline.md](pipeline.md).

---

## Directory Structure
The project is organized into a logical structure for clarity, modularity, and scalability:


```
aussie_nlp_toolkit/
├── aussie-nlp-tools/                     # Core library modules
│   ├── constants.py                      # Shared constants and configurations
│   ├── data_loader/                      # Handles data loading from different formats
│   │   ├── detect_filetype.py            # Detects file types (e.g., HTML, JSON, CSV)
│   │   ├── data_loader_dispatcher.py     # Dispatches files to appropriate loaders
│   │   ├── data_loader_html.py           # Parses HTML files
│   │   ├── data_loader_json.py           # Loads JSON data
│   │   ├── data_loader_csv.py            # Reads CSV files
│   │   ├── data_loader_txt.py            # Processes plain text files
│   │   ├── data_loader_pdf.py            # Handles PDF parsing
│   ├── cleaning/                         # Modules for cleaning and normalisation
│   │   ├── cleaning_dispatcher.py        # Dispatches files to cleaning modules
│   │   ├── clean_html_tags.py            # Removes HTML tags
│   │   ├── normalise_unicode.py          # Normalises Unicode characters
│   │   ├── boilerplate_remover.py        # Removes irrelevant content (e.g., ads, footers)
│   │   ├── remove_duplicates.py          # Deduplicates datasets
│   │   ├── aussie_spelling_normaliser.py # Normalises Australian spelling
│   │   ├── language_filter.py            # Filters out non-English content
│   ├── tokenisation/                     # Tokenisation modules
│   │   ├── tokenising_dispatcher.py      # Dispatches files to tokenisation modules
│   │   ├── split_sentences.py            # Splits text into sentences
│   │   ├── wordpiece_tokeniser.py        # Tokenises text into subwords (e.g., BPE)
│   │   ├── aussie_slang_tokeniser.py     # Detects and tokenises Aussie slang
│   ├── filters/                          # Filters for specific content
│   │   ├── filters_metadata.py           # Filters metadata (e.g., timestamps, author info)
│   │   ├── filters_domains.py            # Filters `.au` domain-specific content
│   │   ├── filters_citation_format.py    # Handles legal/scientific citations
│   ├── deduplication/                    # Modules for deduplication
│   │   ├── deduplicate_minhash.py        # Removes duplicates using MinHash
│   ├── validation/                       # Modules for validation
│   │   ├── validate_pipeline.py          # Validates files through pipeline stages
│   ├── output/                           # Handles output formatting
│   │   ├── generation_dispatcher.py      # Dispatches files to output generators
│   │   ├── write_csv.py                  # Saves data to CSV format
│   │   ├── write_json.py                 # Saves data to JSON format
│   │   └── write_sqlite.py               # Saves data to SQLite databases
├── data/                                 # Main directory for all data-related inputs and outputs
│   ├── raw/                              # Contains unprocessed input data
│   ├── loaded/                           # Contains data after loading stage
│   ├── failed/                           # Contains files that failed processing
│   │   ├── corrupt/                      # Files detected as corrupted
│   │   └── unsupported/                  # Unsupported file types
│   ├── cleaned/                          # Contains data after cleaning/preprocessing
│   ├── processed/                        # Contains tokenized files ready for use
│   ├── validated/                        # Contains validated data files
│   ├── generated/                        # Outputs generated by scripts or pipelines
├── examples/                             # Example scripts demonstrating pipeline functionality.
├── guides/                               # Documentation covering module additions, pipeline execution, and testing.
├── tests/                                # Test suite with 1-to-1 tests for each core module, plus batch processing and pipeline validation.
│   CHANGELOG                             # Project changelog and version history
│   CONTRIBUTING.md                       # Contribution guidelines
│   LICENCE                               # Licence file 
│   main.py                               # Main pipeline orchestrator 
│   pipeline.md                           # Detailed pipeline documentation
│   README.md                             # Comprehensive project overview
│   requirements.txt                      # Dependency list
│   setup.py                              # Makes the library installable
│   VERSION                               # Version information file
```
### Data Directory Structure

The toolkit includes standardized directories for managing data at various stages of the pipeline:

- **`data/raw/`**  
  Contains unprocessed input files directly from external sources. Files are dynamically classified by the `detect_filetype.py` script.

- **`data/loaded/`**  
  Stores raw data extracted by loader modules, serving as temporary intermediary files before cleaning. Temporary files follow a naming convention, such as `<original_filename>_loaded.<extension>`.

- **`data/cleaned/`**  
  Contains data refined by cleaning scripts, such as deduplicated or normalized text. These outputs are ready for further processing.

- **`data/processed/`**  
  Contains structured data prepared for NLP workflows, including tokenized or validated files.

- **`data/generated/`**  
  Stores outputs generated by the pipeline or models, such as predictions, datasets, or reports.

Each directory includes a `.gitkeep` file to maintain the structure in the repository.

---

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/resurgentdev/aussie-nlp-toolkit.git
   cd aussie-nlp-toolkit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the example pipeline:
   ```bash
   python examples/example_pipeline.py
   ```

---

## Testing
The toolkit uses **pytest** for automated testing and follows a 1-to-1 test-to-script convention:
- Each script in the toolkit has a corresponding `test_*.py` file in the `tests/` directory.
- To run all tests:
   ```bash
   pytest tests/
   ```

### Continuous Integration (CI)
We employ CI workflows (e.g., GitHub Actions) to automatically run tests whenever new code is pushed or a pull request is opened. This ensures code quality and prevents regressions.

---

## Contributing
We welcome contributions of all levels! Here’s how to get started:
1. Fork the repo and create a new branch for your feature.
2. Write your code and corresponding tests in the `tests/` directory.
3. Submit a pull request with clear descriptions of your changes.

Please follow [PEP 8](https://peps.python.org/pep-0008/) for coding standards.

---

## Future Roadmap
- Add parallel data processing for scalability.
- Introduce model-specific tokenization modules (e.g., SentencePiece).
- Develop more guides for new contributors.

---

## Licence
This project is licensed under the MIT Licence. See the `LICENCE` file for details.

---

## Acknowledgments
This project draws inspiration from modern NLP tools like Hugging Face, NLTK, and spaCy. Special thanks to contributors for helping us build an "Aussie-flavored" NLP library!

---

