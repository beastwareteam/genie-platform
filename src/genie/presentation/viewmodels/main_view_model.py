from dataclasses import dataclass

from genie.application.query_engine.query_engine import QueryEngine
from genie.application.task_orchestrator.task_orchestrator import TaskOrchestrator
from genie.runtime.event_bus.event_bus import EventBus
from genie.runtime.feature_flags.feature_flags import FeatureFlags


@dataclass
class MainViewState:
    title: str
    last_output: str


class MainViewModel:
    def __init__(
        self,
        query_engine: QueryEngine,
        task_orchestrator: TaskOrchestrator,
        event_bus: EventBus,
        feature_flags: FeatureFlags,
    ) -> None:
        self._query_engine = query_engine
        self._task_orchestrator = task_orchestrator
        self._event_bus = event_bus
        self._feature_flags = feature_flags
        self._state = MainViewState(title="Genie", last_output="Bereit")

    @property
    def state(self) -> MainViewState:
        return self._state

    def submit_prompt(self, prompt: str) -> None:
        result = self._query_engine.run_turn(prompt)
        self._state = MainViewState(title="Genie", last_output=result.output)
        self._event_bus.publish("query.completed", {"output": result.output})
