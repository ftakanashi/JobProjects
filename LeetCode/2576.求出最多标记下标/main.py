#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def check(k):
            if k > n // 2: return False    # 注意这个隐性条件
            for i in range(k):
                j = n - k + i
                if nums[i] * 2 > nums[j]: return False
            return True

        l, r = 0, n // 2
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r * 2