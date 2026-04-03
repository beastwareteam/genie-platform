from pathlib import Path


def test_bootstrap_avoids_direct_orchestration_dependencies() -> None:
    bootstrap_path = Path("src/genie/app/bootstrap.py")
    source = bootstrap_path.read_text(encoding="utf-8")

    forbidden_imports = [
        "from genie.application.query_engine",
        "from genie.application.task_orchestrator",
        "import genie.application.query_engine",
        "import genie.application.task_orchestrator",
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source, (
            "Bootstrap boundary violation: app/bootstrap.py must not depend on "
            "orchestration implementations directly."
        )


def test_bootstrap_uses_container_and_edge_factories() -> None:
    bootstrap_path = Path("src/genie/app/bootstrap.py")
    source = bootstrap_path.read_text(encoding="utf-8")

    required_fragments = [
        "ApplicationContainer.build_default()",
        "return container.edge.server_edge",
        "return LocalHttpServer(edge=edge, host=host, port=port)",
    ]

    for required in required_fragments:
        assert required in source, (
            "Bootstrap should compose app through container/edge factories."
        )
