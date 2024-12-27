# src/application/api/rest/app_factory.py
from sanic import Sanic


from src.application.api.blueprints.rest import if_dynamic_blueprint
from utils.logger import LoggerConfig

# from .user_controller import user_blueprint
# from .session_controller import session_blueprint
logger = LoggerConfig.get_logger(__name__)


class RestAppFactory:

    def __init__(self, config):
        self.config = config

    def create_app(self):

        app = Sanic("ForeFront_REST")
        app.config.update(self.config)

        app.blueprint(if_dynamic_blueprint())

        self._setup_middlewares(app)

        self._setup_exception_handlers(app)

        logger.debug(f"REST app created: {app}")
        if not isinstance(app, Sanic):
            raise ValueError("The factory must return a Forefront sanic app")
        
        return app

    def _setup_middlewares(self, app):
        # Configura middleware specifici
        pass

    def _setup_exception_handlers(self, app):
        # Configura gestori di eccezioni personalizzati
        pass

    def __call__(self):
        return self.create_app()
