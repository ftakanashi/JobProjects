#!/usr/bin/env python
from typing import List

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        n = 0
        for i in range(len(A)):
            n = (n * 2 + A[i]) % 5
            res.append(n == 0)
        return res