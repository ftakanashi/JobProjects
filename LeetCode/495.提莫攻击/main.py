#!/usr/bin/env python
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        n = len(timeSeries)
        for i in range(n-1):
            # ans += min(duration, timeSeries[i+1] - timeSeries[i])    这么写更简化
            if timeSeries[i] + duration >= timeSeries[i+1]:
                ans += (timeSeries[i+1] - timeSeries[i])
            else:
                ans += duration
        ans += duration
        return ans