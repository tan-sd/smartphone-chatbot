import streamlit as st
import time
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model="llama3")
vectorstore = FAISS.load_local("../data/faiss_index", embedding, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 15})
llm = OllamaLLM(model="llama3", temperature=0)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about stock, price, or get a recommendation..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            normalized_prompt = prompt.lower()
            matched_docs = [
                doc for doc in vectorstore.docstore._dict.values()
                if doc.metadata.get("model", "").lower() in normalized_prompt
            ]

            docs = matched_docs if matched_docs else retriever.invoke(prompt)

            # with st.expander("🔍 Retrieved Chunks"):
            #     for i, doc in enumerate(docs):
            #         st.markdown(f"**Match {i+1}:**")
            #         st.code(doc.page_content)

            context = "\n".join([doc.page_content for doc in docs])
            final_prompt = f"""
                You are a friendly, helpful and experienced smartphone sales assistant.
                Use the following context to answer the user's question in a natural, conversational tone.
                Only use information from the context. If it's not there, say you don't have that information.
                Use emoji if appropriate.

                Your job:
                - Suggest phones based on user intent (e.g. budget, power, stock).
                - Never invent data. Stick to listed models and prices in context.
                - Present your answer clearly and naturally.

                Context:
                {context}

                Question:
                {prompt}
            """

            response = llm.invoke(final_prompt)

            display_text = ""
            assistant_block = st.empty()
            for char in response:
                display_text += char
                assistant_block.markdown(display_text)
                time.sleep(0.005)

    st.session_state.messages.append({"role": "assistant", "content": response})