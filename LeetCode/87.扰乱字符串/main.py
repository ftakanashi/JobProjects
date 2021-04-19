#!/usr/bin/env python

from collections import Counter

class Solution:
    def isScramble(self, str1: str, str2: str) -> bool:
        mem = {}

        def similar(a: str, b: str): return Counter(a) == Counter(b)

        def dfs(s1: str, s2: str) -> bool:

            if (s1, s2) in mem: return mem[(s1, s2)]

            if len(s1) == 1: return s1 == s2
            if not similar(s1, s2): return False

            for p in range(1, len(s1)):

                if dfs(s1[:p], s2[:p]) and dfs(s1[p:], s2[p:]):
                    mem[(s1, s2)] = True
                    return True
                if dfs(s1[:p], s2[-p:]) and dfs(s1[p:], s2[:-p]):
                    mem[(s1, s2)] = True
                    return True

            mem[(s1, s2)] = False
            return False

        return dfs(str1, str2)