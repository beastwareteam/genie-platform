from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    app_name: str
    organization: str
    enable_mcp: bool
    enable_background_tasks: bool

    @staticmethod
    def default() -> "AppSettings":
        return AppSettings(
            app_name="Genie Platform",
            organization="BeastwareTeam",
            enable_mcp=True,
            enable_background_tasks=True,
        )
