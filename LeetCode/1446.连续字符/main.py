#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maxPower(self, s: str) -> int:
        i = j = 0
        letter = s[0]
        max_len = 0
        while j < len(s):
            if s[j] != letter:
                max_len = max(max_len, j - i)
                i = j
                letter = s[j]
            j += 1

        max_len = max(max_len, j - i)

        return max_len