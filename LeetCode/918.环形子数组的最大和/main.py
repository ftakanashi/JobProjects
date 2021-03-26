#!/usr/bin/env python
from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 第一次应用kanade算法，求出连续区间最大值，得到第一种可能的答案
        ans = cur = float('-inf')
        for n in A:
            cur = max(cur + n, n)
            ans = max(ans, cur)
        opt1 = ans

        # 第二次应用kaande算法，求出连续区间最小值并且用总和减去它，得到第二种可能的答案
        ans = cur = float('inf')
        for n in A:
            cur = min(cur + n, n)
            ans = min(ans, cur)
        opt2 = sum(A) - ans
        if opt2 == 0: opt2 = opt1    # 特殊情况处理

        return max(opt1, opt2)