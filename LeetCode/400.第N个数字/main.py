#!/usr/bin/env python

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        s = 0
        while n > s:
            i += 1
            s += (9 * pow(10, i-1) * i)

        # i指出了序列第n个数字属于X位数

        k = 0
        base = 0
        while k < i - 1:
            k += 1
            base += (9 * pow(10, k-1) * k)

        # base表示所有1位数，2位数，... (X-1)位数总共有的数字数量
        # 确定了i和base后，只需要看n与base的差值和i之间的关系，就能轻松得到答案

        num = (((n - base - 1) // i)) + pow(10, i-1)
        dig = (n - base) % i
        return int(str(num)[dig-1])