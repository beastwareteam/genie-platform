import argparse

from genie.app.bootstrap import bootstrap_application, bootstrap_http_server
from genie.dev import doctor


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Genie Platform Entry Point")
    parser.add_argument(
        "--server",
        action="store_true",
        help="Startet den lokalen HTTP-Server statt der Desktop-UI.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host für den HTTP-Server (nur mit --server relevant).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8765,
        help="Port für den HTTP-Server (nur mit --server relevant).",
    )
    parser.add_argument(
        "--doctor",
        action="store_true",
        help="Führt einen lokalen Environment- und Architektur-Check aus.",
    )
    parser.add_argument(
        "--doctor-strict",
        action="store_true",
        help="Wie --doctor, aber mit strict Modus für optionale Checks.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.doctor or args.doctor_strict:
        doctor_args = ["--strict"] if args.doctor_strict else []
        raise SystemExit(doctor.main(doctor_args))

    if args.server:
        http_server = bootstrap_http_server(host=args.host, port=args.port)
        print(f"Genie HTTP Server läuft auf {http_server.address}")
        http_server.serve_forever()
        return

    app_controller = bootstrap_application()
    app_controller.run()


if __name__ == "__main__":
    main()
