#!/usr/bin/env python
from typing import List

import string

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        letters = set(string.ascii_lowercase + string.ascii_uppercase)

        def dfs(pos, part):
            if pos == n:
                ans.append(part)
                return
            if s[pos] in letters:
                dfs(pos + 1, part + s[pos].lower())
                dfs(pos + 1, part + s[pos].upper())
            else:
                dfs(pos + 1, part + s[pos])

        dfs(0, "")
        return ans