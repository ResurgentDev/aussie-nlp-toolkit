"""
main.py - Pipeline Orchestrator for Aussie NLP Toolkit

This script serves as the central controller for the Aussie NLP Toolkit pipeline, using Ruffus
to manage workflow logic and dependencies. It replaces dispatcher scripts by defining tasks
and their relationships directly.

Pipeline Stages:
1. Data Loading:
   - Detects file types using `detect_filetype.py`.
   - Routes files to the appropriate loader module (e.g., `data_loader_html.py`).
   - Outputs loaded files to `data/loaded`.

2. Cleaning:
   - Processes loaded files through cleaning modules (e.g., `clean_html_tags.py`, `remove_duplicates.py`).
   - Produces cleaned files in `data/cleaned`.

3. Tokenisation:
   - Splits text into sentences (`split_sentences.py`).
   - Tokenises text into subwords (`wordpiece_tokeniser.py`).
   - Detects and tokenises Australian slang (`aussie_slang_tokeniser.py`).
   - Outputs tokenised files to `data/processed`.

4. Validation:
   - Validates tokenised files to ensure quality and consistency.
   - Outputs validated files to `data/processed`.

5. Data Generation:
   - Converts validated files into final datasets (e.g., JSON, CSV) using generation modules.

Features:
- Full pipeline execution (`pipeline_run` with no targets).
- Sub-pipeline execution (e.g., `pipeline_run([tokenisation_task])` for tokenisation only).
- Batch processing with parallel execution.
- Automatic handling of failed tasks (skipped downstream dependencies).
- Visualization of the pipeline using `pipeline_printout_graph`.

Dependencies:
- Ruffus: Used for pipeline management and visualization.

Usage:
- Run the entire pipeline:
  `python main.py`
- Run specific sub-pipelines:
  `pipeline_run([target_task])`
"""

"""
main.py - Pipeline Orchestrator for Aussie NLP Toolkit

This script orchestrates the pipeline using Ruffus, handling task dependencies, batch processing,
and error management.
"""

from ruffus import *
import os
import logging

# Initialize logging
logger = logging.getLogger("pipeline_logger")
logging.basicConfig(level=logging.INFO)

# Define directories
RAW_DIR = "./data/raw"
FAILED_DIR = "./data/failed"
LOADED_DIR = "./data/loaded"
CLEANED_DIR = "./data/cleaned"
PROCESSED_DIR = "./data/processed"
GENERATED_DIR = "./data/generated"

# Task 1: Detect file type
@transform(
    RAW_DIR + "/*",  # Input: all raw data files
    suffix(""),  # Output suffix will be based on detected file type
    LOADED_DIR + "/filetype_checked.txt"  # Placeholder output for valid files
)
def detect_filetype_task(input_file, output_file):
    # Example logic for detecting file type
    file_type = "html"  # Simulated result (replace with actual detect_filetype.py logic)
    if file_type == "unsupported":
        os.rename(input_file, FAILED_DIR + "/unsupported/" + os.path.basename(input_file))
        logger.warning(f"Unsupported file: {input_file}. Moved to failed.")
    elif file_type == "corrupted":
        os.rename(input_file, FAILED_DIR + "/corrupted/" + os.path.basename(input_file))
        logger.error(f"Corrupted file: {input_file}. Moved to failed.")
    else:
        os.rename(input_file, LOADED_DIR + "/" + file_type + "/" + os.path.basename(input_file))
        logger.info(f"Loaded file: {input_file}. Type: {file_type}.")

# Task 2: Cleaning sub-pipeline
@transform(
    LOADED_DIR + "/*",  # Input: loaded files
    suffix(""),
    CLEANED_DIR + "/*_cleaned.txt"
)
def cleaning_task(input_file, output_file):
    # Example cleaning logic
    logger.info(f"Cleaning file: {input_file}. Output: {output_file}.")

# Task 3: Tokenisation sub-pipeline
@transform(
    CLEANED_DIR + "/*",
    suffix(""),
    PROCESSED_DIR + "/*_tokenised.txt"
)
def tokenisation_task(input_file, output_file):
    # Example tokenisation logic
    logger.info(f"Tokenising file: {input_file}. Output: {output_file}.")

# Task 4: Data Generation
@transform(
    PROCESSED_DIR + "/*",
    suffix(""),
    GENERATED_DIR + "/*_final.json"  # Default output as JSON
)
def data_generation_task(input_file, output_file):
    # Example data generation logic
    logger.info(f"Generating data for file: {input_file}. Output: {output_file}.")

# Generate pipeline visualization
def generate_pipeline_graph():
    from ruffus import pipeline_printout_graph
    pipeline_printout_graph("pipeline_graph.png", "png")

# Run the pipeline
if __name__ == "__main__":
    import sys
    if "--graph" in sys.argv:  # Generate pipeline graph
        generate_pipeline_graph()
    else:  # Run the full pipeline
        pipeline_run(multiprocess=4, verbose=3)
