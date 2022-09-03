#!/usr/bin/env python
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        # 进行一些初始化和初步统计工作
        m, n = len(isInfected), len(isInfected[0])
        direcs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rest = m * n
        for i in range(m):
            for j in range(n):
                rest -= isInfected[i][j]

        # DFS函数
        def dfs(x, y, seen):
            to_be_infected = set()
            need_wall = 0
            if (x, y) in seen or isInfected[x][y] == 0: return to_be_infected, need_wall, seen
            seen.add((x, y))
            for a, b in direcs:
                nx, ny = x + a, y + b
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if isInfected[nx][ny] == 0:    # 下一个格子为0，则将其加入预备被感染的哈希集to_be_infected，同时need_wall += 1
                    to_be_infected.add((nx, ny))
                    need_wall += 1
                elif isInfected[nx][ny] == -1:    # -1是指前一轮中该格子的病毒被灭活，所以不用做任何事
                    pass
                else:    # 该格子是1的情况，开启下一轮dfs
                    nxt_infected, nxt_wall, _ = dfs(nx, ny, seen)
                    to_be_infected = to_be_infected.union(nxt_infected)
                    need_wall += nxt_wall
            return to_be_infected, need_wall, seen

        cache = []    # cache用于保存一轮感染中，所有连通分量的统计数据
        ans = 0
        while rest > 0:
            checked = set()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 1 or (i, j) in checked: continue
                    to_be_infected, need_wall, seen = dfs(i, j, set())
                    checked = checked.union(seen)
                    cache.append((to_be_infected, need_wall, seen))
            cache.sort(key=lambda x: len(x[0]))    # 根据预备感染的方块数量进行排序

            if len(cache) == 0:
                break

            to_be_infected, need_wall, seen = cache.pop()    # 选择含有最多的预备感染方块数的连通分量
            ans += need_wall
            for x, y in seen:
                isInfected[x][y] = -1    # 将这连通分量内的方块全部置-1

            for area, _, _ in cache:
                for x, y in area:
                    if isInfected[x][y] != 1:
                        isInfected[x][y] = 1
                        rest -= 1    # 维护rest

            cache.clear()    # 别忘了每轮感染后将cache清空

        return ans