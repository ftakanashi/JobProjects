#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def countTime(self, time: str) -> int:
        hh, mm = time.split(":")
        ans = 1
        if hh == "??":
            ans *= 24
        elif hh[1] == "?" and hh[0] != "2":
            ans *= 10
        elif hh[1] == "?" and hh[0] == "2":
            ans *= 4
        elif hh[0] == "?" and hh[1] in "0123":
            ans *= 3
        elif hh[0] == "?":
            ans *= 2

        if mm == "??":
            ans *= 60
        elif mm[0] == "?":
            ans *= 6
        elif mm[1] == "?":
            ans *= 10

        return ans