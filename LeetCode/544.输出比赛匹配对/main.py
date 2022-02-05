#!/usr/bin/env python

class Solution:
    def findContestMatch(self, n: int) -> str:
        cands = [i+1 for i in range(n)]
        while len(cands) > 1:
            new_cands = []
            for d in range(len(cands) // 2):
                new_cands.append(
                    f"({cands[d]},{cands[len(cands)-1-d]})"
                )
            cands = new_cands
        return cands[0]