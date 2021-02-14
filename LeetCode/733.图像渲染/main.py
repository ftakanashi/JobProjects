#!/usr/bin/env python
from typing import List

import copy

class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 1
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.fa[root_x] = root_y
        else:
            self.fa[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1

class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                if i > 0 and image[i-1][j] == image[i][j]:
                    uf.union((i-1)*n+j, i*n+j)
                if j > 0 and image[i][j-1] == image[i][j]:
                    uf.union(i*n+j-1, i*n+j)

        new_image = copy.deepcopy(image)
        root = uf.find(sr * n + sc)
        for i in range(m*n):
            if uf.find(i) == root:
                new_image[i//n][i%n] = newColor
        return new_image

class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        new_image = copy.deepcopy(image)
        m, n = len(image), len(image[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        orig_color = image[sr][sc]

        def dfs(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if visited[x][y] == 1 or image[x][y] != orig_color:
                return
            visited[x][y] = 1
            new_image[x][y] = newColor
            for a, b in direcs:
                dfs(x + a, y + b)

        dfs(sr, sc)
        return new_image