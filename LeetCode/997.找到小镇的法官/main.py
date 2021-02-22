#!/usr/bin/env python
from typing import List

class Solution1:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1
        in_map, out_map = {}, {}
        for a, b in trust:
            if a not in out_map:
                out_map[a] = []
            if b not in in_map:
                in_map[b] = []
            out_map[a].append(b)
            in_map[b].append(a)

        for person in in_map:
            if len(in_map[person]) == N - 1 and person not in out_map:
                return person
        return -1

class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l = [0 for _ in range(N)]
        for a, b in trust:
            l[a-1] -= 1
            l[b-1] += 1

        for i, val in enumerate(l):
            if val == N - 1: return i + 1
        return -1