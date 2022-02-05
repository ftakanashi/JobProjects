#!/usr/bin/env python
from typing import List

from collections import defaultdict, Counter
class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for y_prime in self.map[x]:
            if y_prime == y: continue
            edge = abs(y_prime - y)
            ans += (self.map[x-edge][y_prime] * self.map[x-edge][y] * self.map[x][y_prime])
            ans += (self.map[x+edge][y_prime] * self.map[x+edge][y] * self.map[x][y_prime])

        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)