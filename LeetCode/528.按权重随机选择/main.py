#!/usr/bin/env python

import bisect
import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.presum = []
        s = 0
        for ww in w:
            s += ww
            self.presum.append(s)
        self.maxi = self.presum[-1]

    def pickIndex(self) -> int:
        tgt = random.randint(1, self.maxi)
        i = bisect.bisect_left(self.presum, tgt)
        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()