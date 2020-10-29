#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    由于Python没有原生的栈类型
    所以用两个列表来模拟的
'''

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) == 0:
            if len(self.stack1) == 0: return -1
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()