# Day 4 — Vishing & Smishing Simulation Scripts

## Objective
Model voice/SMS social engineering scripts for security awareness training.

## Theory
- Vishing = voice phishing. Attacker impersonates bank, IT, or government.
- Smishing = SMS phishing. Short links + urgency = high click rate.
- Psychological triggers: authority, scarcity, fear, liking.

## What the script does
`vishing_generator.py` generates awareness-training call scripts for different pretexting scenarios, each including an Opener, Hook, and Red Flag section.

## Tools used
- Python (stdlib only)

## Generated Scripts (3 scenarios)
1. **IT Support** — Sqrock IT, pretext: Password Reset
2. **Bank Security Officer** — HBL Bank, pretext: Suspicious Transaction Alert
3. **Government Tax Officer** — FBR, pretext: Tax Refund Verification

## Psychological Trigger Analysis
| Script | Triggers Used | How |
|---|---|---|
| IT Support | Authority, Fear | Poses as internal IT staff (authority); claims "unusual activity" to create fear |
| Bank Security | Authority, Fear, Urgency | Bank officer role (authority); suspicious transaction claim creates fear and urgency to act fast |
| Government Tax Officer | Authority, Scarcity | Government role commands compliance (authority); tax refund framing creates fear of missing out (scarcity) |

All three scripts share a common weakness attackers exploit: asking for a password directly. This is the clearest red flag — legitimate organizations never request passwords over a call.

## Deliverable
3 unique scripts (IT, bank, government) + psychological trigger analysis.