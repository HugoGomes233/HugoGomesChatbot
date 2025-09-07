PDF Q&A Chatbot

Interactive chatbot that answers questions about any PDF using Azure OpenAI, LangChain, and ChromaDB, with a React frontend and Python FastAPI backend.

🚀 Installation

Clone the repository:
git clone <repo-url>
cd <repo-folder>

Create a Python virtual environment and install dependencies:
1. python -m venv venv
2. Linux / Mac: source venv/bin/activate
2. Windows: venv\Scripts\activate
3. pip install -r requirements.txt

Create a .env file with your Azure credentials:
1. AZURE_OPENAI_ENDPOINT=<your-azure-endpoint>
2. AZURE_OPENAI_API_KEY=<your-azure-api-key>
3. AZURE_OPENAI_DEPLOYMENT_NAME=<your-embedding-deployment-name>
4. AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<your-chat-deployment-name>

Install frontend dependencies:
 1. cd frontend
 2. npm install

💻 Usage

Run Backend:
1. uvicorn main:app --reload

The FastAPI backend exposes the /ask endpoint for chat queries.

Run Frontend:
1. npm start

The React frontend displays your CV and an interactive chatbot. Ask questions interactively; the frontend communicates with the FastAPI backend.

🧠 How It Works

Load PDF → The PDF is read and split into chunks.

Vector Store → Chunks are converted to embeddings using Azure OpenAI and stored in ChromaDB.

QA Chain → RetrievalQA with AzureChatOpenAI retrieves relevant chunks and generates answers.

Chat Loop → Frontend displays the conversation in real time with a typing indicator.

📌 Notes

PDFs must be text-based (not scanned images).

Adjust chunk_size and chunk_overlap in CharacterTextSplitter for performance tuning.

Retrieval-based answers depend on the stored chunks in ChromaDB.

⚡ Features

Load and process any PDF file.

Split PDF into chunks for efficient retrieval.

Generate embeddings with Azure OpenAI (text-embedding-3-large).

Store embeddings in Chroma vector database.

Retrieval-based QA with AzureChatOpenAI.

Interactive React frontend with live chat.

📝 Optional

Run Ragas tests to evaluate the bot:
1. python -m ragas_tests.bot_ragas
2. Returns metrics 
