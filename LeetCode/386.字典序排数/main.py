#!/usr/bin/env python
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1
        while len(ans) < n:

            while num <= n:    # 不断优先向下扫描子节点
                ans.append(num)
                num *= 10
            num = num // 10    # 注意此时num其实是一个超界的子节点，将其拉回到其父节点，即不超界的最左下角节点

            while num % 10 == 9:    # 若当前节点是兄弟节点中的最后一个，则回溯。考虑可能回溯多层，因此用while
                num = num // 10
            num += 1    # 向右
        return ans