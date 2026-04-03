from dataclasses import dataclass, field

from genie.domain.ports.tool_port import ToolPort


@dataclass
class ToolRegistry:
    _tools: dict[str, ToolPort] = field(default_factory=dict)

    def register(self, tool: ToolPort) -> None:
        self._tools[tool.name] = tool

    def resolve(self, tool_name: str) -> ToolPort:
        return self._tools[tool_name]

    def names(self) -> list[str]:
        return sorted(self._tools.keys())
