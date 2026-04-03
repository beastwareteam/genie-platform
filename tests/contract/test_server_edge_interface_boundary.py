from pathlib import Path


def test_server_edge_uses_application_interfaces_only() -> None:
    server_edge_path = Path("src/genie/infrastructure/server/server_edge.py")
    source = server_edge_path.read_text(encoding="utf-8")

    forbidden_imports = [
        "from genie.application.query_engine",
        "from genie.application.task_orchestrator",
        "from genie.presentation",
        "import genie.application.query_engine",
        "import genie.application.task_orchestrator",
        "import genie.presentation",
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source, (
            "Server edge boundary violation: infrastructure/server must not import "
            "orchestration implementations or presentation layer directly."
        )

    assert "from genie.application.interfaces" in source, (
        "Expected LocalServerEdge to consume application interfaces."
    )


def test_http_server_does_not_depend_on_orchestration_implementations() -> None:
    http_server_path = Path("src/genie/infrastructure/server/http_server.py")
    source = http_server_path.read_text(encoding="utf-8")

    forbidden_imports = [
        "from genie.application.query_engine",
        "from genie.application.task_orchestrator",
        "from genie.presentation",
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source, (
            "HTTP server boundary violation: server adapter must stay isolated from "
            "orchestration implementations and presentation."
        )
