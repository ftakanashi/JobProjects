#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Heap:
    def __init__(self, lst):
        self._elems = lst
        self.heapify()

    def heapify(self):
        end = len(self._elems) - 1
        for i in range((end - 1) // 2, -1, -1):
            self.shiftDown(i)

    def shiftDown(self, start):
        n = len(self._elems)
        i = start
        j = i * 2 + 1
        if j + 1 < n and self._elems[j + 1] > self._elems[j]:
            j = j + 1

        e = self._elems[start]
        while j < n and self._elems[j] > e:
            self._elems[i] = self._elems[j]
            i = j
            j = i * 2 + 1
            if j + 1 < n and self._elems[j+1] > self._elems[j]:
                j = j + 1
        self._elems[i] = e

    def shiftUp(self, start):
        i = start
        j = (start - 1) // 2
        e = self._elems[start]
        while i > 0 and self._elems[j] < e:
            self._elems[i] = self._elems[j]
            i = j
            j = (i - 1) // 2
        self._elems[i] = e

    def pop(self):
        res = self._elems[0]
        self._elems = self._elems[1:]
        self.shiftDown(0)
        return res

    def append(self, e):
        self._elems.append(e)
        self.shiftUp(len(self._elems) - 1)

    def __len__(self):
        return len(self._elems)

if __name__ == '__main__':
    heap = Heap([2,7,4,1,8,1])
    print(heap._elems)