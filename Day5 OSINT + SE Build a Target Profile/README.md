# Day 5 — OSINT + SE: Build a Target Profile

## Objective
Combine OSINT data into a social engineering threat profile.

## Theory
- Attackers use LinkedIn, GitHub, and Twitter to build detailed target profiles.
- A profile typically includes: name, role, tech stack, colleagues, and habits.
- Defender use: identifying what's publicly exposed helps reduce digital footprint.

## What the script does
`github_profiler.py` takes a GitHub username and aggregates public profile data (name, company, location, top languages, bio, repo count) into a JSON profile using GitHub's public API.

## Tools used
- `requests`
- `json` (stdlib)

## Sample Output
```json
{
  "name": "Yusra imran",
  "company": null,
  "location": null,
  "public_repos": 2,
  "top_langs": {
    "HTML": 1,
    "Python": 1
  },
  "bio": null
}
```

## Attacker Perspective — Threat Analysis
- **Name** enables personalized pretexting (e.g. "Hi Yusra...") which increases email/call credibility.
- **Top languages (Python, HTML)** reveal the target's technical field, allowing an attacker to craft targeted lures — e.g. a fake "GitHub security alert" or a fake job offer matching the target's skills.
- **Public repo count** signals an active developer; an attacker could dig into commit history or README files, which sometimes accidentally expose secrets like API keys or passwords.
- **Company and location were null** in this case — meaning less information was voluntarily exposed, reducing the attacker's available attack surface. This demonstrates the value of limiting what's shared publicly.

## Defender Takeaway
Reviewing what your own public profiles reveal is a simple but effective way to understand — and reduce — your exposure to social engineering attacks.

## Deliverable
Profile JSON + 1-page attacker perspective threat analysis report.