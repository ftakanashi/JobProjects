#!/usr/bin/env python
from typing import List

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        if n == 2: return [0, 1]
        graph = defaultdict(list)
        deg = defaultdict(int)    # 记录每个节点的度数
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            deg[a] += 1
            deg[b] += 1

        border = [i for i in range(n) if deg[i] == 1]    # border记录当前节点中的边缘节点是哪些
        rest = n
        while rest > 2:    # 循环终止条件，只剩下小于两个节点时，他们就是我们要求的答案了
            rest -= len(border)    # 去除边缘节点的计数
            tmp = []    # 统计新一批边缘节点的容器
            for node in border:
                for nxt in graph[node]:
                    # 这里有个比较粗暴的地方，去除边缘节点后并不修改原图。这样很可能会导致下面deg的值出现负数
                    # 不过好在下面判断条件是 deg[nxt] == 1，因此不会出bug
                    deg[nxt] -= 1
                    if deg[nxt] == 1: tmp.append(nxt)

            border = tmp
        return border