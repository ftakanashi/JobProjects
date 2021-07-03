#!/usr/bin/env python

def slide_window(array):
    n = len(array)
    left, right = 0, 0    # 两个指针都初始化在起始位置，window就是left和right间的闭区间

    while right < n:

        while not check_window():
            # 当滑窗不符合要求时