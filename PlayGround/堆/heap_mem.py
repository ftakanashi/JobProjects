#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
方便记忆版的堆实现，几个记忆点：
shiftDown和shiftUp的模板：

e, i, j初始化
while 不越界
    (额外条件)
    break条件
    i赋j值
    ij移动
i赋e值

1. break条件是j和e之间(位置别搞反)带等号比较, shiftUp与堆序一致, shiftDown与堆序相反！！
2. shiftDown的额外条件是j+1和j无等号比较，与堆序一致

'''

class MinHeap:
    def __init__(self, elems):
        self.elems = elems
        for i in range((len(self.elems) - 1) // 2, -1, -1):
            self.shiftDown(i)

    def shiftDown(self, start):
        e, i, j = self.elems[start], start, start * 2 + 1
        while j < len(self.elems):
            if j + 1 < len(self.elems) and self.elems[j+1] < self.elems[j]: j += 1
            if self.elems[j] >= e: break
            self.elems[i] = self.elems[j]
            i, j = j, j * 2 + 1
        self.elems[i] = e

    def shiftUp(self, start):
        e, i, j = self.elems[start], start, (start - 1) // 2
        while j >= 0:
            if self.elems[j] <= e: break
            self.elems[i] = self.elems[j]
            i, j = j, (j - 1) // 2
        self.elems[i] = e

    def push(self, val):
        self.elems.append(val)
        self.shiftUp(len(self.elems) - 1)

    def pop(self):
        assert self.elems
        val = self.elems[0]
        tail = self.elems.pop()
        if len(self.elems) > 0:
            self.elems[0] = tail
            self.shiftDown(0)
        return val

if __name__ == '__main__':
    import random
    l = list(range(10))
    random.shuffle(l)
    print(l)
    heap = MinHeap(l)
    print(heap.elems)
    heap.push(5)
    heap.push(10)
    print(heap.elems)
    while len(heap.elems) > 0:
        print(heap.pop(), end=' ')
        # print(heap.elems)