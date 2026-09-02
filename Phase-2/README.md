## Phase 2 — Web Application Security & Defensive Automation

### Day 16 — HTTP Security Header Analysis

HTTP response headers tell the browser which security policies to enforce for a page. In this task, I checked 4 critical headers: Strict-Transport-Security (forces HTTPS), Content-Security-Policy (only allows loading scripts/resources from trusted sources, which helps prevent XSS attacks), X-Frame-Options (protects against clickjacking), and X-Content-Type-Options (stops the browser from guessing file types). Scanning my local test server showed that Content-Security-Policy and X-Content-Type-Options were configured, while Strict-Transport-Security and X-Frame-Options were missing — representing a real security gap.

### Day 17 — Local Network Port & Service Scanning

Port scanning attempts to establish socket connections across a specified range of ports to determine which services are running (open ports). Commonly risky ports include 5432 (Postgres database) and 8080 (admin consoles) — if these are exposed publicly, the attack surface increases significantly. In this task, I scanned 5 common ports (22, 80, 443, 5432, 8080) on my local machine (127.0.0.1). Result: no ports were found open, meaning none of these services were active on the machine at the time — a clean baseline.

### Day 18 — SQL Injection (SQLi) Log Detection Engine

SQL Injection occurs when an attacker sneaks malicious SQL commands through normal user input, such as `' OR '1'='1` (login bypass) or `UNION SELECT` (extracting extra data). Defenders detect these patterns in access logs using regex — searching for meta-characters like single quotes, `--`, `#`, or keywords like `UNION SELECT`. In this task, I analyzed 3 mock log entries: the first was a normal request (no threat), the second contained a login-bypass attempt (`' OR '1'='1`), and the third contained a UNION-based data extraction attempt. The script correctly flagged both malicious entries along with their source IP, while ignoring the normal request.

### Day 19 — Docker Container Misconfiguration Scanner

Container configuration determines its operational privileges. Running a container as root (no explicit `USER` instruction), using an unpinned `:latest` base image (which can pull unpredictable/unstable versions), or exposing the SSH port (22) are all serious security risks that can lead to host breakout or unauthorized access. In this task, I wrote a static analyzer that parses a Dockerfile line by line to detect these three misconfigurations. Running it against a test Dockerfile detected all three issues: `FROM ubuntu:latest` (unpinned tag), `EXPOSE 22` (SSH port exposed), and no `USER` instruction present (implicit root execution).

