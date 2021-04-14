#!/usr/bin/env python
from typing import List

import heapq
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_nums = [-n for n in nums]
        heapq.heapify(rev_nums)
        for _ in range(k - 1):
            heapq.heappop(rev_nums)
        return -rev_nums[0]

import random
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(l, r, k):
            if l == r: return nums[l]
            pi = random.randint(l, r)
            nums[pi], nums[l] = nums[l], nums[pi]
            pivot = nums[l]
            i = j = l + 1
            while j <= r:
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            i -= 1
            nums[l], nums[i] = nums[i], nums[l]
            # print(pivot, nums)
            if i - l + 1 == k: return nums[i]
            elif i - l + 1 > k:
                return partition(l, i-1, k)
            else:
                return partition(i + 1, r, k - (i - l + 1))

        return partition(0, len(nums) - 1, k)