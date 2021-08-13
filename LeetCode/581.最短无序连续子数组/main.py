#!/usr/bin/env python
from typing import List
import heapq

class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        min_heap = nums.copy()
        heapq.heapify(min_heap)
        i = 0
        while i < n:
            if nums[i] != min_heap[0]: break
            i += 1
            heapq.heappop(min_heap)
        if i == n: return 0
        start = i

        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        i = n-1
        while i >= 0:
            if nums[i] != -max_heap[0]: break
            i -= 1
            heapq.heappop(max_heap)
        end = i
        return end - start + 1

class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        lefts = []
        for i in range(n-1, -1, -1):
            if not lefts or nums[i] < lefts[-1]:
                lefts.append(nums[i])
            else:
                lefts.append(lefts[-1])
        lefts.reverse()

        rights = []
        for i in range(n):
            if not rights or nums[i] > rights[-1]:
                rights.append(nums[i])
            else:
                rights.append(rights[-1])

        i = 0
        while i < n:
            if lefts[i] != nums[i]: break
            i += 1
        left = i
        if left == n: return 0
        i = n - 1
        while i >= 0:
            if rights[i] != nums[i]: break
            i -= 1
        right = i
        return right - left + 1