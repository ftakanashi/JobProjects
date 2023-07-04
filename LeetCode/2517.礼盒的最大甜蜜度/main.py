#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def check(ths):
            prev = float("-inf")
            cnt = 0
            for p in price:
                if p - prev >= ths:
                    cnt += 1
                    prev = p
                if cnt == k: break

            return cnt >= k

        l, r = 0, price[-1] - price[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r