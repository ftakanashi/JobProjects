#!/usr/bin/env python
from typing import List

class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if len(stack) == 0 or stack[-1] < num:
                stack.append(num)
                if len(stack) >= 3: return True

            # 二分查找
            l, r = 0, len(stack) - 1
            while l <= r:
                mid = (l + r) // 2
                if stack[mid] == num:
                    break
                elif stack[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            if l > r:
                stack[l] = num

        return False

class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf'), float('inf')
        for num in nums:
            if num < i:
                i = num
            elif i < num < j:
                j = num
            elif num > j:
                return True

        return False