import os
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from dotenv import load_dotenv

# Load .env 
load_dotenv()

#Curricullum Path
PDF_PATH = os.path.join("data", "my_curricullum.pdf")

# Load and split PDF
def load_pdf(path):
    loader = PyMuPDFLoader(path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
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
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
        model="gpt-4o",
        temperature=0,
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-12-01-preview"
    )
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

# --- Streamlit UI ---
st.set_page_config(page_title="📄 Hugo Gomes Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 Hugo Gomes Chatbot")

# Save state of the chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "qa_chain" not in st.session_state:
    with st.spinner("Loading Hugo Gomes Question Bot..."):
        docs = load_pdf(PDF_PATH)
        vectorstore = create_vectorstore(docs)
        st.session_state.qa_chain = create_qa_chain(vectorstore)
    st.success("✅ Bot Loaded! You can start 👇")

# Render Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat
if query := st.chat_input("Write your question..."):
    # Save User Question
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    if st.session_state.qa_chain:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.qa_chain.invoke(query)
                response = answer["result"]
                st.markdown(response)

        # Save AI Answer
        st.session_state.messages.append({"role": "assistant", "content": response})
