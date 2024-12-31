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
