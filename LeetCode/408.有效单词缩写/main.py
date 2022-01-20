#!/usr/bin/env python
import string

letters = set(string.ascii_lowercase)
digits = set("1234567890")
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        if n < m: return False

        i = j = 0
        while i < n and j < m:
            while i < n and j < m and word[i] == abbr[j]:
                i += 1
                j += 1
            if i == n or j == m: break
            if abbr[j] in letters or abbr[j] == "0": return False

            s = 0
            while j < m and abbr[j] in digits:
                s = s * 10 + int(abbr[j])
                j += 1
            i += s

        return i == n and j == m