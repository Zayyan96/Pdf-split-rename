# PDF Processing Tool

This project provides a tool to split PDF files into individual pages and rename them based on extracted text from a specific region on the first page. It combines pages into new PDF files with filenames based on extracted text and deletes the original files after processing.

## Features

- Split PDFs into individual pages.
- Extract specific text from the first page of each PDF.
- Rename and combine PDF files based on extracted text.
- Clean up filenames by removing invalid characters.

## Setup

### Prerequisites

- Python 3.x
- `PyPDF2` library
- `pdfplumber` library

Install the required libraries using pip:

```sh
pip install PyPDF2 pdfplumber
