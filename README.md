# Sqrock IT Cybersecurity Internship

This repository contains my work and tasks completed during the
Sqrock IT Solution Cybersecurity Internship.

## Internship Tasks

## Day 1  OSINT & Passive Reconnaissance
OSINT (Open-Source Intelligence) means gathering information from publicly available sources.
Passive reconnaissance means collecting information without directly contacting or interacting with the target.
Key OSINT sources include WHOIS, DNS records, Shodan, LinkedIn, and GitHub leaks.
Day 1 focus: Understanding OSINT and passive reconnaissance.

## Day 2 — Email Harvesting & Social Engineering Prep
Email harvesting means collecting addresses from public web sources.
Pretexting means crafting a believable fake identity for social engineering attacks.
Ethics boundary: only target domains you own or have written permission for.

## Day 3 — Phishing Page Anatomy & Detection
Phishing relies on visual cloning of real websites plus urgency triggers.
Common indicators: domain/brand mismatch, missing HTTPS, suspicious URL patterns.
Built a URL risk scorer that flags suspicious domains based on these indicators.

## Day 4 — Vishing & Smishing Simulation Scripts
Vishing (voice phishing) and smishing (SMS phishing) use psychological triggers — authority, scarcity, fear, and liking — to manipulate targets.
Built a script generator that produces awareness-training call scripts with red-flag explanations.
## Day 5 — OSINT + SE: Build a Target Profile
Combined OSINT techniques with social engineering by building a GitHub profile aggregator.
The tool pulls public data (name, top languages, repo count, bio) to demonstrate how attackers build target profiles — and how limiting public info reduces exposure.
## Day 6 — Spear Phishing Email Craft
Built a personalized phishing-awareness email generator using OSINT-style target data (name, company, location).
Demonstrates how spoofed sender addresses and personal hooks make spear phishing convincing, plus a defender-side SPF/DKIM/DMARC setup guide.