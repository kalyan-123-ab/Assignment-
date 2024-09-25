import time
import threading

class RateLimiter:
    def __init__(self):
        self.requests = {}
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.requests:
                self.requests[user_id] = []
            user_requests = self.requests[user_id]

            # Remove requests older than 1 minute
            self.requests[user_id] = [req for req in user_requests if current_time - req < 60]

            if len(self.requests[user_id]) < 5:
                self.requests[user_id].append(current_time)
                return True
            else:
                return False

# Example usage
limiter = RateLimiter()
print(limiter.allow_request('user_1'))  # Will return True or False
