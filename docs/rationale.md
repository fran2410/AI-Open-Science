# Rationale

This document explains the validation process carried out on the 10 test articles located in the `papers` folder.

## Validation of the Keyword Cloud
For the generation of the keyword cloud, the following steps were followed:
1. The PDFs were processed using the [Contador de palabras](https://www.contadordepalabras.com/) platform to obtain the keyword count of the abstracts.
2. The keyword cloud was generated using the `keywordCloud.py` script.
3. The list of words provided by the platform were compared with:
   - The size of the words in the generated image.
   - The debug messages from the script, which displayed the number of detected words in each document and their content.


## Validation of Figures and Links
To verify that the number of extracted figures and links was correct, the following steps were taken:
1. The `charts.py` script was executed to generate a chart displaying the number of figures per document.
2. Each document in the `papers` folder was manually reviewed to check if the extracted number of figures matched the content of the article.
3. The `list.py` script was executed to extract links from the XML documents.
4. The extracted links were verified to ensure correctness and that they did not include bibliographic references.


This process ensured the reliability of the extracted and validated data in the AI-Open-Science project.

