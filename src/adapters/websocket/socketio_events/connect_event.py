from adapters.websocket.socketio_events.base_event import BaseEvent


class ConnectEvent(BaseEvent):
    @property
    def event_name(self) -> str:
        return "connect"

    async def handle(self, sid: str, data: dict) -> None:
        print(f"Client connesso: {sid}")
        await self.emit(sid, {"message": "Benvenuto!"})
