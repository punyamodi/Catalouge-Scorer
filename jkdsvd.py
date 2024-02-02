import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.llms import Ollama
from io import BytesIO

llm = Ollama(model="dolphin-mixtral:latest")

def extract_text(pdf_bytes):
    try:
        pdf_reader = PdfReader(BytesIO(pdf_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extractText().replace('\n', '\r\n').strip() + "\r\n"
        return text
    except Exception as e:
        print(f"Error while processing PDF: {e}")
        return None


def model(text):
    #q= "Evaluate this text carefully. This is from a brochure of a product sold online. Rate this catalog out of 100 and suggest changes" + text

    result = llm("jfbgvjhgfbnkj,gbngfkj,bnkf")

    # Display the evaluation result
    st.subheader("Evaluation Result")
    st.write(result)

    return result

def displayPDF(file):
    # Opening file from file path
    '''with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')'''

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{file}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


st.title("Catalog Scanning App")

uploaded_file = st.file_uploader("Upload Catalog PDF", type="pdf")

if uploaded_file:
    #displayPDF(uploaded_file)
    extracted_text = extract_text(uploaded_file)
    evaluated_result = model(extracted_text)
