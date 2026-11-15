
import streamlit as st
from config import SUBJECTS, DIFFICULTY_LEVELS

st.title("🧪 JEE Chemistry")

chapter = st.selectbox(
    "Select Chapter",
    SUBJECTS["Chemistry"]
)

level = st.selectbox(
    "Difficulty",
    DIFFICULTY_LEVELS
)

st.divider()

tabs = st.tabs([
    "Theory",
    "Reactions",
    "Shortcuts",
    "Practice"
])

with tabs[0]:
    st.subheader(chapter)
    st.info("Chapter-wise Chemistry theory database.")

with tabs[1]:
    st.subheader("Important Reactions")

    reactions = [
        "Aldehyde + HCN → Cyanohydrin",
        "RCHO + [O] → RCOOH",
        "RCOOH + LiAlH4 → RCH2OH",
        "RCHO + H2 → RCH2OH",
        "Alcohol → Alkene + H2O"
    ]

    for reaction in reactions:
        st.write("•", reaction)

with tabs[2]:
    st.subheader("Chemistry Shortcuts")
    st.write("1. Identify the functional group.")
    st.write("2. Check reagent and reaction conditions.")
    st.write("3. Identify major product.")
    st.write("4. Verify stability and selectivity.")

with tabs[3]:
    st.write("Difficulty:", level)
    st.info("Verified Chemistry question bank integration pending.")
