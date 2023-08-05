import streamlit as st
from streamlit_extras.row import row
from auth_firebase import AuthFirebase

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

def _show_signup_section():
    email = st.text_input(label="email")
    password = st.text_input(label="password", type="password")
    confirm_password = st.text_input(label="confirm password", type="password")
    buttons_row = row(3, vertical_align="center")
    buttons_row.button("Sign Up", on_click=_signup_callback, args=(email, password, confirm_password), type="primary", use_container_width=True)

def show_auth_page():
    if not st.session_state["signing"]:
        _show_login_section()
    else:
        _show_signup_section()
