#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            std = s[i]
            while i < len(s) and s[i] == std:
                i += 1
            if i >= j: break
            while j >= 0 and s[j] == std:
                j -= 1

        return max(0, j - i + 1)