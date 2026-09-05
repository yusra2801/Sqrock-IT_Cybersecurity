
import re


class WAFMiddleware:
    def __init__(self):
        self.rules = [
            (re.compile(r"(?i)<script"), "XSS Attempt"),
            (re.compile(r"(?i)union\s+select"), "SQLi Attempt"),
            (re.compile(r"(?i)\.\./\.\./"), "Path Traversal"),
        ]

    def inspect_payload(self, request_data):
        for pattern, rule_name in self.rules:
            if pattern.search(request_data):
                print(f"[WAF BLOCK] Dropped request. Triggered Rule: {rule_name}")
                return False
        print("[WAF ALLOW] Payload is clean.")
        return True


if __name__ == "__main__":
    waf = WAFMiddleware()

    test_requests = [
        "GET /image?file=../../etc/passwd HTTP/1.1",
        "GET /search?q=<script>alert(1)</script> HTTP/1.1",
        "POST /login?user=admin' UNION SELECT password FROM users HTTP/1.1",
        "GET /profile?id=5 HTTP/1.1",
        "GET /welcome?name=Yusra HTTP/1.1",
    ]

    for req in test_requests:
        print(f"\nTesting: {req}")
        waf.inspect_payload(req)