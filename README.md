# QueryBot-backend
The backend for QueryBot, an AI-powered FAQ system designed to provide intelligent and automated responses to user queries. Built with FastAPI, this backend integrates with the DeepSeek language model to deliver accurate and context-aware answers.


# AI-Powered FAQ System Backend

This is the backend for the AI-Powered FAQ System, built using FastAPI. It handles API requests from the frontend and integrates with the DeepSeek language model to generate responses.

## Features

- FastAPI for building the API
- Integration with DeepSeek language model
- CORS support for cross-origin requests
- Logging with Loguru
- Text processing with Langchain

## Requirements

- Python 3.12
- FastAPI
- Uvicorn
- OpenAI
- Loguru
- Pydantic
- Langchain

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/iampujan/QueryBot-backend.git
   cd QueryBot-backend
   ```

2. **Create virtual env with uv and python 3.12. (langenv is the name of the virtual environment.)
  ```bash
   uv venv langvenv --python 3.12
  ```
