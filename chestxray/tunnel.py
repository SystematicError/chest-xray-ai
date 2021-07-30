from pyngrok import ngrok


def create_tunnel(host: str = "0.0.0.0", port: int = 13520) -> str:
    """
    Creates a ngrok tunnel and generates a Session ID to connect to.

    Args:
        host: Host address.
        port: Port number.

    Returns:
        str: Session ID. Used by client to connect to server.
    """
    pass
