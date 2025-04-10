from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

loader = PyPDFLoader("data/sample_claims.pdf")
pages = loader.load_and_split()

db = Chroma.from_documents(pages, OpenAIEmbeddings())
retriever = db.as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)
