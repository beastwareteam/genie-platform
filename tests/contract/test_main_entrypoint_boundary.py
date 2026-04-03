from pathlib import Path


def test_main_entrypoint_depends_on_bootstrap_only() -> None:
    main_path = Path("src/genie/main.py")
    source = main_path.read_text(encoding="utf-8")

    forbidden_imports = [
        "from genie.application.query_engine",
        "from genie.application.task_orchestrator",
        "from genie.infrastructure.server.http_server import",
        "from genie.presentation",
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source, (
            "Main entry boundary violation: src/genie/main.py must not depend on "
            "orchestration/presentation implementations directly."
        )

    required_import = "from genie.app.bootstrap import bootstrap_application, bootstrap_http_server"
    assert required_import in source, "Main entrypoint should compose through bootstrap only."


def test_main_entrypoint_supports_server_flags() -> None:
    main_path = Path("src/genie/main.py")
    source = main_path.read_text(encoding="utf-8")

    required_fragments = ["--server", "--host", "--port", "bootstrap_http_server("]
    for required in required_fragments:
        assert required in source, "Main entrypoint should expose server mode flags."
