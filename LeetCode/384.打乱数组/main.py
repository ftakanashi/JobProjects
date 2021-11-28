#!/usr/bin/env python
from typing import List

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.orig.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randrange(i, n)    # randrange意为从range(i, n)中随机抽取一个数
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()