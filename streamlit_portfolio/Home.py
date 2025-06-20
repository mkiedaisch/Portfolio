import streamlit as st

st.set_page_config(page_title="Matthew Kiedaisch Portfolio", layout="centered")

st.title("👋 Welcome")
st.markdown("___")

st.write(
    """
    Thanks for stopping by — I’m **Matthew Kiedaisch**, a student at UT Austin studying **Mathematics**, with a focus on applying data, logic, and performance to real-world systems. 

    Whether it’s through building simulation models, breaking down complex ideas, or refining my approach in and out of the gym, I’m driven by **precision, challenge, and long-term growth**.

    This site is a snapshot of that mindset — a place to showcase what I’m building and where I’m headed. 
    """
)

st.markdown("---")

st.write("🧭 **Explore the Site:**")

st.page_link("pages/1_About.py", label="👤 About Me", icon="📌")
st.page_link("pages/2_Projects.py", label="📊 Projects", icon="🧠")
st.page_link("pages/3_Resume.py", label="📎 Resume", icon="📄")

st.markdown("___")
st.caption("UT Austin | Math & Finance & CS | Built by me. | Work in Progress with much more to come.")
