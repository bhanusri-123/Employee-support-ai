from rag.rag_chain import answer_policy_question

queries = [

    "What is the WFH policy?",

    "Tell me about leave policy",

    "What does the insurance policy cover?",

    "Explain the travel policy"

]

for query in queries:

    print("=" * 80)

    print(query)

    result = answer_policy_question(query)

    print()

    print(result["policy_text"])

    print()