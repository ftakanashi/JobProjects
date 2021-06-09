#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # 构建前缀和数组
        presum = [0,]
        for n in arr:
            presum.append(presum[-1] ^ n)

        ans = 0
        s_count, s_sum = Counter(), Counter()
        for i, s in enumerate(presum):
            # 扫描各个前缀和值
            if s_count[s] > 0:
                # 如果该值曾出现过，表示要计数新的两两组合之间的差值
                ans += (s_count[s] * (i-1)) - s_sum[s]
            s_count[s] += 1
            s_sum[s] += i

        return ans