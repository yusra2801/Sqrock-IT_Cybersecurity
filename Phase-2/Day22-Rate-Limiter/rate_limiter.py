

import time


class RateLimiter:
    def __init__(self, token_capacity, refill_rate_per_sec):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}

    def allow_request(self, client_ip):
        now = time.time()

        if client_ip not in self.ledger:
            self.ledger[client_ip] = {"tokens": self.capacity, "last_updated": now}

        state = self.ledger[client_ip]
        elapsed = now - state["last_updated"]
        state["tokens"] = min(self.capacity, state["tokens"] + (elapsed * self.refill_rate))
        state["last_updated"] = now

        if state["tokens"] >= 1:
            state["tokens"] -= 1
            return True
        return False


if __name__ == "__main__":
    # Bucket holds 3 tokens, refills at 0.5 tokens/sec (1 token every 2 sec)
    limiter = RateLimiter(token_capacity=3, refill_rate_per_sec=0.5)
    client = "10.0.0.5"

    print("[*] Simulating 6 rapid-fire requests from the same client:\n")
    for i in range(1, 7):
        allowed = limiter.allow_request(client)
        status = "ALLOWED" if allowed else "BLOCKED (rate limit exceeded)"
        print(f"Request {i}: {status}")

    print("\n[*] Waiting 4 seconds to let the bucket refill...\n")
    time.sleep(4)

    for i in range(7, 9):
        allowed = limiter.allow_request(client)
        status = "ALLOWED" if allowed else "BLOCKED (rate limit exceeded)"
        print(f"Request {i}: {status}")