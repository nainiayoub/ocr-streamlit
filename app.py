import streamlit as st
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError


pdf_file = st.file_uploader("Load your PDF file", type="pdf")
languages = {
    'English': 'eng',
    'French': 'fra',
    'Arabic': 'ara',
    'Spanish': 'spa',
}
option = st.selectbox('Select the document language', list(languages.keys()))

st.write('You selected:', option)
@st.cache
def images_to_txt(path):
    images = pdf2image.convert_from_bytes(path)
    all_text = []
    for i in images:
        pil_im = i
        text = pytesseract.image_to_string(pil_im, lang=languages[option])
        # ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
        # ocr_dict now holds all the OCR info including text and location on the image
        # text = " ".join(ocr_dict['text'])
        # text = re.sub('[ ]{2,}', '\n', text)
        all_text.append(text)
    return all_text, len(all_text)

if pdf_file:
    st.info("PDF loaded")
    # stringio = pdf_file.getvalue()
    pdf_path = pdf_file.read()
    st.write(pdf_path)
    texts, nb_pages = images_to_txt(pdf_file.read())
    pages = 'Total pages: '+str(nb_pages)
    st.info(pages)
    output_text = "\n\n".join(texts)
    st.download_button("Download txt", output_text)
