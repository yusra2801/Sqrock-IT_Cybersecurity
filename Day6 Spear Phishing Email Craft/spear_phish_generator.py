
def spear_phish_template(target):
    return f"""
    from : itsupport@{target["company"].lower()}.com
    to : {target["email"]}
    subject : Action Required: Your {target['company']} account will be disabled
    Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspension.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""

targets = [
    {"name": "Yusra", "email": "yusraifzmka@gmail.com", "company": "Sqrock", "location": "Pakistan"},
    {"name": "Mustafa", "email": "mustafa@gmail.com", "company": "TechCorp", "location": "Karachi, Pakistan"},
    {"name": "Sara Khan", "email": "sara@gmail.com", "company": "DataBank", "location": "Lahore, Pakistan"},
]

for t in targets:
    print(spear_phish_template(t))