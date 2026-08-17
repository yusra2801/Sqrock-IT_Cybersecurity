
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json
LOG = []
class HoneypotRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the request details
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "client_ip": self.client_address[0],
            "path": self.path,
            "headers": dict(self.headers)
        }
        LOG.append(log_entry)

        # Respond with a simple message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Honeypot Server</h1></body></html>")
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), HoneypotRequestHandler)
    print("Honeypot server running on http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n[+] Server stopped. Captured logs:")
        print(json.dumps(LOG, indent=2))
    