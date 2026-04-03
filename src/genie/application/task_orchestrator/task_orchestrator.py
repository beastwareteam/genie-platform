from genie.runtime.tasks.registry import TaskRegistry


class TaskOrchestrator:
    def __init__(self, task_registry: TaskRegistry) -> None:
        self._task_registry = task_registry

    def available_tasks(self) -> list[str]:
        return self._task_registry.names()
