
# ==========================================
# JEE AI PRO - CONFIGURATION
# ==========================================

APP_NAME = "JEE AI PRO"
APP_VERSION = "1.0.0"
APP_ICON = "🎓"

# ==========================================
# EXAM SETTINGS
# ==========================================

EXAM_MODES = [
    "JEE Mains",
    "JEE Advanced"
]

SUBJECTS = {
    "Physics": [
        "Units and Dimensions",
        "Kinematics",
        "Laws of Motion",
        "Work Energy Power",
        "Rotational Motion",
        "Gravitation",
        "Properties of Solids and Liquids",
        "Thermodynamics",
        "Kinetic Theory",
        "Oscillations",
        "Waves",
        "Electrostatics",
        "Current Electricity",
        "Magnetism",
        "Electromagnetic Induction",
        "Alternating Current",
        "Electromagnetic Waves",
        "Optics",
        "Dual Nature of Matter",
        "Atoms and Nuclei",
        "Semiconductors",
        "Experimental Skills"
    ],

    "Chemistry": [
        "Some Basic Concepts",
        "Atomic Structure",
        "Chemical Bonding",
        "Chemical Thermodynamics",
        "Solutions",
        "Equilibrium",
        "Redox Reactions",
        "Electrochemistry",
        "Chemical Kinetics",
        "Periodic Table",
        "p-Block Elements",
        "d and f Block Elements",
        "Coordination Compounds",
        "Organic Chemistry Basics",
        "Hydrocarbons",
        "Haloalkanes and Haloarenes",
        "Alcohols Phenols and Ethers",
        "Aldehydes and Ketones",
        "Carboxylic Acids",
        "Amines",
        "Biomolecules",
        "Practical Chemistry"
    ],

    "Mathematics": [
        "Sets and Relations",
        "Complex Numbers",
        "Quadratic Equations",
        "Sequences and Series",
        "Permutations and Combinations",
        "Binomial Theorem",
        "Straight Lines",
        "Circle",
        "Conic Sections",
        "Limits",
        "Continuity and Differentiability",
        "Differentiation",
        "Applications of Derivatives",
        "Indefinite Integration",
        "Definite Integration",
        "Differential Equations",
        "Matrices",
        "Determinants",
        "Vectors",
        "3D Geometry",
        "Probability",
        "Statistics",
        "Trigonometry"
    ]
}

# ==========================================
# DIFFICULTY LEVELS
# ==========================================

DIFFICULTY_LEVELS = [
    "Easy",
    "Medium",
    "Hard",
    "JEE Mains",
    "JEE Advanced",
    "Olympiad Level"
]

# ==========================================
# QUESTION TYPES
# ==========================================

QUESTION_TYPES = [
    "Single Correct",
    "Multiple Correct",
    "Numerical Value",
    "Integer Type",
    "Matrix Match",
    "Assertion Reason"
]

# ==========================================
# AI TEACHER SETTINGS
# ==========================================

AI_SETTINGS = {
    "enabled": False,
    "model": "configure-your-ai-model",
    "temperature": 0.2,
    "max_tokens": 3000,
    "image_solver": False,
    "shortcut_mode": True,
    "detailed_solution": True,
    "telugu_explanation": True
}

# ==========================================
# MOCK TEST SETTINGS
# ==========================================

MOCK_TEST_SETTINGS = {
    "duration_minutes": 180,
    "total_questions": 75,
    "negative_marking": True,
    "show_timer": True,
    "show_result_after_submit": True
}

# These are configurable defaults, not official
# exam rules. Load the relevant year's official
# pattern before generating an actual exam.

# ==========================================
# LEARNING SETTINGS
# ==========================================

LEARNING_SETTINGS = {
    "show_theory": True,
    "show_formulas": True,
    "show_examples": True,
    "show_shortcuts": True,
    "show_pyq": True,
    "show_practice": True
}

# ==========================================
# PERFORMANCE SETTINGS
# ==========================================

PERFORMANCE_SETTINGS = {
    "track_attempts": True,
    "track_accuracy": True,
    "track_weak_chapters": True,
    "save_test_history": True
}

# ==========================================
# DATABASE SETTINGS
# ==========================================

DATABASE_PATH = "database/jee_ai_pro.db"

QUESTION_BANK_PATH = "question_bank/questions.json"

# ==========================================
# APP THEME
# ==========================================

THEME = {
    "background": "#0E1117",
    "card": "#1C2433",
    "primary": "#2563EB",
    "success": "#16A34A",
    "danger": "#DC2626",
    "text": "#FFFFFF"
}

# ==========================================
# LANGUAGE SETTINGS
# ==========================================

LANGUAGES = [
    "English",
    "Telugu",
    "Hindi",
    "Telugu + English"
]

DEFAULT_LANGUAGE = "Telugu + English"

# ==========================================
# SECURITY
# ==========================================

# Never store API keys directly in this file.
# Use Streamlit secrets.toml or environment variables.
