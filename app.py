
import streamlit as st
import random
import json
import os
from datetime import datetime

# ==========================================
# JEE AI PRO - MAIN APPLICATION
# ==========================================

st.set_page_config(
    page_title="JEE AI PRO",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stButton>button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
}
.card {
    background: #1c2433;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "test_answer" not in st.session_state:
    st.session_state.test_answer = None

# ==========================================
# DATA
# ==========================================

SUBJECTS = {
    "Physics": [
        "Units and Dimensions",
        "Kinematics",
        "Laws of Motion",
        "Work Energy Power",
        "Rotational Motion",
        "Gravitation",
        "Thermodynamics",
        "Electrostatics",
        "Current Electricity",
        "Magnetism",
        "Optics",
        "Modern Physics"
    ],

    "Chemistry": [
        "Some Basic Concepts",
        "Atomic Structure",
        "Chemical Bonding",
        "Thermodynamics",
        "Equilibrium",
        "Electrochemistry",
        "Chemical Kinetics",
        "Organic Chemistry",
        "Hydrocarbons",
        "Aldehydes and Ketones",
        "Coordination Compounds"
    ],

    "Mathematics": [
        "Sets and Relations",
        "Complex Numbers",
        "Quadratic Equations",
        "Sequences and Series",
        "Straight Lines",
        "Circle",
        "Conic Sections",
        "Limits",
        "Continuity",
        "Differentiation",
        "Integration",
        "Matrices and Determinants",
        "Probability"
    ]
}

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🎓 JEE AI PRO")

page = st.sidebar.radio(
    "MAIN MENU",
    [
        "Dashboard",
        "Study Material",
        "AI Teacher",
        "Practice Questions",
        "Mock Test",
        "Formula Revision",
        "Performance"
    ]
)

exam = st.sidebar.selectbox(
    "Exam Mode",
    ["JEE Mains", "JEE Advanced"]
)

st.sidebar.markdown("---")
st.sidebar.info("Physics | Chemistry | Mathematics")

# ==========================================
# HEADER
# ==========================================

st.title("🎓 JEE AI PRO")
st.caption("AI Powered JEE Mains & Advanced Preparation")

# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.subheader("Student Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Attempts", st.session_state.attempts)
    c2.metric("Correct Answers", st.session_state.score)

    accuracy = (
        st.session_state.score /
        st.session_state.attempts * 100
        if st.session_state.attempts > 0 else 0
    )

    c3.metric("Accuracy", f"{accuracy:.1f}%")

    st.markdown("---")

    st.subheader("Select Your Subject")

    cols = st.columns(3)

    for i, subject in enumerate(SUBJECTS):
        with cols[i]:
            st.markdown(f"### 📘 {subject}")
            st.write(f"{len(SUBJECTS[subject])} Chapters")
            st.write("Theory | Questions | Revision")

    st.success("Welcome to your JEE preparation journey!")

# ==========================================
# STUDY MATERIAL
# ==========================================

elif page == "Study Material":

    st.subheader("📚 Chapter Wise Learning")

    subject = st.selectbox(
        "Select Subject",
        list(SUBJECTS.keys())
    )

    chapter = st.selectbox(
        "Select Chapter",
        SUBJECTS[subject]
    )

    level = st.radio(
        "Learning Level",
        ["Basic", "JEE Mains", "JEE Advanced"],
        horizontal=True
    )

    st.markdown("---")

    st.subheader(f"{chapter}")

    st.write(f"Subject: {subject}")
    st.write(f"Level: {level}")

    st.info(
        "Chapter content will be loaded from your verified "
        "study material database."
    )

    st.write("### Learning Sections")

    st.checkbox("Theory")
    st.checkbox("Important Formulas")
    st.checkbox("Solved Examples")
    st.checkbox("Practice Problems")
    st.checkbox("PYQ Questions")

# ==========================================
# AI TEACHER
# ==========================================

elif page == "AI Teacher":

    st.subheader("🤖 AI JEE Teacher")

    st.write(
        "Ask your Physics, Chemistry or Mathematics doubts."
    )

    subject = st.selectbox(
        "Subject",
        list(SUBJECTS.keys())
    )

    question = st.text_area(
        "Enter Your Question",
        placeholder="Type your JEE question here..."
    )

    uploaded = st.file_uploader(
        "Upload Question Image",
        type=["png", "jpg", "jpeg"]
    )

    method = st.selectbox(
        "Explanation Type",
        [
            "Detailed Explanation",
            "Shortcut Method",
            "JEE Mains Method",
            "JEE Advanced Method"
        ]
    )

    if st.button("SOLVE QUESTION"):

        if question.strip():
            st.info(
                "Question submitted. Connect an AI API "
                "to generate a verified solution."
            )

            st.write("Selected Subject:", subject)
            st.write("Explanation:", method)

        elif uploaded:
            st.warning(
                "Image uploaded. Connect a vision-capable AI API "
                "to read and solve the image."
            )
        else:
            st.warning("Please enter a question or upload an image.")

# ==========================================
# PRACTICE QUESTIONS
# ==========================================

elif page == "Practice Questions":

    st.subheader("📝 Practice Questions")

    subject = st.selectbox(
        "Subject",
        list(SUBJECTS.keys())
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    st.write("Selected Subject:", subject)
    st.write("Difficulty:", difficulty)

    st.info(
        "Add verified questions to question_bank.json "
        "to enable chapter-wise practice."
    )

# ==========================================
# MOCK TEST
# ==========================================

elif page == "Mock Test":

    st.subheader("⏱️ JEE Mock Test")

    st.write("Exam:", exam)

    questions = [
        {
            "q": "What is the derivative of x²?",
            "options": ["x", "2x", "x²", "2"],
            "answer": "2x"
        },
        {
            "q": "SI unit of force?",
            "options": ["Joule", "Newton", "Watt", "Pascal"],
            "answer": "Newton"
        },
        {
            "q": "Atomic number of Carbon?",
            "options": ["4", "6", "8", "12"],
            "answer": "6"
        }
    ]

    if "mock_questions" not in st.session_state:
        st.session_state.mock_questions = questions

    if "mock_submitted" not in st.session_state:
        st.session_state.mock_submitted = False

    answers = {}

    for i, q in enumerate(st.session_state.mock_questions):

        st.markdown(f"### Q{i+1}. {q['q']}")

        answers[str(i)] = st.radio(
            f"Choose answer {i+1}",
            q["options"],
            key=f"mock_{i}"
        )

    if st.button("SUBMIT TEST"):

        correct = 0

        for i, q in enumerate(st.session_state.mock_questions):
            if answers[str(i)] == q["answer"]:
                correct += 1

        st.session_state.attempts += len(questions)
        st.session_state.score += correct
        st.session_state.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "exam": exam,
            "score": correct,
            "total": len(questions)
        })

        st.session_state.mock_submitted = True
        st.session_state.mock_result = correct

    if st.session_state.mock_submitted:

        correct = st.session_state.mock_result

        st.success(
            f"Your Score: {correct}/{len(questions)}"
        )

        for i, q in enumerate(st.session_state.mock_questions):
            st.write(f"Q{i+1}: Correct Answer: {q['answer']}")

        if st.button("RESTART TEST"):
            st.session_state.mock_submitted = False
            st.rerun()

