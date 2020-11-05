#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def cuttingRope(self, n: int) -> int:
        # 特殊情况处理（cache中这些小长度值都直接作为"片段"来使用
        if n == 2: return 1
        if n == 3: return 2

        # 初始化数组
        cache = [0 for _ in range(n + 1)]

        # 最初的简单子问题解
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        cache[3] = 3

        # 递推
        i = 4
        while i <= n:
            cache[i] = max([cache[j] * cache[i - j] for j in range(1, i//2 + 1)])
            i += 1

        return cache[n]

class Solution2:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        res = 1
        while n > 5:
            res *= 3
            n -= 3

        if n == 5:
            res *= 6
        else:
            res *= n

        return res