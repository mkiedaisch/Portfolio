import streamlit as st

st.title("Resume")

with open("resume.pdf", "rb") as file:
    st.download_button(
        label="📥 Download Resume",
        data=file,
        file_name="resume.pdf",
        mime="application/pdf"
    )

st.write("You can also reach me on LinkedIn or via email.")
