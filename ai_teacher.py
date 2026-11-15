
import streamlit as st

st.title("🤖 JEE AI TEACHER")

subject = st.selectbox(
    "Choose Subject",
    ["Physics", "Chemistry", "Mathematics"]
)

level = st.selectbox(
    "Exam Level",
    ["JEE Mains", "JEE Advanced"]
)

language = st.selectbox(
    "Explanation Language",
    ["Telugu + English", "English", "Hindi"]
)

method = st.selectbox(
    "Solution Method",
    [
        "Detailed Solution",
        "Shortcut Method",
        "Fast Calculation",
        "Concept Explanation"
    ]
)

question = st.text_area(
    "Enter Your Question",
    height=150
)

image_file = st.file_uploader(
    "Upload Question Image",
    type=["png", "jpg", "jpeg"]
)

if st.button("SOLVE WITH AI"):

    if question.strip() or image_file:

        st.info("Question received.")

        st.write("Subject:", subject)
        st.write("Exam:", level)
        st.write("Language:", language)
        st.write("Method:", method)

        st.warning(
            "AI API is not connected yet. "
            "Connect ai_engine.py to generate solutions."
        )

    else:
        st.error("Enter a question or upload an image.")
