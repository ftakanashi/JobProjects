#!/usr/bin/env python

class Solution1:
    def decodeString(self, s: str) -> str:
        i = 0
        res = ''
        while i < len(s):
            if s[i] not in '1234567890':
                res += s[i]
            else:
                # 累计统计数字的各个位数（因为数字可能不止一位数）
                n = 0
                while s[i] in '1234567890':
                    n = n * 10 + int(s[i])
                    i += 1

                # 数字n后面的中括号内部的ptn是什么
                left_count, ptn = 1, ''
                i += 1
                while True:
                    if s[i] == '[': left_count += 1
                    elif s[i] == ']': left_count -= 1
                    if left_count == 0: break
                    ptn += s[i]
                    i += 1

                res += n * self.decodeString(ptn)

            i += 1

        return res

class Solution2:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            res = ''
            while stack[-1] != '[':
                res = stack.pop() + res
            stack.pop()
            n, base = 0, 1
            while len(stack) > 0 and stack[-1] in '1234567890':
                n = int(stack.pop()) * base + n
                base *= 10
            stack.append(n * res)

        return ''.join(stack)