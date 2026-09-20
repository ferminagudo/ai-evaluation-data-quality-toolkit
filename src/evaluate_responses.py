import csv
from pathlib import Path
from collections import Counter


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_evaluations.csv"

REQUIRED_FIELDS = [
    "id",
    "prompt",
    "response_a",
    "response_b",
    "preferred_response",
    "not_preferred_response",
    "reason_a",
    "reason_b",
]


def evaluate_responses():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    print("AI RESPONSE EVALUATION")
    print("=" * 60)

    if not rows:
        print("No evaluation records found.")
        return

    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in rows[0]
    ]

    if missing_fields:
        print(f"Missing required fields: {missing_fields}")
        return

    preferences = Counter()

    for row in rows:
        evaluation_id = row["id"]
        prompt = row["prompt"]
        preferred = row["preferred_response"]

        if preferred not in {"A", "B"}:
            print(
                f"Warning: Invalid preference label "
                f"for evaluation {evaluation_id}: {preferred}"
            )
            continue

        preferences[preferred] += 1

        print(f"\nID: {evaluation_id}")
        print(f"Prompt: {prompt}")
        print(f"Preferred response: {preferred}")
        print(f"Reason: {row['reason_a']}")

    print("\n" + "=" * 60)
    print(f"Evaluations reviewed: {len(rows)}")
    print(f"Preferred response A: {preferences['A']}")
    print(f"Preferred response B: {preferences['B']}")


if __name__ == "__main__":
    evaluate_responses()
