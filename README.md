# QueryBot Backend

The backend for QueryBot, an AI-powered FAQ system designed to provide intelligent and automated responses to user queries. Built with FastAPI, this backend integrates with language models to deliver context-aware answers with high accuracy. This project is build to learn about LangChain and will implement other langchain functionalities to it in other update.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI-%E2%9D%A4-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/OpenAI-API-orange.svg" alt="OpenAI">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</div>

## Features

- 🚀 **FastAPI** for building a high-performance API
- 🤖 **OpenAI integration** for intelligent responses
- 🔄 **CORS support** for cross-origin requests
- 📊 **Logging** with Loguru for better debugging
- 📝 **Text processing** with Langchain for advanced text manipulation

## Requirements

- Python 3.12
- FastAPI
- Uvicorn
- OpenAI
- Loguru
- Pydantic
- Langchain

## ⚙️ Environment Setup

### Prerequisites

- Python 3.12
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/iampujan/QueryBot-backend.git
   cd QueryBot-backend
   ```

2. **Create and activate a virtual environment with uv:**

   ```bash
   uv venv --python 3.12
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root and add:

   ```
   FRONTEND_URL=http://localhost:0000  (Use your frontend url)
   MODEL_NAME=deepseek-chat   (Use your model)
   MODEL_API_URL=https://api.openai.com/v1
   MODEL_API_KEY=your_openai_api_key_here
   ```

## 🚀 Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative documentation: `http://localhost:8000/redoc`

## 📦 Adding Dependencies

To add new dependencies:

```bash
uv add package_name
# Example:
uv add fastapi
```

## 🔗 Frontend

This project works in conjunction with the [QueryBot Frontend](https://github.com/iampujan/Querybot-frontend). For a complete setup, please clone and configure the frontend repository as well.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
