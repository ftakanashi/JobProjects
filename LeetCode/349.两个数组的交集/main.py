#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        shorter, longer = (set1,set2) if len(set1) < len(set2) else (set2,set1)

        return [n for n in shorter if n in longer]

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []
        last = None
        while i < len(nums1) and j < len(nums2):
            n1, n2 = nums1[i], nums2[j]
            if n1 == n2:
                if n1 != last:
                    res.append(n1)
                    last = n1
                i += 1
                j += 1
            elif n1 > n2:
                j += 1
            else:
                i += 1

        return res