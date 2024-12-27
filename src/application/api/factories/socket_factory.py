# src/application/api/websocket/socket_factory.py
from sanic import Sanic
from socketio import AsyncServer
# from adapters.websocket.socketio_events.connect_event import ConnectEvent
# from adapters.websocket.socketio_events.disconnect_event import DisconnectEvent
# from adapters.websocket.socketio_events.message_event import MessageEvent


class WebsocketAppFactory:
    def __init__(self, config)->None:
        self.config = config
        self.sio = AsyncServer(async_mode="sanic")

    def create_app(self)->Sanic:
        app = Sanic("ForeFront_Socket")
        app.config.update(self.config)
        self.sio.attach(app)
        self._register_event_handlers()
        return app

    def _register_event_handlers(self)->None:
        pass
        # Inizializza e registra gli eventi usando gli adapter
        # connect_event = ConnectEvent(self.sio)
        # disconnect_event = DisconnectEvent(self.sio)
        # message_event = MessageEvent(self.sio)

        # self.sio.on("connect", connect_event.handle)
        # self.sio.on("disconnect", disconnect_event.handle)
        # self.sio.on("user_message", message_event.handle)
