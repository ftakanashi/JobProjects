#!/usr/bin/env python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def check(n: int, k: int) -> bool:
            if k % 2: return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if check(n, k):
                ans += 1
            k += 1
        return ans