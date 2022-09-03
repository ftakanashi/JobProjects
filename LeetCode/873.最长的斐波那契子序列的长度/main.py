#!/usr/bin/env python
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num2i = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if arr[j] <= arr[i] // 2: break
                tgt = arr[i] - arr[j]
                k = num2i.get(tgt, -1)
                if k < 0 or k == j or k == i: continue
                dp[j][i] = dp[k][j] + 1 if dp[k][j] >= 3 else 3

        ans = max([max(row) for row in dp])
        return ans