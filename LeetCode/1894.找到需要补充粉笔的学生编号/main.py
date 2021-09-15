#!/usr/bin/env python
from typing import List

import bisect

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        presum = [chalk[0]]
        for i in range(1, len(chalk)):
            presum.append(presum[-1] + chalk[i])
        # print(presum)
        k = k % presum[-1]
        return bisect.bisect(presum, k)