#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % ((n - 1) * 2)
        return time + 1 if time < n else n * 2 - time - 1