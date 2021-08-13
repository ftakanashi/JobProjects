#!/usr/bin/env python
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def check(lim):
            cnt = 1
            s = 0
            for num in nums:
                if s + num > lim:
                    cnt += 1
                    s = num
                else:
                    s += num
                if cnt > m: return False

            return cnt <= m

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l