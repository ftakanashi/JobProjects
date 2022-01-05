#!/usr/bin/env python

from typing import List
from collections import deque

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.unuse = deque(range(maxNumbers))
        self.used = set()

    def get(self) -> int:
        if len(self.unuse) == 0:
            return -1
        cand = self.unuse.popleft()
        self.used.add(cand)
        return cand

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.unuse.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)