#!/usr/bin/env python

from typing import List
import collections

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        # 构建图
        graph = collections.defaultdict(set)
        for i in range(len(routes)): routes[i] = set(routes[i])    # 为了方便之后的操作，全处理成set
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                r1, r2 = routes[i], routes[j]
                if r1.intersection(r2):    # 如果有交集
                    graph[i].add(j)
                    graph[j].add(i)

        # start_route和target_route分别表示含有source站的线路和target栈的线路的集合。
        start_route, target_route = set(), set()
        for i, route in enumerate(routes):
            if source in route: start_route.add(i)
            if target in route: target_route.add(i)

        # 开始BFS。任意的start_route中的线路都可作为起始节点
        queue = collections.deque([])
        for route in start_route:
            queue.append((route, 1))

        seen = set()
        while queue:
            route, depth = queue.popleft()
            if route in target_route: return depth
            seen.add(route)
            for nxt in graph[route]:
                if nxt not in seen:
                    queue.append((nxt, depth + 1))

        return -1