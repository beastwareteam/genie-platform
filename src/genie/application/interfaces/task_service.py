from typing import Protocol


class TaskService(Protocol):
    def available_tasks(self) -> list[str]:
        ...
