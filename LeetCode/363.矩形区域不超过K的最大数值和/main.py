#!/usr/bin/env python

from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def findSubseqRes(nums):
            '''
            输入一个一位数组
            找出其中一个子数组nums[i:j+1]使得sum(nums[i:j+1]) <= k且最大。
            '''
            presum = [0, ]    # presum = SortedList([0,])
            s = 0
            ans = float('-inf')
            for n in nums:
                s += n
                pairpos = bisect.bisect_left(presum, s - k)    # presum.bisect_left(s - k)
                if pairpos < len(presum):    # 如果返回下标等于长度，说明当前presum中不存在>= s-k的数，换句话说，不存在满足要求的s - x <= k
                    ans = max(ans, s - presum[pairpos])
                inspos = bisect.bisect_left(presum, s)    # 这两行：presum.add(s)
                presum.insert(inspos, s)
            return ans

        ans = float('-inf')
        for i in range(m):
            for j in range(i, m):
                # 将每个行间矩阵处理成"列和数组"，从而将其当做一个一维数组来处理
                col_sum = [sum( [matrix[ii][k] for ii in range(i, j+1)] ) for k in range(n)]
                ans = max(ans, findSubseqRes(col_sum))

        return ans