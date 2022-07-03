#!/usr/bin/env python
import math

class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    def factorial(self, x: int) -> int:
        res = 1
        mod = 10 ** 9 + 7
        for i in range(2, x + 1):
            res *= i
            res = res % mod
        return res

    def numPrimeArrangements(self, n: int) -> int:
        prime_cnt = 0
        for i in range(2, n + 1):
            if self.isPrime(i):
                prime_cnt += 1

        ans = 1
        mod = 10 ** 9 + 7
        ans *= self.factorial(prime_cnt)
        ans = ans % mod
        ans *= self.factorial(n - prime_cnt)
        ans = ans % mod
        return ans