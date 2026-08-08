from intents.hybrid import detect_intents

TEST_QUERIES = [

    "Reset my password",

    "I forgot my password",

    "Unlock my account",

    "Show my tickets",

    "Reset my password and show my tickets",

    "How many leave days are remaining?",

    "Apply leave tomorrow",

    "Show my employee profile",

    "What is the WFH policy?",

    "Hello",

    "Thank you",

    "Generate my salary slip",

    "I need help with something"

]

for query in TEST_QUERIES:

    print("=" * 80)

    print("User Query:")
    print(query)

    print()

    result = detect_intents(query)

    print(result)

    print()