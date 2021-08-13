#!/usr/bin/env python
from typing import List
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        # 求某个数字在树中轴对称位置的数字
        def transfer(n):
            orig_n, bits = n, 0
            while n > 0:
                bits += 1
                n = n >> 1
            return orig_n ^ (2**(bits-1) - 1)

        ans = []
        while label > 0:
            ans.append(label)
            label = label // 2

        i = 1    # 倒序排列后，出错的数字总是奇数下标位置的数字
        while i < len(ans):
            ans[i] = transfer(ans[i])
            i += 2

        ans.reverse()    # 最后别忘了reverse
        return ans