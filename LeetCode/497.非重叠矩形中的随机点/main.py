#!/usr/bin/env python
from typing import List

import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = [0, ]
        for x1, y1, x2, y2 in self.rects:
            self.areas.append(self.areas[-1] + (y2-y1+1) * (x2-x1+1))    # 以矩形包含的整数点数量为基准构建前缀和
        self.upperBound = self.areas[-1]

    def pick(self) -> List[int]:
        seed = random.random() * self.upperBound
        i = bisect.bisect_left(self.areas, seed)    # 二分查找随机数所处区间
        x1, y1, x2, y2 = self.rects[i-1]    # 别忘了前缀和数组的i对应的是矩形数组中的下标为i-1的矩形
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()