#!/usr/bin/env python

import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = set(string.ascii_lowercase + string.ascii_uppercase)
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in letters:
                i += 1
            while i < j and s[j] not in letters:
                j -= 1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return "".join(s)