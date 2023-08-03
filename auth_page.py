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

def _goto_signup_callback():
    st.session_state["signing"] = True

def _show_login_section():
    email = st.text_input(label="Email", placeholder="email")
    password = st.text_input(label="Password", placeholder="password", type="password")
    st.button("Log In", on_click=_login_callback, args=(email, password))
    st.button("Go to sign up", on_click=_goto_signup_callback)



def _signup_callback():
    st.session_state["signing"] = False

def _show_signup_section():
    username = st.text_input(label="Username", placeholder="username")
    email = st.text_input(label="Email", placeholder="email")
    password = st.text_input(label="Password", placeholder="password", type="password")
    st.button("Sign In", on_click=_signup_callback)



def show_auth_page():
    if not st.session_state["signing"]:
        _show_login_section()
    else:
        _show_signup_section()
