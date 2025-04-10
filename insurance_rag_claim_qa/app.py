import streamlit as st
from retriever_chain import qa_chain

st.title("📄 Insurance Claim RAG Assistant")
query = st.text_input("Ask about a claim:")

if query:
    response = qa_chain.invoke({"input": query})
    st.write(response['answer'])
