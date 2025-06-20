import streamlit as st
import os

st.set_page_config(page_title="Resume")

st.title("📄 Resume")
st.markdown("___")

st.write("""
Below is a quick visual preview of my resume.  
You can download the full PDF or visit my LinkedIn for more details.

""")

# Show the resume preview image
st.image("resume_preview1.png", caption="Matthew Kiedaisch Resume Preview", use_container_width=True)

st.markdown("---")

# Path to the actual PDF file
resume_path = os.path.join(os.path.dirname(__file__), "..", "Kiedaisch_Matthew_Resume.pdf")

# Download button
with open(resume_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📎 Download Full Resume (PDF)",
    data=PDFbyte,
    file_name="Kiedaisch_Matthew_Resume.pdf",
    mime="application/pdf"
)

# LinkedIn link
st.markdown("""
[🔗 View my LinkedIn](https://www.linkedin.com/in/matthew-kiedaisch)
""")
