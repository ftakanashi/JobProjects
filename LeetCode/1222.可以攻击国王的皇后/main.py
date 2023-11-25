#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        direcs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for a, b in direcs:
            i, j = king
            while i in range(8) and j in range(8):
                if [i, j] in queens:
                    ans.append([i, j])
                    break
                i += a
                j += b

        return ans