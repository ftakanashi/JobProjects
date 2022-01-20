#!/usr/bin/env python
from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        if len(words[0]) != n: return False
        for i in range(n):
            if len(words[i]) > n: return False
            words[i] = words[i] + '-' * (n - len(words[i]))

        for i in range(n):
            for j in range(i, n):
                if words[i][j] != words[j][i]:
                    return False
        return True