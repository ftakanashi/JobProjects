#!/usr/bin/env python
from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        digit_map = {
            "6": "9", "9": "6", "0": "0", "1": "1", "8": "8"
        }

        def dfs(rest):
            if rest == 0: return ["",]
            if rest == 1: return list("018")
            res = []
            for k in digit_map:
                if k == "0" and rest == n: continue
                v = digit_map[k]
                for core in dfs(rest - 2):
                    res.append(f"{k}{core}{v}")
            return res

        return dfs(n)