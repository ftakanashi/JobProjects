#!/usr/bin/env python
from typing import List

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        presum = [1, ]
        for i in range(n):
            presum.append(presum[-1] * nums[i])
        rev_presum = [1, ]
        for i in range(n-1, -1, -1):
            rev_presum.append(rev_presum[-1] * nums[i])
        rev_presum.reverse()

        res = []
        for i in range(1, n+1):
            res.append(presum[i-1] * rev_presum[i])
        return res

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        s = nums[0]
        for i in range(1, n):
            res[i] *= s
            s *= nums[i]

        s = nums[n-1]
        for i in range(n-2, -1, -1):
            res[i] *= s
            s *= nums[i]
        return res