from adapters.websocket.socketio_events.base_event import BaseEvent


class MessageEvent(BaseEvent):
    @property
    def event_name(self) -> str:
        return "message"

    async def handle(self, sid: str, data: dict) -> None:
        print(f"Messaggio ricevuto da {sid}: {data}")
        await self.broadcast({"sid": sid, "message": data})
