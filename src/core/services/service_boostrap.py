import yaml

from src.application.api.rest.healthcheck_handler import HealthCheckHandler
from src.core.services.health.health_service import HealthService
'''
Factory Pattern per la creazione degli handler.
Service Locator Pattern per il registro centralizzato degli handler.
Externalized Configuration per caricare dinamicamente la configurazione delle rotte da un file YAML.
'''

class ServiceBootstrap:
    
    def load_routes_from_yaml(file_path="src/config/resources/rest.yml")->list:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data['rest']['routes']

    def initialize_handlers(): # Service Locator Pattern
        return {
            "healthcheck": HealthCheckHandler(HealthService()), 
            # "user": UserHandler(UserService()),
        }