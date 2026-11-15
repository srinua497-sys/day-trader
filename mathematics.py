
import streamlit as st
from config import SUBJECTS, DIFFICULTY_LEVELS

st.title("📐 JEE Mathematics")

chapter = st.selectbox(
    "Select Chapter",
    SUBJECTS["Mathematics"]
)

level = st.selectbox(
    "Difficulty",
    DIFFICULTY_LEVELS
)

tabs = st.tabs([
    "Concepts",
    "Formulas",
    "Shortcuts",
    "Practice"
])

with tabs[0]:
    st.subheader(chapter)
    st.info("Mathematics concepts and solved examples.")

with tabs[1]:
    formulas = [
        "sin²θ + cos²θ = 1",
        "(a+b)² = a² + 2ab + b²",
        "d(xⁿ)/dx = nxⁿ⁻¹",
        "∫xⁿ dx = xⁿ⁺¹/(n+1) + C",
        "Distance = √[(x₂-x₁)²+(y₂-y₁)²]",
        "Slope = (y₂-y₁)/(x₂-x₁)"
    ]

    for f in formulas:
        st.code(f)

with tabs[2]:
    st.write("• Identify the question pattern.")
    st.write("• Apply the shortest valid formula.")
    st.write("• Check domain and restrictions.")
    st.write("• Verify the final answer.")

with tabs[3]:
    st.write("Difficulty:", level)
    st.info("Connect the Mathematics question database.")
