#!/usr/bin/env python
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        m, n = len(bikes), len(workers)
        data = []
        for i in range(n):
            worker = tuple(workers[i])
            for j in range(m):
                bike = tuple(bikes[j])
                dist = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
                data.append((dist, i, j))

        used_workers = set()
        used_bikes = set()
        ans = [-1 for _ in range(n)]
        done_cnt = 0
        for dist, worker, bike in sorted(data):
            if worker in used_workers or bike in used_bikes: continue
            ans[worker] = bike
            used_workers.add(worker)
            used_bikes.add(bike)
            done_cnt += 1
            if done_cnt == n: break    # 小剪个枝
        return ans