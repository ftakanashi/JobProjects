#!/usr/bin/env python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random
def rand7():
    '''
    一个已经定义好了的，随机返回1-7之间某个整数的函数
    '''
    return int(random.random() * 7) + 1

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        ans = (a-1) * 7 + (b-1)
        while ans >= 40:
            a = rand7()
            b = rand7()
            ans = (a-1) * 7 + (b-1)
        return ans // 4 + 1