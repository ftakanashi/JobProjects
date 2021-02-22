#!/usr/bin/env python
from typing import List

import heapq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        while len(nums) > 0 and nums[0] <= 0:
            heapq.heappop(nums)
        res = 1
        while True:
            if len(nums) == 0 or res != nums[0]:
                break
            while len(nums) > 0 and nums[0] == res:
                heapq.heappop(nums)
            res += 1
        return res

class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = float('inf')

        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])    # 注意一定要abs，否则可能会负下标

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

class Solution3:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < len(nums):
            if 0 < nums[i] < n and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i+1:
                return i + 1
        return n + 1