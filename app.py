import streamlit as st
from streamlit_extras.row import row

from routes.auth_page import show_auth_page
from routes.main_page import show_main_page

def main():
    title_html = "<h1 style='text-align: center;'>Flume</h1>"
    st.markdown(title_html, unsafe_allow_html=True)
    if "logged" not in st.session_state:
        st.session_state["logged"] = False
        st.session_state["signing"] = False
    if st.session_state["logged"]:
        show_main_page()
    else:
        show_auth_page()

if __name__ == "__main__":
    main()
