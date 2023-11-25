#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from heapq import heappush, heappop

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        wait_l, wait_r, work_l, work_r = [], [], [], []
        remain, curr = n, 0

        # wait队列优先度计算函数
        f = lambda i: (-(time[i][0] + time[i][2]), -i)

        # 初始状态，所有人都在左岸的 wait 队列
        for i, t in enumerate(time):
            heappush(wait_l, [f(i), i])

        # 循环条件：只要右边仓库还有箱子或者右岸还有人
        while remain > 0 or work_r or wait_r:

            # 情况1. 有人在右边手拿箱子等待过桥
            if wait_r:
                _, i = heappop(wait_r)
                curr += time[i][2]
                heappush(work_l, [curr + time[i][3], i])

            # 情况2. 右边仓库还有箱子且左边有人等待过桥
            elif remain > 0 and wait_l:
                _, i = heappop(wait_l)
                curr += time[i][0]
                heappush(work_r, [curr + time[i][1], i])
                remain -= 1

            # 情况3. 没人等待过桥（或者右边仓库空了，那左边即使有人等待过桥也没必要过
            else:
                nxt = float("inf")
                if work_l: nxt = min(nxt, work_l[0][0])
                if work_r: nxt = min(nxt, work_r[0][0])
                curr = max(nxt, curr)

            # 后处理，由于 curr 的推进，可以将work完成时间早于当前时间的人都pop出来放到 wait 队列中。
            while work_l and work_l[0][0] <= curr:
                _, i = heappop(work_l)
                heappush(wait_l, [f(i), i])

            while work_r and work_r[0][0] <= curr:
                _, i = heappop(work_r)
                heappush(wait_r, [f(i), i])

        return curr