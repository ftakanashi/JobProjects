#!/usr/bin/env python
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = cnt = 0
        n = len(arr)
        while i < n:
            cnt += 1 if arr[i] > 0 else 2
            if cnt >= n: break
            i += 1

        if cnt > n:
            arr[-1] = 0
            i -= 1
            j = n - 2
        else:
            j = n - 1

        while j > i:
            if arr[i] > 0:
                arr[j] = arr[i]
                j -= 1
            else:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
            i -= 1

        return