from dataclasses import dataclass

from genie.runtime.feature_flags.feature_flags import FeatureFlags
from genie.runtime.tools.registry import ToolRegistry


@dataclass
class QueryResult:
    output: str
    used_tools: list[str]


class QueryEngine:
    def __init__(self, tool_registry: ToolRegistry, feature_flags: FeatureFlags) -> None:
        self._tool_registry = tool_registry
        self._feature_flags = feature_flags

    def run_turn(self, prompt: str) -> QueryResult:
        tools = self._tool_registry.names()
        return QueryResult(
            output=f"Genie processed: {prompt}",
            used_tools=tools,
        )
