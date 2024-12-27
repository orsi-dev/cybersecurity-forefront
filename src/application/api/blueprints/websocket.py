from sanic import Blueprint
from application.api.socket.socket_controller import SocketController
from infrastructure.messaging.socketio_adapter import SocketIOAdapter
from application.authentication.auth_service import AuthService

def create_websocket_blueprint():
    websocket_blueprint = Blueprint("websocket", url_prefix="/ifws", version=1)
    socket_adapter = SocketIOAdapter()
    auth_service = AuthService()

    controller = SocketController(socket_adapter, auth_service)

    websocket_blueprint.add_websocket_route(controller.handle_connect, "/connect")
    websocket_blueprint.add_websocket_route(controller.handle_message, "/message")

    return websocket_blueprint
