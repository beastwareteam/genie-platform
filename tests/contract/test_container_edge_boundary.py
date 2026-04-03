from pathlib import Path


def _extract_build_edge_section(source: str) -> str:
    start = source.index("def build_edge")
    end = source.index("def build_default")
    return source[start:end]


def test_container_build_edge_uses_facade_contract_only() -> None:
    container_path = Path("src/genie/app/container.py")
    source = container_path.read_text(encoding="utf-8")
    build_edge_section = _extract_build_edge_section(source)

    forbidden_fragments = [
        "core.query_engine",
        "core.task_orchestrator",
        "QueryEngine(",
        "TaskOrchestrator(",
    ]

    for forbidden in forbidden_fragments:
        assert forbidden not in build_edge_section, (
            "Edge wiring boundary violation: build_edge must not wire core orchestration "
            "implementations directly."
        )

    required_fragments = [
        "chat_service=core.application_facade",
        "task_service=core.application_facade",
        "session_service=core.application_facade",
    ]

    for required in required_fragments:
        assert required in build_edge_section, (
            "Edge wiring must use the application facade contract."
        )
