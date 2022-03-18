#!/usr/bin/env python
from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
            if security[n-i] >= security[n-i-1]:
                right[n-i-1] = right[n-i] + 1

        ans = []
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                ans.append(i)

        return ans