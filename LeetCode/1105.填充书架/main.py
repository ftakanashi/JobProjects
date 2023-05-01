#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [1000 * 1000 for _ in range(n)]
        dp[0] = books[0][1]

        for i in range(1, n):
            tmp_width = max_height = 0
            for j in range(i, -1, -1):
                tmp_width += books[j][0]
                if tmp_width > shelf_width: break
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], (dp[j-1] if j > 0 else 0) + max_height)

        return dp[-1]