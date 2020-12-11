#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] < target:
            i += 1
        while j >= 0 and nums[j] > target:
            j -= 1

        if i > j:
            i, j = -1, -1

        return [i, j]

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        res_l = self.binarySearch(nums, target, lower=True)
        res_r = self.binarySearch(nums, target, lower=False)
        return [res_l, res_r]

    def binarySearch(self, nums: List[int], target: int, lower: bool) -> int:
        '''
        :param lower:如果是True那么定位第一个target，如果是False定位最后一个target
        '''
        left, right = 0, len(nums) - 1
        found = False
        while left <= right:
            mid = (left + right) // 2

            if not found and nums[mid] == target:
                found = True

            '''
            lower若True，寻找第一个target位置，此时即使nums[mid] == target
            也要继续左移right游标。即使此时mid恰好是第一个target位置也没关系，此时最终left和right会在所求位置-1
            处汇合。接着nums[mid] < target所以left += 1，恰好跳出循环条件且left指向所求位置。
            
            同理，lower是False的时候，也可以类似地分析，此时nums[mid] == target时继续右移left游标，
            left和right最终在所求位置+1处汇合，此时right再-=1，跳出循环且right指向所求位置
            
            综上所述，lower为True时优先左移right并返回left
            lower为False时优先右移left并返回right
            '''
            if (lower and nums[mid] >= target) or (not lower and nums[mid] > target):
                right = mid - 1
            elif (lower and nums[mid] < target) or (not lower and nums[mid] <= target):
                left = mid + 1

        if not found:
            return -1
        else:
            return left if lower else right

    def binarySearch2(self, nums: List[int], target: int, lower: bool) -> int:
        '''
        另一种实现
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if lower:
                    right = mid - 1
                else:
                    left = mid + 1
        if lower:
            return left if left < len(nums) and nums[left] == target else None
        else:
            return left if left > 0 and nums[left - 1] == target else None