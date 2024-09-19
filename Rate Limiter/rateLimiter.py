import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.requests:
                self.requests[user_id] = []
            # Filter out requests that are outside the time window
            self.requests[user_id] = [t for t in self.requests[user_id] if t > current_time - self.time_window]
            if len(self.requests[user_id]) < self.max_requests:
                self.requests[user_id].append(current_time)
                return True
            return False

# Example usage
rate_limiter = RateLimiter(max_requests=5, time_window=60)

def handle_request(user_id):
    if rate_limiter.allow_request(user_id):
        print(f"Request allowed for user {user_id}")
    else:
        print(f"Rate limit exceeded for user {user_id}")

# Simulate user requests
user_id = "Shivam14"
for i in range(10):
    handle_request(user_id)
    time.sleep(3) 
