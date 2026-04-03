from dataclasses import dataclass

from genie.application.facade import ApplicationFacade
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
class CoreContainer:
    settings: AppSettings
    logger_name: str
    feature_flags: FeatureFlags
    event_bus: EventBus
    tool_registry: ToolRegistry
    task_registry: TaskRegistry
    query_engine: QueryEngine
    task_orchestrator: TaskOrchestrator
    application_facade: ApplicationFacade


@dataclass(frozen=True)
class EdgeContainer:
    main_view_model: MainViewModel


@dataclass(frozen=True)
class ApplicationContainer:
    core: CoreContainer
    edge: EdgeContainer

    @property
    def main_view_model(self) -> MainViewModel:
        return self.edge.main_view_model

    @staticmethod
    def build_core() -> CoreContainer:
        settings = AppSettings.default()
        logger = get_logger("genie")
        feature_flags = FeatureFlags.from_settings(settings)
        event_bus = EventBus()
        tool_registry = ToolRegistry()
        task_registry = TaskRegistry()
        query_engine = QueryEngine(tool_registry=tool_registry, feature_flags=feature_flags)
        task_orchestrator = TaskOrchestrator(task_registry=task_registry)
        application_facade = ApplicationFacade(
            query_engine=query_engine,
            task_orchestrator=task_orchestrator,
            settings=settings,
        )
        return CoreContainer(
            settings=settings,
            logger_name=logger.name,
            feature_flags=feature_flags,
            event_bus=event_bus,
            tool_registry=tool_registry,
            task_registry=task_registry,
            query_engine=query_engine,
            task_orchestrator=task_orchestrator,
            application_facade=application_facade,
        )

    @staticmethod
    def build_edge(core: CoreContainer) -> EdgeContainer:
        main_view_model = MainViewModel(
            chat_service=core.application_facade,
            task_service=core.application_facade,
            session_service=core.application_facade,
            event_bus=core.event_bus,
            feature_flags=core.feature_flags,
        )
        return EdgeContainer(main_view_model=main_view_model)

    @staticmethod
    def build_default() -> "ApplicationContainer":
        core = ApplicationContainer.build_core()
        edge = ApplicationContainer.build_edge(core)
        return ApplicationContainer(core=core, edge=edge)
