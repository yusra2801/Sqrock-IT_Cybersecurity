# Day 3 — Phishing Page Anatomy & Detection

## Objective
Analyze phishing page indicators and build a URL risk scorer (not a phishing page itself).

## Theory
- Phishing relies on visual cloning of real websites plus urgency triggers.
- URL tricks: homograph attacks (similar-looking characters) and subdomain abuse (e.g. paypal.login.evil.com).
- Common indicators: domain/brand mismatch, missing HTTPS, suspicious form actions.

## What the script does
`phishing_scorer.py` takes a URL and calculates a risk score (0-100%) based on four factors.

## Scoring Factors Explained
| Factor | Points | Why it's suspicious |
|---|---|---|
| Not using HTTPS | +30 | Legitimate sites use encrypted connections; plain HTTP exposes data |
| Suspicious keyword in domain (login, verify, bank, paypal, etc.) | +20 each | Attackers embed trusted brand/action words to appear legitimate |
| More than 3 dots in domain | +25 | Excessive subdomains can hide the real domain (e.g. paypal.login.evil.com) |
| IP address instead of domain name | +40 | Legitimate businesses use domain names, not raw IPs |

## Tools used
- `re` (regex, stdlib)
- `urllib.parse` (stdlib)

## Test Results (10 URLs)
| URL | Risk Score |
|---|---|
| https://paypal-login.evil.com/verify | 40% |
| https://github.com | 0% |
| http://192.168.1.1/login | 70% |
| https://secure-bank-update.xyz | 20% |
| https://google.com | 0% |
| https://microsoft.com | 0% |
| https://amazon-account-verify.net | 40% |
| http://bank-secure-login.com | 50% |
| https://facebook.com | 0% |
| https://update-your-password.info | 40% |

## Deliverable
Script + test results on 10 sample URLs + explanation of scoring factors.