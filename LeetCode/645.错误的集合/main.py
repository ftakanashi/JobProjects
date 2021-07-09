#!/usr/bin/env python
from typing import List
class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans0 = ans1 = None
        while i < n:
            while i < n and nums[i] == i+1:
                i += 1
            if i == n: break
            tmp = nums[i]
            if nums[tmp-1] == nums[i]:
                ans0 = nums[i]
                ans1 = i + 1
                i += 1
            else:
                nums[tmp-1], nums[i] = nums[i], nums[tmp-1]

        return [ans0, ans1]

class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        setsum = sum(set(nums))
        n = len(nums)
        return [sum(nums) - setsum, ((n+1) * n) // 2 - setsum]