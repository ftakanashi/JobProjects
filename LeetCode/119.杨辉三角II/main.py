#!/usr/bin/env python
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1,]
        while len(res) <= rowIndex:
            for i in range(len(res) - 1, 0, -1):
                res[i] = res[i] + res[i-1]
            res.append(1)
        return res