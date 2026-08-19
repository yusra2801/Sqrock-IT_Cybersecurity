# Day 14 — SE Incident Response Plan

## Objective
Draft and automate a social engineering incident response workflow.

## Theory
- IR phases: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned.
- SE incidents require: account lockout, forensic email analysis, and user notification.
- Documentation is critical for legal, compliance, and insurance purposes.

## What the script does
`ir_automation.py` takes an incident (type + severity) and automatically determines the appropriate containment actions based on severity level and incident type, then saves a full report to `ir_report.json`.

## Tools used
- `json`, `datetime` (stdlib)

## Sample Run
**Incident:** Phishing, Severity: HIGH

**Actions triggered:**
- LOCK user account
- Revoke active sessions
- Notify SOC team
- Preserve mail logs
- Quarantine email
- Block sender domain
- Scan attachments in sandbox

The script also supports `credential_theft` (forces password reset, enables MFA) and `usb_drop` (isolates the machine, runs a malware scan) incident types, connecting back to the attack scenarios simulated on Day 7 and Day 8.

## IR Playbook — Social Engineering Incidents

**1. Preparation**
Maintain an up-to-date contact list for SOC/IT security, and pre-approved containment actions per incident type.

**2. Identification**
Confirm the incident through logs, user reports, or SIEM alerts (as built on Day 13). Classify severity (LOW/MEDIUM/HIGH/CRITICAL).

**3. Containment**
Immediately lock the affected account, revoke active sessions, and isolate any compromised device — before further investigation.

**4. Eradication**
Remove the root cause: quarantine the phishing email, block the sender domain, remove any malicious email rules or malware found.

**5. Recovery**
Restore account access only after a password reset and MFA verification. Monitor the account closely for repeat activity.

**6. Lessons Learned**
Document the full timeline, what worked, what delayed response, and update training/awareness material (as built on Day 11) based on the incident.

## Deliverable
IR script + JSON report sample + 1-page IR playbook document.