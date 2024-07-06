#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from bisect import bisect_left
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda task: task[1])
        st = [[-1, -1, 0]]

        for start, end, duration in tasks:
            k = bisect_left(st, start, key=lambda s: s[0])

            duration -= st[-1][2] - st[k - 1][2]
            if start <= st[k - 1][1]:
                duration -= st[k - 1][1] - start + 1

            if duration <= 0: continue

            while end - st[-1][1] <= duration:
                duration += st[-1][1] - st[-1][0] + 1
                st.pop()
            st.append([end - duration + 1, end, st[-1][2] + duration])

        return st[-1][2]