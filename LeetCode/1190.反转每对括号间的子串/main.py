#!/usr/bin/env python

class Solution1:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                tmp = ''
                while stack and stack[-1] != '(':
                    tmp += stack.pop()
                if stack: stack.pop()
                stack.extend(list(tmp))
            else:
                stack.append(ch)

        return ''.join(stack)

class Solution2:
    def reverseParentheses(self, s: str) -> str:

        n = len(s)

        def rec(start, rev):
            if start == n: return [], start
            i = start
            res = []
            while i < n and s[i] != ')':
                if s[i] not in '()':
                    if rev: res.insert(0, s[i])
                    else: res.append(s[i])
                    i += 1
                elif s[i] == '(':
                    sub_res, end = rec(i + 1, not rev)
                    if rev: res = sub_res + res
                    else: res = res + sub_res
                    i = end + 1
            return res, i

        return ''.join(rec(0, False)[0])


class Solution3:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair_map = [-1 for _ in range(n)]
        stack = []
        cnt = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair_map[i] = j
                pair_map[j] = i
            else:
                cnt += 1

        res = ''
        i, direc = 0, 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair_map[i]
                direc = -direc
            else:
                res = res + s[i]

            i += direc
        return res