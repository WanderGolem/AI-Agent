# Build an AI Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Boot.dev](https://img.shields.io/badge/Created%20with-Boot.dev-purple)
![Status](https://img.shields.io/badge/Status-Completed-green)

A CLI-based AI agent built in Python as part of the Boot.dev "Build an AI Agent in Python" course.

The agent uses an LLM together with custom tool functions to inspect files, read and write code, and run Python programs in order to complete coding tasks autonomously.

## Features

- List files in directories
- Read file contents
- Write or overwrite files
- Execute Python scripts
- Loop through tool calls until a task is complete
- Apply code changes to fix bugs in a sample calculator project

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- Gemini API access
- Unix-like shell (`bash`, `zsh`, etc.)

## Installation

Clone the repository:

```bash
git clone https://github.com/WanderGolem/AI-Agent.git
cd AI-Agent
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


## Example Workflow

The agent can:

1. Inspect the repository structure
2. Read relevant source files
3. Modify broken code
4. Run the program again to verify the fix


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
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
│
├── .gitignore
├── .python-version
├── call_function.py
├── README.md
├── main.py
├── pyproject.toml
├── test_get_files_info.py
├── test_get_file_content.py
├── test_run_python_file.py
├── test_write_file.py
├── uv.lock
└── ...
```


## Testing

Run the tests with:
```bash
uv run pytest
```
You can also run the sample calculator manually:
```bash
uv run calculator/main.py "3 + 7 * 2"
```
## Notes
- The Gemini API is an external service and may rate limit requests.
- Depending on usage, API calls may incur small costs.
- This project was built for learning purposes, it is intended as a learning exercise.

## Acknowledgements
Built as part of the [Boot.dev](https://boot.dev) course [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python).