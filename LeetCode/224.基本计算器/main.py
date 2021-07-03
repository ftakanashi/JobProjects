#!/usr/bin/env python

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == ' ' or ch == '+':
                i += 1
                continue

            res = 0
            if ch == '(' or ch == '-':
                res = ch
            elif ch == ')':
                # 计算括号内值
                while stack[-1] != '(': res += stack.pop()
                stack.pop()
                if stack and stack[-1] == '-':    # 别忘了可能的取负
                    stack.pop()
                    res = -res
            else:
                # 扫描完整的数字
                while i < len(s) and s[i].isdigit():
                    res = res * 10 + (int(s[i]))
                    i += 1
                i -= 1

                # 别忘了可能取负
                if stack and stack[-1] == '-':
                    stack.pop()
                    res = -res

            stack.append(res)
            i += 1

        return sum(stack)