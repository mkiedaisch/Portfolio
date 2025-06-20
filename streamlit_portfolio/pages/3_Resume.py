import streamlit as st

st.title("Resume")

with open("../resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download Resume",
                   data=PDFbyte,
                   file_name="Matthew_Kiedaisch_Resume.pdf",
                   mime="application/pdf")
