#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = n = len(num)

        def f(ch, i):
            """
            从下标 i 开始从右到左寻找第一个字符 ch 所在下标位置
            """
            while i >= 0 and num[i] != ch: i -= 1
            return i

        i = f("0", n - 1)
        if i >= 0:
            ans = min(ans, n - 1)    # 考虑字符串中至少有一个 0 时的特殊情况
            j = max(f("0", i - 1), f("5", i - 1))
            if j >= 0: ans = min(ans, n - j - 2)

        i = f("5", n - 1)
        if i >= 0:
            j = max(f("2", i - 1), f("7", i - 1))
            if j >= 0: ans = min(ans, n - j - 2)

        return ans