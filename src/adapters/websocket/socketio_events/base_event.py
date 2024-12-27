from typing import Any, Dict
from abc import ABC, abstractmethod


class BaseEvent(ABC):
    """
    Classe base per tutti gli eventi WebSocket.
    Ogni evento specifico deve estendere questa classe e implementare il metodo `handle`.
    """

    def __init__(self, socket_adapter):
        """
        Inizializza l'evento con un adapter Socket.IO.
        :param socket_adapter: L'adapter che gestisce la comunicazione WebSocket.
        """
        self.socket_adapter = socket_adapter

    @property
    @abstractmethod
    def event_name(self) -> str:
        """
        Nome dell'evento. Deve essere implementato dalle sottoclassi.
        """
        pass

    @abstractmethod
    async def handle(self, sid: str, data: Dict[str, Any]) -> None:
        """
        Metodo che gestisce la logica dell'evento.
        :param sid: ID della sessione del client.
        :param data: Dati ricevuti dall'evento.
        """
        pass

    async def emit(self, sid: str, data: Dict[str, Any]) -> None:
        """
        Emette un messaggio al client.
        :param sid: ID della sessione del client.
        :param data: Dati da inviare.
        """
        await self.socket_adapter.emit(self.event_name, data, room=sid)

    async def broadcast(self, data: Dict[str, Any]) -> None:
        """
        Invia un messaggio a tutti i client connessi.
        :param data: Dati da inviare.
        """
        await self.socket_adapter.emit(self.event_name, data)
