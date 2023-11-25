#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_i = [(n, i) for i, n in enumerate(nums)]
        nums_with_i.sort(key=lambda x:x[0])

        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums_with_i[left][0] + nums_with_i[right][0]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [nums_with_i[left][1], nums_with_i[right][1]]
        return []