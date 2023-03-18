#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
from collections import Counter, defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # 数据准备，图构建阶段
        node2edge = Counter()
        roads = set([(a, b) for a, b in roads])
        for a, b in roads:
            node2edge[a] += 1
            node2edge[b] += 1

        def connected(a, b):
            return (a, b) in roads or (b, a) in roads

        edge2node = defaultdict(list)
        for node in node2edge:
            edge2node[node2edge[node]].append(node)

        # 找出最多边数和次多边数
        first = second = None
        for e in sorted(edge2node, reverse=True):
            if first is None:
                first = e
            elif second is None:
                second = e
                break

        # 第一种情况
        if len(edge2node[first]) == 0:
            return 0

        # 第二种情况
        elif len(edge2node[first]) == 1:
            ans = first + second - 1
            node1 = edge2node[first][0]
            for node2 in edge2node[second]:
                if not connected(node1, node2):
                    ans = first + second
                    break

        # 第三种情况
        else:
            ans = first * 2 - 1
            node_list = edge2node[first]
            for i in range(len(edge2node[first])):
                for j in range(i):
                    if not connected(node_list[i], node_list[j]):
                        ans = first * 2
                        break

        return ans