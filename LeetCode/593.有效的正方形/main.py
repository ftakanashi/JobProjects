#!/usr/bin/env python
from typing import List

import math
class Solution1:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if self.check(p1, p2, p3, p4): return True
        if self.check(p1, p3, p2, p4): return True
        if self.check(p1, p4, p2, p3): return True
        return False

    def check(self, p1, p2, p3, p4):
        def dist(pa, pb):    # 计算两点距离
            return math.sqrt(
                (pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2
            )

        def equal(f1, f2):    # 判断两个浮点数的相等
            return abs(f1 - f2) <= 1e-5

        def is_mid(pa, pb, mid):    # 判断pa和pb的中点是否是mid
            return equal(abs(mid[0]), abs((pa[0] + pb[0]) / 2)) \
                   and equal(abs(mid[1]), abs((pa[1] + pb[1]) / 2))

        def get_line(pa, pb):    # 计算pa和pb构成的直线的斜率与截距
            if pa[0] == pb[0]:
                return None, pa[0]
            else:
                k = (pb[1] - pa[1]) / (pb[0] - pa[0])
                b = pa[1] - pa[0] * k
                return k, b

        def get_inter(line1, line2):    # 计算两条线的交点
            k1, b1 = line1
            k2, b2 = line2
            if k1 is None and k2 is None:
                return None
            elif k1 is None:
                return (b1, k2*b1+b2)
            elif k2 is None:
                return (b2, k1*b2+b1)
            elif k1 == k2:
                return None
            x = (b1 - b2) / (k2 - k1)
            y = k1 * x + b1
            return x, y

        def is_vertical(line1, line2):    # 判断两条线是否互相垂直
            k1, b1 = line1
            k2, b2 = line2
            if k1 is None:
                return k2 == 0
            if k2 is None:
                return k1 == 0
            return equal(k1 * k2, -1)

        l1 = get_line(p1, p2)
        l2 = get_line(p3, p4)
        if not is_vertical(l1, l2): return False
        if not equal(dist(p1, p2), dist(p3, p4)): return False
        inter = get_inter(l1, l2)
        return is_mid(p1, p2, inter) and is_mid(p3, p4, inter)

class Solution2:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points.sort()
        p1, p2, p3, p4 = points

        def dist(pa, pb):
            return math.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)

        def equal(f1, f2):
            return abs(f1 - f2) <= 1e-5

        p1p2 = dist(p1, p2)
        p1p3 = dist(p1, p3)
        p1p4 = dist(p1, p4)
        p2p3 = dist(p2, p3)
        p2p4 = dist(p2, p4)
        p3p4 = dist(p3, p4)
        return p1p2 > 0 and equal(p1p2, p1p3) and equal(p1p2, p2p4) and equal(p1p2, p3p4) and equal(p1p4, p2p3)