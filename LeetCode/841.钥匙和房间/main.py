#!/usr/bin/env python
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0 for _ in range(n)]

        def dfs(i: int) -> int:
            if visited[i] == 1: return 0
            visited[i] = 1
            s = 1
            for k in rooms[i]:
                s += dfs(k)
            return s

        return dfs(0) == n