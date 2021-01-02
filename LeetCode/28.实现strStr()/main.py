#!/usr/bin/env python

from typing import List

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n: return -1

        def char_hash(s: str) -> int:
            res = 0
            for ch in s:
                res = res * 26 + (ord(ch) - ord('a'))
            return res

        needle_hash = char_hash(needle)
        hay_hash = char_hash(haystack[:m])
        if hay_hash == needle_hash:
            return 0

        i = m
        while i < n:

            del_ch = haystack[i - m]
            del_hash = (ord(del_ch) - ord('a')) * (26 ** (m-1))
            add_ch = haystack[i]
            add_hash = ord(add_ch) - ord('a')

            hay_hash = 26 * (hay_hash - del_hash) + add_hash
            if hay_hash == needle_hash:
                return i - m + 1
            i += 1
        return -1

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:

        def generate_pnext(s: str) -> List[int]:
            i, k, m = 0, -1, len(s)
            pnext = [-1 for _ in range(m)]
            while i < m-1:
                if k == -1 or s[i] == s[k]:
                    pnext[i + 1] = k + 1
                    i += 1
                    k += 1
                else:
                    k = pnext[k]
            return pnext

        n, m = len(haystack), len(needle)
        j, i = 0, 0
        pnext = generate_pnext(needle)
        while j < n and i < m:
            if i == -1 or haystack[j] == needle[i]:
                i += 1
                j += 1
            else:
                i = pnext[i]
        if i == m: return j - i
        return -1