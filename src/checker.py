import csv
from collections import Counter


def load_csv(file_path):
    """Load a CSV file and return rows as dictionaries."""
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_missing_values(rows):
    """Count missing values in every column."""
    if not rows:
        return {}

    missing = {}

    for column in rows[0].keys():
        missing[column] = sum(
            1 for row in rows if not row[column].strip()
        )

    return missing


def count_duplicates(rows):
    """Count duplicate rows."""
    row_tuples = [tuple(row.items()) for row in rows]
    counts = Counter(row_tuples)

    return sum(
        count - 1
        for count in counts.values()
        if count > 1
    )


def get_basic_statistics(rows):
    """Return basic dataset statistics."""
    if not rows:
        return {
            "rows": 0,
            "columns": 0
        }

    return {
        "rows": len(rows),
        "columns": len(rows[0])
    }


def generate_report(file_path):
    """Generate a basic data-quality report."""
    rows = load_csv(file_path)

    numeric_columns = ["age", "purchase_amount"]

    return {
        "statistics": get_basic_statistics(rows),
        "missing_values": count_missing_values(rows),
        "duplicate_rows": count_duplicates(rows),
        "invalid_numeric_values": find_invalid_numeric_values(
            rows,
            numeric_columns
        )
    }

def find_invalid_numeric_values(rows, columns):
    """Find values that cannot be converted to numbers."""
    invalid_values = {}

    for column in columns:
        invalid_values[column] = []

        for row_number, row in enumerate(rows, start=2):
            value = row[column].strip()

            if value:
                try:
                    float(value)
                except ValueError:
                    invalid_values[column].append({
                        "row": row_number,
                        "value": value
                    })

    return invalid_values


if __name__ == "__main__":
    file_path = input("Enter CSV file path: ")

    report = generate_report(file_path)

    print("\n=== DATA QUALITY REPORT ===")

    print("\nDataset:")
    print(f"Rows: {report['statistics']['rows']}")
    print(f"Columns: {report['statistics']['columns']}")

    print("\nMissing Values:")
    for column, count in report["missing_values"].items():
        print(f"{column}: {count}")

    print(f"\nDuplicate Rows: {report['duplicate_rows']}")
