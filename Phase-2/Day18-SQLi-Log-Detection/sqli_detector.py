
import re

MOCK_ACCESS_LOGS = [
    '192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200',
    "10.0.4.12 - \"POST /auth/login?user=admin' OR '1'='1 HTTP/1.1\" 401",
    '172.16.5.9 - "GET /search?q=UNION SELECT null,password FROM users-- HTTP/1.1" 500',
]


def analyze_sqli_signatures(logs):
    sqli_regex = re.compile(r"(?i)('|--|#|UNION\s+SELECT|OR\s+\d+=\d+)")
    for entry in logs:
        if sqli_regex.search(entry):
            source_ip = entry.split(" ")[0]
            print(f"[CRITICAL MALICIOUS PATTERN] Source: {source_ip} -> String: {entry}")
if __name__ == "__main__":
    analyze_sqli_signatures(MOCK_ACCESS_LOGS)