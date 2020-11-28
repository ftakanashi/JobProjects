#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import collections
import itertools
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = collections.Counter(sum(p) for p in itertools.product(A, B))

        count = 0
        for p in itertools.product(C, D):
            s = sum(p)
            if -s in counter:
                count += counter[-s]
        return count