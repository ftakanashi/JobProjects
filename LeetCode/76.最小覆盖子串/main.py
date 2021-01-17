#!/usr/bin/env python
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = collections.Counter(t)
        i, j = 0, 0
        res = ''
        while j < len(s):
            while j < len(s):
                if s[j] in c: c[s[j]] -= 1
                if max(c.values()) == 0: break
                j += 1

            if j == len(s):
                break

            while i < j:
                if s[i] in c: c[s[i]] += 1
                if max(c.values()) > 0: break
                i += 1

            if res == '' or len(res) > j - i + 1:
                res = s[i:j+1]

            i += 1
            j += 1

        return res