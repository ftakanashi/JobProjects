#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def check(k: int, res: List[int]):
            '''
            检查剩余字符串是否符合斐波那契规律的函数
            输入的res保证是长度是2，即前两个数已经确定
            关于返回，当符合斐波那契规律时返回整个res结果列表，否则返回False
            '''
            while k < len(S):
                n = res[-2] + res[-1]
                if n > 2**31 - 1: return False
                if S[k:].startswith(str(n)):
                    res.append(n)
                    k += len(str(n))
                else:
                    return False
            return res if len(res) >= 3 else False

        # 枚举可能的初始两个数的组合
        for i in range(len(S) - 1):
            n1 = int(S[:i + 1])
            if n1 > 2**31 - 1 or (i > 0 and S[0] == '0'):
                continue

            for j in range(i + 1, len(S)):
                n2 = int(S[i + 1:j + 1])
                if n2 > 2**31 - 1 or (S[i+1] == '0' and j - i > 1):
                    break

                init = [n1, n2]
                res = check(j+1, init)
                if res:
                    return res