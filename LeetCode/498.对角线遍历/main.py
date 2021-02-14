#!/usr/bin/env python
from typing import List
import collections
class Solution1:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque([(0, 0)])
        rev_flag = False
        res = []

        while queue:
            sub_res = []
            for i, j in queue:
                sub_res.append(matrix[i][j])
            if rev_flag:
                sub_res.reverse()
            res.extend(sub_res)

            length = len(queue)
            visited = set([])
            for _ in range(length):
                i, j = queue.popleft()
                if i + 1 < m and (i+1, j) not in visited:
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                if j + 1 < n and (i, j+1) not in visited:
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))

            rev_flag = not rev_flag

        return res

class Solution2:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        for pi in range(m + n - 1):
            if pi < m: i, j = pi, 0
            else: i, j = m - 1, pi - m + 1

            sub_res = []
            while 0 <= i < m and 0 <= j < n:
                sub_res.append(matrix[i][j])
                i, j = i - 1, j + 1

            if pi & 1 == 1:
                sub_res.reverse()

            res.extend(sub_res)

        return res