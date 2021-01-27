#!/usr/bin/env python
from typing import List

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            max_len = dp[i]
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len = max(max_len, dp[j] + 1)
            dp[i] = max_len
        return max(dp)


class Solution2:
    '''
    ！！！ 抄的 ！！！
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)