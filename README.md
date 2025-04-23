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

1. **Data Sourcing** – Identify diverse, high-quality sources and track licenses.
2. **Data Loading** – Route raw files to format-specific loader modules.
3. **Preprocessing** – Clean, deduplicate, filter unsafe content, and normalise formats.
4. **Quality Filtering** – Remove low-quality, biased, toxic, or machine-generated text.
5. **Structuring & Metadata** – Add metadata and convert into model-friendly formats.
6. **Balancing** – Balance domain and content-type distribution (code, prose, dialogue).
7. **Tokenisation** – Convert into tokens or subword units.
8. **Validation** – Verify data integrity, structure, and metadata.
9. **Human-in-the-Loop** – Collect annotations, red-teaming data, and RLHF examples.
10. **Data Generation** – Export in final output formats (JSONL, CSV, SQLite).
11. **Documentation & Auditing** – Full data lineage, rationale logs, and summaries.
12. **Data Versioning** – Hash and log outputs for reproducibility and rollback.
13. **Bias and Fairness Audits** – Generate representation and fairness reports.
14. **Evaluation Feedback Loop** – Feed downstream model feedback into data refinements.
15. **Compression & Archival** – Archive and compress long-term or outdated datasets.
16. **Configuration Profiles** – Use modular YAML/JSON config profiles for repeatability.
17. **Red-Team Dataset Versioning & Reuse** – Track versions of adversarial eval sets.

**NOTE:** 
   - Files detected as corrupted are moved into `data/failed/corrupt/`
   - Unsupported file types are moved into `data/failed/unsupported/`  
---

### Detailed Pipeline Documentation
For a complete breakdown of each stage, including module details and file flow, refer to [docs/pipeline.md](docs/pipeline.md).

---

## Directory Structure
The project is organized into a logical structure for clarity, modularity, and scalability:


```
aussie_nlp_toolkit/
├── aussie-nlp-tools/                     # Core library modules
│   ├── data_loader/                      # Loaders for raw input formats
│   ├── preprocessing/                    # Cleaning and normalisation stages
│   ├── tokenisation/                     # Tokenisation and sentence splitting
│   ├── deduplication/                    # Deduplication via MinHash/SimHash
│   ├── filters/                          # Domain- and content-specific filtering
│   ├── validation/                       # Validation modules for pipeline checks
│   ├── output/                           # Final output format generators
│   └── constants.py                      # Shared constants and configuration
├── configs/                              # JSON/YAML configuration profiles
├── data/                                 # All dataset artifacts 
├── examples/                             # Pipeline usage demonstrations
├── guides/                               # Contributor how-tos and design docs
├── tests/                                # Pytest suites (1-to-1 script coverage)
├── main.py                               # Main orchestrator script
├── pipeline.md                           # Detailed stage-by-stage pipeline doc
├── README.md                             # This file
├── CHANGELOG                             # Revision history
├── VERSION                               # Version identifier
├── requirements.txt                      # Dependency list
├── setup.py                              # Setup script
└── LICENCE                               # License details
```
> 🔍 For full `data/` breakdown, see [pipeline.md → File Structure](pipeline.md#file-structure)
> 🔍 For full `tests/` breakdown, see [tests.md](tests.md)

### Data Directory Structure

The toolkit includes standardized directories for managing data at various stages of the pipeline:

- **`data/raw/`**  
  Contains unprocessed input files directly from external sources. Files are dynamically classified by the `detect_filetype.py` script.

- **`data/loaded/`**  
  Stores raw data extracted by loader modules, serving as temporary intermediary files before cleaning. Temporary files follow a naming convention, such as `<original_filename>_loaded.<extension>`.

- **`data/preprocessed/`**  
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
- Add distributed training dataset prep (e.g., Ray, Dask)
- Train/test split automation with leakage detection
- Modular plugin support for third-party filters
---

## Licence
This project is licensed under the GNU General Public License. See the `LICENCE` file for details.

---

## Acknowledgments
This project draws inspiration from modern NLP tools like Hugging Face, NLTK, and spaCy. Special thanks to contributors for helping us build an "Aussie-flavored" NLP library!

---

