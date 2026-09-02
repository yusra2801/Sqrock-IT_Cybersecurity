## Phase 2 — Web Application Security & Defensive Automation

### Day 16 — HTTP Security Header Analysis

HTTP response headers browser ko batate hain ke webpage ke liye kaunsi security policies follow karni hain. Is task mein maine 4 critical headers check kiye: Strict-Transport-Security (HTTPS ko force karta hai), Content-Security-Policy (sirf trusted sources se scripts/resources load karne deta hai, isse XSS attacks rukte hain), X-Frame-Options (clickjacking se bachata hai), aur X-Content-Type-Options (browser ko file type guess karne se rokta hai). Apne local test server pe scan kar ke maine dekha ke Content-Security-Policy aur X-Content-Type-Options configured the, jabke Strict-Transport-Security aur X-Frame-Options missing the — jo ek real security gap hota.

### Day 17 — Local Network Port & Service Scanning

Port scanning ek technique hai jisme specified range ke ports pe socket connections establish karne ki koshish ki jati hai taake pata chale kaunse services chal rahi hain (open ports). Common risky ports mein 5432 (Postgres database) aur 8080 (admin console) shamil hain — agar ye publicly expose hon to attack surface barh jata hai. Is task mein maine apne local machine (127.0.0.1) pe 5 common ports (22, 80, 443, 5432, 8080) scan kiye. Scan result: koi bhi port open nahi mila, matlab is waqt in services mein se koi bhi machine pe active nahi hai — jo ek safe/clean baseline dikhata hai.
