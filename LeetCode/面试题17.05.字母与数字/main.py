#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        presum = [ [0, 0], ]
        diff2pos = {0: -1}
        ans_s = ans_e = -1
        for i, item in enumerate(array):
            tmp = presum[-1].copy()
            tmp[1 if item.isdigit() else 0] += 1

            diff = tmp[0] - tmp[1]
            if diff in diff2pos:
                if i - diff2pos[diff] > ans_e - ans_s:
                    ans_s, ans_e = diff2pos[diff], i
            else:
                diff2pos[diff] = i
            presum.append(tmp)

        return array[ans_s + 1 : ans_e + 1]