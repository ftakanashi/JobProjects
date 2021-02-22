#!/usr/bin/env python

import heapq

class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        count = num = 1
        nums = [1,]
        seen = set([1,])
        while count <= n:
            num = heapq.heappop(nums)
            count += 1
            seen.remove(num)
            if num * 2 not in seen:
                heapq.heappush(nums, num * 2)
                seen.add(num * 2)
            if num * 3 not in seen:
                heapq.heappush(nums, num * 3)
                seen.add(num * 3)
            if num * 5 not in seen:
                heapq.heappush(nums, num * 5)
                seen.add(num * 5)

        return num