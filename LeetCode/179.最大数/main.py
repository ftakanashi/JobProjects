#!/usr/bin/env python
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0: return '0'
        nums = [str(i) for i in nums]

        def partition(l, r):
            if l >= r: return
            pivot = nums[l]
            i = j = l + 1
            while j <= r:
                if pivot + nums[j] < nums[j] + pivot:    # 最关键的一句
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            i -= 1
            nums[l], nums[i] = nums[i], nums[l]
            partition(l, i - 1)
            partition(i + 1, r)

        partition(0, len(nums) - 1)
        return ''.join(nums)