#!/usr/bin/env python
from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_cnt = even_cnt = 0
        for chip in position:
            if chip & 1 == 1:
                odd_cnt += 1
            else:
                even_cnt += 1
        return min(odd_cnt, even_cnt)