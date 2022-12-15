import streamlit as st
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError
import re
from io import StringIO

pdf_file = st.file_uploader("Load your PDF file", type="pdf")

if pdf_file:
    st.info("PDF loaded")
    # stringio = pdf_file.getvalue()
    # pdf_path = pdf_file.read()
    images = pdf2image.convert_from_bytes(pdf_file.read())
    c = 0
    for i in images:
        c = c + 1
        pil_im = i # assuming that we're interested in the first page only
        ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
        # ocr_dict now holds all the OCR info including text and location on the image
        text = " ".join(ocr_dict['text'])
        
        text = re.sub('[ ]{2,}', '\n', text)
        print(text)
        # text = ' '. join((text.split()))
        filename = "page_"+str(c)+".txt"
        with open("./"+filename, 'w', encoding="utf-8") as file:
            file.write(text)