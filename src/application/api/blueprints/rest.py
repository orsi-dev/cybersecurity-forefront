from sanic import Blueprint

from src.application.api.rest.healthcheck_handler import HealthCheckHandler
from src.core.services.health.health_service import HealthService
from src.core.services.service_boostrap import ServiceBootstrap


def if_dynamic_blueprint():
    
    ifrest_blueprint = Blueprint("api", url_prefix="/api", version=1)
    
    # Inizializza gli handler
    handlers = ServiceBootstrap.initialize_handlers()

    routes = ServiceBootstrap.load_routes_from_yaml()
    if not routes:
        raise ValueError("No routes found in the configuration file, exiting...")
    for route in routes:
        handler = handlers[route["handler"]]
        action = getattr(handler, route["action"])  
        ifrest_blueprint.add_route(action, route["url"], methods=route["methods"])
    
    return ifrest_blueprint


