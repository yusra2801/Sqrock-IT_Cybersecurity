


def evaluate_db_credentials(target_ip, credential_dictionary):
    print(f"[*] Evaluating DB Authentication Resilience on: {target_ip}")

    for username, secret in credential_dictionary.items():
        # Flags dangerous combinations like postgres:postgres, admin:admin, or blank passwords
        if username == "postgres" and secret == "postgres":
            print(f"[CRITICAL OUTCOME] Default Administrator Credentials Active: {username}:{secret}")
        elif secret == "":
            print(f"[CRITICAL OUTCOME] Blank Password Detected: {username}:(empty)")
        elif username == secret:
            print(f"[CRITICAL OUTCOME] Username Equals Password: {username}:{secret}")
        else:
            print(f"[-] Evaluation Passed for configuration pair -> {username}:{secret[:3]}***")


if __name__ == "__main__":
    mock_configs = {
        "postgres": "postgres",
        "app_user": "SecureP@ss2026!",
        "admin": "admin",
        "readonly_user": "",
    }
    evaluate_db_credentials("127.0.0.1", mock_configs)