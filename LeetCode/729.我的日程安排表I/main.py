#!/usr/bin/env python
from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        pos = self.booked.bisect_left(end)
        prev_end = self.booked.items()[pos-1][1] if pos > 0 else -1
        if prev_end <= start:
            self.booked[start] = end
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)