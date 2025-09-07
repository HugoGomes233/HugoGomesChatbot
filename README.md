# 📄 PDF Q&A Chatbot

Interactive chatbot that answers questions about any PDF using **Azure OpenAI**, **LangChain**, and **ChromaDB**.  
The project consists of a **Python backend** (FastAPI + LangChain) and a **React frontend** for chat interaction.

---

## ⚡ Features

- Load and process any PDF file.
- Split PDF into chunks for efficient retrieval.
- Generate embeddings using **Azure OpenAI (text-embedding-3-large)**.
- Store embeddings in **Chroma vector database**.
- Retrieval-based QA using **AzureChatOpenAI**.
- Interactive chat UI with React.
- Typing indicator and smooth chat scrolling.

---

## 🚀 Installation

1. Clone the repository:
git clone <repo-url>
cd <repo-folder>

Create a Python virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

Create a .env file with your Azure credentials:
env
AZURE_OPENAI_ENDPOINT=<your-azure-endpoint>
AZURE_OPENAI_API_KEY=<your-azure-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-embedding-deployment-name>
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<your-chat-deployment-name>

Install frontend dependencies:
cd frontend
npm install

💻 Usage
1. Run Backend
uvicorn main:app --reload
FastAPI backend exposes /ask endpoint for the chat queries.

2. Run Frontend
npm start


React frontend Hugo CV and you can interact with a chat bot.

Ask questions interactively; the frontend communicates with FastAPI.

🧠 How It Works
Load PDF → PDF is read and split into chunks.

Vector Store → Chunks are converted to embeddings using Azure OpenAI and stored in ChromaDB.

QA Chain → RetrievalQA with AzureChatOpenAI retrieves relevant chunks and generates answers.

Chat Loop → Frontend displays the conversation and typing indicator in real time.

📌 Notes
PDFs must be text-based (not scanned images).

Adjust chunk_size and chunk_overlap in CharacterTextSplitter for performance tuning.

Retrieval-based answers depend on the stored chunks in ChromaDB.
