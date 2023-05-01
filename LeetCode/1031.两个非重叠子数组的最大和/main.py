#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans1 = self.helper(nums, firstLen, secondLen)
        # 如果firstLen == secondLen，那么没必要计算第二次
        ans2 = self.helper(nums, secondLen, firstLen) if firstLen != secondLen else 0
        return max(ans1, ans2)

    def helper(self, nums, l1, l2):
        i, j = l1, l1 + l2
        s1 = sum(nums[:i])
        s2 = sum(nums[i:j])
        ans = s1 + s2
        s1_max = s1
        while j < len(nums):
            s1 += (nums[i] - nums[i - l1])
            s2 += (nums[j] - nums[j - l2])
            s1_max = max(s1_max, s1)
            ans = max(ans, s1_max + s2)
            i += 1
            j += 1
        return ans