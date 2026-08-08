"""
RAG pipeline.
"""

from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

from rag.retriever import retrieve

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


PROMPT = """
You are an HR Assistant.

Answer ONLY using the policy below.

If the answer is unavailable,
say you don't know.

Policy:

{policy}

Question:

{question}
"""


def answer_policy_question(query):

    docs = retrieve(query)

    policy = docs[0].page_content

    prompt = PROMPT.format(
        policy=policy,
        question=query
    )

    response = llm.invoke(prompt)

    # ----------------------------
    # Extract plain text
    # ----------------------------

    if isinstance(response.content, str):

        answer = response.content

    elif isinstance(response.content, list):

        answer = ""

        for block in response.content:

            if isinstance(block, dict):

                answer += block.get("text", "")

            else:

                answer += str(block)

    else:

        answer = str(response.content)

    return {

        "status": "success",

        "tool": "policy_query",

        "policy_text": answer

    }