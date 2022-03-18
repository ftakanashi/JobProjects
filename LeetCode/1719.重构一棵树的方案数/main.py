#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
        n = len(adj)

        def dfs(node):
            neighbors = adj[node].copy()
            for neb in neighbors:
                adj[neb].remove(node)
                adj[node].remove(neb)
            flag = False
            for neb in sorted(neighbors, key=lambda x:len(adj[x]), reverse=True):
                sec_neighbors = adj[neb]

                for sec_neb in sec_neighbors:
                    if sec_neb not in neighbors: return 0

                if len(adj[neb]) == len(neighbors) - 1:
                    flag = True

                res = dfs(neb)
                if res == 0:
                    return 0
                if res == 2:
                    flag = True

            return 2 if flag else 1

        possible_root = None
        for node in adj:
            if len(adj[node]) == n - 1:
                if possible_root is not None:
                    return 2
                else:
                    possible_root = node
        return dfs(possible_root) if possible_root else 0