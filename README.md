### README.md

```markdown
# PDF Processor

This Python script automates the process of splitting PDF files into individual pages, extracting text from specific regions on the first page, renaming the split PDFs based on the extracted text, and then combining PDFs with the same name into a single file.

## Features

- Splits PDF files into individual pages.
- Extracts text from specific regions of each page.
- Renames the split PDF files based on the extracted text.
- Combines PDFs with the same name into a single file.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pdf-processor.git
   ```
2. Ensure you have Python installed (version 3.6+ recommended).
3. Install the required dependencies using pip:
   ```bash
   pip install PyPDF2 pdfplumber
   ```

## Usage

1. Place the PDF files you want to process in the input directory.
2. Update the paths in the script to match your input and output directories.
3. Run the script:
   ```bash
   python src/pdf_processor.py
   ```

## Configuration

- **Input Directory:** Update the `input_pdf_path` variable with the path to your input PDF files.
- **Output Directory:** Update the `output_folder_path` variable with the path where the split PDFs will be saved.
- **PDF Text Extraction Coordinates:** Adjust the coordinates used for text extraction to match your PDF layout.

## Dependencies

- PyPDF2
- pdfplumber

## Contributing

Feel free to submit pull requests or open issues if you find bugs or have feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### .gitignore

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

