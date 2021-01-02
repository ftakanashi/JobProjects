#!/usr/bin/env python

from typing import List

class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        i, j = float('-inf'), float('-inf')    # 指向已扫描过的最右区间的左右端点
        count = 0
        intervals.sort()
        for l, r in intervals:
            if l >= j:    # 新旧区间完全不重叠
                i, j = l, r
            else:    # 新旧区间重叠
                if r <= j:    # 且新区间更短
                    i, j = l, r
                count += 1    # 无论舍弃哪一个，终归有一个要舍弃，所以count必+1
        return count

class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if (n := len(intervals)) == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        intervals.sort()

        for i in range(1, n):
            max_dp = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0] and max_dp < dp[j] + 1:
                    max_dp = dp[j] + 1
            dp[i] = max_dp

        return n - max(dp)