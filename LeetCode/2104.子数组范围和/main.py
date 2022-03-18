#!/usr/bin/env python
from typing import List

class Solution:
    def helper(self, nums, cmp, reverse):
        '''
        辅助函数，通过单调栈，确定所有位置其 左/右 边距离最近且比本位置的值更 大/小 的位置
        nums: 输入数组
        cmp: 一个函数对象，用于决定维护单调栈时是否pop已有栈顶。
        简单来说，单调栈如果是递增的单调栈（求更小的情况），那么cmp应该是类似于 lambda x,y: x>y
        reverse: 决定是求左边还是右边，在函数体中决定正序还是逆序遍历，以及最终结果数组是否需要反转
        '''
        n = len(nums)
        stack = []
        ran = range(n-1, -1, -1) if reverse else range(n)
        default = n if reverse else -1
        res = []
        for i in ran:
            while stack and cmp(nums[stack[-1]], nums[i]):
                stack.pop()
            res.append(stack[-1] if stack else default)
            stack.append(i)
        if reverse:
            res.reverse()
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        # 注意cmp的微妙的取等时机。简单来说，只要保证上两行和下两行中各自有且只有一个等号，就可以
        left_min = self.helper(nums, lambda x,y: x > y, False)
        right_min = self.helper(nums, lambda x,y: x >= y, True)
        left_max = self.helper(nums, lambda x,y: x < y, False)
        right_max = self.helper(nums, lambda x,y: x <= y, True)

        ans = 0
        for i in range(n):
            # 统计最终结果。针对每个位置，求如下内容
            ans += (
                       (right_max[i] - i) * (i - left_max[i]) - (right_min[i] - i) * (i - left_min[i])
                   ) * nums[i]
        return ans