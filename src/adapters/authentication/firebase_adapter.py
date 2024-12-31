from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError

from src.infrastructure.authentication.firebase_client import FirebaseClient


class FirebaseAdapter:

    def __init__(self, firebase_client: FirebaseClient):

        self.firebase_client = firebase_client

    def create_user(self, email: str, password: str, display_name: str = None):
        try:
            user = auth.create_user(email=email, password=password, display_name=display_name)
            return {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name,
            }
        except EmailAlreadyExistsError:
            raise ValueError("Email already in use.")
        # except InvalidPasswordError:
        #     raise ValueError("Invalid password.")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {str(e)}")

    def delete_user(self, uid: str):
        try:
            auth.delete_user(uid)
        except Exception as e:
            raise ValueError(f"Failed to delete user: {str(e)}")
