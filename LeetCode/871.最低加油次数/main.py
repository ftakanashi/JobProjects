#!/usr/bin/env python
from typing import List

import heapq
from collections import deque

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans, max_reach = 0, startFuel
        heap = []
        stations = deque(stations)

        while max_reach < target:

            while stations and stations[0][0] <= max_reach:
                pos, fuel = stations.popleft()
                heapq.heappush(heap, (-fuel, pos))

            if len(heap) == 0:    # 此时若堆已经空，但是max_reach还未达到target，说明target永远不可达，直接返回-1
                return -1

            fuel, pos = heapq.heappop(heap)
            fuel = -fuel
            max_reach += fuel
            ans += 1

        return ans