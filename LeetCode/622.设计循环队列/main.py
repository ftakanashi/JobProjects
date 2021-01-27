#!/usr/bin/env python

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.max_len = k
        self.insert = 0
        self.pop = 0
        self.current_len = 0

    def enQueue(self, value: int) -> bool:
        if self.current_len == self.max_len:
            return False
        self.queue[self.insert] = value
        self.insert = (self.insert + 1) % self.max_len
        self.current_len += 1
        return True

    def deQueue(self) -> bool:
        if self.current_len == 0:
            return False
        self.queue[self.pop] = None
        self.pop = (self.pop + 1) % self.max_len
        self.current_len -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.pop] if self.current_len > 0 else -1

    def Rear(self) -> int:
        return self.queue[self.insert - 1] if self.current_len > 0 else -1

    def isEmpty(self) -> bool:
        return self.current_len == 0

    def isFull(self) -> bool:
        return self.current_len == self.max_len