#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1. shiftDown和shiftUp都用while下标不越界+break制
2. shiftDown的额外条件是j+1和j比较，与堆序一致
2. break条件是j和e之间(位置别搞反)<=>比较, shiftUp与堆序一致, shiftDown与堆序相反！！
'''

class Heap:
    def __init__(self, lst):
        self.elems = lst
        for i in range((len(self.elems) - 1) // 2, -1, -1):
            self.shiftDown(i)

    def shiftDown(self, start):
        e = self.elems[start]
        i, j = start, start * 2 + 1
        while j < len(self.elems):
            if j + 1 < len(self.elems) and self.elems[j+1] < self.elems[j]:
                j += 1
            if self.elems[j] >= e: break
            self.elems[i] = self.elems[j]
            i, j = j, j * 2 + 1
        self.elems[i] = e

    def shiftUp(self, start):
        e = self.elems[start]
        i, j = start, (start - 1) // 2
        while j >= 0:
            if self.elems[j] <= e: break
            self.elems[i] = self.elems[j]
            i, j = j, (j - 1) // 2
        self.elems[i] = e

    def push(self, val):
        self.elems.append(val)
        self.shiftUp(len(self.elems) - 1)

    def pop(self):
        if len(self.elems) == 0: return
        val = self.elems[0]
        if len(self.elems) > 1:
            self.elems[0] = self.elems.pop()
            self.shiftDown(0)
        else:
            self.elems.pop()
        return val

if __name__ == '__main__':
    l = list(range(10))
    import random
    random.shuffle(l)
    print(l)
    heap = Heap(l)
    print(heap.elems)
    heap.push(5)
    print(heap.elems)
    print(heap.pop())
    print(heap.elems)
    print(heap.pop())
    print(heap.elems)
    while len(heap.elems) > 0:
        print(heap.pop(), end=',')