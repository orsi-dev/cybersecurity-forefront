import firebase_admin
from firebase_admin import credentials


class FirebaseClient:
    def __init__(self, cred_path: str):
        self._initialize_firebase(cred_path)

    def _initialize_firebase(self, cred_path: str):
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
