# Day 13 — SIEM Log Analysis for SE Attack Detection

## Objective
Parse and analyze security logs to detect social engineering patterns.

## Theory
- SIEM = Security Information and Event Management — a system that centralizes and analyzes security logs.
- Social engineering leaves traces: unusual login times, repeated failed attempts, new/suspicious email rules.
- Common log sources: Windows Event Log, mail gateway, web proxy, VPN.

## What the script does
`siem_log_parser.py` scans a sample security log and flags two types of anomalies using regex:
1. **Brute-force pattern** — 3 or more failed login attempts by the same user.
2. **Suspicious email rule** — an auto-forwarding rule ("forward_all") created on any account, a common sign of post-compromise data exfiltration.

## Tools used
- `re` (regex, stdlib)
- `collections.Counter` (stdlib)

## Sample Log Analysis Results
[ALERT] Brute force detected: sara (4 failed login attempts)
[ALERT] Suspicious email rule created by: admin (rule: forward_all) — possible account compromise
[ALERT] Suspicious email rule created by: sara (rule: forward_all) — possible account compromise

The parser correctly ignored `admin`'s 2 failed logins (below the 3-attempt threshold) while flagging `sara`'s 4 failed attempts as a brute-force pattern. Both email rule creations were flagged regardless of failed-login count, since a forwarding rule alone is a strong compromise indicator.

## Deliverable
Parser demo + alert report on provided sample logs.