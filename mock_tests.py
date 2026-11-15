
import streamlit as st
import random
import time

st.title("⏱️ JEE MOCK TEST")

subject = st.selectbox(
    "Subject",
    ["Physics", "Chemistry", "Mathematics", "Full Test"]
)

difficulty = st.selectbox(
    "Level",
    ["JEE Mains", "JEE Advanced"]
)

duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=360,
    value=60
)

sample_questions = [
    {
        "question": "Derivative of x²?",
        "options": ["x", "2x", "2", "x²"],
        "answer": "2x"
    },
    {
        "question": "SI unit of force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": "Newton"
    }
]

if "mock_started" not in st.session_state:
    st.session_state.mock_started = False

if "mock_start_time" not in st.session_state:
    st.session_state.mock_start_time = None

if "mock_questions_page" not in st.session_state:
    st.session_state.mock_questions_page = []

if not st.session_state.mock_started:

    if st.button("START MOCK TEST"):

        st.session_state.mock_questions_page = sample_questions
        st.session_state.mock_start_time = time.time()
        st.session_state.mock_started = True
        st.rerun()

if st.session_state.mock_started:

    elapsed = time.time() - st.session_state.mock_start_time
    remaining = max(0, int(duration * 60 - elapsed))

    st.metric(
        "Time Remaining",
        f"{remaining // 60:02d}:{remaining % 60:02d}"
    )

    answers = {}

    for i, q in enumerate(st.session_state.mock_questions_page):

        st.subheader(f"Q{i+1}. {q['question']}")

        answers[i] = st.radio(
            "Select Answer",
            q["options"],
            key=f"mock_page_{i}"
        )

    if st.button("SUBMIT TEST") or remaining == 0:

        score = 0

        for i, q in enumerate(st.session_state.mock_questions_page):
            if answers.get(i) == q["answer"]:
                score += 1

        st.session_state.mock_result_page = score
        st.session_state.mock_started = False

        st.success(
            f"Your score: {score}/{len(st.session_state.mock_questions_page)}"
        )

        st.rerun()
