### Day 20 — Web Directory Brute-Force Simulation

Unindexed locations like admin panels (`/admin`), environment files (`/.env`), or backups (`/backup.sql`) can leak infrastructure details if left unprotected. Defenders proactively scan their own servers with a wordlist of common sensitive paths to check which ones are reachable, restricted, or don't exist. In this task, I ran a directory brute-force script against my own local Flask test server using 5 common paths. Results: `/admin` returned status 200 (publicly accessible — a real risk if this were a production admin panel), `/dashboard` returned 403 (properly restricted), and `/api/v1`, `/.env`, and `/backup.sql` all returned 404 (not present on this server).

**Remediation:**
- Require authentication on any admin/dashboard route — never leave it publicly accessible
- Never deploy `.env` files or database backups inside the web-served directory
- Use a WAF or reverse proxy rule to block common sensitive paths outrightgit commit -m "Phase 2 - 