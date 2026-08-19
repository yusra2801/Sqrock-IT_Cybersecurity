# Day 15 — Final Project: SE Attack Chain Simulator

## Objective
Build a complete social engineering attack chain demo tool (ethical lab use), combining all tools built across this internship into one CLI application.

## Theory
- Attack chain: OSINT → Profile Build → Phish Craft → Delivery → Exploit → Persist
- Red team exercises expose security gaps before real attackers do
- Every component built across the 15-day program comes together in this final simulation

## What the tool does
`se_chain_simulator.py` is a menu-driven CLI tool combining 5 modules built earlier in this internship:

| Module | Function | Built On |
|---|---|---|
| `osint` | WHOIS + IP lookup on a domain | Day 1 |
| `profile` | GitHub public profile aggregation | Day 5 |
| `phish` | URL phishing risk scorer | Day 3 |
| `template` | Spear-phishing training email generator | Day 6 |
| `ir` | Incident response automation | Day 14 |

## Tools used
- `requests`, `whois`, `socket`, `re`, `json`, `datetime` (all previously used across the internship)

## Live Demo Results

**osint** — google.com
Registrar : MarkMonitor, Inc.
IP : 142.250.200.174

**profile** — GitHub username (yusra2801) profile pulled successfully

**phish** — https://paypal-login.evil.com/verify → flagged as high risk

**template** — Generated a personalized spear-phishing awareness email

**ir** — Simulated a HIGH-severity phishing incident:
```json
{
  "type": "phishing",
  "severity": "HIGH",
  "actions": [
    "LOCK user account",
    "Revoke active sessions",
    "Notify SOC team",
    "Quarantine email",
    "Block sender domain"
  ],
  "timestamp": "2026-08-19 12:16:09.227347"
}
```

All 5 modules ran successfully from a single menu-driven CLI, then exited cleanly via the `exit` command.

## Final Security Report

Across this 15-day internship, the following social engineering attack techniques were simulated end-to-end, alongside matching defenses:

1. **Reconnaissance** (Days 1, 5) — OSINT and profile-building show how much information is publicly available about a target before any attack begins.
2. **Delivery** (Days 2, 4, 6) — Email harvesting, vishing/smishing scripts, and spear-phishing templates demonstrate how attackers craft convincing, personalized lures.
3. **Exploitation** (Days 3, 7, 8, 9, 10) — Phishing URL analysis, credential attacks, USB drops, fake profiles, and honeypots show common exploitation and social-engineering vectors from both attacker and defender perspectives.
4. **Detection & Response** (Days 11, 12, 13, 14) — Awareness training, ML-based phishing detection, SIEM log analysis, and incident response automation demonstrate the defensive side of the same attack chain.
5. **Integration** (Day 15) — This final tool ties reconnaissance, exploitation, and response into a single simulated attack chain, mirroring how real red-team exercises are structured.

**Key takeaway:** Social engineering succeeds by exploiting trust, urgency, and authority rather than technical vulnerabilities — meaning the strongest defense is a combination of technical controls (rate limiting, email authentication, SIEM monitoring) and consistent user awareness training.

## Deliverable
Full integrated tool + live demo (see screenshot) + final security report (above).