#!/usr/bin/env python
from typing import List

import math
import random
class Solution1:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = math.sqrt(random.random()) * self.r
        theta = random.random() * math.pi * 2
        x = r * math.cos(theta) + self.x
        y = r * math.sin(theta) + self.y
        return [x, y]

class Solution2:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.o = (x_center, y_center)
        self.r = radius

    def randPoint(self) -> List[float]:
        x = y = 0
        while True:
            x = random.random() * 2 - 1
            y = random.random() * 2 - 1
            if math.sqrt(x**2 + y**2) <= 1: break
        return [x * self.r + self.o[0], y * self.r + self.o[1]]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

