#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = defaultdict(int)
        for s, e in intervals:
            rooms[s] += 1
            rooms[e] -= 1

        ans = n = 0
        for t in sorted(rooms):
            n += rooms[t]
            ans = max(ans, n)
        return ans