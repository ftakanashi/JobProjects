#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)
        ans = 0
        while diff > 0:
            if diff <= limit:
                ans += 1
                break
            else:
                ans += (diff // limit)
                diff = diff % limit
        return ans