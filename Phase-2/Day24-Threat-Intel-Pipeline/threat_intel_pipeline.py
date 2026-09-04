

MOCK_INTEL_FEED = [
    {"ip": "103.45.67.89", "indicator": "malware_c2", "risk_score": 98},
    {"ip": "185.10.11.12", "indicator": "botnet_node", "risk_score": 85},
    {"ip": "198.51.100.33", "indicator": "brute_forcer", "risk_score": 92},
]


def update_firewall_rules(feed_data):
    print("[*] Ingesting Threat Intelligence Feed...")
    for entry in feed_data:
        if entry.get("risk_score", 0) > 90:
            print(f"[ACTION] HIGH RISK - Deploying block rule for IP: {entry['ip']} (Reason: {entry['indicator']})")
        else:
            print(f"[*] LOGGING - Suspicious activity monitored for IP: {entry['ip']}")


if __name__ == "__main__":
    update_firewall_rules(MOCK_INTEL_FEED)