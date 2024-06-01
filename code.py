import PyPDF2
import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(input_path, file_name)

            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)

                for page_num in range(num_pages):
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                    output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}page{page_num + 1}.pdf')

                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = r'C:\Users\PC\Desktop\Renaming Reports\1. Progress Reports Binders'
    output_folder_path = r'C:\Users\PC\Desktop\Renaming Reports\Progress Reports to be renamed'

    split_pdf(input_pdf_path, output_folder_path)

    # Define the path to your folder containing the PDF files.
pdf_folder = r'C:\Users\Mubasshir PC\Desktop\Renaming Reports\Progress Reports to be renamed'

# List all PDF files in the folder.
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Define a function to clean text for use in file names.
def clean_text(text):
    # Remove invalid characters for file names using regular expressions.
    valid_characters = re.sub(r'[\/:*?"<>|]', '', text)
    # Replace spaces with underscores.
    valid_characters = valid_characters.replace(' ', '_')
    return valid_characters[:100]  # Limit the length of the filename to 100 characters.

# Create a dictionary to store PDF writers for each unique filename.
pdf_writers = {}

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    
    # Open the PDF file using pdfplumber.
    with pdfplumber.open(pdf_path) as pdf:
        # Extract text from a specific region on the first page.
        # Replace (x1, y1, x2, y2) with the coordinates you need for text extraction.
        first_page = pdf.pages[0]
        x1_text, y1_text, x2_text, y2_text = (520, 128, 650, 138)  # Update coordinates for the number
        x1_name, y1_name, x2_name, y2_name = (144, 128, 240, 138)  # Update coordinates for the name
        
        # Extract the number and name from the respective regions.
        number = first_page.crop((x1_text, y1_text, x2_text, y2_text)).extract_text().strip()
        name = first_page.crop((x1_name, y1_name, x2_name, y2_name)).extract_text()
    
    # Clean the extracted text for use in the new file name.
    valid_number = clean_text(number)
    valid_name = clean_text(name)
    
    # Remove problematic characters from the filename
    valid_name = valid_name.replace('\n', '')
    
    # Add the number to the filename
    new_filename = f"{valid_number}_{valid_name} Progress Report.pdf"
    
    # Check if the new_filename already exists in the dictionary.
    if new_filename in pdf_writers:
        # Append the current page to the existing PDF.
        pdf_reader = PdfReader(pdf_path)
        pdf_writer = pdf_writers[new_filename]
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    else:
        # Create a new PDF writer for this unique filename.
        new_path = os.path.join(pdf_folder, new_filename)
        
        # Use PdfWriter instead of PdfFileWriter
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(pdf_path)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # Store the PDF writer in the dictionary.
        pdf_writers[new_filename] = pdf_writer

# Save the combined PDFs to files.
for new_filename, pdf_writer in pdf_writers.items():
    new_path = os.path.join(pdf_folder, new_filename)
    with open(new_path, 'wb') as new_pdf:
        pdf_writer.write(new_pdf)

# Remove the original PDF files after combining them.
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    os.remove(pdf_path)
