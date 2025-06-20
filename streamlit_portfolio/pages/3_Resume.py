import streamlit as st
import os

st.title("Resume")

# Dynamically get path to resume
resume_path = os.path.join(os.path.dirname(__file__), "..", "resume.pdf")

with open(resume_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download Resume",
                   data=PDFbyte,
                   file_name="Matthew_Kiedaisch_Resume.pdf",
                   mime="application/pdf")
