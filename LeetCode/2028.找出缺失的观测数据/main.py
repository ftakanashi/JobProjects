#!/usr/bin/env python
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        rest = mean * (m + n) - sum(rolls)
        avg = rest // n
        if avg < 0 or avg > 6: return []
        if avg == 0 and rest < n: return []
        if avg == 6 and rest > 6 * n: return []

        ans = [avg for _ in range(n)]
        for i in range(rest - avg * n):
            ans[i] += 1
        return ans