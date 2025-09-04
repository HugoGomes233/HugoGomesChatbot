 📄 PDF Q&A Chatbot


Interactive chatbot that answers questions about any PDF using Azure OpenAI, LangChain, and ChromaDB.

⚡ Features

Load and process any PDF file.

Split PDF into chunks for efficient retrieval.

Generate embeddings with Azure OpenAI (text-embedding-3-large).

Store embeddings in Chroma vector database.

Retrieval-based QA with AzureChatOpenAI.

Streamlit-based interactive chatbot UI.

🚀 Installation

Create a .env file:

AZURE_OPENAI_ENDPOINT=<your-azure-endpoint>
AZURE_OPENAI_API_KEY=<your-azure-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-embedding-deployment-name>
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<your-chat-deployment-name>

💻 Usage

Run the Streamlit interface
streamlit run bot_ui.py


Enter the full path of the PDF.

Ask questions interactively.

Streamlit handles the interface and calls the core QA engine.

2. Run Ragas tests (optional)
python -m ragas_tests.bot_ragas


Evaluates the bot against predefined queries in ragas_dataset.py.

Returns metrics or compares answers with expected responses.

🧠 How It Works

Load PDF → Splits PDF text into chunks.

Vector Store → Converts chunks to embeddings and stores them in ChromaDB.

QA Chain → Uses RetrievalQA with AzureChatOpenAI to generate answers.

Chat Loop → Streamlit frontend

📌 Notes

PDFs must be text-based (not scanned images).

Adjust chunk_size and chunk_overlap in CharacterTextSplitter for performance tuning.

Retrieval-based answers depend on the stored chunks.
