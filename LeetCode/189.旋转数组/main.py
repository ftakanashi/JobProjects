#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) in (0, 1) or k == 0:
            return

        cache = nums[-k:]
        j = len(nums) - 1
        i = j - k
        while i >= 0:
            nums[j] = nums[i]
            i -= 1
            j -= 1
        nums[:k] = cache


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        k = k % len(nums)
        count = 0
        for start in range(len(nums)):
            curr = start
            cache = nums[curr]

            # 要是有do-while语句的话就好了。可以Python没有，所以只好用这样的方式来模拟
            # do ... while ...
            nxt = (curr + k) % len(nums)
            cache, nums[nxt] = nums[nxt], cache
            curr = nxt
            count += 1

            while start != curr:
                nxt = (curr + k) % len(nums)
                cache, nums[nxt] = nums[nxt], cache
                curr = nxt
                count += 1

            if count == len(nums): break


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1