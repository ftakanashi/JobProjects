#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import numpy as np
import itertools
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def area(three_points):
            # 用鞋带公式，通过行列式绝对值的办法根据坐标求面积
            (x1, y1), (x2, y2), (x3, y3) = three_points
            return abs(0.5 * np.linalg.det([
                [x1, y1, 1],
                [x2, y2, 1],
                [x3, y3, 1]
            ]))

        max_area = 0
        # 暴力，用itertools更省内存
        for ps in itertools.combinations(points, 3):
            max_area = max(max_area, area(ps))
        return max_area