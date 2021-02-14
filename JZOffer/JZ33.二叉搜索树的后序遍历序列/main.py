#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def rec(left, right) -> bool:
            if left >= right: return True
            pivot = postorder[right]
            bound = right - 1
            while bound >= 0 and postorder[bound] > pivot:
                bound -= 1

            for i in range(left, bound + 1):
                if postorder[i] > pivot: return False

            return rec(left, bound) and rec(bound + 1, right - 1)

        return rec(0, len(postorder) - 1)