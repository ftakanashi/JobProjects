#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 构建图 对于richer中的[ai, bi]，建立一条 ai -> bi 的有向边
        graph = defaultdict(list)
        for a, b in richer:
            graph[a].append(b)

        n = len(quiet)
        ans = [i for i in range(n)]    # 初始化答案数组 注意答案数组保存的是下标，即节点名

        def dfs(node, q_i):
            '''
            node是dfs扫描到这层时的出发节点
            q_i则是本轮扫描最开始的节点的下标
            因此，只有当当前节点保有的安静值(quiet[ans[node]])大于本轮扫描开始节点的那个值(quiet[q_i])，才会更新
            同理，对于下一轮扫描节点的选择，也应该符合上述条件
            '''
            if quiet[ans[node]] > quiet[q_i]:
                ans[node] = q_i
            for nxt in graph[node]:
                if quiet[ans[nxt]] > quiet[q_i]:
                    dfs(nxt, q_i)

        for i in range(n):    # 从每个节点都要开始一轮扫描，确保没有遗漏
            dfs(i, i)
        return ans