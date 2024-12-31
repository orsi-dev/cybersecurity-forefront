import yaml

from src.adapters.authentication.firebase_adapter import FirebaseAdapter
from src.application.api.rest.healthcheck_handler import HealthCheckHandler
from src.application.api.rest.registration_handler import RegistrationHandler
from src.core.services.authentication.firebase_service import FirebaseService
from src.core.services.health.health_service import HealthService
from src.infrastructure.authentication.firebase_client import FirebaseClient

"""
Factory Pattern per la creazione degli handler.
Service Locator Pattern per il registro centralizzato degli handler.
Externalized Configuration per caricare dinamicamente la configurazione delle rotte da un file YAML.
"""


class ServiceBootstrap:

    def load_routes_from_yaml(file_path="src/config/resources/rest.yml") -> list:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data["rest"]["routes"]

    def initialize_handlers():  # Service Locator Pattern

        firebase_client = FirebaseClient(cred_path="src/config/resources/firebase.json")
        firebase_adapter = FirebaseAdapter(firebase_client=firebase_client)

        return {
            "healthcheck": HealthCheckHandler(HealthService()),
            "user_account": RegistrationHandler(FirebaseService(firebase_adapter=firebase_adapter)),
            # "user": UserHandler(UserService()),
        }
