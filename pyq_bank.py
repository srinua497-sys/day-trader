
import streamlit as st
import json
import os

st.title("📚 JEE Previous Year Questions")

subject = st.selectbox(
    "Subject",
    ["Physics", "Chemistry", "Mathematics"]
)

year = st.selectbox(
    "Select Year",
    list(range(2026, 2001, -1))
)

exam = st.selectbox(
    "Exam",
    ["JEE Mains", "JEE Advanced"]
)

chapter = st.text_input(
    "Chapter Filter (optional)"
)

file_path = "question_bank/questions.json"

if os.path.exists(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        filtered = [
            q for q in questions
            if q.get("subject") == subject
            and str(q.get("year")) == str(year)
            and q.get("exam") == exam
            and (
                not chapter.strip()
                or chapter.lower() in q.get("chapter", "").lower()
            )
        ]

        if filtered:

            for i, q in enumerate(filtered):

                st.subheader(f"Question {i+1}")
                st.write(q.get("question", ""))

                with st.expander("Show Answer"):
                    st.write("Answer:", q.get("answer", "Not available"))
                    st.write(
                        "Explanation:",
                        q.get("explanation", "Not available")
                    )

        else:
            st.warning("No matching questions found.")

    except (json.JSONDecodeError, OSError) as e:
        st.error(f"Question bank error: {e}")

else:
    st.warning("Question bank file not found.")
    st.info("Add verified PYQs to question_bank/questions.json.")
