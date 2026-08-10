# Day 6 — Spear Phishing Email Craft (Lab Only)

## Objective
Craft personalized phishing emails for security-awareness training purposes.

## Theory
- Spear phishing targets a specific individual using gathered OSINT (unlike bulk phishing).
- Key elements: spoofed sender address, a personal hook (name/location), and a malicious link or attachment.
- Defense relies on email authentication standards: DMARC, SPF, DKIM.

## What the script does
`spear_phish_generator.py` takes target details (name, email, company, location) and generates a personalized phishing-awareness email using an f-string template.

## Tools used
- Python (stdlib only)

## Generated Emails (3 targets)
1. **Yusra** — Sqrock, Pakistan
2. **Mustafa** — TechCorp, Karachi, Pakistan
3. **Sara Khan** — DataBank, Lahore, Pakistan

Each email uses a spoofed "it-support@company.com" sender, a personalized location-based hook, and an urgency-driven subject line — all pointing to a safe lab-only link (no real data collection).

## Defender Guide — SPF, DKIM, DMARC Setup

**SPF (Sender Policy Framework)**
Add a DNS TXT record listing which mail servers are authorized to send email for your domain.
Example: `v=spf1 include:_spf.google.com ~all`

**DKIM (DomainKeys Identified Mail)**
Digitally signs outgoing emails so receivers can verify they weren't tampered with in transit. Typically enabled through your email provider (e.g. Google Workspace, Microsoft 365), which generates the DNS record for you.

**DMARC (Domain-based Message Authentication)**
Combines SPF and DKIM results and tells receiving servers what to do when a message fails both — reject, quarantine, or allow.
Example DNS record: `v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@yourcompany.com`

**Why it matters:** Without these records, attackers can spoof your domain's "From" address (exactly as this script demonstrates) and receiving mail servers have no way to verify the email is fake.

## Deliverable
3 personalized email drafts + DMARC/SPF setup guide for defenders.s