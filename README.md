PDF Q&A Chatbot

Interactive chatbot that answers questions about any PDF using Azure OpenAI, LangChain, and ChromaDB, with a React frontend and Python FastAPI backend.

🚀 Installation

Clone the repository:
git clone <repo-url>
cd <repo-folder>

Create a Python virtual environment and install dependencies:
python -m venv venv
Linux / Mac: source venv/bin/activate
Windows: venv\Scripts\activate
pip install -r requirements.txt

Create a .env file with your Azure credentials:
AZURE_OPENAI_ENDPOINT=<your-azure-endpoint>
AZURE_OPENAI_API_KEY=<your-azure-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-embedding-deployment-name>
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<your-chat-deployment-name>

Install frontend dependencies:
cd frontend
npm install

💻 Usage

Run Backend:
uvicorn main:app --reload
FastAPI backend exposes the /ask endpoint for chat queries.

Run Frontend:
npm start
React frontend displays your CV and an interactive chatbot. Ask questions interactively; the frontend communicates with the FastAPI backend.

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
python -m ragas_tests.bot_ragas
Returns metrics
