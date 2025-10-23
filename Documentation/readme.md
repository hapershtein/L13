# CLI Agent

This is a CLI agent that uses the Gemini LLM to call existing functions in a local project.

## Installation

1. Clone the repository.
2. Create a virtual environment: `uv venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install the dependencies: `uv pip install -r requirements.txt`

## Usage

```bash
python agent.py "Your command in plain English"
```

## Configuration

1. Create a `.env` file in the root of the project.
2. Add your Gemini API key to the `.env` file:

```
GEMINI_API_KEY=your_api_key
```
