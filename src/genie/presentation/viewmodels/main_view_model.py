from dataclasses import dataclass

from genie.application.interfaces import ChatService, SessionService, TaskService
from genie.runtime.event_bus.event_bus import EventBus
from genie.runtime.feature_flags.feature_flags import FeatureFlags


@dataclass
class MainViewState:
    title: str
    last_output: str


class MainViewModel:
    def __init__(
        self,
        chat_service: ChatService,
        task_service: TaskService,
        session_service: SessionService,
        event_bus: EventBus,
        feature_flags: FeatureFlags,
    ) -> None:
        self._chat_service = chat_service
        self._task_service = task_service
        self._session_service = session_service
        self._event_bus = event_bus
        self._feature_flags = feature_flags
        self._state = MainViewState(title=self._session_service.session_title(), last_output="Bereit")

    @property
    def state(self) -> MainViewState:
        return self._state

    def submit_prompt(self, prompt: str) -> None:
        result = self._chat_service.run_turn(prompt)
        self._state = MainViewState(title=self._session_service.session_title(), last_output=result.output)
        self._event_bus.publish("query.completed", {"output": result.output})
