import streamlit as st
from streamlit_extras.row import row
from firebase.firebase import Firebase

firebase = Firebase()

def _logout_callback():
    firebase.sign_out()
    st.session_state["logged"] = False

def show_main_page():
    image_url = "https://media.tenor.com/Df5NDKON3WYAAAAC/bugs-bunny-looney-tunes.gif"
    image_html = f"""
        <p style='text-align: center;'>
            <img src='{image_url}' alt='bugs bunny'>
        </p>
    """
    st.markdown(image_html, unsafe_allow_html=True)
    buttons_row = row([1,2,1], vertical_align="center")
    buttons_row.empty()
    buttons_row.button("Sign out", on_click=_logout_callback, use_container_width=True)
    buttons_row.empty()