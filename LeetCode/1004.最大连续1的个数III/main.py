#!/usr/bin/env python
from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right, max_len, zeros = 0, 0, 0, 0
        while right < len(A):
            zeros += (1 - A[right])
            max_len = max(max_len, right - left)
            while zeros > K:
                zeros -= (1 - A[left])
                left += 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len