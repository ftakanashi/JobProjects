#!/usr/bin/env python
from typing import List

import heapq
class Solution1:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1, ]
        seen = set([1, ])
        cnt = 0
        while cnt < n:
            num = heapq.heappop(heap)
            cnt += 1
            if cnt == n: return num
            for p in primes:
                cand = num * p
                if cand in seen: continue
                heapq.heappush(heap, num * p)
                seen.add(cand)


class Solution2:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        pointers = [1] * m

        for i in range(2, n + 1):
            min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
            dp[i] = min_num
            for j in range(m):
                if dp[pointers[j]] * primes[j] == min_num:
                    pointers[j] += 1

        return dp[n]