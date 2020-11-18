#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        while j > 0 and nums[j - 1] >= nums[j]:
            j -= 1

        if j <= 0:    # nums整个都是逆序的情况
            nums.reverse()
            return

        pivot = j - 1

        j = len(nums) - 1
        while nums[j] <= nums[pivot]:    # 第二次扫描，确定待交换值的位置
            j -= 1
        nums[j], nums[pivot] = nums[pivot], nums[j]

        def partition(left, right):    # 快排的子函数，这里可以拿来做序列一部分的重排
            if left >= right: return
            i = d = left + 1
            while d <= right:
                if nums[left] > nums[d]:
                    nums[i], nums[d] = nums[d], nums[i]
                    i += 1
                d += 1
            i -= 1
            nums[i], nums[left] = nums[left], nums[i]
            partition(left, i - 1)
            partition(i + 1, right)

        partition(pivot + 1, len(nums) - 1)