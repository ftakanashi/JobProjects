#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def minOperations(self, s: str) -> int:

        def check(init_prev):
            prev = init_prev
            tmp = 0
            for ch in s:
                if ch != prev:
                    prev = ch
                else:
                    tmp += 1
                    prev = "0" if prev == "1" else "1"
            return tmp

        return min(check("0"), check("1"))