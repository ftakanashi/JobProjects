#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = logs[0][0]
        max_v = logs[0][1]
        for i in range(1, len(logs)):
            v = logs[i][1] - logs[i - 1][1]
            if v >= max_v:
                if v == max_v:
                    ans = min(logs[i][0], ans)
                else:
                    ans = logs[i][0]
                max_v = v

        return ans