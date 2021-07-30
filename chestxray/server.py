from logging import ERROR, getLogger
from platform import platform
from sys import modules

from flask import Flask, request

modules["flask.cli"].show_server_banner = lambda *args: None
getLogger("werkzeug").setLevel(ERROR)

app = Flask("")


@app.route("/server-info")
def server_info():
    return platform()


@app.route("/", methods=["POST"])
def scan_xray():
    return


def start_server(host: str = "0.0.0.0", port: int = 13520):
    """
    Server for webclient, can recieve and scan images.

    Args:
        host: Host address.
        port: Port number.
    """
    print(f"[server] Running on http://{host}:{port}")
    app.run(host=host, port=port)
