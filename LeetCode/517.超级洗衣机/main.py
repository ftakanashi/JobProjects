#!/usr/bin/env python
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0: return -1
        avg = total // n

        out = [machines[i] - avg for i in range(n)]    # 净给出数组

        presum = [out[0], ]    # 求out的前缀和数组
        for i in range(1, n):
            presum.append(presum[-1] + out[i])

        ans = 0
        for i in range(n):
            ans = max(ans, abs(presum[i]), out[i])    # 最终答案是取所有前缀和的绝对值以及out值的最大值
        return ans