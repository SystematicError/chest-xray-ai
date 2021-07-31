from logging import ERROR, getLogger
from platform import platform
from sys import modules

from flask import Flask, request

from .tunnel import start_tunnel
from .xray import XrayScanner

modules["flask.cli"].show_server_banner = lambda *args: None
getLogger("werkzeug").setLevel(ERROR)

app = Flask("")
xray = XrayScanner()


@app.route("/")
def home_page() -> str:
    """Home page of website, lets users quickly access different features"""
    return "Still under development :)"


@app.route("/server-info")
def server_info() -> str:
    """Returns host information for the client to verify."""
    return platform()


@app.route("/scan-xray", methods=["POST"])
def scan_xray() -> str:
    """Scans the provided image and returns the AI's predictions."""
    try:
        response = str(xray.scan_xray(request.files["image"].read()))
    except Exception as error:
        response = {"error": str(error)}
    finally:
        print("[server] Sending results\n")
        return response


def start_server(host: str = "0.0.0.0", port: int = 13520) -> None:
    """
    Server for webclient, can recieve and scan images.

    Args:
        host: Host address.
        port: Port number.
    """
    server_id = start_tunnel(host, port)
    print(f"[server] Running locally http://{host}:{port}")
    print(f"[server] Server ID is {server_id}\n")
    app.run(host, port)
