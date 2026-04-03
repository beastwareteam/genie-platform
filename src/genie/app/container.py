from dataclasses import dataclass

from genie.application.query_engine.query_engine import QueryEngine
from genie.application.task_orchestrator.task_orchestrator import TaskOrchestrator
from genie.presentation.viewmodels.main_view_model import MainViewModel
from genie.runtime.event_bus.event_bus import EventBus
from genie.runtime.feature_flags.feature_flags import FeatureFlags
from genie.runtime.tasks.registry import TaskRegistry
from genie.runtime.tools.registry import ToolRegistry
from genie.shared.config.settings import AppSettings
from genie.shared.logging.logger import get_logger


@dataclass(frozen=True)
class ApplicationContainer:
    settings: AppSettings
    logger_name: str
    feature_flags: FeatureFlags
    event_bus: EventBus
    tool_registry: ToolRegistry
    task_registry: TaskRegistry
    query_engine: QueryEngine
    task_orchestrator: TaskOrchestrator
    main_view_model: MainViewModel

    @staticmethod
    def build_default() -> "ApplicationContainer":
        settings = AppSettings.default()
        logger = get_logger("genie")
        feature_flags = FeatureFlags.from_settings(settings)
        event_bus = EventBus()
        tool_registry = ToolRegistry()
        task_registry = TaskRegistry()
        query_engine = QueryEngine(tool_registry=tool_registry, feature_flags=feature_flags)
        task_orchestrator = TaskOrchestrator(task_registry=task_registry)
        main_view_model = MainViewModel(
            query_engine=query_engine,
            task_orchestrator=task_orchestrator,
            event_bus=event_bus,
            feature_flags=feature_flags,
        )
        return ApplicationContainer(
            settings=settings,
            logger_name=logger.name,
            feature_flags=feature_flags,
            event_bus=event_bus,
            tool_registry=tool_registry,
            task_registry=task_registry,
            query_engine=query_engine,
            task_orchestrator=task_orchestrator,
            main_view_model=main_view_model,
        )
