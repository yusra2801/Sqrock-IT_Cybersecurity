
import re
import json
import datetime
import requests
import whois
import socket
from urllib.parse import urlparse


# ===== MODULE 1: OSINT =====
def module_osint():
    domain = input("Enter domain to scan: ")
    try:
        w = whois.whois(domain)
        ip = socket.gethostbyname(domain)
        print(f"\nRegistrar : {w.registrar}")
        print(f"IP        : {ip}")
    except Exception as e:
        print(f"OSINT scan failed: {e}")


# ===== MODULE 2: PROFILE =====
def module_profile():
    username = input("Enter GitHub username: ")
    try:
        base = "https://api.github.com"
        u = requests.get(f"{base}/users/{username}").json()
        profile = {
            "name": u.get("name"),
            "company": u.get("company"),
            "location": u.get("location"),
            "public_repos": u.get("public_repos"),
            "bio": u.get("bio"),
        }
        print(json.dumps(profile, indent=2))
    except Exception as e:
        print(f"Profile build failed: {e}")


# ===== MODULE 3: PHISH SCORE =====
KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]

def module_phish():
    url = input("Enter URL to score: ")
    p = urlparse(url)
    score = 0
    if not url.startswith("https"):
        score += 30
    for kw in KEYWORDS:
        if kw in p.netloc:
            score += 20
    if p.netloc.count('.') > 3:
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    print(f"\n{url} -> Risk Score: {min(score, 100)}%")


# ===== MODULE 4: SPEAR PHISH TEMPLATE =====
def module_template():
    name = input("Target name: ")
    email = input("Target email: ")
    company = input("Target company: ")
    location = input("Target location: ")

    email_text = f"""
From    : it-support@{company.lower()}.com
To      : {email}
Subject : Action Required: Your {company} account will be disabled

Hi {name},

Our security team noticed a login from {location}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""
    print(email_text)


# ===== MODULE 5: INCIDENT RESPONSE =====
def module_ir():
    incident_type = input("Incident type (phishing/credential_theft/usb_drop): ")
    severity = input("Severity (LOW/MEDIUM/HIGH/CRITICAL): ").upper()

    actions = []
    if severity in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions", "Notify SOC team"]
    if incident_type == 'phishing':
        actions += ["Quarantine email", "Block sender domain"]
    if incident_type == 'credential_theft':
        actions += ["Force password reset", "Enable MFA"]
    if incident_type == 'usb_drop':
        actions += ["Isolate affected machine", "Run malware scan"]

    print("\nActions Taken:")
    for a in actions:
        print(f"  [x] {a}")

    report = {"type": incident_type, "severity": severity, "actions": actions,
               "timestamp": str(datetime.datetime.now())}
    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("IR report saved: ir_report.json")


# ===== MAIN MENU =====
MODULES = {
    "osint": ("Run passive OSINT on a domain", module_osint),
    "profile": ("Build target profile from public data", module_profile),
    "phish": ("Score a URL for phishing indicators", module_phish),
    "template": ("Generate spear-phishing training email", module_template),
    "ir": ("Trigger incident response workflow", module_ir),
}

def menu():
    while True:
        print("\n■■■ SE CHAIN SIMULATOR ■■■")
        print("Sqrock Cybersecurity Internship — Final Project\n")
        for k, (desc, _) in MODULES.items():
            print(f"  [{k}] {desc}")
        print("  [exit] Quit")

        choice = input("\nSelect module: ").strip().lower()

        if choice == "exit":
            print("Goodbye!")
            break
        elif choice in MODULES:
            print(f"\n[+] Launching {choice} module...\n")
            MODULES[choice][1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()