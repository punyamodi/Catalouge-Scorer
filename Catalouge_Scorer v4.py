import base64
import streamlit as st
import PyPDF2
from langchain_community.llms import Ollama
import os

llm = Ollama(model="dolphin-mistral:7b-v2-q8_0")

def model(text):
    question="summarize the text: '"+text+"'"#summarize the text ke jaqah jo model se karwana hai woh dalna hoga
    result = llm.invoke(question)
    st.subheader("Evaluation Result")
    st.write(result)
    return result

def displayPDF(file):
    # Opening file from file path
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title("Catalog Scanning App")

pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

if pdf_file is not None:
    displayPDF(pdf_file)

    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Extract the content
    content = ""
    for page in range(len(pdf_reader.pages)):
        content += pdf_reader.pages[page].extract_text()

    model(content)