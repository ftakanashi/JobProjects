#!/usr/bin/env python
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        F = float('inf')
        n = len(s)

        pos = -F
        left = [-F for _ in range(n)]
        for i in range(n):
            if s[i] == c:
                pos = i
            left[i] = pos

        pos = F
        right = [F for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            right[i] = pos

        ans = [
            min(i - left[i], right[i] - i) for i in range(n)
        ]
        return ans