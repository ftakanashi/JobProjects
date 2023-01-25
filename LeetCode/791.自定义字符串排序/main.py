#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch2i = {ch: i for i, ch in enumerate(order)}

        def check(ch):
            """
            排序依据字符在order中出现的下标，越小的越靠前。
            若从未在order中出现，根据题意，直接赋予无穷大
            """
            if ch not in ch2i: return float('inf')
            return ch2i[ch]

        return "".join(sorted([ch for ch in s], key=check))