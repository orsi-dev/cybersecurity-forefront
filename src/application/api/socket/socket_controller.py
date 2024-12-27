from sanic import Blueprint
from sanic.response import json
from application.authentication.auth_service import AuthService
from infrastructure.messaging.socketio_adapter import SocketIOAdapter

class SocketController:
    def __init__(self, socket_adapter: SocketIOAdapter, auth_service: AuthService):
        self.socket_adapter = socket_adapter
        self.auth_service = auth_service

    async def handle_connect(self, request, ws):
        """Gestisce l'evento di connessione WebSocket."""
        user_token = request.headers.get("Authorization")

        # Validazione del token
        user = await self.auth_service.validate_token(user_token)
        if not user:
            await ws.close()
            return
        
        # Collegamento del client agli eventi
        await self.socket_adapter.register_client(ws, user)
        await ws.send("Connection established!")

    async def handle_message(self, request, ws, data):
        """Gestisce i messaggi WebSocket."""
        # Esempio di inoltro al core degli eventi
        event_type = data.get("event")
        payload = data.get("payload")

        # Routing basato sul tipo di evento
        response = await self.socket_adapter.route_event(event_type, payload)
        await ws.send(response)
