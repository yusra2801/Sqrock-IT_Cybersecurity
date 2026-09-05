
def aggregate_reports(mock_data):
    unified_findings = []
    print("[*] Aggregating Vulnerability Scans...")

    for issue in mock_data:
        if issue["severity"] == "HIGH":
            unified_findings.append(issue)
            print(f"[+] Aggregated: {issue['vuln']} (Source: {issue['tool']}, Severity: {issue['severity']})")
        else:
            print(f"[-] Skipped (below threshold): {issue['vuln']} (Source: {issue['tool']}, Severity: {issue['severity']})")

    return unified_findings


if __name__ == "__main__":
    # Mocking outputs from multiple different security scanning tools
    mock_scan_results = [
        {"tool": "Bandit", "vuln": "Hardcoded Password", "severity": "HIGH"},
        {"tool": "Trivy", "vuln": "Outdated OpenSSL Library", "severity": "HIGH"},
        {"tool": "Bandit", "vuln": "Use of eval()", "severity": "MEDIUM"},
        {"tool": "Nikto", "vuln": "Missing Security Header", "severity": "LOW"},
        {"tool": "Trivy", "vuln": "Unpinned Docker Base Image", "severity": "MEDIUM"},
    ]

    findings = aggregate_reports(mock_scan_results)

    print(f"\n[*] Final Unified Report: {len(findings)} HIGH severity findings requiring immediate action.")
    for f in findings:
        print(f"    -> {f['vuln']} ({f['tool']})")