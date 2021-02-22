#!/usr/bin/env python

from typing import List

class Solution1:
    def minNumber(self, nums: List[int]) -> str:

        def lt(a, b):
            sa = str(a)
            sb = str(b)
            return sa + sb < sb + sa

        def partition(left, right):
            if left >= right: return
            pivot = nums[left]
            i = j = left + 1
            while j <= right:
                if lt(nums[j], pivot):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            i -= 1
            nums[left], nums[i] = nums[i], nums[left]
            partition(left, i - 1)
            partition(i + 1, right)

        partition(0, len(nums) - 1)
        return ''.join([str(i) for i in nums])

class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        nums = [-1 for _ in range(n)]
        nums[0] = 1
        for i in range(1, n):
            v2, v3, v5 = nums[p2] * 2, nums[p3] * 3, nums[p5] * 5
            min_v = min(v2, v3, v5)
            nums[i] = min_v
            if min_v == v2: p2 += 1
            if min_v == v3: p3 += 1
            if min_v == v5: p5 += 1
        return nums[-1]