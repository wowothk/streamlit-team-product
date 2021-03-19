import streamlit as st
from lib.progress_report.pr import progress
from lib.planning.pl import planning

def main():
    st.sidebar.title("Kalkula")
    action = st.sidebar.selectbox("Navigation", ["Productivity", "Planning", "Progress Report"])
    if action == "Productivity":
        st.title("Productivity")
    elif action == "Planning":
        st.title("Planning")
        planning()
    elif action == "Progress Report":
        st.title("Progress Report")
        progress()

if __name__ == "__main__":
    main()