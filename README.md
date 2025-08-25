 📄 PDF Q&A Chatbot


Interactive chatbot that answers questions about any PDF using Azure OpenAI, LangChain, and FAISS.

⚡ Features

   Load and process any PDF file.
   
   Split PDF into chunks for efficient retrieval.
   
   Generate embeddings with Azure OpenAI (text-embedding-3-large).
   
   Store embeddings in FAISS vector database.
   
   Retrieval-based QA with AzureChatOpenAI.
   
   Terminal-based interactive chatbot.

🚀 Installation

Create a .env file:

AZURE_OPENAI_ENDPOINT=<your-azure-endpoint>
AZURE_OPENAI_API_KEY=<your-azure-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=<your-embedding-deployment-name>
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<your-chat-deployment-name>

💻 Usage

Run the chatbot:

  python app.py
  
  Enter the full path of the PDF.
  
  Ask questions about its content.
  
  Type exit or quit to stop.

🧠 How It Works

  Load PDF – Split PDF text into chunks.
  
  Vector Store – Convert chunks to embeddings and store in FAISS.
  
  QA Chain – Use RetrievalQA with AzureChatOpenAI for answers.
  
  Chat Loop – Continuously interact with the PDF until exit.

📌 Notes

  PDFs must be text-based (not scanned images).
  
  Adjust chunk_size and chunk_overlap in RecursiveCharacterTextSplitter for performance tuning.
  
  Retrieval-based answers depend on the stored chunks.
