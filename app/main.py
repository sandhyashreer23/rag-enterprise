from fastapi import FastAPI
from app.schemas import QuestionRequest, QuestionResponse

app = FastAPI(
    title="RAG Engineering Assistant API"
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/ask")
def ask(request: QuestionRequest):

    return QuestionResponse(
        answer=f"You asked: {request.question}"
    )