#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找第二个模板：左移时不排除mid
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                right = mid

        # 特殊情况，当数组没有旋转，此时right一直不动而left一直加，最终两者在数组外的len(nums)位置相遇
        if left == len(nums):
            left = 0
        return nums[left]