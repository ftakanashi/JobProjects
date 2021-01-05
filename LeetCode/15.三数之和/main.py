#!/usr/bin/env python

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        prev = None
        res = set()
        while i < len(nums) - 2:
            if nums[i] > 0: break
            if nums[i] == prev:    # 外层循环的优化
                i += 1
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] < -(nums[l] + nums[r]):
                    l += 1
                elif nums[i] > -(nums[l] + nums[r]):
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))    # 由于list不能被hash化，所以add的对象是tuple
                    l += 1
                    r -= 1
            prev = nums[i]
            i += 1

        return list(res)