#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        stack.append(num[0])
        i = 1
        while i < len(num) and k > 0:
            if len(stack) == 0 or int(num[i]) >= int(stack[-1]):
                # 仍然是不递减序列
                stack.append(num[i])
                i += 1
            else:
                # 删除不递减序列的最后一个数字
                stack.pop()
                k -= 1

        # 尾巴处理
        # 此时有两种情况。第一，k还不是0。此时说明栈中整个序列是一个不递减序列，此时从末尾删除即可
        # 第二，i还没有扫描到末尾就完成了k次删除，此时最后输出代码的统一，直接把剩余数字全部入栈。
        if k > 0:
            while k > 0:
                stack.pop()
                k -= 1
        else:
            while i < len(num):
                stack.append(num[i])
                i += 1

        return ''.join(stack).lstrip('0') or '0'