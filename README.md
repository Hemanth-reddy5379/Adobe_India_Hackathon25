Here is your cleaned-up version of the **"Connecting the Dots Challenge Solution"** with all unnecessary symbols and technical clutter removed, while preserving clarity and professionalism:

---

# Connecting the Dots Challenge Solution

## Project Overview

The Connecting the Dots Challenge aims to transform static PDFs into intelligent, interactive resources. The solution addresses two core problems: extracting structured document outlines and delivering persona-driven insights based on specific tasks.

This approach converts PDFs into structured, searchable knowledge bases that prioritize content based on the user's role and goals.

---

## Challenge 1A: Document Structure Extraction

### Objective

Extract structured outlines from PDFs by identifying the document title and hierarchical headings (H1, H2, H3) along with corresponding page numbers. The output is provided in a clean JSON format.

### Key Features

* Supports PDF documents up to 50 pages
* Title extraction using metadata, first-page content, and fallback patterns
* Heading detection based on font size, style, and formatting cues
* Produces structured JSON with heading levels and page locations
* Supports batch processing for multiple files

### Technical Specifications

* Compatible with AMD64 systems using Docker
* CPU-only processing (8 cores, 16 GB RAM)
* No internet access during runtime
* No use of machine learning models (≤ 200MB)
* Processing time under 10 seconds per PDF
* Outputs valid UTF-8 JSON

### How to Run

1. Place input PDFs in the `input` folder
2. Build the Docker container:

   ```
   docker build -t connecting-dots-solution .
   ```
3. Run the challenge:

   ```
   docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots-solution python main.py
   ```
4. Check the `output` folder for results

### Implementation Approach

**Title Extraction**

* Analyzes metadata and large-font elements on the first page
* Applies fallback methods like filename parsing when metadata is unavailable

**Heading Detection**

* Uses font size, weight, and patterns (e.g., numbered headings like 1.1, 1.1.1)
* Recognizes document type and layout to adjust detection logic

**Hierarchical Classification**

* Assigns heading levels (H1-H4) using relative font sizing and spacing
* Validates structure to ensure logical flow

**Text Extraction Tools**

* PyMuPDF and PDFplumber are used to analyze font properties and extract layout-aware content
* Output is cleaned and normalized

---

## Challenge 1B: Persona-Driven Document Intelligence

### Objective

Extract and rank the most relevant sections from a group of documents based on a specific user persona and a clearly defined task.

### Input Requirements

* A collection of 3–10 related PDF documents
* A persona definition including role and experience level
* A job-to-be-done, describing the user’s goal
* A configuration JSON specifying documents, persona, and task

### Output

* Persona and task metadata
* Ranked document sections based on relevance
* Source attribution and refined content tailored to the persona

### Technical Specifications

* CPU-only processing
* Model usage under 1 GB
* Offline execution
* Processing time under 60 seconds
* UTF-8 encoded JSON output

### How to Run

1. Prepare a JSON config file in the `input` folder
2. Run the following Docker command:

   ```
   docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots-solution python challenge1b_main.py input/collection_config.json output/persona_results.json
   ```

### Implementation Highlights

* Parses persona configuration and validates inputs
* Reuses Challenge 1A’s structural extraction logic
* Generates structured JSON output

### Upcoming Features

* Semantic similarity scoring using sentence embeddings
* Persona-based optimization using embedding comparison
* Ranking system for section relevance
* Enhanced content extraction methods

---

## Architecture and Design

* Modular code structure with reusable components
* Clear separation between parsing, analysis, and output generation
* Easily extensible for new document types or analysis methods
* Error handling for invalid PDFs and inconsistent formatting

---

## Heading Detection Strategy

* Combines font features, layout cues, and document flow
* Tailors detection logic for reports, papers, and technical documents
* Applies post-validation to fix or eliminate inconsistencies

---

## Testing and Validation

* Tested with a variety of PDF layouts and types
* Handles edge cases such as malformed files and missing metadata
* Validates JSON output structure and hierarchy
* Ensures compliance with all performance and hardware constraints

---

## Compliance and Constraints

* Entirely offline processing
* Efficient use of CPU and memory
* No hardcoded values
* No use of external APIs or internet access

---

## Submission Checklist

* Source code under version control
* Dockerfile at project root
* All required libraries included in container
* `README.md` with documentation
* `approach_explanation.md` included for Challenge 1B
* Challenge 1A implemented and functional
* Challenge 1B partially implemented

---

## Getting Started

1. Clone the repository
2. Build the Docker container
3. Place PDF files in the `input` folder
4. Run Challenge 1A to extract structure
5. Create a configuration file for Challenge 1B
6. Run Challenge 1B for persona-driven analysis
7. Review results in the `output` folder

---

## Project Structure

```
├── Challenge_1a/              
│   ├── src/                  
│   ├── input/                
│   ├── output/               
│   └── main.py               
├── Challange_1b/             
│   ├── approach_explanation.md  
│   ├── challenge1b_processor.py 
│   └── input/                
├── Dockerfile                
└── README.md                 
```

---

Let me know if you'd like this version as a downloadable `.md` file or if you want to integrate images, diagrams, or example outputs.
