#!/usr/bin/env python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        total_res = []

        def dfs(i: int, res: List[str]):
            # 递归终止条件
            if i == n or len(res) == 4:
                if i == n and len(res) == 4:
                    total_res.append('.'.join(res))
                return

            if s[i] == '0':    # 如果当前递归剩余子串第一个就是0，那只能取0一个位数
                dfs(i + 1, res + ['0', ])
            else:    # 否则就开始扫描剩余子串，从中取出一到三个数字尝试探索
                for j in range(i, n):
                    if j - i >= 3: break    # 剪枝
                    num = int(s[i:j+1])
                    if num <= 255:
                        dfs(j+1, res + [s[i:j+1], ])

        dfs(0, [])
        return total_res