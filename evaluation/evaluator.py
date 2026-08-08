import json
import time

from intents.hybrid import detect_intents

from evaluation.metrics import accuracy


def evaluate():

    with open(
        "evaluation/test_dataset.json",
        "r",
        encoding="utf-8"
    ) as file:

        dataset = json.load(file)

    correct = 0

    total = len(dataset)

    rb = 0

    llm = 0

    total_time = 0

    total_confidence = 0

    for sample in dataset:

        start = time.perf_counter()

        result = detect_intents(
            sample["query"]
        )

        total_time += (
            time.perf_counter() - start
        )

        method = result.get("method")

        if method == "rule_based":
            rb += 1
        else:
            llm += 1

        intents = result.get("intents", [])

        if not intents:
            continue

        predicted = intents[0]["intent"]

        if predicted == sample["expected_intent"]:
            correct += 1

        if "confidence" in intents[0]:

            total_confidence += (
                intents[0]["confidence"] * 100
            )

        else:

            score = intents[0].get("score", 0)

            total_confidence += min(
                score * 25,
                100
            )

    print()

    print("=" * 60)

    print("Evaluation Report")

    print("=" * 60)

    print()

    print(

        f"Accuracy           : {accuracy(correct,total)} %"

    )

    print(

        f"Rule-Based Queries : {rb}"

    )

    print(

        f"LLM Queries        : {llm}"

    )

    print(

        f"Average Confidence : {round(total_confidence/total,2)} %"

    )

    print(

        f"Average Time       : {round(total_time/total,4)} sec"

    )

    print()