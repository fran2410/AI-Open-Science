
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


