#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        presum = [0]
        pos = {0: 0}
        for h in hours:
            val = presum[-1] + (1 if h > 8 else -1)
            presum.append(val)
            if val not in pos:
                pos[val] = len(presum) - 1

        ans = 0
        for i in range(len(presum) - 1, -1, -1):
            if presum[i] > 0:
                ans = max(ans, i)
            else:
                if presum[i] - 1 in pos:    # 注意考虑 presum[i] 可能是最小值，此时不存在 presum[i] - 1
                    ans = max(ans, i - pos[presum[i] - 1])

        return ans