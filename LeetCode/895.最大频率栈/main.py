#!/usr/bin/env python
class FreqStack:

    def __init__(self):
        self.counter = {}
        self.stacks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val not in self.counter:
            self.counter[val] = 0
        self.counter[val] += 1

        freq = self.counter[val]
        self.maxFreq = max(self.maxFreq, freq)

        if freq not in self.stacks:
            self.stacks[freq] = []
        self.stacks[freq].append(val)

    def pop(self) -> int:
        max_freq_stack = self.stacks[self.maxFreq]
        res = max_freq_stack.pop()
        self.counter[res] -= 1
        if len(max_freq_stack) == 0:    # 别忘了这个处理
            self.maxFreq -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()