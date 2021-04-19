#!/usr/bin/env python

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.data = []
        self.i = 0

    def next(self, price: int) -> int:
        stack, data = self.stack, self.data
        while stack and data[stack[-1]] <= price:
            stack.pop()
        res = self.i - (stack[-1] if stack else -1)
        stack.append(self.i)
        data.append(price)
        self.i += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)