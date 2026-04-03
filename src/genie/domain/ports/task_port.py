from typing import Protocol


class TaskPort(Protocol):
    type_name: str

    def run(self, payload: dict) -> dict:
        ...
