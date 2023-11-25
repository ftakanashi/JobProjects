#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i = ans = 0
        while i < n - 1:
            if s[i] == "0" and s[i + 1] == "1":
                # 发现标记 "01"
                p, q = i, i + 1
                tmp = 0
                while p >= 0 and s[p] == "0" and q < n and s[q] == "1":
                    tmp += 1
                    p -= 1
                    q += 1
                ans = max(ans, tmp)
                i = q
            else:
                i += 1

        return ans * 2