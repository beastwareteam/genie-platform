from dataclasses import asdict, dataclass

from genie.application.interfaces import ChatService, SessionService, TaskService


@dataclass(frozen=True)
class ServerPromptRequest:
    prompt: str


@dataclass(frozen=True)
class ServerPromptResponse:
    title: str
    output: str
    used_tools: list[str]
    available_tasks: list[str]


class LocalServerEdge:
    def __init__(
        self,
        chat_service: ChatService,
        task_service: TaskService,
        session_service: SessionService,
    ) -> None:
        self._chat_service = chat_service
        self._task_service = task_service
        self._session_service = session_service

    def health(self) -> dict[str, str]:
        return {
            "status": "ok",
            "service": "genie-local-server-edge",
            "title": self._session_service.session_title(),
        }

    def handle_prompt(self, request: ServerPromptRequest) -> ServerPromptResponse:
        result = self._chat_service.run_turn(request.prompt)
        return ServerPromptResponse(
            title=self._session_service.session_title(),
            output=result.output,
            used_tools=result.used_tools,
            available_tasks=self._task_service.available_tasks(),
        )

    def handle_prompt_as_dict(self, request: ServerPromptRequest) -> dict[str, object]:
        response = self.handle_prompt(request)
        return asdict(response)
