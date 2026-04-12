# Build an AI Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Boot.dev](https://img.shields.io/badge/Created%20with-Boot.dev-purple)
![Status](https://img.shields.io/badge/Status-work%20in%20progress-yellow)

This project is a small CLI-based AI agent that uses an LLM to inspect files, edit code, and run Python scripts in order to complete coding tasks.

## Features

- List files in a directory
- Read file contents
- Write file contents
- Run Python files
- Repeatedly call tools until a task is complete

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- Access to the Gemini API
- A Unix-like shell such as `bash` or `zsh`

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd <repo-name>
```

Install dependencies:

```bash
uv sync
```

## Setup
Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Usage
Run the agent with a task description:

```bash
uv run main.py "fix my calculator app"
```

Example Output

```bash
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# The app is working correctly now.
```

## Project Structure

```bash
.
├── calculator/
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   ├── main.py
│   └── tests.py
│
├── functions/
│   ├── get_files_info.py
│
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
├── test_get_files_info.py
├── uv.lock
└── ...
```

## Notes
- The Gemini API is an external service and may rate limit requests.
- Depending on usage, API calls may incur small costs.
- This project is intended as a learning exercise.

## Acknowledgements
Built as part of the [Boot.dev](https://boot.dev) course [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python).

