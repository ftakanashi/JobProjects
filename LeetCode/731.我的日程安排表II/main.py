#!/usr/bin/env python
from typing import List

from collections import defaultdict

class MyCalendarTwo:

    def __init__(self):
        self.diff = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.diff[start] += 1
        self.diff[end] -= 1
        s = 0
        for pos in sorted(self.diff):
            if pos > end: break
            s += self.diff[pos]
            if s > 2:
                self.diff[start] -= 1
                self.diff[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)