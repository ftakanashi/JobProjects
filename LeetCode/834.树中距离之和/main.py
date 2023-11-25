#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 构建图
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # 构建dp、sz、ans数组
        # 三个数组的含义分别是：
        #   dp: 0作为根节点时，各个节点到其所有子节点的距离的总和
        #   sz: 各个节点子树中的节点总数
        #   ans: 最终需要返回的，每个节点到其余所有节点的距离的总和
        ans = [0 for _ in range(n)]
        dp = [0 for _ in range(n)]
        sz = [1 for _ in range(n)]

        # 第一个dfs，填充dp和sz
        def dfs(node, parent):
            for nxt in graph[node]:
                if nxt == parent: continue
                dfs(nxt, node)
                dp[node] += dp[nxt] + sz[nxt]
                sz[node] += sz[nxt]

        # 第二个dfs，进行递归地换根，填充ans
        def dfs2(node, parent):
            ans[node] = dp[node]
            for nxt in graph[node]:
                if nxt == parent: continue

                # 保存相关值，方便后续回溯
                dpn, szn, dpx, szx = dp[node], sz[node], dp[nxt], sz[nxt]

                # 换根
                dp[node] -= (dp[nxt] + sz[nxt])
                sz[node] -= sz[nxt]
                dp[nxt] += (dp[node] + sz[node])
                sz[nxt] += sz[node]

                # 进入下一层递归
                dfs2(nxt, node)

                # 恢复相关值，回溯
                dp[node], sz[node], dp[nxt], sz[nxt] = dpn, szn, dpx, szx

        dfs(0, -1)
        dfs2(0, -1)
        return ans