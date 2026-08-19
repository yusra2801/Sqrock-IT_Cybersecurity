
import re
from collections import Counter

LOG_SAMPLE = """
2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:16 SUCCESS_LOGIN user=admin ip=45.33.32.156
2024-01-15 08:00:01 SUCCESS_LOGIN user=riya ip=192.168.1.10
2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
2024-01-15 09:12:03 FAILED_LOGIN user=sara ip=88.21.4.90
2024-01-15 09:12:05 FAILED_LOGIN user=sara ip=88.21.4.90
2024-01-15 09:12:07 FAILED_LOGIN user=sara ip=88.21.4.90
2024-01-15 09:12:09 FAILED_LOGIN user=sara ip=88.21.4.90
2024-01-15 10:00:00 SUCCESS_LOGIN user=ali ip=192.168.1.15
2024-01-15 11:45:20 EMAIL_RULE_CREATED user=sara rule=forward_all
2024-01-15 14:20:00 FAILED_LOGIN user=ali ip=192.168.1.15
"""

def analyze_logs(logs):
    print("=== SIEM Log Analysis Report ===\n")

    # Find brute-force patterns (3+ failed logins from same user)
    fails = re.findall(r'FAILED_LOGIN user=(\w+) ip=([\d.]+)', logs)
    fail_counts = Counter(u for u, _ in fails)

    for user, count in fail_counts.items():
        if count >= 3:
            print(f"[ALERT] Brute force detected: {user} ({count} failed login attempts)")

    # Find suspicious email rule creation
    rules = re.findall(r'EMAIL_RULE_CREATED user=(\w+) rule=(\w+)', logs)
    for user, rule in rules:
        if rule == "forward_all":
            print(f"[ALERT] Suspicious email rule created by: {user} (rule: {rule}) — possible account compromise")

    print("\n=== Analysis Complete ===")

analyze_logs(LOG_SAMPLE)