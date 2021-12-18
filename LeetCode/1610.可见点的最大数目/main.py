#!/usr/bin/env python
from typing import List

from math import atan2, pi
class Solution:
    def getTheta(self, point1: List[int], point2: List[int]) -> float:
        '''
        在保证point1与point2不是同一个点的情况下，输出point2相对point1的极角
        '''
        x1, y1 = point1
        x2, y2 = point2
        theta = atan2(y2-y1, x2-x1)
        if theta < 0:
            theta += 2*pi    # 为了后续扫描方便，直接将[-pi, 0]的输出加上一个周期，转换成[pi, 2pi]范围内
        return theta

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        thetas, base = [], 0
        for point in points:
            if point == location:
                base += 1    # 与location重合的点无论如何都可见，所以当做一个基准值统计出来即可
            else:
                thetas.append(self.getTheta(location, point))
        thetas.sort()
        thetas.extend([t + 2*pi for t in thetas])
        # 至此，thetas已经是一个升序且扩充了一个周期的极角数组

        angle = angle * pi / 180    # 360度角度制转2pi角度制

        # 滑窗
        l = r = 0
        max_len = 0
        while r < len(thetas):
            if thetas[l] >= 2*pi: break    # 当左端点也进入扩充部分时实际上就不用再重复计算了
            while thetas[r] - thetas[l] > angle:
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len + base