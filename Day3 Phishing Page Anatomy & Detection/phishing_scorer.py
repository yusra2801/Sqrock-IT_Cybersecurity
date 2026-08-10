
import re
from urllib.parse import urlparse

KEYWORDS = ["login", "signin", "account", "update", "verify", "password", "banking", "paypal", "credit card", "social security", "ssn"
]
def phish_score(url):
    p = urlparse(url)
    score = 0
    if not url.startswith("https://"):
        score += 30
    for kw in KEYWORDS:
     if kw in p.netloc:
        score += 20
    if p.netloc.count('.') > 3:
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
    return min(score, 100)
url = [
     "https://paypal-login.evil.com/verify",
    "https://github.com",
    "http://192.168.1.1/login",
    "https://secure-bank-update.xyz",
    "https://google.com",
    "https://microsoft.com",
    "https://amazon-account-verify.net",
    "http://bank-secure-login.com",
    "https://facebook.com",
    "https://update-your-password.info",
]
for u in url:
    print(f"{u} -> Risk: {phish_score(u)}%")