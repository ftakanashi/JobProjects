#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        for i in range(n):
            for j in range(n):
                cnt[nums[i] & nums[j]] += 1

        ans = 0
        for i in range(n):
            for val, count in cnt.items():
                if nums[i] & val == 0:
                    ans += count
        return ans