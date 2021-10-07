#!/usr/bin/env python

class Solution1:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def check_in(point, square):
            a, b = point
            x1, y1, x2, y2 = square
            if x1 <= a <= x2 and y1 <= b <= y2:
                return True
            return False

        min_x = min(ax1, ax2, bx1, bx2)
        max_x = max(ax1, ax2, bx1, bx2)
        min_y = min(ay1, ay2, by1, by2)
        max_y = max(ay1, ay2, by1, by2)
        square1 = (ax1, ay1, ax2, ay2)
        square2 = (bx1, by1, bx2, by2)
        ans = 0
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                pivot = (x+0.5, y+0.5)
                if check_in(pivot, square1) or check_in(pivot, square2):
                    ans += 1
        return ans

class Solution2:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapX = max(min(ax2, bx2) - max(ax1, bx1), 0)
        overlapY = max(min(ay2, by2) - max(ay1, by1), 0)
        overlap = overlapX * overlapY
        return area1 + area2 - overlap