#!/usr/bin/env python
from typing import List

import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        ans = 0
        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(heap, (i + days[i] - 1, apples[i]))    # 跟日期相关的统一成下标天了
            while heap and heap[0][0] < i:
                heapq.heappop(heap)
            if heap:    # 若heap为空，也不能直接结束遍历，而只是今天不吃苹果了而已
                heap[0] = (heap[0][0], heap[0][1] - 1)
                if heap[0][1] == 0: heapq.heappop(heap)
                ans += 1

        day = n    # 注意区分day和ans的区别。这里我们仍然需要一个day值表示计算到第几天了，否则无法判断某批苹果是否过期
        while heap:
            exp_day, apple_num = heapq.heappop(heap)
            if exp_day < day: continue
            diff = min(exp_day - day + 1, apple_num)    # 目前存货可供我们连续吃苹果的天数，是这两者中较小值
            ans += diff
            day += diff

        return ans