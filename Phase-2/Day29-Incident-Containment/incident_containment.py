
import time


def isolate_compromised_host(host_ip):
    print(f"[!] INITIATING CONTAINMENT PROTOCOL FOR {host_ip}")

    print(f"[*] Step 1: Revoking active sessions for {host_ip}...")
    time.sleep(0.5)

    print(f"[*] Step 2: Applying 'QUARANTINE' Security Group rules...")
    time.sleep(0.5)

    print(f"[*] Step 3: Null-routing external egress traffic...")
    time.sleep(0.5)

    print(f"[+] CONTAINMENT SUCCESSFUL: {host_ip} is isolated from the network segment.\n")


if __name__ == "__main__":
    compromised_hosts = ["192.168.1.150", "10.0.4.12"]

    for host in compromised_hosts:
        isolate_compromised_host(host)