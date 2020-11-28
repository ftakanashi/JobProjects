#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List, Tuple

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        # 由于除了归并排序本身的排序操作，还需要统计重要对数目，因此
        # 在每层递归返回的时候都要返回这两个信息
        def merge_sort_and_count(nums: List[int]) -> Tuple[List[int], int]:
            if len(nums) <= 1: return nums, 0
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            left, left_count = merge_sort_and_count(left)
            right, right_count = merge_sort_and_count(right)

            m, n = len(left) - 1, len(right) - 1

            # 统计重要对
            i, j = 0, 0
            count = left_count + right_count
            # 以右子数组为基准统计
            while j <= n:
                # 扫描每个左子数组的元素
                while i <= m:
                    # 当发现有大于当前右子数组数时，增加重要对数目
                    if left[i] > right[j] * 2:    # 和JZ51代码唯一不同的地方，这里要乘以2
                        count += (m - i + 1)
                        break
                    i += 1
                j += 1

            # 常规归并排序操作
            i, j = 0, 0
            res = []
            while i <= m and j <= n:
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i <= m:
                res.extend(left[i:])
            if j <= n:
                res.extend(right[j:])

            return res, count

        return merge_sort_and_count(nums)[1]