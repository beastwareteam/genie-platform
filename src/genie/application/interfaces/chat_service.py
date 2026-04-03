from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ChatResponse:
    output: str
    used_tools: list[str]


class ChatService(Protocol):
    def run_turn(self, prompt: str) -> ChatResponse:
        ...
