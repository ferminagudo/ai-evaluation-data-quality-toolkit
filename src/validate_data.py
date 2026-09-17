import csv
from collections import Counter
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_evaluations.csv"

REQUIRED_FIELDS = [
    "id", "prompt", "response_a", "response_b",
    "preferred_response", "not_preferred_response",
    "reason_a", "reason_b"
]

def validate_data():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    issues = []
    ids = [row["id"] for row in rows]

    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        issues.append(f"Duplicate IDs: {duplicates}")

    for number, row in enumerate(rows, start=2):
        for field in REQUIRED_FIELDS:
            if not row.get(field, "").strip():
                issues.append(f"Missing {field} at CSV row {number}")

        if row.get("preferred_response") not in {"A", "B"}:
            issues.append(f"Invalid preferred_response at CSV row {number}")

    print("DATA QUALITY VALIDATION")
    print("=" * 60)
    print(f"Records checked: {len(rows)}")
    print(f"Issues found: {len(issues)}")

    if issues:
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No validation issues found.")

if __name__ == "__main__":
    validate_data()
