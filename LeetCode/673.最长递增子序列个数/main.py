#!/usr/bin/env python
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp_len = [1 for _ in range(n)]
        dp_con = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp_len[i] > dp_len[j] + 1:
                        pass
                    elif dp_len[i] == dp_len[j] + 1:
                        dp_con[i] += dp_con[j]
                    else:
                        dp_len[i] = dp_len[j] + 1
                        dp_con[i] = dp_con[j]

        count = 0
        max_len = max(dp_len)
        for i, l in enumerate(dp_len):
            if l == max_len: count += dp_con[i]
        return count