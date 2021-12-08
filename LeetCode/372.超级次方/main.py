#!/usr/bin/env python
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD    # a本身可能就很大，所以先削一波

        def quick_pow(x, n):
            '''
            快速幂模板，用O(logn)复杂度计算出x^n
            '''
            res = 1
            while n > 0:
                if n & 1 == 1:
                    res *= x
                x *= x
                n = n >> 1
            return res

        ans = 1
        base = a
        for i in range(len(b) - 1, -1, -1):    # 从低位向高位，扫描b中的各个数
            ans = ans * quick_pow(base, b[i]) % MOD    # 累乘 (a^(10^k)) ^ b[i]
            base = quick_pow(base, 10) % MOD    # 让a^(10^k)也水涨船高
        return ans