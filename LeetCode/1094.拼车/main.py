#!/usr/bin/env python
from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = defaultdict(int)
        for people, start, end in trips:
            diff[start] += people
            diff[end] -= people
        s = 0
        for node in sorted(diff):
            s += diff[node]
            if s > capacity: return False
        return True