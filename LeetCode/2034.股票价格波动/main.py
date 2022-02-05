#!/usr/bin/env python

import heapq
class StockPrice:

    def __init__(self):
        self.map = {}    # 核心哈希表
        self.curr = -1    # 最新的时间
        self.minHeap = []    # 小顶堆
        self.maxHeap = []    # 大顶堆

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))
        self.map[timestamp] = price
        self.curr = max(self.curr, timestamp)

    def current(self) -> int:
        return self.map[self.curr]

    def maximum(self) -> int:
        while self.map[self.maxHeap[0][1]] != -self.maxHeap[0][0]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.map[self.minHeap[0][1]] != self.minHeap[0][0]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()