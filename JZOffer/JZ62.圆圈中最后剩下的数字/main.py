#!/usr/bin/env python

class Solution1:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        i = 0
        while len(nums) > 1:
            i = (i + m - 1) % len(nums)
            nums.pop(i)
        return nums[0]


class Solution2:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = ((m - 1) % i + 1 + ans) % i
        return ans