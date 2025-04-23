# Pipeline Documentation

The Aussie NLP Toolkit processes data through distinct stages, ensuring flexibility, modularity, and scalability. Each stage is controlled by a dispatcher, and files flow sequentially through sub-pipelines.

---

## 1. Data Sourcing

### Purpose:
Identify, import, and document datasets from a wide range of high-quality, domain-relevant sources.

### Workflow:
- Manual or automated scraping (e.g. academic, government, `.au` domain websites).
- Bulk imports of datasets (e.g. Common Crawl, legal corpora).
- Source metadata and licensing are tracked during ingestion.

### Outputs:
- Source files placed into `data/raw/`.
- Logs and metadata saved in `data/logs/sourcing/`.

---

## 2. Data Loading

### Purpose:
Determine file types, route to proper loaders, and convert raw data into structured form.

### Workflow:
1. **`data_loader_dispatcher.py`**
2. **`detect_filetype.py`**
3. **Loader Modules**: `data_loader_html.py`, `data_loader_json.py`, etc.

### Outputs:
- Successfully loaded files → `data/loaded/`
- Unsupported file types → `data/failed/unsupported/`
- Corrupted files → `data/failed/corrupt/`

---

## 3. Preprocessing 

### Purpose:
Clean, deduplicate, normalise, and filter sensitive content in preparation for quality filtering.

### Workflow:
- `clean_html_tags.py`
- `normalise_unicode.py`
- `boilerplate_remover.py`
- `deduplicate_minhash.py` (or `remove_duplicates.py`)
- `aussie_spelling_normaliser.py`
- `language_filter.py`
- `unsafe_content_filter.py` *(to be created)*

### Outputs:
- Preprocessed files in `data/preprocessed/`

---

## 4. Quality Filtering 

### Purpose:
Remove low-quality, offensive, or otherwise unsuitable data for LLM training.

### Workflow:
- `filter_low_quality.py` *(to be created)*
- `filter_machine_generated.py` *(to be created)*
- `fix_encoding_issues.py` *(to be created)*
- `filter_toxicity.py` *(to be created)*
- `filter_copyrighted.py` *(to be created)*

### Outputs:
- Filtered files in `data/filtered/`

---

## 5. Structuring & Metadata 

### Purpose:
Attach metadata and convert content into training-friendly formats.

### Workflow:
- `assign_metadata.py` *(to be created)*
- `convert_to_jsonl.py` *(to be created)*
- `convert_to_tfrecord.py` *(optional)*

### Outputs:
- Structured files in `data/structured/`

---

## 6. Balancing 

### Purpose:
Ensure fair representation of domains and content types.

### Workflow:
- `content_balancer.py` *(to be created)*
- `domain_equaliser.py` *(to be created)*

### Outputs:
- Balanced datasets in `data/balanced/`

---

## 7. Tokenisation

### Purpose:
Split content into subword units for LLM ingestion.

### Workflow:
1. `tokenising_dispatcher.py`
2. Modules: `split_sentences.py`, `wordpiece_tokeniser.py`, `aussie_slang_tokeniser.py`

### Outputs:
- Tokenised files in `data/processed/`

---

## 8. Validation

### Purpose:
Verify correctness and pipeline compliance.

### Workflow:
- `validate_pipeline.py`

### Outputs:
- Validated files in `data/validated/`

---

## 9. Human-in-the-Loop 

### Purpose:
Enable expert annotation, evaluation, and safety testing.

### Workflow:
- Manual or semi-automated annotation (e.g. prompts, classification).
- Red-teaming or safety eval generation.
- Tools TBD or external integrations.

### Outputs:
- Instructional and safety datasets in `data/hitl/` and `data/eval/`

---

## 10. Data Generation

### Purpose:
Produce final datasets in user-requested formats.

### Workflow:
- `generation_dispatcher.py`
- Modules: `write_json.py`, `write_csv.py`, `write_sqlite.py`

### Outputs:
- Final datasets in `data/generated/`

---

## 11. Documentation & Auditing 

### Purpose:
Ensure transparent, traceable data workflows.

### Workflow:
- Track changes across all pipeline stages.
- Generate data cards and metadata summaries.
- Log filtering rationale and source history.

