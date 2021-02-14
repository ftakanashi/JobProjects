#!/usr/bin/env python
from typing import List

class Solution:
    def binarySearch(self, nums: List[int], n: int) -> int:
        '''
        这个方法功能等同于bisect.bisect_left
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == n: return mid
            if nums[mid] < n:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = nums[:k]
        window.sort()
        res = [window[k//2] if k & 1 == 1 else (window[k//2-1] + window[k//2]) / 2]

        for i in range(k, len(nums)):
            ins_i = self.binarySearch(window, nums[i])
            window.insert(ins_i, nums[i])
            del_i = self.binarySearch(window, nums[i-k])
            del window[del_i]
            res.append(window[k//2] if k & 1 == 1 else (window[k//2-1] + window[k//2]) / 2)

        return res