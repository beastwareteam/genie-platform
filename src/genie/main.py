from genie.app.bootstrap import bootstrap_application


def main() -> None:
    app_controller = bootstrap_application()
    app_controller.run()


if __name__ == "__main__":
    main()
