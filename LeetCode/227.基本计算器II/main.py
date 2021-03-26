#!/usr/bin/env python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        prev = '+'
        for ch in s+'+':    # 额外加一个加号
            if ch == ' ': continue
            if ch.isdigit():    # 进行数字各个位数的扫描
                n = n * 10 + int(ch)
                continue

            if prev == '*': stack.append(stack.pop() * n)
            elif prev == '/':
                a = stack.pop()
                if (a > 0) ^ (n > 0):    # 异号的情况
                    res = int(a / n)
                else:    # 同号的情况
                    res = a // n
                stack.append(res)
            elif prev == '+': stack.append(n)
            elif prev == '-': stack.append(-n)

            # 最后别忘了更新prev符号以及将n置零
            prev = ch
            n = 0

        return sum(stack)