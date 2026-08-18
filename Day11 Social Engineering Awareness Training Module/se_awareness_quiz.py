
import json

QUESTIONS = [
    {"q": "An email asks you to verify your password via a link. You should:",
     "opts": ["A) Click the link", "B) Call IT directly", "C) Reply with password"],
     "ans": "B", "exp": "Always verify via official channels, never click email links."},

    {"q": "You find a USB drive in the parking lot. You should:",
     "opts": ["A) Plug it in to check", "B) Hand to security", "C) Keep it"],
     "ans": "B", "exp": "USB drops are a classic baiting attack vector."},

    {"q": "A caller claims to be your bank and asks for your card PIN. You should:",
     "opts": ["A) Give the PIN", "B) Hang up and call the bank's official number", "C) Ask them to text it"],
     "ans": "B", "exp": "Banks never ask for your PIN over the phone."},

    {"q": "A LinkedIn message from a stranger offers a great job if you click a link. You should:",
     "opts": ["A) Click immediately", "B) Verify the company independently first", "C) Reply with your resume and phone number"],
     "ans": "B", "exp": "Unsolicited job offers are a common pretexting tactic."},

    {"q": "Which is the strongest sign of a phishing website?",
     "opts": ["A) Uses HTTPS", "B) Domain doesn't match the real company", "C) Has a logo"],
     "ans": "B", "exp": "A mismatched domain is a major red flag, regardless of design quality."},

    {"q": "Your coworker asks you to share your login 'just this once' because they're locked out. You should:",
     "opts": ["A) Share it, they're a coworker", "B) Refuse and direct them to IT", "C) Share it but change password later"],
     "ans": "B", "exp": "Credentials should never be shared, even with trusted colleagues."},

    {"q": "An SMS says your package is stuck and asks you to pay a small fee via a link. You should:",
     "opts": ["A) Pay quickly to release it", "B) Check directly with the courier's official app/site", "C) Forward it to friends"],
     "ans": "B", "exp": "This is a classic smishing tactic using urgency and small amounts."},

    {"q": "What makes spear phishing more dangerous than regular phishing?",
     "opts": ["A) It's sent in bulk", "B) It's personalized using information about the target", "C) It always uses malware"],
     "ans": "B", "exp": "Personalization from OSINT makes spear phishing far more convincing."},

    {"q": "You notice a strange email rule was created in your inbox, forwarding all mail elsewhere. This suggests:",
     "opts": ["A) Normal browser update", "B) Possible account compromise", "C) Nothing to worry about"],
     "ans": "B", "exp": "Auto-forwarding rules are a common sign an account has been compromised."},

    {"q": "The best overall defense against social engineering is:",
     "opts": ["A) Antivirus software", "B) Ongoing awareness training", "C) A strong Wi-Fi password"],
     "ans": "B", "exp": "Technical controls help, but trained, alert users are the strongest defense."},
]

def run_quiz():
    score = 0
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}: {q['q']}")
        for o in q['opts']:
            print(f"  {o}")
        ans = input("Your answer (A/B/C): ").strip().upper()
        if ans == q['ans']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. {q['exp']}")

    print(f"\nFinal Score: {score}/{len(QUESTIONS)}")

    report = {"score": score, "total": len(QUESTIONS)}
    with open("quiz_score.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Score saved to quiz_score.json")

run_quiz()