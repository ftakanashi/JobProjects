#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def longestMountain(self, A: List[int]) -> int:

        if len(A) < 3:    # 特殊情况处理
            return 0

        i = 1    # 从第二个元素开始扫描
        max_len = 0
        while i < len(A) - 1:    # 扫描至倒数第二个元素
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                # 不符合这个条件的话说明此位置不能作为山顶

                # 探索左边界
                left = i - 1
                my_max_len = 3    # 初始默认长度是3
                while left > 0 and A[left - 1] < A[left]:
                    left -= 1
                    my_max_len += 1

                # 探索右边界
                right = i + 1
                while right < len(A) - 1 and A[right] > A[right + 1]:
                    right += 1
                    my_max_len += 1

                # 更新最长长度
                max_len = max(my_max_len, max_len)

                # 如果右边界本身已经超过数组长度，就没啥好说的了
                # 如果右边界为超过数组长度，下一个可能的山顶是right+1
                i = right + 1
                if len(A) - i + 1 < max_len:
                    # 优化：如果剩下的节点总数已经少于当前得到的max_len，那么没必要继续扫描
                    return max_len
            else:
                i += 1

        return max_len