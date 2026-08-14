"""
Log File Analyzer - Python console application

Parses web server access logs in the standard "Combined Log Format"
(the format used by Apache/Nginx) and produces summary statistics:
 - Requests per status code
 - Top requested URLs
 - Top client IP addresses
 - Requests per hour
 - Total bandwidth transferred

Example log line this parses:
127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326

If your log format differs, adjust LOG_PATTERN accordingly.
"""

import re
import os
from collections import Counter, defaultdict

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\S+)'
)


def parse_log_file(path):
    entries = []
    skipped = 0

    with open(path, "r", errors="replace") as f:
        for line_num, line in enumerate(f, 1):
            match = LOG_PATTERN.search(line)
            if not match:
                skipped += 1
                continue

            data = match.groupdict()
            data["size"] = 0 if data["size"] == "-" else int(data["size"])
            data["status"] = int(data["status"])
            entries.append(data)

    return entries, skipped


def extract_hour(datetime_str):
    # Format: 10/Oct/2023:13:55:36 +0000 -> extract "10/Oct/2023:13"
    try:
        return datetime_str.split(":")[0] + ":" + datetime_str.split(":")[1]
    except IndexError:
        return "unknown"


def format_size(num_bytes):
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} TB"


def print_status_breakdown(entries):
    status_counts = Counter(e["status"] for e in entries)

    print("\nStatus Code Breakdown:")
    print("-" * 30)
    for status, count in sorted(status_counts.items()):
        category = {
            "2": "Success",
            "3": "Redirect",
            "4": "Client Error",
            "5": "Server Error",
        }.get(str(status)[0], "Other")
        print(f"  {status} ({category}): {count}")


def print_top_urls(entries, top_n=10):
    url_counts = Counter(e["url"] for e in entries)

    print(f"\nTop {top_n} Requested URLs:")
    print("-" * 30)
    for url, count in url_counts.most_common(top_n):
        print(f"  {count:>6}  {url}")


def print_top_ips(entries, top_n=10):
    ip_counts = Counter(e["ip"] for e in entries)

    print(f"\nTop {top_n} Client IPs:")
    print("-" * 30)
    for ip, count in ip_counts.most_common(top_n):
        print(f"  {count:>6}  {ip}")


def print_requests_per_hour(entries):
    hour_counts = defaultdict(int)
    for e in entries:
        hour = extract_hour(e["datetime"])
        hour_counts[hour] += 1

    print("\nRequests per Hour:")
    print("-" * 30)
    for hour in sorted(hour_counts.keys()):
        count = hour_counts[hour]
        bar = "#" * min(count // max(1, len(entries) // 50), 50)
        print(f"  {hour}  {count:>6}  {bar}")


def print_bandwidth(entries):
    total_bytes = sum(e["size"] for e in entries)
    avg_bytes = total_bytes / len(entries) if entries else 0

    print("\nBandwidth:")
    print("-" * 30)
    print(f"  Total transferred: {format_size(total_bytes)}")
    print(f"  Average per request: {format_size(avg_bytes)}")


def print_errors(entries, top_n=10):
    error_entries = [e for e in entries if e["status"] >= 400]

    if not error_entries:
        print("\nNo error responses (4xx/5xx) found.")
        return

    error_urls = Counter(e["url"] for e in error_entries)

    print(f"\nTop URLs Causing Errors (4xx/5xx) - {len(error_entries)} total error requests:")
    print("-" * 30)
    for url, count in error_urls.most_common(top_n):
        print(f"  {count:>6}  {url}")


def main():
    print("===== Log File Analyzer =====\n")

    path = input("Enter path to log file: ").strip()
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    entries, skipped = parse_log_file(path)

    if not entries:
        print("No valid log entries could be parsed. Check that the file matches the expected log format.")
        return

    print(f"\nParsed {len(entries)} log entries ({skipped} line(s) skipped/unparseable).")

    while True:
        print("\n--------------------------------")
        print("1. Status code breakdown")
        print("2. Top requested URLs")
        print("3. Top client IPs")
        print("4. Requests per hour")
        print("5. Bandwidth summary")
        print("6. Top error-causing URLs")
        print("7. Full report (all of the above)")
        print("8. Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print_status_breakdown(entries)
        elif choice == "2":
            print_top_urls(entries)
        elif choice == "3":
            print_top_ips(entries)
        elif choice == "4":
            print_requests_per_hour(entries)
        elif choice == "5":
            print_bandwidth(entries)
        elif choice == "6":
            print_errors(entries)
        elif choice == "7":
            print_status_breakdown(entries)
            print_top_urls(entries)
            print_top_ips(entries)
            print_requests_per_hour(entries)
            print_bandwidth(entries)
            print_errors(entries)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
