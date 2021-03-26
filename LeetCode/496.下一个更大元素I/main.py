#!/usr/bin/env python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2i = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[stack[-1]] < nums2[i]:
                stack.pop()
            if stack: n2i[nums2[i]] = stack[-1]
            else: n2i[nums2[i]] = -1
            stack.append(i)

        res = []
        for n in nums1:
            res.append(nums2[n2i[n]] if n2i[n] > 0 else -1)
        return res