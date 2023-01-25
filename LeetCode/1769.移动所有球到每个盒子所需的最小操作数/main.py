#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        dp = [0 for _ in range(n)]

        total = 0
        for i, ball in enumerate(boxes):
            if ball == "1":
                dp[0] += i
                total += 1

        left = 0 if boxes[0] == "0" else 1
        for i in range(1, n):
            right = total - left
            dp[i] = dp[i - 1] + left - right
            if boxes[i] == "1":
                left += 1
        return dp