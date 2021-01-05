#!/usr/bin/env python
from typing import List

class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s: str, l: int, r: int):
            if l == n and r == n:
                res.append(s)
                return
            if l < n:
                dfs(s + '(', l+1, r)
            if l > r:
                dfs(s + ')', l, r+1)

        dfs('', 0, 0)
        return res