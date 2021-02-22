#!/usr/bin/env python

class Solution1:
    def sumNums(self, n: int) -> int:
        if n == 1: return 1
        return n + self.sumNums(n-1)

class Solution2:
    def sumNums(self, n: int) -> int:
        return sum(range(1, n+1))

class Solution3:
    def sumNums(self, n: int) -> int:
        return (n ** 2 + n) >> 1

class Solution4:
    def sumNums(self, n: int) -> int:

        def multi(a: int, b: int) -> int:
            ans = 0
            while b > 0:
                if b & 1 == 1: ans += a
                a = a << 1
                b = b >> 1
            return ans

        return multi(n, n+1) >> 1