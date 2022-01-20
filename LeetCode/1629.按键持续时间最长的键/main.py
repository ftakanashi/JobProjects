#!/usr/bin/env python
from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keytime = {}
        n = len(keysPressed)
        keytime[keysPressed[0]] = releaseTimes[0]
        for i in range(1, n):
            period = releaseTimes[i] - releaseTimes[i-1]
            key = keysPressed[i]
            if key not in keytime or keytime[key] < period:
                keytime[key] = period

        for k in sorted(keytime, reverse=True, key=lambda x:(keytime[x], x)):
            return k