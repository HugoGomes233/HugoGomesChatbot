import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from datetime import datetime

# Load .env 
load_dotenv()

PDF_PATH = os.path.join("data", "my_curricullum.pdf")

# Get Current Year
current_date = datetime.now()

# Load and split PDF
def load_pdf():
    loader = PyMuPDFLoader(PDF_PATH)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
    return splitter.split_documents(documents)

# Create Vectorstore
def create_vectorstore(docs):
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        model="text-embedding-3-large",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-12-01-preview"
    )
    return Chroma.from_documents(docs, embeddings)

# Create QA Chain
def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 5, "fetch_k": 10})
    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
        model="gpt-4o",
        temperature=0,
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-12-01-preview",
    )

    # Prompt in first person with context
    template = f"""
        I am Hugo Gomes and I will answer in the first person.
        Use only information from my resume to answer the question but be kind when there are no questions, remember that we are in the year {current_date}.
        If the question is ambiguous (e.g., "where are you from?"), assume it refers to me.
        If you cannot find an exact answer in the documents, respond: Say that you are not that sure but u think that the answer is... and then provide your best guess based on the context.

        Documents: {{context}}

        Question: {{question}}
        Answer:
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt, "document_variable_name": "context"},
        return_source_documents=True
    )

    return qa_chain, llm
