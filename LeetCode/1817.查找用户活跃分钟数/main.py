#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        tmp = defaultdict(set)
        for user, time in logs:
            tmp[user].add(time)

        ans = [0 for _ in range(k)]
        for user, times in tmp.items():
            ans[len(times) - 1] += 1

        return ans