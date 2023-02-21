#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        diff = k - n
        change = {}    # change用于保存和最初的 n 个 a 相比，哪些位置需要替换为哪些字母
        for rev in range(n - 1, -1, -1):
            if diff > 25:
                change[rev] = "z"
                diff -= 25
            elif diff > 0:
                change[rev] = chr(ord("a") + diff)
                diff = 0
            elif diff == 0:
                break

        ans = "".join(change.get(i, "a") for i in range(n))
        return ans