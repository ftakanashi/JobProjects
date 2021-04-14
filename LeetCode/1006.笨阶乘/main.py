#!/usr/bin/env python

class Solution:
    def clumsy(self, N: int) -> int:
        ope_i = 0    # ope_i是0123，分别对应*/+-。
        stack = [N, ]
        for n in range(N-1, 0, -1):
            if ope_i > 1:
                stack.append(n if ope_i == 2 else -n)
            else:
                pre = stack.pop()
                stack.append(pre * n if ope_i == 0 else int(pre / n))    # 还是注意Python带有负数时的//操作有问题
            ope_i = (ope_i + 1) % 4

        return sum(stack)