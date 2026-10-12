
import hashlib
import json
import sys
from pathlib import Path

BASELINE_FILE = Path("baseline.json")


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_baseline(file_path):
    """Save the original hash of a file."""
    path = Path(file_path)

    if not path.is_file():
        print("Error: File does not exist.")
        return

    file_hash = calculate_hash(path)

    baseline = {
        "file": str(path.resolve()),
        "sha256": file_hash
    }

    BASELINE_FILE.write_text(
        json.dumps(baseline, indent=4),
        encoding="utf-8"
    )

    print("Baseline saved successfully.")
    print("File:", path)
    print("SHA-256:", file_hash)


def check_integrity(file_path):
    """Compare the current hash with the saved hash."""
    path = Path(file_path)

    if not path.is_file():
        print("Error: File does not exist.")
        return

    if not BASELINE_FILE.is_file():
        print("Error: Baseline not found. Run baseline first.")
        return

    baseline = json.loads(
        BASELINE_FILE.read_text(encoding="utf-8")
    )

    if str(path.resolve()) != baseline["file"]:
        print("Error: This is not the file in the baseline.")
        return

    current_hash = calculate_hash(path)
    saved_hash = baseline["sha256"]

    print("File:", path)
    print("Saved hash:  ", saved_hash)
    print("Current hash:", current_hash)

    if current_hash == saved_hash:
        print("RESULT: File is unchanged.")
    else:
        print("ALERT: File contents have changed!")


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python integrity_checker.py baseline <file>")
        print("  python integrity_checker.py check <file>")
        return

    command = sys.argv[1]
    file_path = sys.argv[2]

    if command == "baseline":
        save_baseline(file_path)
    elif command == "check":
        check_integrity(file_path)
    else:
        print("Error: Use 'baseline' or 'check'.")


if __name__ == "__main__":
    main()
