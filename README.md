# AI-Open-Science

[![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/) 
[![DOI](https://zenodo.org/badge/927066469.svg)](https://doi.org/10.5281/zenodo.14882666) 
[![Documentation Status](https://readthedocs.org/projects/ai-open-science/badge/?version=latest)](https://readthedocs.org/projects/ai-open-science/?badge=latest) 
[![GitHub release](https://img.shields.io/github/release/fran2410/AI-Open-Science.svg)](https://github.com/fran2410/AI-Open-Science/releases/)

## Description

This repository provides tools for extracting and visualizing information from scientific papers in XML format. Using [GROBID](https://github.com/kermitt2/grobid). for document processing, the scripts generate keyword clouds, charts displaying the number of figures per document, and extract links from XML files.

## Features
Given a XML file (or a directory with some of them) the tool will extract the data and make:
- **Keyword Cloud**: Keyword cloud based on the abstract information.
- **Charts**: Charts visualization showing the number of figures per article.
- **Links**: list of the links found in each paper while ignoring references.

## Project Structure

```
├── papers/              # Original research papers
├── data/                # XML files 
├── scripts/             # Python scripts for data extraction and visualization
│   ├── keywordCloud.py  # Generates a keyword cloud from abstracts
│   ├── charts.py        # Creates charts showing the number of figures per document
│   ├── list.py          # Extracts links from XML files (excluding references)
├── results/             # Output directory for generated files
├── docs/                # Additional documentation 
├── tests/               # Tests to check functionality 
```

# Prerequisites

Make sure you have the following installed:
- [Conda](https://docs.conda.io/en/latest/miniconda.html) (Miniconda or Anaconda)
- [Poetry](https://python-poetry.org/docs/#installation)

# Installation

##  Clone the repository:
   ```bash
   git clone https://github.com/fran2410/AI-Open-Science.git
   cd AI-Open-Science
   ```
## Conda

#### Create and activate the Conda environment
```bash
conda create -n ai-open-science python=3.13 
conda activate ai-open-science
```

## Poetry

#### 1. Install Poetry
If you don’t have Poetry installed, run:
```bash
pip install poetry
```

#### 2. Install project dependencies
Run the following command in the root of the repository to install dependencies:
```bash
poetry install
```

## Activate enviroment
Activate the enviroment to start working:
```bash
conda activate ai-open-science
```

## Verify installation
You can check if everything is correctly installed by running:
```bash
python -c "import matplotlib, wordcloud; print('Installation successful')"
```

## Generate Keyword Cloud  
Extracts keywords from abstracts in XML files and creates a word cloud.

**Command:**
```bash
python scripts/keywordCloud.py <folder_with_xmls>
```
**Output:** `results/keywordCloud.jpg`

## Chart Figures Count  
Counts the number of figures in each XML file and generates a bar chart.

**Command:**
```bash
python scripts/charts.py <folder_with_xmls>
```
**Output:** `results/charts.jpg`

## Extract Links  
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

