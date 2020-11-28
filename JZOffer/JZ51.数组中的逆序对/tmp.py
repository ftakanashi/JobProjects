#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort_and_count(nums: List[int]) -> int:
            if len(nums) <= 1: return 0
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            left_count = merge_sort_and_count(left)
            right_count = merge_sort_and_count(right)

            m, n = len(left) - 1, len(right) - 1

            # count
            i, j = 0, 0
            count = left_count + right_count
            while j <= n:
                while i <= m:
                    if left[i] > right[j]:
                        count += (m - i + 1)
                        break
                    i += 1
                j += 1

            # merge
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

            return count

        return merge_sort_and_count(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [7,5,6,4]
    print(solution.reversePairs(nums))