#!/usr/bin/env python
from typing import List

class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 确定equations中出现过的字母集合，并且每个字母进行编号
        char_set = set([])
        for x, y in equations:
            char_set.add(x)
            char_set.add(y)
        char_map = {ch: i for i, ch in enumerate(char_set)}
        n = len(char_map)

        # 用邻接表的方式表示图，注意对角线位置默认全是1。
        graph = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            graph[i][i] = 1.0
        for i, (x, y) in enumerate(equations):
            graph[char_map[x]][char_map[y]] = values[i]
            graph[char_map[y]][char_map[x]] = 1.0 / values[i]

        # DFS函数
        def dfs(i :int, j: int, visited: List[int]) -> int:
            visited[i] = True
            if graph[i][j] is not None:    # 如果可以直接连通
                return graph[i][j]

            # 连不通时
            for pos in range(n):
                if not visited[pos] and graph[i][pos] is not None:
                    # i -> pos能连通，探索pos -> j的可能
                    path = dfs(pos, j, visited)
                    if path > 0:    # pos -> j能连通
                        return graph[i][pos] * path    # 返回整条路径的权重积
            return -1

        res = []
        for qx, qy in queries:
            if qx not in char_map or qy not in char_map:
                res.append(-1.0)
            else:
                visited = [False for _ in range(n)]    # 注意针对每个query进行DFS搜索的时候都要用新的visited
                res.append(dfs(char_map[qx], char_map[qy], visited))
        return res