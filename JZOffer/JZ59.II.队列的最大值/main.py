#!/usr/bin/env python
import collections
import heapq

class MaxQueue1:

    def __init__(self):
        self.queue = collections.deque([])
        self.counter = {}
        self.heap = []

    def max_value(self) -> int:
        if not self.queue: return -1
        while -self.heap[0] not in self.counter:
            heapq.heappop(self.heap)
        return -self.heap[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        heapq.heappush(self.heap, -value)
        if value not in self.counter:
            self.counter[value] = 1
        else:
            self.counter[value] += 1

    def pop_front(self) -> int:
        if not self.queue: return -1
        val = self.queue.popleft()
        self.counter[val] -= 1
        if self.counter[val] == 0: del self.counter[val]
        return val

class MaxQueue2:

    def __init__(self):
        self.main = collections.deque([])
        self.max_vs = collections.deque([])    # 辅助队列

    def max_value(self) -> int:
        return self.max_vs[0] if self.max_vs else -1

    def push_back(self, value: int) -> None:
        self.main.append(value)
        while len(self.max_vs) > 0 and self.max_vs[-1] < value:
            self.max_vs.pop()
        self.max_vs.append(value)

    def pop_front(self) -> int:
        if not self.main: return -1
        val = self.main.popleft()
        if self.max_vs[0] == val:
            self.max_vs.popleft()
        return val