# src/core/authentication/service/firebase_service.py
import logging
from src.adapters.authentication.firebase_adapter import FirebaseAdapter


class FirebaseService:
    def __init__(self, firebase_adapter: FirebaseAdapter):
        self.firebase_adapter = firebase_adapter

    async def register_user(self, email: str, password: str, display_name: str = None):
        logging.info("Registering user with email: %s", email)
        try:
            return self.firebase_adapter.create_user(email, password, display_name)
        except ValueError as e:
            raise ValueError(f"Failed to register user: {str(e)}")

    async def delete_user(self, uid: str):
        logging.info("Deleting user with uid: %s", uid)
        try:
            return self.firebase_adapter.delete_user(uid)
        except ValueError as e:
            raise ValueError(f"Failed to delete user: {str(e)}")
