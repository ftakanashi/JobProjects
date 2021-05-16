#!/usr/bin/env python

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count_nodes(num):
            cnt, base = 0, 0
            while num <= n:
                if num * 10 <= n:
                    cnt += (10 ** base)
                else:
                    cnt += min(n - num + 1, 10 ** base)    # 为了排除第一次进入循环就进入这个分支时，需要返回1，即10**0
                num *= 10
                base += 1
            return cnt

        num = 1
        k -= 1
        while k > 0:
            new_count = count_nodes(num)
            if k > new_count:    # 说明答案不在当前子树内
                k -= new_count
                num += 1    # 转移到右边兄弟节点去探索
            elif k < new_count:    # 说明答案在当前子树内
                k -= 1
                num *= 10    # 转移到当前子树内探索
            else:    # 说明答案恰好是右边兄弟节点
                num += 1
                break
        return num