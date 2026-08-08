from graph.graph_builder import chatbot_graph

queries = [

    "Reset my password",

    "Show my employee profile",

    "How many leave days are remaining?",

    "Show my tickets",

    "What is the WFH policy?"

]

for query in queries:

    print("=" * 80)

    print("User:", query)

    state = {

        "query": query,

        "intent_result": {},

        "tool_result": [],

        "response": ""

    }

    result = chatbot_graph.invoke(state)

    print("\nBot:")

    print(result["response"])

    print()