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