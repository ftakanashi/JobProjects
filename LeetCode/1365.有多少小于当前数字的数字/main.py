#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for n_i, n in enumerate(nums):
            for e_n in nums:
                if e_n < n:
                    res[n_i] += 1
        return res


class Solution2:

    def quickSort(self, nums: List[tuple], left: int, right:int):
        '''
        快排，注意输入数组的格式，是[(n, i) for i, n in enumerate(nums)]
        '''
        if left >= right: return

        i = d = left + 1
        while i <= right:
            if nums[i][0] < nums[left][0]:    # 基准值比较时只用[0]
                nums[i], nums[d] = nums[d], nums[i]    # 交换时整个元组交换
                d += 1
            i += 1
        nums[d - 1], nums[left] = nums[left], nums[d - 1]    # 交换时整个元组交换

        self.quickSort(nums, left, d - 2)
        self.quickSort(nums, d, right)


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_with_i = [(n, i) for i, n in enumerate(nums)]
        self.quickSort(nums_with_i, 0, len(nums) - 1)

        # 此时，nums还是原数组，而nums_with_i是排序好的扩展数组
        res = [0] * len(nums)
        prev = nums_with_i[0][0]
        i = 1
        while i < len(nums):
            if nums_with_i[i][0] == prev:    # 如果和上一个数字相同，则沿用上个数字的res值
                res[nums_with_i[i][1]] = res[nums_with_i[i-1][1]]
            else:    # 当前数字左边共有几个数字，也就是下标i的值
                res[nums_with_i[i][1]] = i
            prev = nums_with_i[i][0]
            i += 1

        return res