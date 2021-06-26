#!/usr/bin/env python

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        def sum_with(k, N):
            return (1 - k ** N) // (1 - k)

        for N in range(len(bin(n)) - 2, 1, -1):
            l = 2
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                v = sum_with(mid, N)

                if v < n:
                    l = mid + 1
                elif v > n:
                    r = mid - 1
                else:
                    return str(mid)