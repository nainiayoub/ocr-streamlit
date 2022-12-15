import streamlit as st
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError
import re
from io import StringIO

pdf_file = st.file_uploader("Load your PDF file", type="pdf")


def images_to_txt(path):
    images = pdf2image.convert_from_path(path)
    all_text = []
    for i in images:
        pil_im = i
        text = pytesseract.image_to_string(pil_im, lang='eng')
        all_text.append(text)
    return all_text, len(all_text)

if pdf_file:
    st.info("PDF loaded")
    # stringio = pdf_file.getvalue()
    # pdf_path = pdf_file.read()

    texts, nb_pages = images_to_txt(pdf_file.read())
    pages = 'Total pages: '+str(nb_pages)
    st.info(pages)
    # output_text = "\n\n".join(texts)
    st.download_button("Download txt", texts)
    # for i in images:
    #     c = c + 1
    #     pil_im = i # assuming that we're interested in the first page only
    #     ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
    #     # ocr_dict now holds all the OCR info including text and location on the image
    #     text = " ".join(ocr_dict['text'])
        
    #     text = re.sub('[ ]{2,}', '\n', text)
    #     st.write(text)
    #     # text = ' '. join((text.split()))
    #     filename = "page_"+str(c)+".txt"
    #     with open("./"+filename, 'w', encoding="utf-8") as file:
    #         file.write(text)