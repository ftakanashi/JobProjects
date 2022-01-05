#!/usr/bin/env python
from collections import deque

class Logger1:

    def __init__(self):
        self.valid = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.valid and timestamp - self.valid[message] < 10:
            return False
        else:
            self.valid[message] = timestamp
            return True

class Logger2:

    def __init__(self):
        self.q = deque()
        self.seen = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and self.q[0][0] <= timestamp - 10:
            _, msg = self.q.popleft()
            self.seen.remove(msg)
        if message in self.seen:
            return False
        else:
            self.q.append((timestamp, message))
            self.seen.add(message)
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)