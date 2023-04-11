#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check(span: List[int]) -> bool:
            """
            判断某一个子数组span是否符合题目要求，通过排序后可以得到等差数列
            """

            _min, _max = float("inf"), float("-inf")
            for num in span:
                _min = min(_min, num)
                _max = max(_max, num)

            if _max == _min:
                return True
            if (_max - _min) % (len(span) - 1) != 0:
                return False

            diff = (_max - _min) // (len(span) - 1)
            span_set = set(span)
            if len(span_set) < len(span):
                return False

            t = _min
            while t <= _max:
                if t not in span_set: return False
                t += diff
            return True

        return [check(nums[start: end + 1]) for start, end in zip(l, r)]