#!/usr/bin/env python
from typing import List

class Solution:
    def helper(self, nums: List[int]) -> int:
        stack = []
        left, right = [], []
        i = 0
        while i < len(nums):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left.append(-1 if not stack else stack[-1])
            stack.append(i)
            i += 1

        i = len(nums) - 1
        stack = []
        while i >= 0:
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right.append(len(nums) if not stack else stack[-1])
            stack.append(i)
            i -= 1
        right.reverse()

        i = 0
        res = 0
        while i < len(nums):
            res = max(res, (right[i] - left[i] - 1) * nums[i])
            i += 1
        return res


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if j == 0 or matrix[i][j] != '1': matrix[i][j] = int(matrix[i][j])
                else: matrix[i][j] = matrix[i][j-1] + 1

        res = 0
        for j in range(n-1, -1, -1):
            res = max(res, self.helper([matrix[i][j] for i in range(m)]))
        return res