# democlient.py
import asyncio
import os
import sys
from dotenv import load_dotenv
from fastmcp import Client # type: ignore
# Import all potential transport classes
from fastmcp.client.transports import (
    StreamableHttpTransport,
    SSETransport,
    # Add other transports here if needed
)

# Load environment variables from .env file
load_dotenv()

def get_transport():
    """Dynamically selects the transport based on environment variables."""
    transport_type = os.getenv("FASTMCP_TRANSPORT", "streamable-http")
    host = os.getenv("FASTMCP_HOST", "127.0.0.1")
    port = int(os.getenv("FASTMCP_PORT", "8000"))

    if transport_type == "streamable-http":
        path = os.getenv("FASTMCP_STREAMABLE_HTTP_PATH", "/mcp/")
        url = f"http://{host}:{port}{path}"
        print(f"--> Using StreamableHttpTransport with URL: {url}")
        return StreamableHttpTransport(url)

    # Add other transport types here in the future if needed

    print(f"Error: Unsupported transport type '{transport_type}'", file=sys.stderr)
    sys.exit(1)

async def example():
    transport = get_transport()
    async with Client(transport=transport) as client:
        # Await client_ping()
        await client.ping()
        print("Ping successful!\n")

        # List available tools to confirm greet is available
        tools = await client.list_tools()
        print(f"Available tools: {tools}\n")

        # Call the greet tool using call_tool method
        # Pass parameters as a dictionary instead
        greeting = await client.call_tool("greet", {"name": "Alice"})
        print(f"Greeting result: {greeting}\n")

if __name__ == "__main__":
    asyncio.run(example())