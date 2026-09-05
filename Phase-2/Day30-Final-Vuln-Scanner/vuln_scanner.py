
import socket
import re


class AutomatedScanner:
    def __init__(self, target_host):
        self.target_host = target_host
        self.findings = []

    def run_recon(self):
        print(f"[*] Running Reconnaissance on {self.target_host}...")
        common_ports = [22, 80, 443, 5432, 8080]
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            result = sock.connect_ex((self.target_host, port))
            if result == 0:
                self.findings.append({"type": "Open Port", "detail": f"Port {port}", "severity": "MEDIUM"})
                print(f"    [!] Open port found: {port}")
            sock.close()

    def run_vuln_checks(self):
        print(f"[*] Executing Vulnerability Audits...")
        mock_log_samples = [
            "GET /profile?id=5 HTTP/1.1",
            "POST /login?user=admin' OR '1'='1 HTTP/1.1",
        ]
        sqli_regex = re.compile(r"(?i)('|--|OR\s+\d+=\d+)")
        for entry in mock_log_samples:
            if sqli_regex.search(entry):
                self.findings.append({"type": "SQLi Pattern", "detail": entry, "severity": "HIGH"})
                print(f"    [!] Suspicious pattern in log: {entry}")

    def generate_report(self):
        print(f"[*] Compiling Final Security Report for {self.target_host}...\n")
        print("=" * 50)
        print(f"SECURITY SCAN REPORT — {self.target_host}")
        print("=" * 50)
        if not self.findings:
            print("No findings.")
        for f in self.findings:
            print(f"[{f['severity']}] {f['type']}: {f['detail']}")
        print("=" * 50)


if __name__ == "__main__":
    print("=== SQROCK INTERNSHIP FINAL PROJECT ===\n")
    scanner = AutomatedScanner("127.0.0.1")
    scanner.run_recon()
    scanner.run_vuln_checks()
    scanner.generate_report()
    print("\n[-] Scan Complete.")