#!/usr/bin/env python

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k: return -1

        def check(day):
            bloom_count = flower_count = 0
            for b in bloomDay:
                if b <= day:
                    flower_count += 1
                    if flower_count == k:
                        bloom_count += 1
                        flower_count = 0
                        if bloom_count == m: return True
                else:
                    flower_count = 0
            return False

        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l