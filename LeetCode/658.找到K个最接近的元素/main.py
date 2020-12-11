#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 特殊情况处理，显然，当x比最大数还大或者比最小数还小的时候
        # 直接可以返回所求序列
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]

        res = self.binarySearch(arr, x)
        left, right = res, res + 1
        # 这里注意一个细节。由于有了上面特殊情况的处理，此时二分查找返回的res最小是0（不会是-1），最大是len(arr) - 2
        # （不会是len(arr) - 1）。由于后者的限制，所以可以放心地指定right为res + 1而不用担心越界。

        count = 0
        while left >= 0 and right < len(arr) and count < k:
            # 在保证不越界的情况下拓展区间
            l_gap = abs(arr[left] - x)
            r_gap = abs(arr[right] - x)
            if l_gap <= r_gap:    # 当gap相同时优先左指针
                left -= 1
            else:
                right += 1
            count += 1

        # 如果count还不到k，说明之前循环跳出是因为某个指针到边界了。再后处理把另一个指针移动，直到凑足k个元素
        while count < k and left >= 0:
            left -= 1
            count += 1
        while count < k and right < len(arr):
            right += 1
            count += 1

        return arr[left + 1 : right]    # 模拟一下就可以知道，答案的left, right是个开区间

    def binarySearch(self, nums: List[int],  target: int) -> int:
        '''
        经典二分查找
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        # 当没有找到target时，返回target预插入位置的前一个
        # 即最后一个比target小的数的位置，这里是right
        return right