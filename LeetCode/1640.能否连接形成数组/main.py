#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        p2p = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        x = y = None
        while i < len(arr):
            num = arr[i]
            if x is None:
                if num not in p2p: return False
                x, y = p2p[num], 0
            if num != pieces[x][y]: return False
            y += 1
            if y >= len(pieces[x]): x = None
            i += 1
        return True