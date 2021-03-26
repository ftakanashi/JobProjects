#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
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

class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        fin_len = n - k
        if fin_len == 0: return '0'    # 如果k等于n，最终结果肯定是空，所以直接返回0

        for ch in num:
            while k > 0 and stack and stack[-1] > ch:    # 在还未删除k次的情况下保持栈的单调性
                stack.pop()
                k -= 1
            stack.append(ch)

        res = ''.join(stack)    # 得到初步结果
        if len(res) > fin_len:    # 如果初步结果大于预期长度 取其前n-k位即可
            res = res[:fin_len]
        res = res.lstrip('0')    # 去除前导0
        return res if res else '0'