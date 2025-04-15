# Pipeline Documentation

The Aussie NLP Toolkit processes data through distinct stages, ensuring flexibility, modularity, and scalability. Each stage is controlled by a dispatcher, and files flow sequentially through sub-pipelines.

## 1. Data Loading

### Purpose:
Determine the file type of each input in `data/raw/` and route it to the appropriate loader module. 
If a file is unsupported, it is moved to `data/failed/unsupported/`. 
If a file is corrupt, it is moved to `data/failed/corrupt/`. 
All valid files are passed to their designated loading module for structured processing and stored in `data/loaded/`.

### Workflow:
1. **`data_loader_dispatcher.py`**
   - Iterates over files in `data/raw/`.
   - Routes files to `detect_filetype.py` for classification.
   - Calls the appropriate loader module based on the file type.
   - Moves unsupported files to `data/failed/unsupported/`.
   - Moves corrupt files to `data/failed/corrupt/`.

2. **`detect_filetype.py`**
   - Determines file type (e.g., HTML, JSON, CSV).
   - Identifies unsupported formats and moves them to `data/failed/unsupported/`.
   - Detects corrupted files and moves them to `data/failed/corrupt/`.
   - Routes valid files to loader modules for structured processing.

3. **Loader Modules**
   - Process files based on type:
     - `data_loader_html.py`
     - `data_loader_json.py`
     - `data_loader_csv.py`
     - `data_loader_txt.py`
     - `data_loader_pdf.py`

### Outputs:
- Successfully loaded files → `data/loaded/`
- Unsupported file types → `data/failed/unsupported/`
- Corrupted files → `data/failed/corrupt/`

---

## 2. Cleaning (Sub-pipeline)

### Purpose:
Refine loaded data by removing noise, standardizing formats, deduplicating, and filtering content.

### Workflow:
1. **`cleaning_dispatcher.py`**
   - Manages file flow through cleaning modules.
   - Ensures files progress sequentially.

2. **Cleaning Modules** (executed in order):
   - `clean_html_tags.py`: Removes unnecessary HTML tags.
   - `normalise_unicode.py`: Standardizes Unicode characters.
   - `boilerplate_remover.py`: Removes irrelevant content (e.g., ads, headers).
   - `remove_duplicates.py`: Deduplicates text for unique content.
   - `aussie_spelling_normaliser.py`: Applies Australian English spelling conventions.
   - `language_filter.py`: Filters content by language.

### Outputs:
- Refined files in `data/cleaned/`.

---

## 3. Tokenisation (Sub-pipeline)

### Purpose:
Split text into smaller, meaningful units (sentences, tokens, slang terms) for NLP tasks.

### Workflow:
1. **`tokenising_dispatcher.py`**
   - Manages file flow through tokenisation modules.
   - Ensures files progress sequentially.

2. **Tokenisation Modules** (executed in order):
   - `split_sentences.py`: Splits text into sentences.
   - `wordpiece_tokeniser.py`: Tokenises text into subwords.
   - `aussie_slang_tokeniser.py`: Detects and tokenises Aussie slang terms.

### Outputs:
- Tokenised files in `data/processed/`.

---

## 4. Validation

### Purpose:
Ensure data integrity and completeness for downstream tasks.

### Workflow:
1. **`validate_pipeline.py`**
   - Validates the last output from Tokenisation.
   - Saves validated files or logs failures.

### Outputs:
- Validated files in `data/processed/`.

---

## 5. Data Generation

### Purpose:
Produce final datasets in user-specified formats (e.g., JSON, CSV, SQLite).

### Workflow:
1. **`generation_dispatcher.py`**
   - Determines output format(s) based on user input.
   - Routes files to corresponding generation modules.

2. **Generation Modules**:
   - `write_json.py`
   - `write_csv.py`
   - `write_sqlite.py`

### Outputs:
- Final datasets in `data/generated/`.

---

## File Structure
The pipeline uses the following directory structure:

```
aussie_nlp_toolkit/ 
├── data/raw/        # Input files (user-managed) 
├── data/loaded/     # Successfully loaded files (ready for processing) 
├── data/failed/     # Files that failed processing 
│ ├── corrupt/       # Corrupted files detected during loading 
│ ├── unsupported/   # Unsupported file types 
├── data/cleaned/    # Files after the Cleaning sub-pipeline 
│ ├── cleaning/      # Intermediate cleaning files 
├── data/processed/  # Files after the Tokenisation sub-pipeline 
│ ├── tokenising/    # Intermediate tokenising files 
├── data/validated/  # Fully validated data ready for output generation 
├── data/generated/  # Final datasets in specified formats
```

## Running the Toolkit

### Options:
1. **Individual Modules**  
   Run any module with specific file input. Example:  

```python
python aussie-nlp-tools/cleaning/remove_duplicates.py input_file.txt
```

2. **Sub-Pipelines**  
Run dispatchers to process files through specific stages. Example:  

```python
python aussie-nlp-tools/cleaning/cleaning_dispatcher.py
```


3. **Full Pipeline**  
Run `main.py` to process all files in `data/raw/`. Example:  

```python
python main.py --output csv
```

### Logs:
Detailed logs are generated for debugging and tracking progress.
