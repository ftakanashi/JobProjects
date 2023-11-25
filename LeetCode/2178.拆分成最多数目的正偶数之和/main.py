#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1 == 1: return []
        i = 2
        ans = []
        while finalSum >= i:
            ans.append(i)
            finalSum -= i
            i += 2
        ans[-1] += finalSum
        return ans