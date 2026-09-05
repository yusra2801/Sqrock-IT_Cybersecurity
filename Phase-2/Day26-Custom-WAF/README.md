### Day 26 — Building a Custom Web Application Firewall (WAF) Engine

A Web Application Firewall (WAF) sits at the application edge, inspecting incoming traffic against signature rules and blocking known attack patterns (SQLi, XSS, Path Traversal) before they ever reach the backend logic. In this task, I built a middleware class that checks each incoming request against 3 regex-based rules. Testing against 5 mock requests correctly blocked a path traversal attempt (`../../etc/passwd`), an XSS payload (`<script>alert(1)</script>`), and a SQL injection attempt (`UNION SELECT`), while two legitimate requests passed through cleanly.

**Inline vs. Reverse Proxy WAF deployment:**
- **Inline WAF:** sits directly in the traffic path as middleware inside the application itself (like this script) — simple to deploy but adds load directly onto the app server and only protects that one application.
- **Reverse Proxy WAF:** sits in front of the application as a separate layer (e.g. Cloudflare, ModSecurity on Nginx) — inspects and filters traffic before it ever reaches any backend server, so one WAF can protect multiple applications and doesn't consume the app's own resources.