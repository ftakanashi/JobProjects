#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import numpy as np
import itertools
class Solution1:
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


class Solution2:
    def getHull(self, points: List[List[int]]) -> List[List[int]]:
        '''
        Andrew算法求凸包
        '''
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(points)
        if n < 4:
            return points

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        points.sort()

        hull = []
        # 求凸包的下半部分
        for i, p in enumerate(points):
            while len(hull) > 1 and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            while len(hull) > m and cross(hull[-2], hull[-1], points[i]) <= 0:
                hull.pop()
            hull.append(points[i])
        hull.pop()  # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        return hull

    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        hull = self.getHull(points)
        n = len(hull)
        ans = 0
        for i in range(n):
            p = hull[i]
            k = i + 2
            for j in range(i + 1, n - 1):
                q = hull[j]
                while k < n - 1:    # 独立于 j 的 k 的遍历进程
                    r = hull[k]
                    nr = hull[k + 1]
                    curr = triangleArea(p[0], p[1], q[0], q[1], r[0], r[1])
                    nxt = triangleArea(p[0], p[1], q[0], q[1], nr[0], nr[1])
                    if curr >= nxt: break
                    k += 1

                r = hull[k]
                ans = max(ans, triangleArea(p[0], p[1], q[0], q[1], r[0], r[1]))

        return ans