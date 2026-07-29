import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def build_vector_database():
    print("Loading documents from ./data...")
    # Using DirectoryLoader with TextLoader to load all text files in data directory
    loader = DirectoryLoader('./data', glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
    documents = loader.load()
    print(f"Loaded {len(documents)} raw documents.")

    # Chunking Strategy: RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")

    # Embedding Model: Open-source sentence-transformer
    print("Initializing HuggingFaceEmbeddings (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Persist in ChromaDB
    persist_dir = "./chroma_db"
    print(f"Storing chunks in Chroma DB at '{persist_dir}'...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    print(f"Vector store successfully saved to '{persist_dir}'.")

if __name__ == "__main__":
    build_vector_database()
