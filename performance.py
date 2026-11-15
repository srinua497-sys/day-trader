
import streamlit as st
import pandas as pd

st.title("📊 JEE PERFORMANCE ANALYSIS")

if "history" not in st.session_state:
    st.session_state.history = []

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

total = st.session_state.attempts
correct = st.session_state.score

accuracy = (
    correct / total * 100
    if total > 0 else 0
)

c1, c2, c3 = st.columns(3)

c1.metric("Total Questions", total)
c2.metric("Correct Answers", correct)
c3.metric("Accuracy", f"{accuracy:.2f}%")

st.divider()

st.subheader("Mock Test History")

if st.session_state.history:

    df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(
        "Download Performance Excel/CSV",
        df.to_csv(index=False),
        file_name="jee_performance.csv",
        mime="text/csv"
    )

else:
    st.info("Complete mock tests to view your performance.")
