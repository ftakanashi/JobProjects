#!/usr/bin/env python
from typing import List

from collections import defaultdict
import bisect

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tours = defaultdict(list)
        for a, b in tickets:
            bisect.insort(tours[a], b)    # 构建邻接表时就保证下一个节点列表有序

        res = []
        def dfs(pos, rest):
            if len(tours[pos]) == 0:
                if rest == 0:
                    res.append(pos)    # 别忘了最后一个节点也要收割
                    return True
                return False

            res.append(pos)    # 收割当前节点并继续检查下一节点
            for i, nxt in enumerate(tours[pos]):    # 按顺序遍历，保证字典序最小
                tours[pos].pop(i)
                if dfs(nxt, rest - 1): return True
                tours[pos].insert(i, nxt)
            res.pop()
            return False

        dfs('JFK', len(tickets))
        return res

import heapq
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)
        for pos in graph:
            heapq.heapify(graph[pos])    # 采用堆保证时刻可以取到剩余边中使得字典序最小的那个

        stack = []
        def dfs(pos):
            while graph[pos]:
                nxt = heapq.heappop(graph[pos])
                dfs(nxt)
            # 只有确认某个节点出发的都已经用完了，再将这个节点入栈
            stack.append(pos)

        dfs("JFK")
        stack.reverse()    # 最后别忘了栈是倒着的，所以要逆序一下。
        return stack