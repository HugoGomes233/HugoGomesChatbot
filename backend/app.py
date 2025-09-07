from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from core.bot_core import load_pdf, create_vectorstore, create_qa_chain

# -----------------------------
# Initialize FastAPI app
# -----------------------------
app = FastAPI(
    title="Hugo GPT QA API",
    description="API to query a PDF-based QA system using LangChain",
    version="1.0.0",
)

# -----------------------------
# Configure CORS (Cross-Origin Resource Sharing)
# -----------------------------
# This allows a frontend (like React) hosted on a different domain/port
# to make HTTP requests to this FastAPI backend.
# Note: restrict to your frontend URL.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- in prod, set to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load PDF and initialize QA chain
# -----------------------------
# These operations are done at startup to avoid re-loading files
# or creating the vectorstore on every API call.
docs = load_pdf()                       # Load documents from PDF
vectorstore = create_vectorstore(docs)  # Convert documents to a searchable vector database
qa_chain, _ = create_qa_chain(vectorstore)  # Initialize QA chain (LangChain)

# -----------------------------
# Request schema
# -----------------------------
# Define the shape of incoming POST request body for /ask endpoint.
# Using Pydantic BaseModel ensures validation and type safety.
class Question(BaseModel):
    query: str  # The user question to be answered by the QA chain

# -----------------------------
# POST /ask endpoint
# -----------------------------
@app.post("/ask")
def ask_question(request: Question):
    """
    Accepts a user question, queries the QA chain, and returns an answer.

    Args:
        request (Question): A Pydantic model containing the 'query' string.

    Returns:
        dict: JSON response with the key 'answer' containing the answer text.

    Raises:
        HTTPException: Returns status code 500 if any error occurs.
    """
    try:
        # Call the QA chain with the user's query
        result = qa_chain.invoke({"query": request.query})

        # Return only the answer
        return {
            "answer": result["result"],
        }

    except Exception as e:
        # Catch any exception and return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail=str(e))