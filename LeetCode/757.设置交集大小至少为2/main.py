#!/usr/bin/env python
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 按照右边界从小到大排序
        intervals.sort(key=lambda x:x[1])

        n = len(intervals)
        totals = [0 for _ in range(n)]    # 记录结果集合中每个区间对应的已经加入集合的数字个数，目标是totals中所有数字>=2
        ans = set()

        # 开始遍历
        for i, (start, end) in enumerate(intervals):
            pivot = end    # 根据贪心原则，尽量选择区间靠右的数字作为基准

            # 避免end之前可能已经被加入集合做一个小修正
            while pivot in ans and pivot >= start:
                pivot -= 1

            while totals[i] < 2:
                ans.add(pivot)
                totals[i] += 1
                for j in range(i+1, n):    # 向后遍历剩余集合
                    if pivot < intervals[j][0]:
                        break
                    totals[j] += 1
                pivot -= 1

        return len(ans)