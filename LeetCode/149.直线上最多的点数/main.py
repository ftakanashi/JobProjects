#!/usr/bin/env python
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def analyze(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            k = (y2 - y1) / (x2 - x1) if x1 != x2 else float('inf')
            return k

        ans = 1
        for i in range(n):
            counter = {}
            for j in range(i+1, n):
                k = analyze(points[i], points[j])
                if k not in counter: counter[k] = 1    # 因为包括基准点自身，所以至少是1不是0
                counter[k] += 1
                ans = max(ans, counter[k])

        return ans