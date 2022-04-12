#!/usr/bin/env python
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        counter = {"A": 0, "B": 0}
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                counter[colors[i]] += 1

        return counter["A"] > counter["B"]