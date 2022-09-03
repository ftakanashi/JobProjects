#!/usr/bin/env python
from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i, j = 0, n - 1
        ans = 0

        pos = j
        while colors[pos] == colors[i]:
            pos -= 1
        ans = max(ans, pos - i)

        pos = i
        while colors[pos] == colors[j]:
            pos += 1
        ans = max(ans, j - pos)

        return ans