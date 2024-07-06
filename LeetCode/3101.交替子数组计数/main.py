#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = prev = 0
        for i in range(1, n):
            if nums[i] != nums[i-1]: continue
            ans += ((i - prev) * (i - prev + 1)) // 2
            prev = i
        ans += ((n - prev) * (n - prev + 1)) // 2
        return ans