#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            if row[0] == 1:
                symbol = "".join([str(n ^ 1) for n in row])
            else:
                symbol = "".join([str(n) for n in row])
            cnt[symbol] += 1

        return max(cnt.values())