#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        return n // 2 if n & 1 == 0 else n