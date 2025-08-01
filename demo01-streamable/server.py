# server.py
import os
from fastmcp import FastMCP # type: ignore

mcp = FastMCP(name="MyServer")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Server configuration is loaded from environment variables.
    # `fastmcp` automatically loads host and port from its settings.
    # We manually load the transport type here.
    transport_type = os.getenv("FASTMCP_TRANSPORT", "streamable-http")
    
    # The settings are loaded from .env when FastMCP is instantiated
    host = mcp.settings.host
    port = mcp.settings.port
    
    print(f"--> Starting server on http://{host}:{port}...")
    mcp.run(transport=transport_type)