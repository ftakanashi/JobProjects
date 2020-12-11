#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import itertools
class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i, j in itertools.combinations(range(len(nums) - 1), 2):     # 枚举i,j
            # 在j+1到末尾的剩余数组中二分查找
            left = j + 1
            right = len(nums) - 1
            s = nums[i] + nums[j]
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < s:
                    left = mid + 1
                else:
                    right = mid - 1
            k = right    # 注意此时的k的定义是，剩余数组中满足nums[i] + nums[j] > nums[k]的最后一个数
            count += (k - j)

        return count

class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        i = 0

        while i < len(nums) - 2:
            j = i + 1
            k = i + 2
            while j < len(nums) - 1:
                if k == j: k += 1
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += (k - j - 1)    # 注意这里的k定义是，剩余数组中不满足nums[i] + nums[j] > nums[k]的第一个数，所以要减一
                j += 1
            i += 1
        return count