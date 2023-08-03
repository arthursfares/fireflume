import streamlit as st

def show_main_page():
    image_url = "https://media.tenor.com/Df5NDKON3WYAAAAC/bugs-bunny-looney-tunes.gif"
    image_html = f"""
        <p style='text-align: center;'>
            <img src='{image_url}' alt='bugs bunny'>
        </p>
    """
    st.markdown(image_html, unsafe_allow_html=True)

def logout_callback():
    st.session_state["logged"] = False

def show_logout_page():
    st.session_state["logged"] = False
    with signout_section:
        st.button("Log out", key="logout", on_click=logout_callback)

def login(email: str, password: str) -> bool:
    if not email or not password:
        return False
    return email == "obiwan" and password == "hellothere"

def login_callback(email, password):
    if login(email, password):
        st.session_state["logged"] = True
    else:
        st.session_state["logged"] = False
        st.error("Invalid email or password")

def show_login_page():
    with signin_section:
        if not st.session_state.get("logged"):
            email = st.text_input(label="Email", placeholder="email")
            password = st.text_input(label="Password", placeholder="password", type="password")
            st.button("Log In", on_click=login_callback, args=(email, password))

header_section = st.container()
signin_section = st.container()
main_section = st.container()
signout_section = st.container()

with header_section:
    st.title("Flume")
    if "logged" not in st.session_state:
        st.session_state["logged"] = False
    if st.session_state["logged"]:
        show_logout_page()
        show_main_page()
    else:
        show_login_page()
