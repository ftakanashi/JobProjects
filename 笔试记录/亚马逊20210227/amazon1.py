#!/usr/bin/env python

class MaxHeap:
    def __init__(self, elems):
        self.elems = elems
        for i in range((len(elems) - 1) // 2, -1, -1):
            self.shiftDown(i)

    def shiftDown(self, start):
        e, i, j = self.elems[start], start, start * 2 + 1
        while j < len(self.elems):
            if j + 1 < len(self.elems) and self.elems[j+1] > self.elems[j]: j+=1
            if self.elems[j] <= e: break
            self.elems[i] =self.elems[j]
            i, j = j, j * 2 + 1
        self.elems[i] = e

    def pop(self):
        val = self.elems[0]
        tail = self.elems.pop()
        if len(self.elems) > 0:
            self.elems[0] = tail
            self.shiftDown(0)
        return val

    def peek(self):
        return self.elems[0] if self.elems else None

def getMaxUnit(num, boxes, unitSize, unitsPerBox, truckSize):
    # WRITE YOUR CODE HERE
    data = list(zip(unitsPerBox, boxes))
    heap = MaxHeap(data)
    res = 0
    for _ in range(truckSize):
        print(heap.elems)
        if heap.peek() is None: break
        unix, cnt = heap.peek()
        res += unix
        cnt -= 1
        if cnt == 0: heap.pop()
        else: heap.elems[0] = (unix, cnt)
    print(heap.elems)
    return res

if __name__ == '__main__':
    a = list(range(1,10))
    b = list(range(1,10))
    import random
    random.shuffle(a)
    random.shuffle(b)
    print(a)
    print(b)
    res = getMaxUnit(9, a, 9, b, 10)
    print(res)