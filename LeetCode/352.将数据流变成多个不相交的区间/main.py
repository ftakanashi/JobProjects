#!/usr/bin/env python
from typing import List

class SummaryRanges:

    def __init__(self):
        self.ranges = []
        self.seen = set()

    def search(self, target: int) -> int:    # 二分辅助方法
        l, r = 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > self.ranges[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def addNum(self, val: int) -> None:
        if val in self.seen: return
        self.seen.add(val)
        n = len(self.ranges)
        if n == 0:    # 初始情况
            self.ranges.append([val, val])
            return

        i = self.search(val)
        # 判断插入位置两侧区间是否至少有一侧会因为新数的进入而变化
        if (i > 0 and self.ranges[i-1][1] == val - 1) or (i < n and self.ranges[i][0] == val + 1):
            if (i > 0 and self.ranges[i-1][1] == val - 1) and (i < n and self.ranges[i][0] == val + 1):
                # 若两侧都会变化，那说明新数可以粘合原有的两个区间，因此粘合区间并且去除掉一个
                self.ranges[i-1][1] = self.ranges[i][1]
                self.ranges.pop(i)
            elif i > 0 and self.ranges[i-1][1] == val-1:
                self.ranges[i-1][1] = val
            else:
                self.ranges[i][0] = val
        else:
            self.ranges.insert(i, [val, val])


    def getIntervals(self) -> List[List[int]]:
        return self.ranges

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()