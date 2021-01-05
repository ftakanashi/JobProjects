#!/usr/bin/env python
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:    # 剪枝优化1
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:    # 剪枝优化2
                continue
            for j in range(i + 1, n - 2):
                s = nums[i] + nums[j]
                if s + nums[j+1] + nums[j+2] > target:    # 剪枝优化3
                    break
                if s + nums[n-1] + nums[n-2] < target:    # 剪枝优化4
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    if s + nums[l] + nums[r] > target:
                        r -= 1
                    elif s + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:    # 优化
                            l += 1
                        l += 1
                        while l < r and nums[r] == nums[r-1]:    # 优化
                            r -= 1
                        r -= 1

        return list(res)