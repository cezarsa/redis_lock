import time

__version__ = '0.1.0'

class RedisLock:

    def __init__(self, redis, lock_key='redis-lock', lock_timeout=5*60):
        self.lock_key = lock_key
        self.lock_timeout = lock_timeout
        self.redis = redis

    def acquire_lock(self):
        now = int(time.time())
        result = self.redis.setnx(self.lock_key, now + self.lock_timeout + 1)
        if result == 1 or result is True:
            self.acquire_time = now
            return True

        current_lock_timestamp = self.redis.get(self.lock_key)
        if not current_lock_timestamp:
            return False
        current_lock_timestamp = int(current_lock_timestamp)

        if now > current_lock_timestamp:
            next_lock_timestamp = self.redis.getset(self.lock_key, now + self.lock_timeout + 1)
            if not next_lock_timestamp:
                return False
            next_lock_timestamp = int(next_lock_timestamp)

            if next_lock_timestamp == current_lock_timestamp:
                self.acquire_time = now
                return True

        return False

    def release_lock(self):
        now = int(time.time())
        if now > self.acquire_time + self.lock_timeout:
            # key expired, do nothing and let other clients handle it
            return
        self.acquire_time = None
        self.redis.delete(self.lock_key)
