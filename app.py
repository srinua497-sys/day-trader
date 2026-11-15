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

# ------------------------------------------
# STUDY MATERIAL DATABASE
# Add more chapters here: STUDY_CONTENT["Chapter Name"] = {section: markdown}
# ------------------------------------------
STUDY_CONTENT = {
    "Kinematics": {
        "Theory": (
            "Kinematics describes motion without considering its cause.\n\n"
            "- **Displacement** is a vector (change in position); **distance** is a scalar.\n"
            "- **Velocity** = rate of change of displacement; **acceleration** = rate of change of velocity.\n"
            "- For constant acceleration, the three equations of motion apply.\n"
            "- The slope of an x-t graph gives velocity; the slope of a v-t graph gives acceleration; "
            "the area under a v-t graph gives displacement.\n"
            "- In projectile motion, horizontal and vertical motions are independent."
        ),
        "Important Formulas": (
            "- $v = u + at$\n"
            "- $s = ut + \\tfrac{1}{2}at^2$\n"
            "- $v^2 = u^2 + 2as$\n"
            "- Projectile range: $R = \\dfrac{u^2 \\sin 2\\theta}{g}$\n"
            "- Max height: $H = \\dfrac{u^2 \\sin^2\\theta}{2g}$\n"
            "- Time of flight: $T = \\dfrac{2u\\sin\\theta}{g}$"
        ),
        "Solved Examples": (
            "**Example.** A car starts from rest and accelerates at $2\\ \\text{m/s}^2$ for $5$ s. "
            "Find its final velocity and distance covered.\n\n"
            "- $v = u + at = 0 + 2(5) = 10$ m/s\n"
            "- $s = ut + \\tfrac12 at^2 = 0 + \\tfrac12(2)(25) = 25$ m"
        ),
        "Practice Problems": (
            "1. A body is thrown vertically upward at 20 m/s. Find the maximum height ($g = 10\\ \\text{m/s}^2$).\n"
            "2. Find the range of a projectile launched at 30 m/s at 45° ($g = 10\\ \\text{m/s}^2$).\n"
            "3. A train slows from 30 m/s to 10 m/s in 10 s. Find the acceleration and distance covered."
        ),
        "PYQ Questions": "Add verified previous-year questions for this chapter to STUDY_CONTENT.",
    },
    "Laws of Motion": {
        "Theory": (
            "- **Newton's First Law:** a body stays at rest or in uniform motion unless acted on by a net force.\n"
            "- **Newton's Second Law:** net force equals rate of change of momentum.\n"
            "- **Newton's Third Law:** every action has an equal and opposite reaction.\n"
            "- **Friction:** static friction adjusts up to a maximum $\\mu_s N$; kinetic friction is $\\mu_k N$.\n"
            "- Always draw a free-body diagram before writing equations."
        ),
        "Important Formulas": (
            "- $\\vec F = m\\vec a$\n"
            "- $\\vec p = m\\vec v$, $\\ \\vec F = \\dfrac{d\\vec p}{dt}$\n"
            "- $f_s \\le \\mu_s N$, $\\ f_k = \\mu_k N$\n"
            "- Block on incline (smooth): $a = g\\sin\\theta$"
        ),
        "Solved Examples": (
            "**Example.** A 5 kg block is pulled by a 20 N horizontal force on a surface with "
            "kinetic friction of 5 N. Find the acceleration.\n\n"
            "Net force $= 20 - 5 = 15$ N, so $a = F/m = 15/5 = 3\\ \\text{m/s}^2$."
        ),
        "Practice Problems": (
            "1. A 2 kg block rests on a rough surface with $\\mu_s = 0.5$. Find the minimum horizontal force to move it ($g = 10$).\n"
            "2. Find the acceleration of a block sliding down a smooth $30^\\circ$ incline.\n"
            "3. Two masses 3 kg and 2 kg are connected over a smooth pulley. Find the acceleration."
        ),
        "PYQ Questions": "Add verified previous-year questions for this chapter to STUDY_CONTENT.",
    },
    "Complex Numbers": {
        "Theory": (
            "A complex number is $z = a + ib$ with $i^2 = -1$.\n\n"
            "- Modulus: $|z| = \\sqrt{a^2 + b^2}$\n"
            "- Conjugate: $\\bar z = a - ib$, and $z\\bar z = |z|^2$\n"
            "- Polar form: $z = r(\\cos\\theta + i\\sin\\theta) = re^{i\\theta}$\n"
            "- The $n$th roots of unity are equally spaced on the unit circle."
        ),
        "Important Formulas": (
            "- $|z_1 z_2| = |z_1||z_2|$\n"
            "- $|z_1 + z_2| \\le |z_1| + |z_2|$ (triangle inequality)\n"
            "- De Moivre: $(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$\n"
            "- Cube roots of unity: $1 + \\omega + \\omega^2 = 0$, $\\ \\omega^3 = 1$"
        ),
        "Solved Examples": (
            "**Example 1.** Find $|3 + 4i|$.\n\n$\\sqrt{3^2 + 4^2} = 5$.\n\n"
            "**Example 2.** Simplify $(1 + i)^2$.\n\n$1 + 2i + i^2 = 2i$."
        ),
        "Practice Problems": (
            "1. Find the modulus and argument of $1 + i\\sqrt3$.\n"
            "2. Evaluate $\\left(\\dfrac{1+i}{1-i}\\right)^{8}$.\n"
            "3. If $\\omega$ is a cube root of unity, find $(1+\\omega)^3$."
        ),
        "PYQ Questions": "Add verified previous-year questions for this chapter to STUDY_CONTENT.",
    },
}

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
        content = STUDY_CONTENT.get(chapter)
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
