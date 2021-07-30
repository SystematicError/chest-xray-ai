from logging import ERROR, getLogger
from platform import platform
from sys import modules

from flask import Flask, request

from .xray import XrayScanner

modules["flask.cli"].show_server_banner = lambda *args: None
getLogger("werkzeug").setLevel(ERROR)

app = Flask("")
xray = XrayScanner()


@app.route("/server-info")
def server_info() -> str:
    return platform()


@app.route("/scan-xray", methods=["POST"])
def scan_xray() -> str:
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
    print(f"[server] Running on http://{host}:{port}\n")
    app.run(host=host, port=port)
