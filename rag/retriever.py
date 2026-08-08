"""
Retriever
"""

from rag.vector_store import create_vector_store


VECTOR_STORE = create_vector_store()


def retrieve(query, k=1):

    return VECTOR_STORE.similarity_search(

        query,

        k=k

    )