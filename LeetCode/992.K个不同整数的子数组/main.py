#!/usr/bin/env python
from typing import List

import collections

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        prev_r = 0
        window = collections.Counter()
        count = 0
        for l in range(n - K + 1):    # 大于n - K + 1的左边界的子数组，不可能符合题意不用看
            r = prev_r
            # 探索最短的右边界
            while r < n and len(window) < K:
                window[A[r]] += 1
                r += 1
            if len(window) < K: break    # 说明探索右边界直到尽头也没发现符合题意的，因此直接放弃当前以及以后所有左边界

            # 探索最长右边界
            prev_r = r
            while r < n:
                if A[r] not in window: break
                r += 1

            # 这个实现中，实际上prev_r和r分别指向最短右边界的右边一位和最长右边界的右边一位
            count += (r - prev_r + 1)

            # 别忘了实时维护因为左边界移动引起的counter的变化
            window[A[l]] -= 1
            if window[A[l]] == 0: del window[A[l]]

        return count