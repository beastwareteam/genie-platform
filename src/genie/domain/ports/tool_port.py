from typing import Protocol


class ToolPort(Protocol):
    name: str

    def execute(self, payload: dict) -> dict:
        ...
