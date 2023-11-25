#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [None for _ in range(len(queries))]
        intervals.sort(key=lambda x: x[0])    # 以左端点大小为基准，排序intervals
        queries = list(sorted(enumerate(queries), key=lambda x: x[1]))    # 排序queries，带下标信息
        heap = []

        p = 0
        for i, q in queries:
            # 将所有可能包含q的区间，即左端点小于等于q的区间入堆，堆序以区间长度和右端点为基准
            while p < len(intervals) and intervals[p][0] <= q:
                s, e = intervals[p]
                l = e - s + 1
                heapq.heappush(heap, (l, e))
                p += 1

            # 将所有右端点小于q的区间pop掉，这些区间不可能是包含q的，也就不用谈什么最小区间了
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # 堆不为空则堆顶区间为q对应的最小区间，否则-1
            ans[i] = heap[0][0] if len(heap) > 0 else -1

        return ans