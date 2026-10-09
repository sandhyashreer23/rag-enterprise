# Enterprise RAG Assistant API

## Overview

This project is a FastAPI-based backend service for a Retrieval-Augmented Generation (RAG) application.

The API accepts user questions, retrieves relevant information from a vector database, and generates answers using Large Language Models.

The project demonstrates backend engineering, API development, testing, and AI application development.

## Features

- FastAPI REST API
- Pydantic data validation
- Interactive Swagger documentation
- Automated API testing with Pytest
- Ready for Docker deployment
- Designed for RAG integration

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Docker

## API Endpoints

### GET /

Returns API status.

Example response:

```json
{
  "message": "API is running"
}

POST /ask
Example request: {
  "question": "What is RAG?"
}

example response: {
  "answer": "You asked: What is RAG?"
}

Install dependencies:
pip install -r requirements.txt

Run the application:
python -m uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

Run automated tests:
pytest

Current test status:
2 tests passing