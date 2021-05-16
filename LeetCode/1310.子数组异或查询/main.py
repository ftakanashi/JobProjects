#!/usr/bin/env python

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        presum, s = [0, ], 0
        for n in arr:
            s = s ^ n
            presum.append(s)

        res = []
        for a, b in queries:
            res.append(presum[b+1] ^ presum[a])
        return res