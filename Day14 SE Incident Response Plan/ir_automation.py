
import datetime
import json

def ir_response(incident):
    print(f"\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")

    actions = []

    if incident['severity'] in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions",
                     "Notify SOC team", "Preserve mail logs"]

    if incident['type'] == 'phishing':
        actions += ["Quarantine email", "Block sender domain",
                     "Scan attachments in sandbox"]

    if incident['type'] == 'credential_theft':
        actions += ["Force password reset", "Enable MFA if not already active"]

    if incident['type'] == 'usb_drop':
        actions += ["Isolate affected machine", "Run full malware scan"]

    print("\nActions Taken:")
    for a in actions:
        print(f"  [x] {a}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\nIR report saved: ir_report.json")


# Simulate an incident
ir_response({"type": "phishing", "severity": "HIGH", "user": "riya@sqrock.com"})