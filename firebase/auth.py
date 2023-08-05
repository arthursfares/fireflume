import pyrebase
from .firebase_config import firebase_config

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class AuthFirebase(metaclass=Singleton):
    def __init__(self):
        firebase = pyrebase.initialize_app(firebase_config)
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        response = self.auth.sign_in_with_email_and_password(email, password)
        print(self.auth.current_user)
        # print(response)

    def sign_up(self, email, password):
        response = self.auth.create_user_with_email_and_password(email, password)
        # print(response)

    def sign_out(self):
        print(self.auth.current_user)
        self.auth.current_user = None
        print(self.auth.current_user)
        # print(response)