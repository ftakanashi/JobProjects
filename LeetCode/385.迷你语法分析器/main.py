#!/usr/bin/env python

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        n = len(s)
        i = 0
        digits = set("1234567890-")
        stack = []
        while i < n:
            if s[i] in digits:    # 碰到数字时，完整解析整个数字
                num, minus = 0, False
                while i < n and s[i] in digits:
                    if s[i] == "-":
                        minus = True
                    else:
                        num = num * 10 + int(s[i])
                    i += 1
                if minus: num = -num
                stack.append(NestedInteger(num))
            elif s[i] == ",":    # 碰到逗号直接跳过
                i += 1
            elif s[i] == "[":    # 碰到左括号
                stack.append(s[i])
                i += 1
            elif s[i] == "]":    # 碰到右括号
                new = NestedInteger()
                cache = []
                while stack and stack[-1] != "[":
                    cache.append(stack.pop())
                for item in reversed(cache):    # 设置一个中间缓存cache，保证顺序的正确
                    new.add(item)
                stack.pop()
                stack.append(new)
                i += 1

        return stack[0]