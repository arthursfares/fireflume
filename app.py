import streamlit as st
from streamlit_extras.row import row

from routes.auth_page import show_auth_page
from routes.main_page import show_main_page

def main():
    if "logged" not in st.session_state:
        st.session_state["logged"] = False
        st.session_state["signing"] = False
    if not st.session_state["logged"]:
        title_html = "<p style='text-align: center;'> <img src='https://media.tenor.com/p3JESU9FOfoAAAAi/this-is-fine-fire.gif' width='100'> </p>"
        st.markdown(title_html, unsafe_allow_html=True)
        title_html = "<h3 style='text-align: center;'>fireflume</h3>"
        st.markdown(title_html, unsafe_allow_html=True)
    if st.session_state["logged"]:
        show_main_page()
    else:
        show_auth_page()

if __name__ == "__main__":
    main()