### Outputs:
- Documentation in `docs/` and `data/logs/`

---

## 12. Data Versioning

### Purpose:
Track versions of datasets and processing stages for reproducibility and lineage tracing.

### Workflow:
- Hash output datasets at key stages.
- Store checksums, timestamps, and processing metadata.
- Maintain changelogs for pipeline alterations affecting the data.

### Outputs:
- Versioned datasets and metadata in `data/versions/`

---

## 13. Bias and Fairness Audits

### Purpose:
Evaluate the dataset for demographic balance, representation biases, and potential fairness issues.

### Workflow:
- Analyse the distribution of content across key dimensions (e.g., gender, ethnicity, geography).
- Use metrics like entropy, representation ratios, and topic skew.
- Generate summaries and charts for reporting.

### Modules (planned):
- `bias_metrics.py` *(to be created)*  
- `representation_reporter.py` *(to be created)*

### Outputs:
- Audit reports stored in `data/logs/audits/`

---

## 14. Feedback Loop from Evaluation

### Purpose:
Use evaluation results (e.g., model failures, unsafe generations) to iteratively improve dataset quality.

### Workflow:
- Analyse failed model outputs and problematic prompts.
- Trace issues back to source data using metadata lineage.
- Update filters or rebalance inputs accordingly.

### Outputs:
- Feedback logs and improvement notes in `data/logs/eval_feedback/`

---

## 15. Compression & Archival

### Purpose:
Save disk space and maintain long-term access to historical dataset states.

### Workflow:
- Compress large intermediate or final datasets (e.g., `.tar.gz`, `.xz`).
- Archive deprecated or superseded versions.
- Automate periodic archival.

### Outputs:
- Archived snapshots in `data/archive/`

---

## 16. Configuration Profiles

### Purpose:
Enable reproducible and flexible processing using externalised config files.

### Workflow:
- Define YAML or JSON profiles for different tasks (e.g., RLHF, instruction tuning).
- Pass configs to pipeline modules as runtime input.
- Profiles include filter thresholds, target ratios, paths, etc.

### Outputs:
- Config files stored in `configs/`

---

## 17. Red-Team Dataset Versioning & Reuse

### Purpose:
Maintain a library of adversarial prompts and test sets for safety evaluation.

### Workflow:
- Tag red-team datasets with versions and lineage.
- Link responses to source prompt and evaluation notes.
- Extendable by SMEs or external annotators.

### Outputs:
- Versioned red-team datasets in `data/eval/redteam_versions/`

---

## File Structure 
```
aussie_nlp_toolkit/
├── data/
│   ├── raw/                              # Original scraped or imported data
│   ├── loaded/                           # Structured intermediate files
│   ├── preprocessed/                     # Deduplicated, filtered, normalised text
│   ├── filtered/                         # Quality-filtered data
│   ├── structured/                       # With attached metadata, JSONL etc.
│   ├── balanced/                         # Domain- and format-balanced corpora
│   ├── processed/                        # Tokenised data
│   ├── validated/                        # Post-validation output
│   ├── generated/                        # Final datasets in output formats
│   ├── hitl/                             # Human-in-the-loop and RLHF datasets
│   ├── eval/                             # Evaluation sets
│   │   └── redteam_versions/             # Versioned red-team datasets
│   ├── logs/                             # Audit trails, sourcing metadata, feedback
│   │   ├── sourcing/                     # Metadata about data source origin, licensing
│   │   ├── audits/                       # Bias, fairness, and demographic audit reports
│   │   └── eval_feedback/                # Failures, red flags, and downstream eval results
│   ├── archive/                          # Compressed and frozen archives
│   ├── versions/                         # Versioned snapshots and changelogs
│   └── failed/                           # Corrupt or unsupported files
│       ├── corrupt/                      # Files detected as corrupted	
│       └── unsupported/                  # Unsupported file types
```

---

## Running the Toolkit

### Options:
1. Individual Modules
2. Sub-Pipelines
3. Full Pipeline: `python main.py --output csv`

---

### Logs:
Detailed logs are generated for debugging and tracking progress.
