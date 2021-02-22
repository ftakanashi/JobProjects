#!/usr/bin/env python
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        candidates = list(range(1, n+1))

        def rec(res: List[int], rest_k: int):
            if len(candidates) == 1: return ''.join(str(i) for i in res + candidates)

            base = reduce(lambda x,y:x*y, range(1, len(candidates)))
            i = 0
            while rest_k > (i + 1) * base:
                i += 1

            res.append(candidates[i])
            candidates.pop(i)
            return rec(res, rest_k - i * base)

        return rec([], k)