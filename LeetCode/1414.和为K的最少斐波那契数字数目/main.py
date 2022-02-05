#!/usr/bin/env python
import bisect

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        nums = [1, 1]
        while nums[-2] + nums[-1] <= k:
            nums.append(nums[-2] + nums[-1])
        ans = 0
        while k > 0:
            pos = bisect.bisect(nums, k)
            k -= nums[pos - 1]
            ans += 1
        return ans