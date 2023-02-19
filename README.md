# Automatic reading of text in the image of a document

The aim of this repository is to create a program capable of reading a text written in an image. The image contains a photograph of a page of a document which can be taken with a free angle of view (inclination, perspective effect, etc.). It is therefore a question of estimating this angle of view in order to straighten the image so that it seems to be taken from the front. Then, it is necessary to implement a detection of lines, words and then letters in order to reconstitute the entire text.

![results](docs\res.png "results")

## Prerequisites 

- matplotlib
- opencv
- numpy
- scipy
- python=3.8
- jupyter
- pytesseract

See more in [requirements.txt](requirements.txt) and [environment.yml](environment.yml)

## Installation
1. Install Jupyter Notebook by following the instructions from the official Jupyter website.
2. Install the required Python libraries by running the following command in the terminal:

```bash
pip install -r requirements.txt
```

or create a virtual env with conda (preferred method)

```bash
conda env create -f environment.yml
```

3. Download and install Tesseract OCR from the official Tesseract GitHub repository
 [here](https://github.com/UB-Mannheim/tesseract/wiki).

## Usage
1. Clone or download the repository to your local machine.
2. Open the [`auto_read.ipynb`](auto_read.ipynb) file in Jupyter Notebook.
3. Replace the path to the sample image in the code with the path to your own image.
4. Replace the path to the `tesseract.exe` in the code with the path relative to your own installation.
5. Run the cells in the Jupyter Notebook to see the output.

### With CLI

```bash
python auto_read.py [path to your image (.png or .jpg)]
```
## Result
The output will be the extracted text from the document image. The text will be displayed in a readable format and can be used for further processing or analysis.