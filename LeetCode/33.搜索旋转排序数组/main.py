#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if target == nums[0] else -1

        # 寻找turn point
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:    # 注意这个等号，当nums只有两个数比如[1,3]时，没这个等号死循环
                left = mid + 1
            elif nums[mid] < nums[0]:
                right = mid - 1
        turn = right
        # 绝大多数情况，right都是turn point,即排序数组中最大的数。
        # 但是除了[3,1]这种两个数且第一个较大的情况，最终情况是left越界，right是1。此时turn要减去1。
        if len(nums) == left:
            turn -= 1

        # 确定target可能存在的范围
        if nums[0] <= target <= nums[turn]:
            left, right = 0, turn
        elif nums[turn + 1] <= target <= nums[-1]:
            left, right = turn + 1, len(nums) - 1
        else:
            return -1

        # 第二次二分查找
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # 解法1寻找turnpoint时，这里都让left = mid + 1了
                # 但是实际上如果上面条件成立，0到mid之间的就确定是有序的子数组
                # 此时没必要再去找turn point，直接right = mid - 1搜索即可
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 同上注释
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1