#!/usr/bin/env python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count, di, i, j = 0, 0, 0, 0
        d = direcs[di]
        res = []
        while count < m * n:
            while 0 <= i < m and 0 <= j < n and visited[i][j] == 0:
                res.append(matrix[i][j])
                count += 1
                visited[i][j] = 1
                i += d[0]
                j += d[1]

            i -= d[0]    # 别忘了，上面循环结束后i,j是越界状态，要减回去
            j -= d[1]
            di += 1
            if di >= 4: di = 0
            d = direcs[di]
            i += d[0]
            j += d[1]

        return res


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    res.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res