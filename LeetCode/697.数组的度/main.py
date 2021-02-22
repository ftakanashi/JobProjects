#!/usr/bin/env python
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = {}
        for i, n in enumerate(nums):
            if n not in counter:
                counter[n] = [1, i, i]
            else:
                counter[n][0] += 1
                counter[n][2] = i

        res = float('inf')
        prev = None
        for k in sorted(counter, reverse=True, key=lambda x:counter[x][0]):
            if prev and counter[k][0] < prev: break
            res = min(res, counter[k][2] - counter[k][1] + 1)
            prev = counter[k][0]
        return res