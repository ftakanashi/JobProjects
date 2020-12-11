#!/usr/bin/env python
# -*- coding:utf-8 -*-

class myheap:

    @classmethod
    def shiftUp(cls, lst, start):
        e = lst[start]
        i = start
        j = (i - 1) // 2
        while j >= 0 and lst[j] < e:
            lst[i] = lst[j]
            i, j = j, (j - 1) // 2
        lst[i] = e

    @classmethod
    def heapAppend(cls, lst, e):
        lst.append(e)
        cls.shiftUp(lst, len(lst) - 1)

    @classmethod
    def shiftDown(cls, lst, start):
        e = lst[start]
        i, j = start, start * 2 + 1
        if j + 1 < len(lst) and lst[j+1] > lst[j]:
            j = j + 1
        while j < len(lst) and lst[j] > e:
            lst[i] = lst[j]
            i, j = j, j * 2 + 1
            if j + 1 < len(lst) and lst[j+1] > lst[j]:
                j = j + 1
        lst[i] = e

    @classmethod
    def heapify(cls, lst):
        end = len(lst) - 1
        for i in range(end // 2, -1, -1):
            cls.shiftDown(lst, i)

    @classmethod
    def heappop(cls, lst):
        e = lst[0]
        del lst[0]
        return e

if __name__ == '__main__':
    l = [0,1,2,3,4,5,6,7,8,9]
    myheap.heapify(l)
    print(l)
    myheap.heapAppend(l, 7)
    print(l)

    for _ in range(6):
        e = myheap.heappop(l)
    print(e)
    print(l)