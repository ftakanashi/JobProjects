#!/usr/bin/env python
import string

upper = set(string.ascii_uppercase)

class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        i = 0
        stack = []
        while i < n:
            if code[i] == "<":    # 扫描到 < 的情况，开始分类讨论

                if i == n - 1: return False    # 第一种情况

                if code[i + 1] in upper:    # 第二种情况
                    j = code.find(">", i)
                    if j == -1: return False
                    tag_name = code[i + 1:j]
                    if not 1 <= len(tag_name) <= 9 or not all(ch in upper for ch in tag_name): return False
                    stack.append(tag_name)
                    i = j + 1

                elif code[i + 1] == "/":    # 第三种情况
                    j = code.find(">", i)
                    if j == -1: return False
                    tag_name = code[i + 2:j]
                    if not stack or stack[-1] != tag_name: return False
                    stack.pop()
                    i = j + 1
                    if len(stack) == 0 and i < n:
                        return False

                elif code[i + 1] == "!":    # 第四种情况
                    if not stack: return False
                    cdata_tag = code[i + 2:i + 9]
                    if cdata_tag != "[CDATA[": return False
                    j = code.find("]]>", i)
                    if j == -1: return False
                    i = j + 1

                else:    # 所有非此情况，都无法形成合法的标签或者cdata，所以直接False
                    return False

            else:    # 所有扫描到非 < 的情况，讨论都比较简单
                if len(stack) == 0: return False
                i += 1

        return len(stack) == 0