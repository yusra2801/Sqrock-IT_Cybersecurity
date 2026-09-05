

import json


def send_alert_webhook(webhook_url, alert_data):
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": (
            f"CRITICAL SECURITY ALERT\n"
            f"Type: {alert_data['type']}\n"
            f"Source: {alert_data['ip']}"
        )
    }

    print(f"[*] Dispatching webhook to {webhook_url[:30]}...")
    print(f"[*] Payload: {json.dumps(payload)}")
    # Simulated execution (no real network call made in this lab)
    # response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    print("[+] Webhook dispatched successfully.\n")


if __name__ == "__main__":
    mock_alerts = [
        {"type": "Multiple Failed Logins", "ip": "10.0.0.5"},
        {"type": "SQL Injection Attempt Detected", "ip": "172.16.5.9"},
        {"type": "Unusual Outbound Traffic Volume", "ip": "192.168.1.50"},
    ]

    for alert in mock_alerts:
        send_alert_webhook("https://hooks.slack.com/services/T000/B000/XXX", alert)