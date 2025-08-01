# FastMCP Demo 01: Streamable HTTP Transport

This project is a simple client-server application demonstrating the basic features of the `fastmcp` library. It includes a server that exposes a `greet` tool and a client that connects to the server to use this tool.

This specific demo is located in the `demo01-streamable` directory and focuses on the `streamable-http` transport.

## Features

- A `fastmcp` server with a simple RPC-style tool.
- A `fastmcp` client that can:
  - Ping the server to check for connectivity.
  - List available tools on the server.
  - Call tools with parameters.
- Dynamic transport configuration via environment variables.

## Project Structure

```
mcpdemo/
├── .venv/
├── .env
├── democlient.py
├── server.py
├── requirements.txt
└── README.md
```

## Prerequisites

  - Python's built-in `venv`
  - Anaconda or Miniconda
- `make` for running the demo commands easily.

## Setup

1.  **Clone the repository and navigate to the project root:**
    ```sh
    git clone <repository-url>
    cd mcpdemo
    ```

2.  **Create a clean virtual environment:**

    If you have an existing `.venv` directory, it's best to remove it to avoid conflicts from previous installations.
    ```sh
    rm -rf .venv
    ```
    Now, create and activate a new virtual environment:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    The `requirements.txt` file in the project root should contain the following to ensure all necessary packages, including the server components and correct dependency versions, are installed:
    ```txt
    fastmcp[server]
    pydantic-settings
    python-dotenv
    ```

    Install the dependencies from this file:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

The application is configured using environment variables, which are loaded from a `.env` file within the `demo01-streamable` directory. A template is provided for convenience.

1.  **Navigate to the demo directory:**
    ```sh
    cd demo01-streamable
    ```

2.  **Create your local `.env` file from the example:**
    ```sh
    cp .env.example .env
    ```

The `.env` file is pre-configured for local development and does not need to be changed to run the demo.

-   `FASTMCP_TRANSPORT`: The transport protocol to use. Currently, only `streamable-http` is implemented in this demo.
-   `FASTMCP_HOST`: The host address for the server to bind to and the client to connect to.
-   `FASTMCP_PORT`: The port for the server to listen on and the client to connect to.
-   `FASTMCP_STREAMABLE_HTTP_PATH`: The URL path for the `streamable-http` transport.

## Usage

This demo includes a `Makefile` in the `demo01-streamable` directory for easy execution.

**Make sure you are in the `demo01-streamable` directory before running these commands.**

1.  **Run the server:**

    Open a terminal and run:
    ```sh
    make run-server
    ```

    You should see output indicating the server has started, similar to this:
    ```
    --> Starting server on http://127.0.0.1:8000...
    INFO:     Started server process [xxxxx]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```

2.  **Run the client:**

    Open a second terminal (while still in the `demo01-streamable` directory) and run:
    ```sh
    make run-client
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
