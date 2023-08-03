import streamlit as st

def _logout_callback():
    st.session_state["logged"] = False

def show_main_page():
    st.button("Log out", key="logout", on_click=_logout_callback)
    image_url = "https://media.tenor.com/Df5NDKON3WYAAAAC/bugs-bunny-looney-tunes.gif"
    image_html = f"""
        <p style='text-align: center;'>
            <img src='{image_url}' alt='bugs bunny'>
        </p>
    """
    st.markdown(image_html, unsafe_allow_html=True)
