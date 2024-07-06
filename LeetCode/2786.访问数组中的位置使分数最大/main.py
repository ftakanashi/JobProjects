#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:

        odd_max = eve_max = float("-inf")    # 不能设置为-1，因为后面依赖于max计算时，分数可能被扣成比-1更小的负分
        if nums[0] & 1 == 1: odd_max = nums[0]
        else: eve_max = nums[0]

        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] & 1 == 1:
                curr = max(odd_max + nums[i], eve_max + nums[i] - x)
                ans = max(curr, ans)
                odd_max = max(odd_max, curr)
            else:
                curr = max(eve_max + nums[i], odd_max + nums[i] - x)
                ans = max(curr, ans)
                eve_max = max(eve_max, curr)

        return ans