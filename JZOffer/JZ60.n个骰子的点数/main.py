#!/usr/bin/env python
from typing import List

class Solution1:
    def dicesProbability(self, n: int) -> List[float]:

        def dfs(s: int, rest: int, target: int, mem: dict) -> int:
            if target - s > rest * 6 or (s >= target and rest > 0): return 0
            if rest == 1: return 1
            if (s, rest, target) in mem: return mem[(s, rest, target)]
            count = 0
            for i in range(1, 7):
                count += dfs(s + i, rest - 1, target, mem)
            mem[(s, rest, target)] = count
            return count

        dem = 6 ** n
        res = []
        for i in range(n, 6*n+1):
            res.append(dfs(0, n, i, {}) / dem)
        return res


class Solution2:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [0 for _ in range(6*n+1)]
        for j in range(1, 7):
            dp[j] = 1

        for i in range(n - 1):
            for j in range((i+2)*6, i-1, -1):
                v = 0
                for k in range(1, 7):
                    if j - k <= 0: continue
                    v += dp[j-k]
                dp[j] = v

        res = []
        dem = 6 ** n
        for j in range(n, 6*n+1):
            res.append(dp[j] / dem)
        return res