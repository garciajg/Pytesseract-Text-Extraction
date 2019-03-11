from tempfile import TemporaryDirectory
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, 
                                    PDFPageCountError, 
                                    PDFSyntaxError)

def pdf_to_images(pdf_path="mypdf.pdf"):
    """
    Turns a PDF with multiple pages to a list of images
    using a temporary directory
    """
    with TemporaryDirectory() as path:
        images = convert_from_path(pdf_path, output_folder=path)
        return images

def get_image_text(image=None):
    """
    Reads text from an image using Tesseract framework
    """
    if image == None:
        raise Exception("Missing image")
    text = pytesseract.image_to_string(image)
    return text

# Reading text from PDF turned to images
images = pdf_to_images(pdf_path="mypdf.pdf")
text_from_page_one = get_image_text(images[0])

# Reading text from image of a scanned PDF
text = get_image_text("scanned_pdf.jpeg")
print(text)
