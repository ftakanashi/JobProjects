#!/usr/bin/env python
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def complex2tuple(num):
            r, c = num.split("+")
            r = int(r)
            c = int(c[:-1])
            return (r, c)

        r1, c1 = complex2tuple(num1)
        r2, c2 = complex2tuple(num2)
        r_ans = r1 * r2 - c1 * c2
        c_ans = r1 * c2 + r2 * c1
        return f"{r_ans}+{c_ans}i"