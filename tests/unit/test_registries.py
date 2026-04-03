from genie.runtime.tasks.registry import TaskRegistry
from genie.runtime.tools.registry import ToolRegistry


class DummyTool:
    name = "dummy"

    def execute(self, payload: dict) -> dict:
        return payload


class DummyTask:
    type_name = "dummy_task"

    def run(self, payload: dict) -> dict:
        return payload


def test_tool_registry_register_and_resolve() -> None:
    registry = ToolRegistry()
    tool = DummyTool()
    registry.register(tool)
    assert registry.resolve("dummy") is tool


def test_task_registry_register_and_resolve() -> None:
    registry = TaskRegistry()
    task = DummyTask()
    registry.register(task)
    assert registry.resolve("dummy_task") is task
