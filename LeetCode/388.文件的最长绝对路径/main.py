#!/usr/bin/env python

class Solution:
    def isFile(self, s: str) -> bool:    # 判断是否是文件
        return s.find(".") != -1

    def countIndent(self, s: str) -> int:    # 计算文件/目录的层级
        cnt = 0
        for ch in s:
            if ch == "\t": cnt += 1
            else: break
        return cnt

    def lengthLongestPath(self, input: str) -> int:
        items = input.split("\n")
        stack = []
        ans = i = 0
        while i < len(items):
            ind = self.countIndent(items[i])
            while stack and len(stack) > ind:
                stack.pop()

            stack.append(items[i].lstrip("\t"))    # 别忘了进行路径合并时要去掉左边多余的\t
            if self.isFile(items[i]):
                ans = max(ans, len("\\".join(stack)))

            i += 1

        return ans