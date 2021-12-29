#!/usr/bin/env python

# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(n):
            if knows(cand, i):
                cand = i

        for i in range(n):
            if i == cand: continue
            if knows(i, cand) and not knows(cand, i): continue
            return -1
        return cand