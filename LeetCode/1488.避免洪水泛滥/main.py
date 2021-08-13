#!/usr/bin/env python
from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 初始化，构建 池子：出现位置队列 的字典
        full = set()
        rain_days = defaultdict(deque)
        for i, rain in enumerate(rains):
            if rain > 0:
                rain_days[rain].append(i)

        heap = []
        res = [-1 for _ in range(len(rains))]
        for i, rain in enumerate(rains):
            if rain > 0:    # 若当天下雨试图向rain号池子灌水
                if rain in full: return []    # 如果此时rain号池已经有水，则洪水泛滥
                full.add(rain)    # 否则，rain号池入哈希集
                rain_days[rain].popleft()    # 其实此处还有一个隐性制约，即这个pop出的值一定是i
                if len(rain_days[rain]) > 0:    # 若之后还有rain号池子出现
                    heapq.heappush(heap, rain_days[rain][0])    # 将其位置入堆
            else:    # 若当天是晴天，则可以抽水
                if len(heap) > 0:    # 之后还会下雨，因此这天必须未雨绸缪
                    tgt = heapq.heappop(heap)    # 找到最紧急的那天会灌满哪个池
                    res[i] = rains[tgt]    # 抽干这个池
                    full.remove(rains[tgt])    # 从哈希集中移除池
                else:
                    res[i] = 1    # 这个坑… 即晴天在结果数组中也必须有值且不能是-1，这里随便设置成1

        return res