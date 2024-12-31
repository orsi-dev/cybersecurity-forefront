import logging
from typing import Any, Dict
from sanic import Blueprint, Request
from sanic.exceptions import InvalidUsage
from src.core.services.service_boostrap import ServiceBootstrap


def map_params(request: Request, params: list) -> Dict[str, Any]:
    """
    Mappa i parametri dal request agli argomenti definiti nel file YAML.
    """
    mapped_params = {}
    for param in params:
        name = param["name"]
        param_type = param["type"]
        required = param.get("required", False)

        # Leggi il parametro dal body o query string
        value = request.json.get(name) if request.json else request.args.get(name)

        if required and value is None:
            raise InvalidUsage(f"Missing required parameter: {name}")

        if value is not None:
            # Converti il tipo
            try:
                mapped_params[name] = eval(param_type)(value)
            except ValueError:
                raise InvalidUsage(f"Invalid value for parameter: {name}")

    return mapped_params


def if_dynamic_blueprint():
    ifrest_blueprint = Blueprint("api", url_prefix="/api", version=1)

    # Inizializza gli handler
    handlers = ServiceBootstrap.initialize_handlers()

    # Carica le rotte dal file YAML
    routes = ServiceBootstrap.load_routes_from_yaml()
    if not routes:
        raise ValueError("No routes found in the configuration file, exiting...")

    for route in routes:
        handler = handlers[route["handler"]]
        action = getattr(handler, route["action"])
        route_name = f"{route['url'].replace('/', '_')}_{route['methods'][0].lower()}"

        async def route_handler(request: Request, handler=action, params=route.get("params", [])):
            mapped_params = map_params(request, params)
            logging.info(f"Request params: {mapped_params}")
            return await handler(**mapped_params)

        ifrest_blueprint.add_route(route_handler, route["url"], methods=route["methods"], name=route_name)

    return ifrest_blueprint
