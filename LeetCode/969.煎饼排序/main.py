#!/usr/bin/env python
from typing import List

class Solution:
    def findMax(self, arr: List[int], end: int) -> int:
        '''
        寻找arr中[:end+1]范围内最大值的下标
        '''
        _max = float('-inf')
        ans = -1
        for i, num in enumerate(arr):
            if i > end: break
            if num > _max:
                _max = num
                ans = i
        return ans

    def reversePart(self, arr: List[int], start: int, end: int):
        '''
        将arr的[start:end+1]部分翻转。双指针。
        '''
        i, j = start, end
        while i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for end in range(len(arr) - 1, 0, -1):
            max_i = self.findMax(arr, end)
            if max_i == end: continue
            self.reversePart(arr, 0, max_i)
            ans.append(max_i + 1)
            self.reversePart(arr, 0, end)
            ans.append(end + 1)

        return ans