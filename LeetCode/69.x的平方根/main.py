#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x

        # 经典二分查找模板
        left, right = 1, x - 1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid

        # 注意，当最后一轮循环，left == right的时候
        # 此时显然有mid == left == right.
        # 如果mid ** 2 < x，那么mid就是所求值，又因为left = mid + 1了，所以right才是要求的值
        # 反过来，如果mid ** 2 > x，那么所求值是当前这个值左边那个，因此right = mid - 1刚好到左边，所以right还是要求的值
        # 因此最终返回right不会有错
        return right

class Solution2:
    def mySqrt(self, n: int) -> int:
        '''
        ！！！注意输入的参数名变成n了。
        '''
        if n == 0: return 0

        x = n
        eps = 1e-6
        while True:
            y = x ** 2 - n
            if y < eps:
                break
            x = (x / 2) + (n / (2*x))
        return int(x)