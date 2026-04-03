from genie.application.interfaces.chat_service import ChatResponse, ChatService
from genie.application.interfaces.session_service import SessionService
from genie.application.interfaces.task_service import TaskService
from genie.application.query_engine.query_engine import QueryEngine
from genie.application.task_orchestrator.task_orchestrator import TaskOrchestrator
from genie.shared.config.settings import AppSettings


class ApplicationFacade(ChatService, TaskService, SessionService):
    def __init__(
        self,
        query_engine: QueryEngine,
        task_orchestrator: TaskOrchestrator,
        settings: AppSettings,
    ) -> None:
        self._query_engine = query_engine
        self._task_orchestrator = task_orchestrator
        self._settings = settings

    def run_turn(self, prompt: str) -> ChatResponse:
        result = self._query_engine.run_turn(prompt)
        return ChatResponse(output=result.output, used_tools=result.used_tools)

    def available_tasks(self) -> list[str]:
        return self._task_orchestrator.available_tasks()

    def session_title(self) -> str:
        return self._settings.app_name
