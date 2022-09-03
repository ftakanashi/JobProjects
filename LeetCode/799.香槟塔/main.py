#!/usr/bin/env python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured, ]
        curr_row = 0
        while curr_row < query_row:
            new_row = [0 for _ in range(len(row) + 1)]
            for i, v in enumerate(row):
                if v > 1:
                    flowed = (v - 1) / 2
                    new_row[i] += flowed
                    new_row[i + 1] += flowed
            row = new_row
            curr_row += 1

        return min(1, row[query_glass])