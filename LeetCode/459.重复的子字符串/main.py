#!/usr/bin/env python

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        for i in range(n // 2 if n & 1 == 0 else n // 2 + 1):    # 为了避免len(s) == 2的情况时的尴尬状况，这里分奇偶性讨论
            if n % (i + 1) == 0 and s == s[:i+1] * (n // (i+1)):
                return True
        return False