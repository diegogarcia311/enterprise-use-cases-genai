from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

def classify_document(pdf_path):
    docs = PyPDFLoader(pdf_path).load_and_split()
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db.similarity_search("Is this a 1040 form?", k=1)[0].page_content
