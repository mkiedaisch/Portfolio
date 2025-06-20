import streamlit as st
st.set_page_config(
    page_title="Matthew Kiedaisch Portfolio",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown("""
    <style>
        body { font-family: 'Segoe UI', sans-serif; }
        .css-1d391kg { padding-top: 2rem; }
        .css-ffhzg2 { font-size: 18px; }
        .stButton>button {
            background-color: #222;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Matthew Kiedaisch Portfolio", layout="centered")

st.title("Welcome to My Portfolio")
st.write("""
I'm Matthew Kiedaisch, a Mathematics major at UT Austin with a growing passion for quantitative finance, data analytics, and predictive modeling.

This site showcases my personal projects, skillset, and journey toward a career in high-impact problem solving.
""")
