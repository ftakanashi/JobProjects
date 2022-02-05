#!/usr/bin/env python
from functools import lru_cache as cache

class Solution:
    def canWin(self, currentState: str) -> bool:

        @cache
        def dfs(state):
            n = len(state)
            for i in range(n-1):
                if state[i:i+2] == "++":
                    newState = state[:i] + "--" + state[i+2:]
                    if not dfs(newState): return True
            return False

        return dfs(currentState)