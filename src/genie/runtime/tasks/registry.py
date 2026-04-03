from dataclasses import dataclass, field

from genie.domain.ports.task_port import TaskPort


@dataclass
class TaskRegistry:
    _tasks: dict[str, TaskPort] = field(default_factory=dict)

    def register(self, task: TaskPort) -> None:
        self._tasks[task.type_name] = task

    def resolve(self, task_type: str) -> TaskPort:
        return self._tasks[task_type]

    def names(self) -> list[str]:
        return sorted(self._tasks.keys())
