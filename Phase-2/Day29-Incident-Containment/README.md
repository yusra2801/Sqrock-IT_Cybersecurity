### Day 29 — Incident Containment & Asset Isolation Scripting

Fast containment prevents lateral movement — stopping an attacker from spreading further into the network once a host is compromised. Automated scripts can interact with hypervisors, cloud APIs, or network controllers to quarantine an infected asset by revoking sessions, applying restrictive security group rules, and cutting off outbound traffic. In this task, I built a containment script that simulates a 3-step isolation process on a compromised host: revoking active sessions, applying quarantine security group rules, and null-routing external egress. Running it against two mock compromised hosts (192.168.1.150 and 10.0.4.12) successfully completed all 3 steps for both, confirming the isolation logic runs consistently regardless of the target IP.

**Incident Response (IR) playbook overview for automated quarantining:**
1. **Detect** — SIEM/monitoring flags a compromise indicator (e.g. from Day 28's webhook alert)
2. **Verify** — an analyst confirms it isn't a false positive before triggering containment
3. **Contain** — this script's logic runs: revoke sessions → quarantine → cut egress
4. **Investigate** — forensic analysis proceeds on the isolated (but still running) host
5. **Recover** — once cleaned/patched, the host is released back into the network segment