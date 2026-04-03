from dataclasses import dataclass

from genie.shared.config.settings import AppSettings


@dataclass(frozen=True)
class FeatureFlags:
    enable_mcp: bool
    enable_background_tasks: bool

    @staticmethod
    def from_settings(settings: AppSettings) -> "FeatureFlags":
        return FeatureFlags(
            enable_mcp=settings.enable_mcp,
            enable_background_tasks=settings.enable_background_tasks,
        )
