# Day 2 — Email Harvesting & Social Engineering Prep

## Objective
Harvest emails ethically from public web sources and understand pretexting fundamentals.

## Theory
- Email harvesting: collecting addresses from public web sources.
- Pretexting: crafting a believable fake identity for SE attacks.
- Ethics boundary: only target domains you own or have written permission for.

## What the script does
`email_harvester.py` scrapes email addresses from a webpage's HTML using a regex pattern, or extracts them from a given text sample.

## Tools used
- `requests`
- `re` (regex, stdlib)

## How to run
python email_harvester.py
## Emails found (sample test)
info@sqrock.com
support@sqrock.com

## Write-up — How Attackers Use This
Email harvesting is often the first step in a social engineering attack chain...
[baaki wala write-up jo maine diya tha, yahan paste kar do]

## Deliverable
Script + list of found emails + write-up on how attackers use this.