
import socket


def scan_local_ports(host, ports):
    print(f"[*] Initiating Socket Sweep on: {host}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[!] OPEN SERVICE DETECTED: Port {port}")
        sock.close()
if __name__ == "__main__":
    # NOTE: only run against your own local machine, never real infrastructure
    scan_local_ports("127.0.0.1", [22, 80, 443, 5432, 8080])
