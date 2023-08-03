import streamlit as st
from streamlit_extras.row import row

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

def _forgot_password():
    pass

def _show_login_section():
    email = st.text_input(label="email")
    password = st.text_input(label="password", type="password")
    buttons_row = row([1, 1, 1], vertical_align="center")
    buttons_row.button("Sign In", on_click=_login_callback, args=(email, password), type="primary", use_container_width=True)
    buttons_row.button("Create account", on_click=_goto_signup_callback, use_container_width=True)
    buttons_row.button("Forgot password?", on_click=_forgot_password, use_container_width=True)



def _signup_callback():
    st.session_state["signing"] = False

def _show_signup_section():
    email = st.text_input(label="email")
    password = st.text_input(label="password", type="password")
    buttons_row = row(3, vertical_align="center")
    buttons_row.button("Sign Up", on_click=_signup_callback, type="primary", use_container_width=True)



def show_auth_page():
    if not st.session_state["signing"]:
        _show_login_section()
    else:
        _show_signup_section()
