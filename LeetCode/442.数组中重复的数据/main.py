#!/usr/bin/env python
from typing import List

class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = set()
        while i < len(nums):
            if nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    res.add(nums[i])
                    i += 1
                else:
                    tmp1, tmp2 = nums[i], nums[nums[i] - 1]
                    nums[i], nums[tmp1 - 1] = tmp2, tmp1
            else:
                i += 1
        return list(res)

class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res