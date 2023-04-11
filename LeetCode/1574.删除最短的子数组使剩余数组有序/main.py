#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # 确定 j 的边界
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0: return 0
        # 此时 arr[j:] 是有序的

        ans = j    # 而答案就有了保底值为 j

        for i in range(n):

            # 保证 xxx 部分有序
            if i > 0 and arr[i] < arr[i - 1]:
                break

            # 针对 i ，寻找最小的 j 满足 arr[i] <= arr[j] 或者 j == n(即zzz中没有大于等于arr[i]的数，此时是去尾的情况)
            # 注意，即使上一轮循环 j == n 了，再次进入到这里也不会报错，因为 j<n 才会访问 arr[j] 并进入循环
            while j < n and arr[j] < arr[i]:
                j += 1

            ans = min(ans, j - i - 1)

        return ans