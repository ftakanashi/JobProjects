#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = r = 0
        n = len(nums)
        ans = 0

        while l < n and r < n:

            # 收缩第一波左边界，跳过所有不符合要求的起始值
            while l < n and (nums[l] & 1 == 1 or nums[l] > threshold):
                l += 1

            # 扩展右边界
            r = l
            odd = 0
            while r < n and nums[r] & 1 == odd and nums[r] <= threshold:
                odd = odd ^ 1
                ans = max(ans, r - l + 1)
                r += 1
            if r == n: break

            # 直接将左边界跳到当前右边界
            l = r

        return ans