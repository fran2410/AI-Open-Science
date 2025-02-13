

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
