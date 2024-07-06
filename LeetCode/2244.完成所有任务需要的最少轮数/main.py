#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        ans = 0
        for t, c in cnt.items():
            if c == 1: return -1
            ans += (c + 2) // 3
        return ans