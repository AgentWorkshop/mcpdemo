# FastMCP Demo 01

This project is a simple client-server application demonstrating the basic features of the `fastmcp` library. It includes a server that exposes a `greet` tool and a client that connects to the server to use this tool.

## Features

- A `fastmcp` server with a simple RPC-style tool.
- A `fastmcp` client that can:
    - Ping the server to check for connectivity.
    - List available tools on the server.
    - Call tools with parameters.
- Dynamic transport configuration via environment variables.

## Prerequisites

- Python 3.8+
- A way to manage Python environments, such as:
    - Python's built-in `venv`
    - Anaconda or Miniconda

## Setup

Choose the environment management tool you prefer.

### Option 1: Using `venv`

1.  **Create and activate a virtual environment:**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

2.  **Install dependencies:**

    It's recommended to create a `requirements.txt` file with the following content:

    ```txt
    fastmcp
    python-dotenv
    ```

    Then install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Option 2: Using Anaconda/Miniconda

1.  **Create and activate a conda environment:**

    You can choose any name for your environment. We'll use `fastmcp-demo` as an example.

    ```sh
    conda create --name fastmcp-demo python=3.9 -y
    conda activate fastmcp-demo
    ```
    *(Note: You can use any Python version 3.8 or higher.)*

2.  **Install dependencies:**

    It's recommended to create a `requirements.txt` file with the following content:

    ```txt
    fastmcp
    python-dotenv
    ```

    Then install the dependencies using `pip` inside your conda environment:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

The application is configured using environment variables. The client (`democlient.py`) uses a `.env` file to load these variables.

Create a `.env` file in the `demo01` directory with the following content:

```env
# .env
FASTMCP_TRANSPORT="streamable-http"
FASTMCP_HOST="127.0.0.1"
FASTMCP_PORT="8000"
FASTMCP_STREAMABLE_HTTP_PATH="/mcp/"
```

These variables are used by both the server and the client:

-   `FASTMCP_TRANSPORT`: The transport protocol to use. Currently, only `streamable-http` is implemented in this demo.
-   `FASTMCP_HOST`: The host address for the server to bind to and the client to connect to.
-   `FASTMCP_PORT`: The port for the server to listen on and the client to connect to.
-   `FASTMCP_STREAMABLE_HTTP_PATH`: The URL path for the `streamable-http` transport.

## Usage

1.  **Run the server:**

    Open a terminal, make sure your virtual environment is activated, and run:

    ```sh
    python server.py
    ```

    You should see output indicating the server has started, similar to this:
    ```
    --> Starting server with transport: streamable-http
    INFO:     Started server process [xxxxx]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```

2.  **Run the client:**

    Open a second terminal, activate the virtual environment, and run:

    ```sh
    python democlient.py
    ```

    The client will connect to the server, perform a few actions, and print the results.

### Expected Client Output

```
--> Using StreamableHttpTransport with URL: http://127.0.0.1:8000/mcp/
Ping successful!

Available tools: [{'name': 'greet', 'description': 'Greet a user by name.', 'parameters': {'type': 'object', 'properties': {'name': {'type': 'string', 'title': 'Name'}}, 'required': ['name']}}]

Greeting result: Hello, Alice!

```


### Reference
- Demo of HTTP Streamable in MCP using FastMCP | model context protocol example [Youtube](https://www.youtube.com/watch?v=9jGXTDkhjek
