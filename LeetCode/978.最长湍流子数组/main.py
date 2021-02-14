#!/usr/bin/env python
from typing import List

class Solution1:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)
        l, r = 0, 1
        max_len = 1 if arr[l] == arr[r] else 2
        while r < len(arr) - 1:
            if (arr[r-1] < arr[r] and arr[r+1] < arr[r]) or (arr[r-1] > arr[r] and arr[r+1] > arr[r]):
                r += 1
                max_len = max(max_len, r - l + 1)
            else:
                l = r
                r += 1
        return max_len

class Solution2:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp_great, dp_less = 1, 1
        max_len = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp_less = dp_great + 1
                dp_great = 1
            elif arr[i] < arr[i-1]:
                dp_great = dp_less + 1
                dp_less = 1
            else:
                dp_great = dp_less = 1

            max_len = max(max_len, dp_great, dp_less)
        return max_len