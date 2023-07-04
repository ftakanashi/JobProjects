#!/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import permutations
from collections import Counter

class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        return sum(len(set(permutations(tiles, i))) for i in range(1, len(tiles) + 1))

class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def dfs(pos):
            res = 1
            for t in counter:
                if counter[t] == 0: continue
                counter[t] -= 1
                res += dfs(pos + 1)
                counter[t] += 1

            return res

        return dfs(0) - 1