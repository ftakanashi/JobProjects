#!/usr/bin/env python
from typing import List

class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:

        def get_cnt(k):
            cnt = 0
            for num in nums:
                if num <= k: cnt +=1
            return cnt

        n = len(nums) - 1
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            mid_cnt = get_cnt(mid)
            if mid_cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        i, j = nums[0], nums[nums[0]]
        while i != j:
            i = nums[i]
            j = nums[nums[j]]
        i = 0
        while i != j:
            i = nums[i]
            j = nums[j]
        return i