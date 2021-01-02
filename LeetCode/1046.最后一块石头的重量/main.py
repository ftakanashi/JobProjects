#!/usr/bin/env python

from typing import List

class Heap:
    def __init__(self, lst):
        self._elems = lst
        self.heapify()

    def heapify(self):
        end = len(self._elems) - 1
        for i in range(end // 2, -1, -1):
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
        '''
        注意pop操作，pop出堆顶后，
        **是将堆尾的元素拿到堆顶来做shift down**
        不是直接在剩余数组顺序上直接shift down。
        '''
        res = self._elems[0]
        self._elems = self._elems[1:]
        if len(self._elems) > 0:
            self._elems = self._elems[-1:] + self._elems[:-1]
            self.shiftDown(0)
        return res

    def append(self, e):
        self._elems.append(e)
        self.shiftUp(len(self._elems) - 1)

    def __len__(self):
        return len(self._elems)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0: return 0
        if len(stones) == 1: return stones[0]

        heap = Heap(stones)
        while len(heap) > 1:
            stone1 = heap.pop()
            stone2 = heap.pop()
            new = abs(stone1 - stone2)
            if new > 0:
                heap.append(new)

        if len(heap) == 1:
            return heap.pop()
        else:
            return 0

        # 使用heapq进行堆操作代码如下：
        # dummy = [(-s, s) for s in stones]
        # heapq.heapify(dummy)
        # while True:
        #     stone1 = heapq.heappop(dummy)
        #     stone2 = heapq.heappop(dummy)
        #     new = abs(stone1[1] - stone2[1])
        #     if new > 0:
        #         heapq.heappush(dummy, (-new, new))

        #     if len(dummy) == 0 or len(dummy) == 1:
        #         break

        # if len(dummy) == 0:
        #     return 0
        # else:
        #     return dummy[0][1]