#!/usr/bin/env python
from typing import List

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i and nums[i] < n:
                k = nums[i]
                nums[i], nums[k] = nums[k], nums[i]

        for i, num in enumerate(nums):
            if num == n:
                return i
        return n

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            res = res ^ i ^ n
        res = res ^ len(nums)    # 别忘了还要运算len(nums)本身
        return res