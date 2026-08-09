# Day 1 — OSINT & Passive Reconnaissance

## Objective
Understand passive information gathering using publicly available sources — no direct contact with the target.

## What the script does
`osint.py` takes a domain name as input and collects:
- WHOIS information (registrar, creation/expiration dates)
- IP address
- IP geolocation (country, city, ISP)
- DNS information (hostname, aliases)
- HTTP/HTTPS status info

## Tools used
- `python-whois`
- `socket`
- `requests`

## How to run
python osint.py
Then enter a domain name (e.g. `google.com`) when prompted.

## Deliverable
Script output screenshot + this report.