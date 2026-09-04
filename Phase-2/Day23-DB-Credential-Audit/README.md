### Day 23 — Postgres Database Credential Auditing

Database engines are prime targets for attackers, and weak or default credentials present a catastrophic entry risk. Automated credential auditing checks identify these weaknesses before an external attacker maps them. In this task, I built an auditor that flags 3 dangerous patterns: default admin credentials (`postgres:postgres`), username equal to password (e.g. `admin:admin`), and blank passwords. Testing against 4 mock configurations found 3 critical issues — default Postgres credentials, an `admin:admin` pair, and a blank password on a `readonly_user` account — while one strong, unique password passed the evaluation cleanly.

**Secure Postgres configuration recommendations:**
- Never use default or username-matching credentials — enforce strong, unique passwords for every role
- Disable blank-password authentication entirely (`password_encryption` + reject empty secrets)
- Apply connection limits per role to reduce brute-force/DoS exposure
- Use row-level security (RLS) so even an authenticated low-privilege user can't read data outside their scope