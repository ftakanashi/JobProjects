#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Heap:

    def __init__(self, elems):
        self._elems = list(elems)
        self.buildHeap()

    def is_empty(self):
        return len(self._elems) == 0

    def peek(self):
        print(self._elems)

    def buildHeap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.shift_down(self._elems[i], i, end)

    def shift_up(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while j >= 0:
            if elems[j] <= e:
                break
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def shift_down(self, e, start, end):
        elems, i, j = self._elems, start, start * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    def enqueue(self, e):
        self._elems.append(e)
        self.shift_up(e, len(self._elems) - 1)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Empty Heap')
        e0 = self._elems[0]
        e = self._elems.pop()
        if not self.is_empty():
            self.shift_down(e, 0, len(self._elems))
        return e0

if __name__ == '__main__':
    import random
    data = list(range(12))
    random.shuffle(data)
    heap = Heap(data)
    heap.peek()
    heap.enqueue(6)
    heap.peek()

    print(heap.dequeue())
    heap.peek()