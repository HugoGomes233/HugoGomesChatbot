import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

#NEW
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

from datetime import datetime

# -----------------------------
# Load environment variables
# -----------------------------
# Reads variables from a .env file into os.environ
# Used for Azure API keys, deployment names, and endpoints
load_dotenv()

# -----------------------------
# PDF file path
# -----------------------------
# This is the resume PDF that will be used to create the QA knowledge base
PDF_PATH = os.path.join("data", "my_curricullum.pdf")

# -----------------------------
# Current date (for prompt context)
# -----------------------------
# We include the current year in the prompt so responses are up-to-date
current_date = datetime.now()

# -----------------------------
# Function: load_pdf
# -----------------------------
# Loads the PDF and splits it into chunks for vector embedding
def load_pdf():
    """
    Loads the PDF file and splits it into smaller text chunks.

    Returns:
        List[Document]: A list of chunked documents ready for embedding.
    """
    # Load PDF using PyMuPDFLoader
    loader = PyMuPDFLoader(PDF_PATH)
    documents = loader.load()

    # Split documents into manageable chunks for embedding
    splitter = CharacterTextSplitter(
        separator="\n\n",  # Split on double newlines
        chunk_size=800,    # Max characters per chunk
        chunk_overlap=100  # Overlap to preserve context between chunks
    )

    return splitter.split_documents(documents)

# -----------------------------
# Function: create_vectorstore
# -----------------------------
# Converts documents into vector embeddings using Azure OpenAI
def create_vectorstore(docs):
    """
    Creates a Chroma vectorstore from a list of documents using embeddings.

    Args:
        docs (List[Document]): Chunked documents to embed.

    Returns:
        Chroma: Vectorstore containing embedded documents for retrieval.
    """
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model=os.getenv("GEMINI_EMBEDDING_MODEL"), # Gemini embedding model
        google_api_key=os.getenv("GEMINI_API_KEY") # Your Gemini API key
    )

    # Create and return the Chroma vectorstore
    return Chroma.from_documents(docs, embeddings)

# -----------------------------
# Function: create_qa_chain
# -----------------------------
# Sets up the retrieval-based QA system using the vectorstore and LLM
def create_qa_chain(vectorstore):
    """
    Creates a RetrievalQA chain using the vectorstore and Gemini Chat LLM.

    Args:
        vectorstore (Chroma): Precomputed vectorstore of embedded documents.

    Returns:
        Tuple[RetrievalQA, AzureChatOpenAI]: The QA chain and the LLM instance.
    """
    # Create a retriever from the vectorstore with top 5 results per query
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    # Initialize Azure Chat LLM for generating responses
    llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_CHAT_MODEL"),      # Modelo de LLM (podes usar gemini-1.5-flash se quiseres algo mais rápido e gratuito)
    temperature=0,                             # Deterministic responses
    google_api_key=os.getenv("GOOGLE_API_KEY") # Gemini API key
)

    # -----------------------------
    # Custom prompt template
    # -----------------------------
    # Designed to answer in first person from Hugo's resume
    # Handles ambiguous questions and provides best guesses when unsure
    template = f"""
        I am Hugo Gomes and I will answer in the first person.
        Use only information from my resume to answer the question but be kind when there are no questions, remember that we are in the year {current_date}.
        If the question is ambiguous (e.g., "where are you from?"), assume it refers to me.
        If you cannot find an exact answer in the documents, respond: Say that you are not that sure but you think that the answer is... and then provide your best guess based on the context.

        Documents: {{context}}

        Question: {{question}}
        Answer:
    """

    # Wrap template into LangChain PromptTemplate
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    # Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # Combines all retrieved chunks into one prompt
        chain_type_kwargs={"prompt": prompt, "document_variable_name": "context"},
        return_source_documents=True  # Include source documents in the response
    )

    return qa_chain, llm
