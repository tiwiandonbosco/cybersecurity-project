
from collections import Counter
from pathlib import Path
import sys

LOG_FILE = Path("sample_auth.log")
FAILURE_THRESHOLD = 3


def analyze_logs(file_path):
    total_events = 0
    successes = 0
    failures = 0
    failed_ips = Counter()
    failed_users = Counter()

    if not file_path.is_file():
        print("Error: Log file does not exist.")
        return

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 4:
                print(f"Warning: Invalid log format at line {line_number}.")
                continue

            timestamp, username, ip_address, status = [
                part.strip() for part in parts
            ]

            if status not in ("SUCCESS", "FAILED"):
                print(f"Warning: Invalid status at line {line_number}.")
                continue

            total_events += 1

            if status == "SUCCESS":
                successes += 1
            else:
                failures += 1
                failed_ips[ip_address] += 1
                failed_users[username] += 1

    print("\n===== LOGIN LOG ANALYSIS =====")
    print(f"Total valid events: {total_events}")
    print(f"Successful logins: {successes}")
    print(f"Failed logins: {failures}")

    print("\nFailed attempts by IP:")
    for ip_address, count in failed_ips.most_common():
        print(f"{ip_address}: {count}")

    print("\nFailed attempts by username:")
    for username, count in failed_users.most_common():
        print(f"{username}: {count}")

    print("\n===== SECURITY ALERTS =====")
    alerts_found = False

    for ip_address, count in failed_ips.most_common():
        if count >= FAILURE_THRESHOLD:
            alerts_found = True
            print(
                f"ALERT: {ip_address} had {count} failed "
                f"login attempts."
            )

    if not alerts_found:
        print("No IP addresses exceeded the failure threshold.")

    print("\nAnalysis complete.")


def main():
    file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else LOG_FILE

    if len(sys.argv) > 2:
        print("Usage: python login_log_analyzer.py [log_file]")
        return

    analyze_logs(file_path)


if __name__ == "__main__":
    main()
