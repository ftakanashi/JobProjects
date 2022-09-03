#!/usr/bin/env python
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        s_contrib = []
        e_contrib = []
        for i, v in enumerate(values):
            s_contrib.append(v + i)
            e_contrib.append(v - i)

        max_contrib = s_contrib[0]
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, e_contrib[i] + max_contrib)
            if max_contrib < s_contrib[i]:
                max_contrib = s_contrib[i]

        return ans