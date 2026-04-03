from pathlib import Path


def test_main_view_model_does_not_import_orchestration_implementations() -> None:
    view_model_path = Path("src/genie/presentation/viewmodels/main_view_model.py")
    source = view_model_path.read_text(encoding="utf-8")

    forbidden_imports = [
        "from genie.application.query_engine",
        "from genie.application.task_orchestrator",
        "import genie.application.query_engine",
        "import genie.application.task_orchestrator",
    ]

    for forbidden in forbidden_imports:
        assert forbidden not in source, (
            "ViewModel boundary violation: presentation/viewmodels must not import "
            "query_engine or task_orchestrator implementations directly."
        )

    assert "from genie.application.interfaces" in source, (
        "Expected MainViewModel to consume application interfaces."
    )
