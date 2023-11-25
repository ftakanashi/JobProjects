#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        ans = None

        for pivot in range(n):
            i, j = pivot + 1, n - 1
            while i < j:
                s = nums[pivot] + nums[i] + nums[j]
                diff = abs(s - target)
                if diff == 0: return s
                if diff < min_diff:
                    min_diff = diff
                    ans = s
                if s > target:
                    j -= 1
                else:
                    i += 1
        return ans