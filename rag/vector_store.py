"""
Creates a FAISS vector store.
"""
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from rag.loader import load_documents


def create_vector_store():

    docs = load_documents()

    langchain_docs = []

    for doc in docs:

        langchain_docs.append(

            Document(

                page_content=doc["text"],

                metadata={

                    "source": doc["name"]

                }

            )

        )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    return FAISS.from_documents(

        langchain_docs,

        embeddings

    )