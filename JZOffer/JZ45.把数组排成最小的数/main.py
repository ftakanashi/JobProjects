#!/usr/bin/env python

from typing import List

class Solution1:
    def minNumber(self, nums: List[int]) -> str:

        def lt(a, b):
            sa = str(a)
            sb = str(b)
            return sa + sb < sb + sa

        def partition(left, right):
            if left >= right: return
            pivot = nums[left]
            i = j = left + 1
            while j <= right:
                if lt(nums[j], pivot):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            i -= 1
            nums[left], nums[i] = nums[i], nums[left]
            partition(left, i - 1)
            partition(i + 1, right)

        partition(0, len(nums) - 1)
        return ''.join([str(i) for i in nums])