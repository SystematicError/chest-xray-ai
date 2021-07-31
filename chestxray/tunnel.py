from pyngrok import ngrok


def start_tunnel(host: str = "0.0.0.0", port: int = 13520) -> str:
    """
    Creates a ngrok tunnel and generates a Session ID to connect to.

    Args:
        app: Flask application to start tunnel on.
        host: Host address.
        port: Port number.

    Returns:
        str: Session ID. Used by client to connect to server.
    """
    try:
        url = ngrok.connect(port, "http").public_url
        print(f"[tunnel] Created tunnel at {url}")
        server_id = url.replace("http://", "").replace(".ngrok.io", "")
    except Exception:
        print("[tunnel] Failed to create tunnel")
        server_id = "unavailable"
    finally:
        return server_id
