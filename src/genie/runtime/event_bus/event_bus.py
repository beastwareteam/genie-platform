from collections.abc import Callable

EventHandler = Callable[[str, dict], None]


class EventBus:
    def __init__(self) -> None:
        self._handlers: list[EventHandler] = []

    def subscribe(self, handler: EventHandler) -> None:
        self._handlers.append(handler)

    def publish(self, event_name: str, payload: dict) -> None:
        for handler in self._handlers:
            handler(event_name, payload)
