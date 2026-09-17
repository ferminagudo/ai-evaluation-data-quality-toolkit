import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_evaluations.csv"

def evaluate_responses():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    print("AI RESPONSE EVALUATION")
    print("=" * 60)

    for row in rows:
        print(f"\nID: {row['id']}")
        print(f"Prompt: {row['prompt']}")
        print(f"Preferred response: {row['preferred_response']}")
        print(f"Reason: {row['reason_a']}")

    print(f"\nEvaluations reviewed: {len(rows)}")

if __name__ == "__main__":
    evaluate_responses()
