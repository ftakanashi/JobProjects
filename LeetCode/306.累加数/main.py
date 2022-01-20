#!/usr/bin/env python

class Solution:
    def check(self, num: str, i: int, j: int) -> bool:
        '''
        当第一、第二个数字分别是num[:i+1]和num[i+1:j+1]时，是否符合累加数要求
        '''
        num1 = int(num[:i+1])
        num2 = int(num[i+1:j+1])
        k = j + 1
        while k < len(num):
            s = num1 + num2
            if num[k:].startswith(str(s)):    # 相当符合Python的暴力写法…
                num1 = num2
                num2 = s
                k += len(str(s))
            else:
                break
        return k == len(num)    # 只要判断最后指针k是否扫描完整个num即可

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(n-2):
            if num[0] == "0" and i > 0: break    # 因为数字不以0开头，所以若num[0]是0，那么i只能取0
            for j in range(i+1, n-1):
                if num[i+1] == "0" and j > i + 1: break    # 因为数字不以0开头，所以若num[i+1]是0，那么j只能取i+1
                if self.check(num, i, j):
                    return True
        return False