## Phase 2 — Web Application Security & Defensive Automation

### Day 16 — HTTP Security Header Analysis

HTTP response headers browser ko batate hain ke webpage ke liye kaunsi security policies follow karni hain. Is task mein maine 4 critical headers check kiye: Strict-Transport-Security (HTTPS ko force karta hai), Content-Security-Policy (sirf trusted sources se scripts/resources load karne deta hai, isse XSS attacks rukte hain), X-Frame-Options (clickjacking se bachata hai), aur X-Content-Type-Options (browser ko file type guess karne se rokta hai). Apne local test server pe scan kar ke maine dekha ke Content-Security-Policy aur X-Content-Type-Options configured the, jabke Strict-Transport-Security aur X-Frame-Options missing the — jo ek real security gap hota.
