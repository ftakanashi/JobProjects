#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def movesToMakeZigzag(self, orig_nums: List[int]) -> int:
        ans = float("inf")
        n = len(orig_nums)

        def helper(start):
            """
            从下标start开始的模式
            """
            nums = orig_nums.copy()
            tmp = 0
            for i in range(start, n, 2):
                if i > 0 and nums[i] >= nums[i - 1]:
                    tmp += (nums[i] - nums[i - 1] + 1)
                    nums[i] = nums[i - 1] - 1
                if i < n - 1 and nums[i] >= nums[i + 1]:
                    tmp += (nums[i] - nums[i + 1] + 1)
                    nums[i] = nums[i + 1] - 1

            return tmp

        ans = min(ans, helper(0))
        ans = min(ans, helper(1))
        return ans