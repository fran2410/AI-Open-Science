# AI-Open-Science

[![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)  [![DOI](https://zenodo.org/badge/.svg)](https://zenodo.org/badge/latestdoi/)  
[![Documentation Status](https://readthedocs.org/projects/grobid/badge/?version=latest)](https://readthedocs.org/projects/grobid/?badge=latest)
[![GitHub release](https://img.shields.io/github/release/fran2410/AI-Open-Science.svg)](https://github.com/fran2410/AI-Open-Science/releases/)

## Description

This repository provides tools for extracting and visualizing information from scientific papers in XML format. Using [GROBID](https://github.com/kermitt2/grobid). for document processing, the scripts generate keyword clouds, charts displaying the number of figures per document, and extract links from XML files.

## Project Structure

```
├── papers/         # Original research papers
├── data/           # XML files 
├── scripts/        # Python scripts for data extraction and visualization
│   ├── keywordCloud.py  # Generates a keyword cloud from abstracts
│   ├── charts.py        # Creates charts showing the number of figures per document
│   ├── list.py          # Extracts links from XML files (excluding references)
├── results/        # Output directory for generated files
├── documentation/  # Additional documentation 
```

## Requirements

### Dependencies

Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt
```

### XML Processing with GROBID

This repository contains scripts and data for processing XML files extracted from research papers using [GROBID](https://github.com/kermitt2/grobid).  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fran2410/AI-Open-Science.git
   cd AI-Open-Science
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

### 1. Generate Keyword Cloud  
Extracts keywords from abstracts in XML files and creates a word cloud.

**Command:**
```bash
python scripts/keywordCloud.py <folder_with_xmls>
```
**Output:** `results/keywordCloud.jpg`

### 2. Chart Figures Count  
Counts the number of figures in each XML file and generates a bar chart.

**Command:**
```bash
python scripts/charts.py <folder_with_xmls>
```
**Output:** `results/charts.jpg`

### 3. Extract Links  
Extracts links from XML files while ignoring references.

**Command:**
```bash
python scripts/list.py <folder_with_xmls>
```
**Output:** `results/links.txt`

## Examples

For a sample execution with provided XML data, see the `results/` directory or run the scripts with sample files in `data/`.

## Where to Get Help

For any issues or questions, please open an issue in the [project issues](https://github.com/fran2410/AI-Open-Science/issues).

## Acknowledgements

Special thanks to the developers of [GROBID](https://github.com/kermitt2/grobid) for their tool for processing scientific documents.

## License

This project is distributed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). Contributions to the project must follow the same licensing terms.

