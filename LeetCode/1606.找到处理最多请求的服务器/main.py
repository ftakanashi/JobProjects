#!/usr/bin/env python
from typing import List

import heapq

from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        task_counts = [0 for _ in range(k)]
        busy = []
        available = SortedList([i for i in range(k)])
        n = len(arrival)

        for i in range(n):
            # 扫描每个task
            # 扫描busy堆顶，将所有此时可用的服务器重新加入available
            while busy and busy[0][0] <= arrival[i]:
                time, server = heapq.heappop(busy)
                available.add(server)

            # 需要drop
            if len(available) == 0:
                print(f"Drop Task{i}")
                continue

            pos = available.bisect_left(i % k)
            if pos == len(available): pos = 0    # 越界时记得轮转
            target = available[pos]

            print(f"Dispatch Task{i} to Server{target}")
            task_counts[target] += 1
            available.remove(target)
            heapq.heappush(busy, (arrival[i] + load[i], target))

        max_count = max(task_counts)
        return [i for i, cnt in enumerate(task_counts) if cnt == max_count]