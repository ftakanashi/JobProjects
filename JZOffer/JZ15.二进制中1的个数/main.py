#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n & 1
            n = (n >> 1)
        return res


class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        p = 1
        for _ in range(32):
            if n & p == p:
                res += 1
            p = p << 1
        return res


class Solution3:
    def hammingWeight(self, n: int) -> int:
        res = 0
        p = 1
        for _ in range(32):
            if n & p == p:
                res += 1
            p = p << 1
        return res


class Solution4:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n & (n - 1)  # 每进行一次操作就减少一个1
            res += 1
        return res
