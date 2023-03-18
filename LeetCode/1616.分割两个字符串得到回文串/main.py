#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def simpleCheck(self, s: str) -> bool:
        """
        简单检查s的回文性
        """
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        return i >= j

    def helper(self, a: str, b: str) -> bool:
        """
        检查 a前缀 + b后缀 的可能性
        """
        n = len(a)
        i, j = 0, n - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1

        if i >= j: return True
        if self.simpleCheck(b[i:j + 1]) or self.simpleCheck(a[i:j + 1]):
            return True

        return False

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.simpleCheck(a) or self.simpleCheck(b) or self.helper(a, b) or self.helper(b, a)