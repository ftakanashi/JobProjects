#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 初始化，将每个会议的开始时间和会议的对应关系维护到哈希表
        n, start_map = 0, {}
        for e in events:
            n = max(n, e[1])
            if e[0] not in start_map:
                start_map[e[0]] = []
            start_map[e[0]].append(e)

        # 开始扫描每一天
        meetings = []
        count = 0
        for d in range(1, n+1):     # 注意程序里所有的"天"都是从1开始的
            # 将今天开始的会议入堆，堆里保存的是[end, start]，因为是要以结束日期作为依据维持堆序
            for m in start_map.get(d, []):
                heapq.heappush(meetings, [m[1], m[0]])

            # 去除堆中已经结束的会议
            while meetings and meetings[0][0] < d:
                heapq.heappop(meetings)

            # 如果此时还有会议未参加，即堆非空，就参加堆顶表示的会议
            if meetings:
                heapq.heappop(meetings)
                count += 1

        return count