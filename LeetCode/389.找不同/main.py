#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = {}
        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1

        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return ch
            counter[ch] -= 1

class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in (s + t):
            res = res ^ ord(ch)
        return chr(res)