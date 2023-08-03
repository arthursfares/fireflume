import streamlit as st

def _login(email: str, password: str) -> bool:
    if not email or not password:
        return False
    return email == "obiwan" and password == "hellothere"

def _login_callback(email, password):
    if _login(email, password):
        st.session_state["logged"] = True
    else:
        st.session_state["logged"] = False
        st.error("Invalid email or password")

def show_login_page():
    with st.container():
        email = st.text_input(label="Email", placeholder="email")
        password = st.text_input(label="Password", placeholder="password", type="password")
        st.button("Log In", on_click=_login_callback, args=(email, password))
