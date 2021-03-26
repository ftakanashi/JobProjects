#!/usr/bin/env python

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder or preorder == '#': return True
        stack = []
        nodes = preorder.split(',')
        for i, node in enumerate(nodes):
            stack.append(node)
            while len(stack) > 2 and stack[-3] != '#' and stack[-2] == '#' and stack[-1] == '#':
                for _ in range(3): stack.pop()
                stack.append('#')

            if stack == ['#',]:    # 因为上面循环最后总会加入一个#，所以此处判断栈为空，其实是判栈是否只有一个#元素
                return i == len(nodes) - 1    # 是否遍历完了所有元素