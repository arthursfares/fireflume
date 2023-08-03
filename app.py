import streamlit as st

from login_page import show_auth_page
from main_page import show_main_page

def main():
    st.title("Flume")
    if "logged" not in st.session_state:
        st.session_state["logged"] = False
        st.session_state["signing"] = False
    if st.session_state["logged"]:
        show_main_page()
    else:
        show_auth_page()

if __name__ == "__main__":
    main()
