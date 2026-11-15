
import streamlit as st
from config import SUBJECTS, DIFFICULTY_LEVELS

st.title("⚛️ JEE Physics")

chapters = SUBJECTS["Physics"]

chapter = st.selectbox("Select Chapter", chapters)

level = st.selectbox("Difficulty", DIFFICULTY_LEVELS)

st.divider()

st.subheader(chapter)

tabs = st.tabs([
    "Theory",
    "Formulas",
    "Examples",
    "Practice"
])

with tabs[0]:
    st.info("Physics theory will be loaded from the chapter database.")
    st.write("Understand concepts before solving numerical problems.")

with tabs[1]:
    st.subheader("Important Physics Formulas")

    formulas = [
        "v = u + at",
        "s = ut + 1/2 at²",
        "v² = u² + 2as",
        "F = ma",
        "K.E. = 1/2 mv²",
        "P = W/t",
        "V = IR",
        "F = qvB sinθ"
    ]

    for f in formulas:
        st.code(f)

with tabs[2]:
    st.write("Solved examples will be organized chapter-wise.")

with tabs[3]:
    st.write("Difficulty:", level)
    st.info("Connect the verified question bank to display practice questions.")
