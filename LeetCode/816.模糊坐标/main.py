#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
class Solution:
    def checkSeg(self, seg: str) -> bool:
        if len(seg) > 1 and seg.startswith("0") and seg.endswith("0"):
            return False
        return True

    def getPosFloat(self, s: str) -> List[str]:
        res = []
        if len(s) == 1 or not s.startswith("0"):
            res.append(s)
        for i in range(1, len(s)):
            front, rear = s[:i], s[i:]
            if rear.endswith("0"): continue
            if front.startswith("0") and len(front) > 1: continue
            res.append(f"{front}.{rear}")
        return res

    def ambiguousCoordinates(self, s: str) -> List[str]:
        cands = []
        s = s[1:-1]
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            if self.checkSeg(a) and self.checkSeg(b):
                cands.append((a, b))

        ans = []
        for seg_a, seg_b in cands:
            for a in self.getPosFloat(seg_a):
                for b in self.getPosFloat(seg_b):
                    ans.append(f"({a}, {b})")
        return ans