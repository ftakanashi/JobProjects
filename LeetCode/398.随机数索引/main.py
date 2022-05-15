#!/usr/bin/env python
from typing import List
from collections import defaultdict

import random

class Solution1:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for ni, num in enumerate(nums):
            self.map[num].append(ni)

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])

class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        ans = -1
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if random.random() < (1 / cnt): ans = i    # 蓄水池抽样
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)