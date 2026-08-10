
def generate_vishing_script(target_company , attacker_role , pretext):
    script = f"""
=== Vishing Awareness Script ===
Caller Role :{attacker_role}
Target Organization :{target_company}
Pretext :{pretext}

[OPENER]
'Hi, this is Alex from {attacker_role} at {target_company}.
We detected unusual activity on your account.'

[HOOK]
'I need to verify your identity — can you confirm
your employee ID and current password?'

[RED FLAG for Awareness]
-> Legitimate {attacker_role} will NEVER ask for passwords.
-> Always verify via official internal channels.
"""
    return script
scripts = [
    generate_vishing_script("Sqrock It" , "IT Support" , "Password Reset"),
    generate_vishing_script("HBLBank" , "Bank Security Officer" , "Suspicious Transaction Alert"),
     generate_vishing_script("FBR", "Government Tax Officer", "Tax Refund Verification"),
]
for s in scripts:
    print(s)
    