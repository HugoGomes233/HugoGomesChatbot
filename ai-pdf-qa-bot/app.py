import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

# Load .env 
load_dotenv()

# Load and split PDF into chunks
def load_pdf(path):
    loader = PyPDFLoader(path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return text_splitter.split_documents(documents)

# Create Vectorial Base FAISS with embeddings
def create_vectorstore(docs):
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        model="text-embedding-3-large", 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-12-01-preview"
    )
    return FAISS.from_documents(docs, embeddings)

# Create the QA Chain of Questions and Answers
def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  
    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),  
        model="gpt-4o",
        temperature=0,
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-12-01-preview"
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff" 
    )
    return qa_chain

if __name__ == "__main__":
    while True:
        pdf_path = input("Enter the PDF full path that you want to create a QA bot: ").strip()
    
        # Check if the file exists
        if os.path.isfile(pdf_path):
            print(f"Found file: {pdf_path}")
            break  
        else:
            print(f"File not found at '{pdf_path}'. Please try again.\n")

    print(f"Loading PDF {pdf_path}...")

    # 1. Load PDF
    docs = load_pdf(pdf_path)

    # 2. Create Vectorial Base
    vectorstore = create_vectorstore(docs)

    # 3. Create Chain
    qa_chain = create_qa_chain(vectorstore)

    print("\nAsk me something about the pdf (write exit or quit to leave)\n")

    while True:
        query = input("Question: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = qa_chain.invoke(query)
        print(f"Answer: {answer['result']}\n")