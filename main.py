import sys
from dotenv import find_dotenv, load_dotenv
from sanic import Sanic
from sanic.worker.loader import AppLoader
from src.application.api.factories.app_factory import RestAppFactory
from src.application.api.factories.socket_factory import WebsocketAppFactory
from src.config.loader import ConfigLoader
from utils.logger import LoggerConfig


def load_config(app_type: str) -> dict:
    logger = LoggerConfig.get_logger(__name__)
    try:
        logger.info("Loading application configuration...")
        config = ConfigLoader(config_files=["src/config/resources/config.yml", "src/config/resources/rest.yml"])
        app_config = config.get(app_type)
        if not app_config:
            raise ValueError("App configuration is missing or empty.")
        logger.info("Configuration loaded successfully.")
        return app_config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise


def create_app(app_type: str) -> Sanic:
    load_dotenv(dotenv_path=find_dotenv(), verbose=True, override=True)

    logger_config = LoggerConfig(config_path="src/config/resources/logging.yml")
    logger_config.setup_logger()

    logger = LoggerConfig.get_logger(__name__)
    logger.info(f"Starting application setup for app_type: {app_type}")

    app_config = load_config(app_type)

    if app_type == "forefront_rest":
        logger.info("Creating REST application...")
        app_factory = RestAppFactory(app_config)
    elif app_type == "forefront_socket":
        logger.info("Creating WebSocket application...")
        app_factory = WebsocketAppFactory(app_config)
    else:
        logger.error(f"Unknown app type: {app_type}")
        raise ValueError(f"Unknown app type: {app_type}")

    return app_factory.create_app()


def app_factory_loader() -> Sanic:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <app_type>")
        print("app_type: forefront_rest | forefront_socket")
        sys.exit(1)

    app_type = sys.argv[1]
    return create_app(app_type)


if __name__ == "__main__":
    try:
        app_loader = AppLoader(factory=app_factory_loader)
        app = app_loader.load()
        port = app.config.get("port", 8000)
        app.prepare(port=port, debug=True, dev=True, auto_reload=True)
        print("Registered Routes:")
        for i, (uri, route) in enumerate(app.router.routes_all.items(), start=1):
            # `route.handler` è la funzione gestore della rotta
            print(
                f"Route {i}, Name: {route.handler.__name__}, Methods: {', '.join(route.methods)}, URI: /{'/'.join(uri)}"
            )
        Sanic.serve(primary=app, app_loader=app_loader)
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
