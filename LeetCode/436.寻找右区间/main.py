#!/usr/bin/env python
from typing import List

class Solution:
    def binary(self, data, target):
        '''
        二分查找。data是扩张后带有下标且排好序的数组。
        target是要查找的某个基准区间的右端点
        '''
        l, r = 0, len(data) - 1
        while l <= r:
            mid = (l + r) // 2
            if data[mid][0] < target:    # 因为某个区间的左端点恰好是基准区间右端点时也认可，所以不能取等号
                l = mid + 1
            else:
                r = mid - 1
        return data[l][-1] if l < len(data) else -1

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        data = [(s, e, i) for i, (s, e) in enumerate(intervals)]
        data.sort()
        return [self.binary(data, e) for s, e in intervals]