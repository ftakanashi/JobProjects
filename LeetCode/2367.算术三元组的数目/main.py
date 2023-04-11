#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        ans = 0
        for num in nums:
            if num - diff in seen and num + diff in seen:
                ans += 1
        return ans