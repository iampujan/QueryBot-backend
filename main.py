from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from loguru import logger
import os
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_API_URL = os.getenv("MODEL_API_URL")
MODEL_API_KEY=os.getenv("MODEL_API_KEY")

class ChatRequest(BaseModel):
    question: str

client = OpenAI(api_key=os.getenv(MODEL_API_KEY), base_url=MODEL_API_URL)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
async def chatbot(request: ChatRequest):
    try:
        chunks = text_splitter.split_text(request.question)
        responses = []
        for chunk in chunks:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for answering FAQs"},
                    {"role": "user", "content": chunk},
                ],
                stream=False
            )
            responses.append(response.choices[0].message.content)

        combined_response = " ".join(responses)
        return {"answer": combined_response}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)