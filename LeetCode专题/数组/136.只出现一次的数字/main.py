#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)