from typing import Protocol


class SessionService(Protocol):
    def session_title(self) -> str:
        ...
