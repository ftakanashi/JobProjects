#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        i = 0
        while i < n and nums[i] != 0: i += 1
        j = i
        while True:
            while j < n and nums[j] == 0: j += 1
            if j == n: break
            nums[i] = nums[j]
            nums[j] = 0
            while i < n and nums[i] != 0: i += 1
        return nums