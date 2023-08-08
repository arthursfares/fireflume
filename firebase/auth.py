import pyrebase
import streamlit as st
# from firebase_config import firebase_config

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class AuthFirebase(metaclass=Singleton):
    def __init__(self):
        ''' for config values stored in streamlit secrets '''
        config = {}
        for key in st.secrets:
            config[str(key)] = st.secrets[str(key)]
        firebase = pyrebase.initialize_app(config)
        ''' for config values stored in python firebase_config.py file '''
        # firebase = pyrebase.initialize_app(firebase_config)
        ''' services initialization '''
        self.auth = firebase.auth()
        # self.storage = firebase.storage()
        # self.database = firebase.database()

    def sign_in(self, email, password):
        response = self.auth.sign_in_with_email_and_password(email, password)
        # current user id values can be accessed with self.auth.current_user

    def sign_up(self, email, password):
        response = self.auth.create_user_with_email_and_password(email, password)

    def sign_out(self):
        self.auth.current_user = None

    def reset_password(self, email):
        response = self.auth.send_password_reset_email(email)