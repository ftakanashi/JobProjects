#!/usr/bin/env python
from typing import List

class Solution:
    def timeGap(self, time_a, time_b):
        hours = time_b[0] - time_a[0]
        return hours * 60 - time_a[1] + time_b[1]

    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [tuple(map(int, p.split(":"))) for p in timePoints]
        if len(times) > 24 * 60: return 0
        times.sort()
        times.append((times[0][0] + 24, times[0][1]))
        ans = float('inf')
        for i in range(len(times) - 1):
            t = self.timeGap(times[i], times[i+1])
            if t == 0: return 0
            ans = min(ans, t)
        return ans