#!/usr/bin/env python

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]

        rev1 = ''.join(reversed(num1))
        rev2 = ''.join(reversed(num2))
        for i in range(m):
            for j in range(n):
                res[i+j] += ( int(rev1[i]) * int(rev2[j]) )

        for i in range(m + n - 1):
            if res[i] >= 10:
                res[i+1] += (res[i] // 10)
                res[i] = res[i] % 10
        return ''.join(reversed([str(c) for c in res])).lstrip('0')