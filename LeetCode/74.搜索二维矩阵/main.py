#!/usr/bin/env python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            mx, my = mid // n, mid % n
            mid_v = matrix[mx][my]
            if mid_v == target: return True
            elif mid_v < target:
                left = mid + 1
            else:
                right = mid - 1
        return False