#!/usr/bin/env python
from typing import List

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                a, b = nums[i], nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = a, b
            i += 1

        res = []
        for i in range(1, n+1):
            if i != nums[i-1]: res.append(i)
        return res