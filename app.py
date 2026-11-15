import streamlit as st
from datetime import datetime

# ==========================================
# JEE AI PRO - COMPLETE APPLICATION
# Run with:  streamlit run app.py
# ==========================================

st.set_page_config(page_title="JEE AI PRO", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.main { background-color: #0e1117; }
.stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
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
DEFAULT_STATE = {
    "score": 0,
    "attempts": 0,
    "history": [],
    "mock_submitted": False,
    "mock_result": 0,
    "mock_questions": None,
    "study_selection": {},
    "practice_checked": {},
}
for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================
# DATA
# ==========================================
SUBJECTS = {
    "Physics": [
        "Units and Dimensions", "Kinematics", "Laws of Motion",
        "Work Energy Power", "Rotational Motion", "Gravitation",
        "Thermodynamics", "Electrostatics", "Current Electricity",
        "Magnetism", "Optics", "Modern Physics",
    ],
    "Chemistry": [
        "Some Basic Concepts", "Atomic Structure", "Chemical Bonding",
        "Thermodynamics", "Equilibrium", "Electrochemistry",
        "Chemical Kinetics", "Organic Chemistry", "Hydrocarbons",
        "Aldehydes and Ketones", "Coordination Compounds",
    ],
    "Mathematics": [
        "Sets and Relations", "Complex Numbers", "Quadratic Equations",
        "Sequences and Series", "Straight Lines", "Circle",
        "Conic Sections", "Limits", "Continuity", "Differentiation",
        "Integration", "Matrices and Determinants", "Probability",
    ],
}

LEARNING_SECTIONS = [
    "Theory",
    "Important Formulas",
    "Solved Examples",
    "Practice Problems",
    "PYQ Questions",
]

# Study material lives in study_content.py (keep it in the same folder)
from study_content import STUDY_CONTENT

# ------------------------------------------
# PRACTICE QUESTION BANK
# Key: (subject, chapter) -> list of {q, options, answer, explanation, difficulty}
# ------------------------------------------
QUESTION_BANK = {
    ("Physics", "Kinematics"): [
        {"difficulty": "Easy", "q": "A body starts from rest with acceleration 4 m/s². Its velocity after 3 s is?",
         "options": ["6 m/s", "12 m/s", "7 m/s", "24 m/s"], "answer": "12 m/s",
         "explanation": "v = u + at = 0 + 4×3 = 12 m/s."},
        {"difficulty": "Medium", "q": "A ball is thrown up at 20 m/s (g = 10 m/s²). Maximum height reached?",
         "options": ["10 m", "20 m", "40 m", "5 m"], "answer": "20 m",
         "explanation": "H = u²/2g = 400/20 = 20 m."},
        {"difficulty": "Hard", "q": "For the same speed, which launch angle gives the maximum projectile range on level ground?",
         "options": ["30°", "45°", "60°", "90°"], "answer": "45°",
         "explanation": "R ∝ sin 2θ, which is maximum when 2θ = 90°."},
    ],
    ("Physics", "Laws of Motion"): [
        {"difficulty": "Easy", "q": "A 2 kg mass is acted on by a net force of 10 N. Its acceleration is?",
         "options": ["5 m/s²", "20 m/s²", "0.2 m/s²", "12 m/s²"], "answer": "5 m/s²",
         "explanation": "a = F/m = 10/2 = 5 m/s²."},
        {"difficulty": "Medium", "q": "Acceleration of a block on a smooth 30° incline (g = 10 m/s²)?",
         "options": ["10 m/s²", "5 m/s²", "8.66 m/s²", "2.5 m/s²"], "answer": "5 m/s²",
         "explanation": "a = g sin 30° = 10 × 0.5 = 5 m/s²."},
    ],
    ("Mathematics", "Complex Numbers"): [
        {"difficulty": "Easy", "q": "The value of i⁴ is?",
         "options": ["-1", "1", "i", "-i"], "answer": "1",
         "explanation": "i² = -1, so i⁴ = (i²)² = 1."},
        {"difficulty": "Medium", "q": "The modulus of 3 + 4i is?",
         "options": ["7", "5", "25", "1"], "answer": "5",
         "explanation": "√(9 + 16) = 5."},
        {"difficulty": "Medium", "q": "If ω is a non-real cube root of unity, 1 + ω + ω² equals?",
         "options": ["1", "-1", "0", "ω"], "answer": "0",
         "explanation": "The sum of all cube roots of unity is zero."},
    ],
    ("Chemistry", "Atomic Structure"): [
        {"difficulty": "Easy", "q": "The number of electrons in a neutral carbon atom is?",
         "options": ["4", "6", "8", "12"], "answer": "6",
         "explanation": "Carbon has atomic number 6."},
        {"difficulty": "Medium", "q": "Maximum number of electrons in the n = 3 shell is?",
         "options": ["8", "18", "32", "2"], "answer": "18",
         "explanation": "Capacity = 2n² = 2×9 = 18."},
    ],
}

FORMULAS = {
    "Physics": ["v = u + at", "s = ut + 1/2 at²", "F = ma",
                "K.E. = 1/2 mv²", "P = W/t", "V = IR"],
    "Chemistry": ["PV = nRT", "pH = -log[H⁺]", "M = Moles / Volume", "ΔG = ΔH - TΔS"],
    "Mathematics": ["d/dx (xⁿ) = nxⁿ⁻¹", "sin²θ + cos²θ = 1",
                    "(a+b)² = a² + 2ab + b²", "∫xⁿ dx = xⁿ⁺¹/(n+1) + C"],
}

MOCK_QUESTIONS = [
    {"q": "What is the derivative of x²?", "options": ["x", "2x", "x²", "2"], "answer": "2x"},
    {"q": "SI unit of force?", "options": ["Joule", "Newton", "Watt", "Pascal"], "answer": "Newton"},
    {"q": "Atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": "6"},
]

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("🎓 JEE AI PRO")
page = st.sidebar.radio(
    "MAIN MENU",
    ["Dashboard", "Study Material", "AI Teacher", "Practice Questions",
     "Mock Test", "Formula Revision", "Performance"],
)
exam = st.sidebar.selectbox("Exam Mode", ["JEE Mains", "JEE Advanced"])
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
    accuracy = (st.session_state.score / st.session_state.attempts * 100
                if st.session_state.attempts else 0)
    c3.metric("Accuracy", f"{accuracy:.1f}%")
    st.markdown("---")
    st.subheader("Select Your Subject")
    cols = st.columns(3)
    for i, subject_name in enumerate(SUBJECTS):
        with cols[i]:
            st.markdown(f"### 📘 {subject_name}")
            st.write(f"{len(SUBJECTS[subject_name])} Chapters")
            st.write("Theory | Questions | Revision")
    st.success("Welcome to your JEE preparation journey!")

# ==========================================
# STUDY MATERIAL
# ==========================================
elif page == "Study Material":
    st.subheader("📚 Chapter Wise Learning")

    subject = st.selectbox("Select Subject", list(SUBJECTS.keys()))
    chapter = st.selectbox("Select Chapter", SUBJECTS[subject])
    level = st.radio("Learning Level", ["Basic", "JEE Mains", "JEE Advanced"], horizontal=True)

    st.markdown("---")
    st.subheader(chapter)
    st.write(f"Subject: {subject}  |  Level: {level}")

    st.write("### Learning Sections")
    selected_sections = []
    for section in LEARNING_SECTIONS:
        if st.checkbox(section, key=f"study_{subject}_{chapter}_{section}"):
            selected_sections.append(section)

    if st.button("SUBMIT / LOAD CHAPTER", type="primary",
                 use_container_width=True, key="submit_study_material"):
        if not selected_sections:
            st.warning("Please select at least one learning section.")
        else:
            st.session_state.study_selection = {
                "subject": subject,
                "chapter": chapter,
                "level": level,
                "sections": selected_sections,
            }

    # Render from session state so content stays visible across reruns
    sel = st.session_state.study_selection
    if sel and sel["subject"] == subject and sel["chapter"] == chapter:
        st.success(f"Loaded: {chapter} ({sel['level']})")
        content = STUDY_CONTENT.get((subject, chapter))
        if content is None:
            st.info(
                f"Content for **{chapter}** is not added yet. "
                "Add it to STUDY_CONTENT in app.py to display it here."
            )
            for s in sel["sections"]:
                st.write(f"✅ {s}")
        else:
            for s in sel["sections"]:
                with st.expander(f"📖 {s}", expanded=True):
                    st.markdown(content.get(s, "Content not available."))

# ==========================================
# AI TEACHER
# ==========================================
elif page == "AI Teacher":
    st.subheader("🤖 AI JEE Teacher")
    st.write("Ask your Physics, Chemistry or Mathematics doubts.")
    subject = st.selectbox("Subject", list(SUBJECTS.keys()))
    question = st.text_area("Enter Your Question", placeholder="Type your JEE question here...")
    uploaded = st.file_uploader("Upload Question Image", type=["png", "jpg", "jpeg"])
    method = st.selectbox(
        "Explanation Type",
        ["Detailed Explanation", "Shortcut Method", "JEE Mains Method", "JEE Advanced Method"],
    )
    if st.button("SOLVE QUESTION", type="primary"):
        if question.strip():
            st.info("Question received. Connect an AI API to generate a verified step-by-step solution.")
            st.write("Selected Subject:", subject)
            st.write("Explanation:", method)
            st.text_area("Your submitted question", value=question, disabled=True)
        elif uploaded is not None:
            st.image(uploaded, caption="Uploaded question", use_container_width=True)
            st.warning("Image received. Connect a vision-capable AI API to read and solve the image.")
        else:
            st.warning("Please enter a question or upload an image.")

# ==========================================
# PRACTICE QUESTIONS
# ==========================================
elif page == "Practice Questions":
    st.subheader("📝 Practice Questions")
    subject = st.selectbox("Subject", list(SUBJECTS.keys()))
    chapter = st.selectbox("Chapter", SUBJECTS[subject])
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    bank = [q for q in QUESTION_BANK.get((subject, chapter), [])
            if q["difficulty"] == difficulty]

    if not bank:
        st.info(
            f"No {difficulty} questions for {chapter} yet. "
            "Add them to QUESTION_BANK in app.py."
        )
    else:
        base = f"practice_{subject}_{chapter}_{difficulty}"
        for i, q in enumerate(bank):
            st.markdown(f"### Q{i+1}. {q['q']}")
            st.radio("Choose answer", q["options"], index=None, key=f"{base}_{i}")

        if st.button("CHECK ANSWERS", type="primary", key=f"{base}_check"):
            st.session_state.practice_checked[base] = True
            for i, q in enumerate(bank):
                choice = st.session_state.get(f"{base}_{i}")
                if choice is not None:
                    st.session_state.attempts += 1
                    if choice == q["answer"]:
                        st.session_state.score += 1

        if st.session_state.practice_checked.get(base):
            st.markdown("---")
            for i, q in enumerate(bank):
                choice = st.session_state.get(f"{base}_{i}")
                if choice is None:
                    st.warning(f"Q{i+1}: not answered. Correct answer: {q['answer']}")
                elif choice == q["answer"]:
                    st.success(f"Q{i+1}: Correct ✅  {q['explanation']}")
                else:
                    st.error(f"Q{i+1}: Wrong ❌ Correct answer: {q['answer']}. {q['explanation']}")

# ==========================================
# MOCK TEST
# ==========================================
elif page == "Mock Test":
    st.subheader("⏱️ JEE Mock Test")
    st.write("Exam:", exam)

    if st.session_state.mock_questions is None:
        st.session_state.mock_questions = MOCK_QUESTIONS

    answers = {}
    for i, q in enumerate(st.session_state.mock_questions):
        st.markdown(f"### Q{i+1}. {q['q']}")
        answers[str(i)] = st.radio(f"Choose answer {i+1}", q["options"], key=f"mock_answer_{i}")

    if st.button("SUBMIT TEST", type="primary"):
        correct = sum(1 for i, q in enumerate(st.session_state.mock_questions)
                      if answers[str(i)] == q["answer"])
        total_questions = len(st.session_state.mock_questions)
        st.session_state.attempts += total_questions
        st.session_state.score += correct
        st.session_state.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "exam": exam,
            "score": correct,
            "total": total_questions,
        })
        st.session_state.mock_submitted = True
        st.session_state.mock_result = correct

    if st.session_state.mock_submitted:
        correct = st.session_state.mock_result
        total_questions = len(st.session_state.mock_questions)
        st.success(f"Your Score: {correct}/{total_questions}")
        for i, q in enumerate(st.session_state.mock_questions):
            st.write(f"Q{i+1}: Correct Answer: {q['answer']}")
        if st.button("RESTART TEST"):
            st.session_state.mock_submitted = False
            st.session_state.mock_result = 0
            st.rerun()

# ==========================================
# FORMULA REVISION
# ==========================================
elif page == "Formula Revision":
    st.subheader("📐 Formula Revision")
    subject = st.selectbox("Select Subject", list(SUBJECTS.keys()))
    for formula in FORMULAS[subject]:
        st.markdown(f"<div class='card'>{formula}</div>", unsafe_allow_html=True)

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
        st.dataframe(st.session_state.history, use_container_width=True)
    else:
        st.info("Complete a mock test to see your performance.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.caption("JEE AI PRO | Physics • Chemistry • Mathematics | JEE Mains + Advanced")
