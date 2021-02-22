#!/usr/bin/env python

class Heap:
    '''
    同一个类实现大/小顶堆
    '''
    def __init__(self, elems, order='min'):
        self.elems = elems
        self.order = order
        for i in range((len(self.elems) - 1) // 2, -1, -1):
            self.shiftDown(i)

    def shiftDown(self, start):
        e, i, j, n = self.elems[start], start, start * 2 + 1, len(self.elems)
        while j < n:
            if j + 1 < n:
                if (self.order == 'min' and self.elems[j+1] < self.elems[j]) or \
                        (self.order == 'max' and self.elems[j+1] > self.elems[j]): j += 1

            if (self.order == 'min' and self.elems[j] >= e) or \
                    (self.order == 'max' and self.elems[j] <= e): break
            self.elems[i] = self.elems[j]
            i, j = j, j * 2 + 1
        self.elems[i] = e

    def shiftUp(self, start):
        e, i, j, n = self.elems[start], start, (start - 1) // 2, len(self.elems)
        while j >= 0:
            if (self.order == 'min' and self.elems[j] <= e) or \
                    (self.order == 'max' and self.elems[j] >= e): break
            self.elems[i] = self.elems[j]
            i, j = j, (j - 1) // 2
        self.elems[i] = e

    def pop(self):
        assert len(self.elems) > 0
        val = self.elems[0]
        tail = self.elems.pop()
        if len(self.elems) > 0:
            self.elems[0] = tail
            self.shiftDown(0)
        return val

    def push(self, val):
        self.elems.append(val)
        self.shiftUp(len(self.elems) - 1)

    def __len__(self):
        return len(self.elems)

    def peek(self):
        return self.elems[0]

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = Heap([], order='min')
        self.maxHeap = Heap([], order='max')

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 or num < self.maxHeap.peek():
            self.maxHeap.push(num)
        else:
            self.minHeap.push(num)

        while len(self.maxHeap) < len(self.minHeap):
            self.maxHeap.push(self.minHeap.pop())
        while len(self.maxHeap) > len(self.minHeap) + 1:
            self.minHeap.push(self.maxHeap.pop())
        # print(self.maxHeap.elems, self.minHeap.elems)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap.peek() + self.maxHeap.peek()) / 2
        elif len(self.maxHeap) == len(self.minHeap) + 1:
            return self.maxHeap.peek()