#!/usr/bin/env python
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0 for i in range(len(nums) + 1)]
        s = 0
        for i, n in enumerate(nums):
            s += n
            self.prefix[i+1] = s

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j+1] - self.prefix[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)