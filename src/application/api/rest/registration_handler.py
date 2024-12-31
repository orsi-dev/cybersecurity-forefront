import logging

from sanic import json


class RegistrationHandler:
    def __init__(self, service):
        self.service = service  # Dependency Injection
        self.logger = logging.getLogger(self.__class__.__name__)

    async def register_user(self, email: str, password: str, display_name: str) -> dict:
        self.logger.info("Registering user with email: %s", email)
        await self.service.register_user(email, password, display_name)
        self.logger.info("User registered successfully")
        return json({"message": "User registered successfully"}, status=200)

    async def delete_user(self, uid: str) -> dict:
        self.logger.info("Deleting user with uid: %s", uid)
        await self.service.delete_user(uid)
        self.logger.info("User deleted successfully")
        return json({"message": "User deleted successfully"}, status=200)
