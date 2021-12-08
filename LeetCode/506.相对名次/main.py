#!/usr/bin/env python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        num2pos = {s: i for i, s in enumerate(score)}
        ans = [None for _ in range(n)]
        for i, s in enumerate(sorted(num2pos, reverse=True)):
            if i == 0:
                title = 'Gold Medal'
            elif i == 1:
                title = 'Silver Medal'
            elif i == 2:
                title = 'Bronze Medal'
            else:
                title = str(i + 1)
            ans[num2pos[s]] = title
        return ans