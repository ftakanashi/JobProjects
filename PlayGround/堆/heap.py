#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Heap:
    '''
    类实现
    '''

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
            if elems[j] <= e:    # 大顶堆 elems[j] >= e
                break
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def shift_down(self, e, start, end):
        elems, i, j = self._elems, start, start * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:    # 如果是大顶堆这里换elems[j+1] > elems[j]
                j += 1
            if e < elems[j]:    # 大顶堆：e > elems[j]
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

    # 通过自己实现的Heap类玩耍
    data = list(range(12))
    random.shuffle(data)
    heap = Heap(data)
    heap.peek()
    heap.enqueue(6)
    heap.peek()
    print(heap.dequeue())
    heap.peek()

    # 通过内建的堆类heapq玩耍
    # 注意，给出的数据本体queue，始终是一个列表
    # heapq的各个方法可以把queue中的数据始终维护成一个有堆序的堆，但是并没有改变其数据结构
    import heapq
    queue = list(range(12))
    random.shuffle(queue)
    heapq.heapify(queue)    # 建堆操作
    print(queue[0])    # peek
    heapq.heappush(queue, 6)    # enqueue
    print(queue[0])    # peek
    print(heapq.heappop(queue))    # dequeue
    print(queue[0])