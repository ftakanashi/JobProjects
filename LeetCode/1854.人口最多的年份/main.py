#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        for a, b in logs:
            years.append((a, 1))
            years.append((b, -1))

        diff = defaultdict(int)
        for year, t in years:
            diff[year] += t

        max_p, max_year = 0, None
        popu = 0
        for year in sorted(diff):
            popu += diff[year]
            if popu > max_p:
                max_p = popu
                max_year = year

        return max_year