# ==========================================
# FORMULA REVISION
# ==========================================

elif page == "Formula Revision":

    st.subheader("📐 Formula Revision")

    subject = st.selectbox(
        "Select Subject",
        list(SUBJECTS.keys())
    )

    formulas = {
        "Physics": [
            "v = u + at",
            "s = ut + 1/2 at²",
            "F = ma",
            "K.E. = 1/2 mv²",
            "P = W/t",
            "V = IR"
        ],

        "Chemistry": [
            "PV = nRT",
            "pH = -log[H⁺]",
            "M = Moles / Volume",
            "ΔG = ΔH - TΔS"
        ],

        "Mathematics": [
            "d/dx (xⁿ) = nxⁿ⁻¹",
            "sin²θ + cos²θ = 1",
            "(a+b)² = a² + 2ab + b²",
            "∫xⁿ dx = xⁿ⁺¹/(n+1) + C"
        ]
    }

    for formula in formulas[subject]:
        st.markdown(
            f"<div class='card'>{formula}</div>",
            unsafe_allow_html=True
        )

# ==========================================
# PERFORMANCE
# ==========================================

elif page == "Performance":

    st.subheader("📊 Performance Analysis")

    total = st.session_state.attempts
    correct = st.session_state.score

    accuracy = correct / total * 100 if total else 0

    st.metric("Questions Attempted", total)
    st.metric("Correct Questions", correct)
    st.metric("Accuracy", f"{accuracy:.2f}%")

    if st.session_state.history:

        st.subheader("Mock Test History")

        st.dataframe(
            st.session_state.history,
            use_container_width=True
        )

    else:
        st.info("Complete a mock test to see your performance.")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "JEE AI PRO | Physics • Chemistry • Mathematics | "
    "JEE Mains + Advanced"
)
