
def analyze_dockerfile(path):
    print(f"[*] Parsing Container Directives: {path}\n")
    has_explicit_user = False

    try:
        with open(path, "r") as file:
            for idx, line in enumerate(file, 1):
                cleaned = line.strip().upper()

                if cleaned.startswith("USER"):
                    has_explicit_user = True

                if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                    print(f"[RISK DETECTED] Line {idx}: Root baseline uses unpinned 'latest' tag.")
                if "EXPOSE 22" in cleaned:
                    print(f"[CRITICAL PROHIBITED] Line {idx}: Core networking exposes SSH protocol channel (Port 22).")

        if not has_explicit_user:
            print("[RISK DETECTED] Non-compliant posture: Explicit USER instructions are absent (Implicit Root execution risk).")

    except FileNotFoundError:
        print(f"[!] Error: File not found - {path}")


if __name__ == "__main__":
    analyze_dockerfile("test_dockerfile")