import streamlit as st
from bot_core import load_pdf, create_vectorstore, create_qa_chain



# --- Streamlit UI ---
st.set_page_config(page_title="📄 Hugo Gomes Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 Hugo Gomes Chatbot")

# Save state of the chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "qa_chain" not in st.session_state:
    with st.spinner("Loading Hugo Gomes Question Bot..."):
        docs = load_pdf()
        vectorstore = create_vectorstore(docs)
        st.session_state.qa_chain = create_qa_chain(vectorstore)[0]
        
    if len(st.session_state.messages) == 0:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Hello! I am Hugo Gomes, what do you want to know about me?"
        })

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
