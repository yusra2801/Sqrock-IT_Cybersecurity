
import requests
import re
def harvest_emails(url):
    html = requests.get(url , timeout=20).text
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
    return emails
sample_html = "Contact us at info@sqrock.com or support@sqrock.com for queries."
found = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', sample_html)
for email in found:
    print(email)
