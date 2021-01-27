#!/usr/bin/env python
from typing import List

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[x] < self.rank[y]:
                self.fa[root_x] = root_y
            else:
                self.fa[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        ind = lambda a,b: a * n + b
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    uf.find(ind(i,j))
                    if i >= 1 and grid[i-1][j] == '1':
                        uf.union(ind(i,j), ind(i-1, j))
                    if j >= 1 and grid[i][j-1] == '1':
                        uf.union(ind(i,j), ind(i, j-1))

        return sum([1 if k == uf.find(k) else 0 for k in uf.fa])

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direcs = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int):
            visited[i][j] = 1
            for a, b in direcs:
                if 0 <= i + a < m and 0 <= j + b < n and visited[i+a][j+b] == 0 and grid[i][j] == '1':
                    dfs(i+a, j+b)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count