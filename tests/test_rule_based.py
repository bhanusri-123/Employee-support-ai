from intents.rule_based import detect_intents


TEST_QUERIES = [

    "Reset my password.",

    "I forgot my password.",

    "Unlock my account.",

    "Show my tickets.",

    "Reset my password and show my tickets.",

    "How many leave days do I have?",

    "Apply leave tomorrow.",

    "Show my profile.",

    "What is the WFH policy?",

    "Hi",

    "Thank you",

    "I need help."
]


for query in TEST_QUERIES:

    print("=" * 70)

    print(query)

    print()

    print(detect_intents(query))

    print()