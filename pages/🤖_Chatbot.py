import streamlit as st
import time
from langchain_cohere import ChatCohere
from langchain.llms import Cohere
import os
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import requests
import concurrent.futures

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
llm = ChatCohere(cohere_api_key=COHERE_API_KEY)

with open("./data/summary.txt", "r", encoding="utf-8") as file:
    txt_text = file.read()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_text(txt_text)

cohere_embeddings = CohereEmbeddings(model= "embed-english-v3.0",cohere_api_key=COHERE_API_KEY)
documents = [Document(page_content=chunk) for chunk in chunks]
vector_store = FAISS.from_documents(documents, cohere_embeddings)

retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

def create_answer(prompt, timeout_duration=10):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(qa_chain.run, prompt)
            response = future.result(timeout=timeout_duration)
        if not response:
            return "Error: No response received from the API."
        return response
    except concurrent.futures.TimeoutError:
        return "Error: Getting a response from the chatbot engine takes longer than expected 🧐. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to the chatbot engine 🙁. Please try again later."
    except Exception as e:  # Catch any other exceptions
        return f"Error: An unexpected error occurred 🤨. Please try again later."


def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
st.header("Ask questions about me from the AI assistant 🤖")
st.write("""I created this chatbot specifically to answer questions you might have about me. It works with a vector store that I loaded with information 
         about myself that I do not mind sharing publicly. In theory, the bot should only answer questions that can be answered based on the vector store
          and questions that are in its basic knowledge (like 'how much is 2+2?'). However, it is always possible to make bots 'hallucinate' so please do not take 
         everything it says seriously, especially if you are trying to push its boundaries. Enjoy! 😊""")

if "messages" not in st.session_state:
    st.session_state.messages = []

#display placeholder before first message
if not st.session_state.messages:
    st.chat_message("assistant").markdown("Hello! I'm Eniko Kakas' assistant. How can I help you today?")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know about Eniko Kakas?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner(" "):
            # Generate assistant response
            response = st.write_stream(response_generator(create_answer(prompt))) #{create_answer(prompt)}
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

