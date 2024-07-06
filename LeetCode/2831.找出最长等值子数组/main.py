#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = 0
        for points in pos.values():
            l = r = 0
            while r < len(points):
                while points[r] - points[l] - (r - l) > k:
                    l += 1
                ans = max(ans, r - l + 1)
                r += 1

        return ans