## Phase 2 — Web Application Security & Defensive Automation

### Day 16 — HTTP Security Header Analysis

HTTP response headers tell the browser which security policies to enforce for a page. In this task, I checked 4 critical headers: Strict-Transport-Security (forces HTTPS), Content-Security-Policy (only allows loading scripts/resources from trusted sources, which helps prevent XSS attacks), X-Frame-Options (protects against clickjacking), and X-Content-Type-Options (stops the browser from guessing file types). Scanning my local test server showed that Content-Security-Policy and X-Content-Type-Options were configured, while Strict-Transport-Security and X-Frame-Options were missing — representing a real security gap.

### Day 17 — Local Network Port & Service Scanning

Port scanning attempts to establish socket connections across a specified range of ports to determine which services are running (open ports). Commonly risky ports include 5432 (Postgres database) and 8080 (admin consoles) — if these are exposed publicly, the attack surface increases significantly. In this task, I scanned 5 common ports (22, 80, 443, 5432, 8080) on my local machine (127.0.0.1). Result: no ports were found open, meaning none of these services were active on the machine at the time — a clean baseline.

### Day 18 — SQL Injection (SQLi) Log Detection Engine

SQL Injection occurs when an attacker sneaks malicious SQL commands through normal user input, such as `' OR '1'='1` (login bypass) or `UNION SELECT` (extracting extra data). Defenders detect these patterns in access logs using regex — searching for meta-characters like single quotes, `--`, `#`, or keywords like `UNION SELECT`. In this task, I analyzed 3 mock log entries: the first was a normal request (no threat), the second contained a login-bypass attempt (`' OR '1'='1`), and the third contained a UNION-based data extraction attempt. The script correctly flagged both malicious entries along with their source IP, while ignoring the normal request.

### Day 19 — Docker Container Misconfiguration Scanner

Container configuration determines its operational privileges. Running a container as root (no explicit `USER` instruction), using an unpinned `:latest` base image (which can pull unpredictable/unstable versions), or exposing the SSH port (22) are all serious security risks that can lead to host breakout or unauthorized access. In this task, I wrote a static analyzer that parses a Dockerfile line by line to detect these three misconfigurations. Running it against a test Dockerfile detected all three issues: `FROM ubuntu:latest` (unpinned tag), `EXPOSE 22` (SSH port exposed), and no `USER` instruction present (implicit root execution).

### Day 20 — Web Directory Brute-Force Simulation

Unindexed locations like admin panels (`/admin`), environment files (`/.env`), or backups (`/backup.sql`) can leak infrastructure details if left unprotected. Defenders proactively scan their own servers with a wordlist of common sensitive paths to check which ones are reachable, restricted, or don't exist. In this task, I ran a directory brute-force script against my own local Flask test server using 5 common paths. Results: `/admin` returned status 200 (publicly accessible — a real risk if this were a production admin panel), `/dashboard` returned 403 (properly restricted), and `/api/v1`, `/.env`, and `/backup.sql` all returned 404 (not present on this server).

### Day 21 — Cross-Site Scripting (XSS) Payload Sanitizer

Cross-Site Scripting (XSS) happens when untrusted user input is placed into a webpage without proper encoding, letting an attacker's script execute in another user's browser. Converting raw characters into their safe equivalents (e.g. `<` becomes `&lt;`) prevents the browser from treating injected text as executable markup. In this task, I tested the sanitizer against 10 adversarial payloads — script tags, event-handler based attacks (`onerror`, `onload`, `onclick`), a `javascript:` URI, and one normal harmless comment. All 9 malicious payloads were HTML-escaped, so even ones not explicitly keyword-stripped (like the `onclick` example) became inert since the surrounding tags were no longer real HTML. The normal comment passed through completely unchanged, confirming the sanitizer doesn't break legitimate input.

### Day 22 — API Rate Limiting Token Bucket Logic

Uncapped API endpoints can be abused by automated scripts for brute-force attacks or Denial of Service (DoS). The Token Bucket algorithm protects against this by giving each client a fixed number of "tokens" (capacity) that deplete with each request and refill gradually over time at a fixed rate. In this task, I implemented a rate limiter with a bucket capacity of 3 tokens, refilling at 0.5 tokens/sec (1 token every 2 seconds). Simulating 6 rapid-fire requests from the same client showed the first 3 were allowed (using up all tokens) and the next 3 were blocked. After waiting 4 seconds for the bucket to refill (~2 tokens), 2 more requests were successfully allowed — confirming the refill logic works correctly over time.

### Day 23 — Postgres Database Credential Auditing

Database engines are prime targets for attackers, and weak or default credentials present a catastrophic entry risk. Automated credential auditing checks identify these weaknesses before an external attacker maps them. In this task, I built an auditor that flags 3 dangerous patterns: default admin credentials (`postgres:postgres`), username equal to password (e.g. `admin:admin`), and blank passwords. Testing against 4 mock configurations found 3 critical issues — default Postgres credentials, an `admin:admin` pair, and a blank password on a `readonly_user` account — while one strong, unique password passed the evaluation cleanly.

### Day 24 — Automated Threat Intel IP Blocking Pipeline

Threat Intelligence feeds aggregate Indicators of Compromise (IoCs) gathered from sensors distributed globally. Automating perimeter protection based on this data means malicious infrastructure can be blocked instantly, without waiting for a human analyst to review every entry. In this task, I built a pipeline that ingests a mock threat intel feed and automatically deploys a firewall block rule for any IP with a risk score above 90, while lower-risk IPs are simply logged for monitoring. Testing against 3 mock entries correctly blocked the malware C2 server (score 98) and the brute-forcer (score 92), while the botnet node (score 85) was logged rather than blocked — reflecting a graduated response based on severity rather than an all-or-nothing approach.

### Day 25 — File Upload Vulnerability & Magic Bytes Validator

Attackers often bypass file-extension checks by renaming executable scripts (e.g. `.php`) to look like harmless files (e.g. `.jpg`). Checking the actual binary header (magic bytes) instead of trusting the file extension confirms whether the content genuinely matches the claimed format. In this task, I built a validator that reads the first bytes of a file and compares them against known signatures for PNG and JPEG. I tested it against two files: a genuine PNG (correct magic bytes) and a file disguised as a `.jpg` that actually contained PHP code. The validator correctly passed the real PNG and flagged the fake `.jpg` as an invalid signature — exactly the kind of malicious upload attempt this check is meant to catch.