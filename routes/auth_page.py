import streamlit as st
from streamlit_extras.row import row
from firebase.auth import AuthFirebase

auth_firebase = AuthFirebase(); 

def _login(email: str, password: str) -> bool:
    if not email or not password:
        return False
    try:
        auth_firebase.sign_in(email, password)
        return True
    except:
        st.error("Invalid email or password")
        return False

def _login_callback(email, password):
    if _login(email, password):
        st.session_state["logged"] = True
    else:
        st.session_state["logged"] = False
    clear_text_input()
        

def _goto_signup_callback():
    st.session_state["signing"] = True
    clear_text_input()

def _forgot_password():
    pass

def _show_login_section():
    email = st.text_input(label="email", key="signin_email")
    password = st.text_input(label="password", type="password", key="signin_password")
    buttons_row = row([1, 1, 1], vertical_align="center")
    buttons_row.button("Sign In", on_click=_login_callback, args=(email, password), type="primary", use_container_width=True)
    buttons_row.button("Create account", on_click=_goto_signup_callback, use_container_width=True)
    buttons_row.button("Forgot password?", on_click=_forgot_password, use_container_width=True)



def _signup_callback(email: str, password: str, confirm_password: str):
    if password != confirm_password:
        st.error("passwords don't match")
    else:
        try:
            auth_firebase.sign_up(email, password)
            st.info("Success", icon="⭐")
            st.session_state["signing"] = False
        except:
            st.error("Inform a valid email and password")
    clear_text_input()

def _goto_signin_callback():
    st.session_state["signing"] = False
    clear_text_input()

def _show_signup_section():
    email = st.text_input(label="email", key="signup_email")
    password = st.text_input(label="password", type="password", key="signup_password")
    confirm_password = st.text_input(label="confirm password", type="password", key="signup_confirm_password")
    buttons_row = row(3, vertical_align="center")
    buttons_row.button("Sign Up", on_click=_signup_callback, args=(email, password, confirm_password), type="primary", use_container_width=True)
    buttons_row.button("Sign In", on_click=_goto_signin_callback, use_container_width=True)

def show_auth_page():
    if not st.session_state["signing"]:
        _show_login_section()
    else:
        _show_signup_section()

def clear_text_input():
    st.session_state["signin_email"] = ""
    st.session_state["signin_password"] = ""
    st.session_state["signup_email"] = ""
    st.session_state["signup_password"] = ""
    st.session_state["signup_confirm_password"] = ""