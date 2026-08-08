"""
Policy Tool
"""

from rag.rag_chain import answer_policy_question


def get_policy(query, policy_data=None):

    return answer_policy_question(query)