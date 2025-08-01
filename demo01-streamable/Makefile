# Makefile for the demo01 project

# Use the shell that the user is running make from
SHELL := /bin/bash

# Define the virtual environment directory
VENV_DIR := .venv
# Define the python executable from the venv
PYTHON := $(VENV_DIR)/bin/python

# We use a marker file to track the last successful dependency sync.
# This ensures 'make' re-installs dependencies if pyproject.toml changes.
SYNC_MARKER = $(VENV_DIR)/.sync-marker

.PHONY: all install run-server run-client clean help

all: help

# Target to set up the virtual environment and install dependencies
install: $(SYNC_MARKER)

$(SYNC_MARKER): pyproject.toml
	@echo "--> Creating/updating virtual environment and syncing dependencies with uv..."
	@uv venv $(VENV_DIR)
	@uv pip sync -p $(PYTHON) pyproject.toml
	@touch $(SYNC_MARKER)

# Target to run the server
run-server: install
	@echo "--> Starting server on http://127.0.0.1:8000..."
	@$(PYTHON) server.py

# Target to run the client
run-client: install
	@echo "--> Running client..."
	@$(PYTHON) democlient.py

# Target to clean up the virtual environment
clean:
	@echo "--> Cleaning up virtual environment..."
	@rm -rf $(VENV_DIR)

# Help target to show available commands
help:
	@echo "Available commands:"
	@echo "  make install      - Create venv and install dependencies from pyproject.toml."
	@echo "  make run-server   - Start the MCP server (run in a separate terminal)."
	@echo "  make run-client   - Run the MCP client (run after starting the server)."
	@echo "  make clean        - Remove the virtual environment."